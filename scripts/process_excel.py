from pathlib import Path
import pandas as pd, json, math, re, sys
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'data/source/BaseDatos_red_piezometrica_SAC.xlsx'
OUT=ROOT/'data/generated'; OUT.mkdir(parents=True,exist_ok=True)

def clean(v):
    if pd.isna(v): return None
    if isinstance(v,pd.Timestamp): return v.isoformat()
    if hasattr(v,'item'): v=v.item()
    if isinstance(v,float) and (math.isnan(v) or math.isinf(v)): return None
    return v

def slug_col(s):
    s=str(s).strip().lower().translate(str.maketrans('áéíóúñ','aeioun'))
    return re.sub(r'[^a-z0-9]+','_',s).strip('_')

if not SRC.exists(): sys.exit(f'No existe {SRC}')
try:
    xls=pd.ExcelFile(SRC)
except Exception as e:
    sys.exit(f'No se pudo abrir el Excel: {e}')
required_sheets={'DATOS GENERALES','LECTURAS'}
missing_sheets=required_sheets-set(xls.sheet_names)
if missing_sheets:
    sys.exit('Faltan hojas obligatorias: '+', '.join(sorted(missing_sheets)))
master=pd.read_excel(SRC,sheet_name='DATOS GENERALES').dropna(how='all')
read=pd.read_excel(SRC,sheet_name='LECTURAS').dropna(how='all')
master.columns=[slug_col(c) for c in master.columns]; read.columns=[slug_col(c) for c in read.columns]
required_master={'piezometro','estacion_de_monitoreo','cuenca','municipio','longitud','latitud'}
required_read={'piezometro','fecha_muestreo','nivel_estatico','temperatura','conductividad'}
mm=required_master-set(master.columns); mr=required_read-set(read.columns)
if mm: sys.exit('DATOS GENERALES: faltan columnas: '+', '.join(sorted(mm)))
if mr: sys.exit('LECTURAS: faltan columnas: '+', '.join(sorted(mr)))

for c in ['piezometro','estacion_de_monitoreo','cuenca','municipio','predio','acuifero_monitoreado']:
    if c in master: master[c]=master[c].astype('string').str.strip()
read['piezometro']=read['piezometro'].astype('string').str.strip()
read['fecha_muestreo']=pd.to_datetime(read['fecha_muestreo'],errors='coerce')

# Se excluyen filas vacías o sin identificador de piezómetro.
master=master[master['piezometro'].notna() & (master['piezometro'].str.len()>0)].copy()
read=read[read['piezometro'].notna() & read['fecha_muestreo'].notna()].copy()

if 'serial_sensor' in master:
    master['serial_sensor']=master['serial_sensor'].apply(lambda x: None if pd.isna(x) else str(int(x)) if isinstance(x,(int,float)) and float(x).is_integer() else str(x))

# Privacidad por diseño: solo estos campos pueden salir al dataset público.
# Cualquier columna nueva del Excel queda privada por defecto hasta revisión explícita.
PUBLIC_MASTER_FIELDS = [
    'cuenca', 'departamento', 'municipio', 'estacion_de_monitoreo', 'piezometro',
    'longitud', 'latitud', 'z', 'predio', 'fecha_construccion', 'profundidad',
    'acuifero_monitoreado', 'nivel_estatico_base', 'nivel_estatico_msnm',
    'profundidad_sensor', 'serial_sensor', 'muestreo',
    'ficha', 'disenos_mecanicos', 'fotos', 'icon_ft', 'icon_dm', 'icon_foto'
]
public_master_cols = [c for c in PUBLIC_MASTER_FIELDS if c in master.columns]
master_records=[
    {k:clean(v) for k,v in r.items()}
    for r in master[public_master_cols].to_dict('records')
]
measure_cols=['altura_columna_de_agua','nivel_estatico','temperatura','conductividad']
measure_records=[]
for r in read.sort_values(['piezometro','fecha_muestreo']).to_dict('records'):
    item={'piezometro':clean(r.get('piezometro')),'fecha':r['fecha_muestreo'].date().isoformat()}
    for c in measure_cols: item[c]=clean(r.get(c))
    measure_records.append(item)

# Calidad: el Excel consolida dos lecturas diarias pero FECHA MUESTREO no conserva la hora.
# Por eso dos filas del mismo día NO se consideran duplicadas. Solo se marcan filas totalmente idénticas.
quality=[]; global_last=read['fecha_muestreo'].max()
for pid in sorted(master['piezometro'].dropna().unique()):
    g=read[read['piezometro']==pid].sort_values('fecha_muestreo')
    if g.empty:
        quality.append({'piezometro':pid,'registros':0,'primera_lectura':None,'ultima_lectura':None,'esperados':0,'completitud_pct':0,'duplicados':0,'nulos':0,'estado':'sin_datos'}); continue
    first,last=g.fecha_muestreo.min(),g.fecha_muestreo.max()
    days=(last.normalize()-first.normalize()).days+1
    expected=max(1,days*2) # muestreo declarado: cada 12 horas
    dup=int(g.duplicated(['fecha_muestreo']+measure_cols).sum())
    nulls=int(g[measure_cols].isna().sum().sum())
    comp=min(100,round(len(g)/expected*100,1))
    lag=(global_last-last).days if pd.notna(global_last) else 0
    state='ok' if comp>=90 and lag<=7 else ('incompleto' if comp>=60 else 'critico')
    quality.append({'piezometro':pid,'registros':len(g),'primera_lectura':first.date().isoformat(),'ultima_lectura':last.date().isoformat(),'esperados':expected,'completitud_pct':comp,'duplicados':dup,'nulos':nulls,'estado':state})

meta={
 'fuente':SRC.name,'generado':pd.Timestamp.now().isoformat(),'registros':len(read),
 'piezometros_maestro':int(master['piezometro'].nunique()),'piezometros_con_datos':int(read['piezometro'].nunique()),
 'cuencas':int(master['cuenca'].nunique()),'estaciones':int(master['estacion_de_monitoreo'].nunique()),
 'municipios':int(master['municipio'].nunique()),'acuiferos':int(master['acuifero_monitoreado'].nunique()),
 'fecha_min':read.fecha_muestreo.min().date().isoformat(),'fecha_max':read.fecha_muestreo.max().date().isoformat(),
 'nota_calidad':'LECTURAS conserva fecha sin hora; se esperan 2 registros por día según muestreo de 12 horas.'
}
for name,obj in [('master.json',master_records),('measurements.json',measure_records),('quality.json',quality),('meta.json',meta)]:
    (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print('Generados:',len(master_records),'piezómetros y',len(measure_records),'lecturas')
