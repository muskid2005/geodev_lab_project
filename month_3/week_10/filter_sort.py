import pandas as pd

pop = pd.read_csv("data/raw/localgovenment_population.csv")
big = pop[pop["population"] > 35000]

print(f"States over 35,000: {len(big)}")

ranked = pop.sort_values("population", ascending=False)
print(ranked.head(3))

pop["population_thousand"] = pop["population"]/1000
print(pop.head(3))

total_population = pop.sum()
print(f"Total Population: {total_population}")