import geopandas as gpd

highway = gpd.read_file("data/processed/Highway.gpkg", layer="highway")
highway.to_file("data/processed/week10_outputs.gpkg", layer="highway_copy")
highway.drop(columns="geometry").to_csv("month_3/week_10/highway_table.csv", index=False)
print(gpd.list_layers("data/processed/week10_outputs.gpkg"))