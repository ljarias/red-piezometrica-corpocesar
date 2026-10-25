"use strict";

// Prueba funcional mínima de popupContent mediante DOM simulado y API nativa Node.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const app = fs.readFileSync(path.join(__dirname, "..", "assets", "app.js"), "utf8");
const start = app.indexOf("function popupContent(r){");
const end = app.indexOf("function renderMap(", start);
assert.ok(start >= 0 && end > start, "La función popupContent debe ser identificable");

function createNode(type) {
  return {
    type,
    className: "",
    textContent: "",
    children: [],
    append(...children) { this.children.push(...children); },
  };
}

const document = {
  createElement: createNode,
  createTextNode(value) {
    const node = createNode("#text");
    node.textContent = String(value);
    return node;
  },
};

const popupContent = vm.runInNewContext(
  app.slice(start, end) + "\npopupContent;",
  { document, num: value => String(value) },
);

function flatten(node) {
  return node.textContent + node.children.map(flatten).join("");
}

test("P08: campos del Excel se incorporan como texto y nunca como etiquetas HTML", () => {
  const payload = "<img src=x onerror=alert(1)>";
  const popup = popupContent({
    piezometro: "P-01",
    predio: payload,
    estacion_de_monitoreo: payload,
    cuenca: payload,
    acuifero_monitoreado: payload,
    profundidad: 31,
  });
  assert.equal(popup.type, "div");
  assert.ok(flatten(popup).includes(payload));
  assert.equal(popup.children.filter(node => node.type === "img").length, 0);
  assert.equal(popup.children.find(node => node.type === "b").textContent, payload);
  assert.ok(popup.children.every(node => !("innerHTML" in node)));
});
