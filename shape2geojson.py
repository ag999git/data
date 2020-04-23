# Script to convert shape file(s) to geoJSON
import geopandas as gpd
path2shp = r'your_shape_file.shp'  # Path to shape file (must be .shp)
file = gpd.read_file(path2shp)
path2json = r'your_geojson_file.json'  # Path geojson file (must be .json)
file.to_file(path2json, driver="GeoJSON")
