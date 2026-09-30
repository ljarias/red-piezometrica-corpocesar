#!/usr/bin/env bash
python3 scripts/vendor_frontend.py || exit 1
python3 -m http.server 8000
