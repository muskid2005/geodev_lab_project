import pandas as pd
# import geopandas as gpd

pop = pd.read_csv("data/raw/state_population.csv")

print(pop.head())
print(f"Shapes: {pop.shape}")
print(f"Columns: {list(pop.columns)}")
print(pop.dtypes)
print(pop["population"].describe())