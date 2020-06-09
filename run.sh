#!/bin/bash

for f in *.min.json; do
    echo "$f"
    python geojson_lines.py --filename $f
done