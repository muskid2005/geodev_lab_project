import geopandas as gpd

highway = gpd.read_file("data/processed/Highway.gpkg", layer="highway")

first = highway.geometry.iloc[0]

print(type(first))
print(first)
print(f"Valid: {first.is_valid}")
print(f"Centriod: {first.centroid}")