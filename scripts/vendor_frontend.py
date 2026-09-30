from __future__ import annotations

import base64
import hashlib
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ASSETS = [
    {
        "url": "https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js",
        "path": ROOT / "assets/vendor/chartjs/chart.umd.min.js",
        "sha384": "vsrfeLOOY6KuIYKDlmVH5UiBmgIdB1oEf7p01YgWHuqmOHfZr374+odEv96n9tNC",
    },
    {
        "url": "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js",
        "path": ROOT / "assets/vendor/leaflet/leaflet.js",
        "sha384": "cxOPjt7s7Iz04uaHJceBmS+qpjv2JkIHNVcuOrM+YHwZOmJGBXI00mdUXEq65HTH",
    },
    {
        "url": "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
        "path": ROOT / "assets/vendor/leaflet/leaflet.css",
        "sha384": "sHL9NAb7lN7rfvG5lfHpm643Xkcjzp4jFvuavGOndn6pjVqS6ny56CAt3nsEVT4H",
    },
    {
        "url": "https://unpkg.com/leaflet@1.9.4/dist/images/layers.png",
        "path": ROOT / "assets/vendor/leaflet/images/layers.png",
        "sha384": null,
    },
    {
        "url": "https://unpkg.com/leaflet@1.9.4/dist/images/layers-2x.png",
        "path": ROOT / "assets/vendor/leaflet/images/layers-2x.png",
        "sha384": null,
    },
    {
        "url": "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
        "path": ROOT / "assets/vendor/leaflet/images/marker-icon.png",
        "sha384": null,
    },
    {
        "url": "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
        "path": ROOT / "assets/vendor/leaflet/images/marker-icon-2x.png",
        "sha384": null,
    },
    {
        "url": "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
        "path": ROOT / "assets/vendor/leaflet/images/marker-shadow.png",
        "sha384": null,
    },
]


def digest_sha384(data: bytes) -> str:
    return base64.b64encode(hashlib.sha384(data).digest()).decode("ascii")


def main() -> int:
    for asset in ASSETS:
        target: Path = asset["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(asset["url"], timeout=30) as response:
            data = response.read()
        actual = digest_sha384(data)
        expected = asset["sha384"]
        if expected is not None and actual != expected:
            raise RuntimeError(
                f"Integridad invalida para {asset['url']}: esperado {expected}, recibido {actual}"
            )
        if expected is None:
            print(f"[HASH] {target.relative_to(ROOT)} · SHA-384 {actual}")
        target.write_bytes(data)
        print(f"[OK] {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
