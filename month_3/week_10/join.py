import pandas as pd
import geopandas as gpd

facilities = pd.read_csv("data/raw/health_facilities.csv")
pop = pd.read_csv("data/raw/localgovenment_population.csv")

first_try = facilities.merge(pop, left_on= "lga", right_on="lganame", how="left")
matched = first_try["population"].notna().sum()

print(f"Matched on first try: {matched} of {len(facilities)}")

def clean_name(name):
    return name.strip().upper().replace("-", " ")

facilities["join_key"] = facilities["lga"].apply(clean_name)
pop["join_key"] = pop["lganame"].apply(clean_name)

joined = facilities.merge(pop, on="join_key", how="left")
matched = joined["population"].notna().sum()

print(f"Matched after cleaning: {matched} of {len(facilities)}")
print(joined[["lga", "population"]])

