# State-zip-code-GeoJSON

See this repo for the [source](https://github.com/OpenDataDE/State-zip-code-GeoJSON)

It is often convenient to work with lines of geojson data for filtering and modifiying. This repo was created for just that purpose. The [tippecanoe package](https://www.npmjs.com/package/tippecanoe) is what converts the geojson into a file of just lines of geojson features.

To convert a file of geojson lines back to a FeatureCollection run `lines_geojson.py` with a `filename` flag set with the name of the geojson lines file to convert. Example below

`python lines_geojson.py --filename ak_alaska_zip_codes_geo.min.json.lines`