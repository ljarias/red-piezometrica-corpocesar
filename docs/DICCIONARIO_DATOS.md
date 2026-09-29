# Diccionario de datos público

## master.json
| Campo | Descripción | Tipo | Publicación |
|---|---|---|---|
| cuenca | Cuenca hidrográfica | texto | Pública |
| departamento | Departamento | texto | Pública |
| municipio | Municipio | texto | Pública |
| estacion_de_monitoreo | Código de estación | texto | Pública |
| piezometro | Identificador del piezómetro | texto | Pública |
| longitud | Coordenada geográfica | decimal | Sujeta a clasificación institucional |
| latitud | Coordenada geográfica | decimal | Sujeta a clasificación institucional |
| z | Cota de referencia | decimal | Pública técnica |
| predio | Predio asociado | texto | Sujeta a clasificación institucional |
| fecha_construccion | Fecha de construcción | fecha | Pública técnica |
| profundidad | Profundidad del piezómetro | decimal | Pública técnica |
| acuifero_monitoreado | Unidad acuífera | texto | Pública técnica |
| nivel_estatico_base | Nivel estático base | decimal | Pública técnica |
| nivel_estatico_msnm | Nivel base absoluto | decimal | Pública técnica |
| profundidad_sensor | Profundidad del sensor | decimal | Pública técnica |
| serial_sensor | Serial del sensor | texto | Sujeta a clasificación institucional |
| muestreo | Frecuencia declarada | texto | Pública técnica |
| ficha/disenos_mecanicos/fotos | Recursos documentales | URL HTTPS | Sujeta a clasificación institucional |

Campos expresamente excluidos del artefacto público: propietario, x, y y fecha_prueba_bombeo.

## measurements.json
| Campo | Descripción | Tipo |
|---|---|---|
| piezometro | Referencia al maestro | texto |
| fecha | Fecha de lectura | YYYY-MM-DD |
| altura_columna_de_agua | Altura de columna de agua | decimal/nulo |
| nivel_estatico | Nivel estático | decimal/nulo |
| temperatura | Temperatura | decimal/nulo |
| conductividad | Conductividad | decimal/nulo |

## quality.json
Resume registros, rango temporal, esperados, completitud, duplicados, nulos y estado por piezómetro.

## meta.json
Manifiesto del dataset: fuente, hash SHA-256, versión de esquema/ETL, fecha de generación, conteos, rango temporal y nota metodológica.
