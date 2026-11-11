import geopandas as gpd
import matplotlib.pyplot as plt

road = gpd.read_file("data/processed/Highway.gpkg", layer="highway")
facilities = gpd.read_file("data/processed/facilities.gpkg", layer="facilities")

fig, ax = plt.subplots(figsize=(7, 8))
road.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Health facilities nigeria")
ax.set_axis_off()

fig.savefig("month_3/week_10/facilities_map.png", dpi=150, bbox_inches="tight")
print("Map saved")