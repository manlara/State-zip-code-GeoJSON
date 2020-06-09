# example
# python lines_geojson.py --filename ak_alaska_zip_codes_geo.min.json.lines
# creates ak_alaska_zip_codes_geo.min.json.lines.geojson
import os
import argparse
import json

def main(filename):
    features = []
    with open(filename) as f:
        for line in f:
            features.append(json.loads(line))
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    with open(filename+".geojson", "w") as f:
        json.dump(geojson, f)

if __name__ == "__main__":
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument("--filename", type=str, help="name of geojson file to turn into lines")
    args = main_parser.parse_args()
    main(args.filename)
