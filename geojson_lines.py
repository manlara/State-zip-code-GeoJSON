import os
import argparse

def main(filename):
    cmd = "tippecanoe-json-tool {filename} > {filename}.lines".format(filename=filename)
    os.system(cmd)

if __name__ == "__main__":
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument("--filename", type=str, help="name of geojson file to turn into lines")
    args = main_parser.parse_args()
    main(args.filename)
