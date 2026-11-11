# Week 10: GeoPandas, layers as tables

## What this folder contains
- `explore_pandas.py`: first look at the ward and population tables, sorting, and checking statistical summaries.
- `explore_layer.py`: inspects spatial files, lists layers using pyogrio, and checks coordinate reference systems.
- `coords_to_points.py`: converts raw coordinate CSV data into spatial point geometries and saves as a GeoPackage.
- `filter_sort.py`: filters and sorts tabular data based on specific administrative criteria.
- `goem_props.py`: analyzes geometric properties of spatial features like bounding boxes and extents.
- `join.py`: cleans string attributes and joins population data to administrative ward polygons.
- `make_map.py`: plots and saves the final thematic map visualization.
- `save_outputs.py`: demonstrates multi-format exporting of spatial layers and tables.
- `facilities_map.png`: map of health facilities by ward.
- `wards_table.csv`: exported table of ward attributes.

## How to run it
From the repository root, you can run individual scripts using `uv run`:
uv run month-03/week-10/explore_pandas.py
uv run month-03/week-10/explore_layer.py
uv run month-03/week-10/coords_to_points.py
uv run month-03/week-10/filter_sort.py
uv run month-03/week-10/goem_props.py
uv run month-03/week-10/join.py
uv run month-03/week-10/make_map.py
uv run month-03/week-10/save_outputs.py

## What i found
- The analysis reveals the spatial distribution and concentration of health facilities relative to administrative boundaries and population data in Ibadan North. Successfully merging the demographic data with spatial layers provides clear insights into regional infrastructure coverage and resource allocation.

## What went wrong and how I fixed it
- I didn't have enough data to work with properly, so I had to find and download new datasets. Additionally, initial join attempts and file saves failed due to mismatched text formatting and missing output directories, which I fixed by writing a custom string-cleaning function and ensuring proper path handling.
