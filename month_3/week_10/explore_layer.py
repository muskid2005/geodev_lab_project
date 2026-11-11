import geopandas as gpd

print(gpd.list_layers("data/processed/Highway.gpkg"))

highway = gpd.read_file("data/processed/Highway.gpkg", layer="highway")

print(highway.head())
print(f"Row and Column: {highway.shape}")
print(highway.geom_type.value_counts())
print(f"CRS {highway.crs}")
print(f"Bounds {highway.total_bounds}")
