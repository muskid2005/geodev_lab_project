# Week 2: Data Note

## Dataset 1: GRID3 NGA – Health Facilities v2.0
* **Source:** [GRID3 Nigeria](https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about)
* **Feature Count:** 13 features (Filtered for Pedro Gbagada)
* **Geometry Type:** Point
* **Key Columns:** `Country`, `State`, `lga`, `ward`
* **Gaps & Missing Values:** No missing data was observed across any of the key columns.

## Dataset 2: GRID3 NGA – Operational Wards v1.0
* **Source:** [GRID3 Nigeria](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about)
* **Feature Count:** 1 feature (Filtered for Pedro Gbagada)
* **Geometry Type:** Polygon
* **Key Columns:** `wardname`
* **Gaps & Missing Values:** No missing data was observed across any of the key columns.

## Dataset 3: Roads
* **Source:** [OpenStreetMap via QGIS (OSM Extractor)](https://www.openstreetmap.org)
* **Feature Count:** 189 features (Filtered for Pedro Gbagada)
* **Geometry Type:** LineString
* **Key Columns:** `name`, `highway`, `surface`, `ref`
* **Gaps & Missing Values:** Approximately 77.25% of the features lack entries in the `name` column, 91.96% are missing a `ref`, 91.53% lack `surface` data, and 4.23% are missing the `highway` attribute.

## Dataset 4: Highways
* **Source:** [OpenStreetMap via QGIS (OSM Extractor)](https://www.openstreetmap.org)
* **Feature Count:** 2 features (Filtered for Pedro Gbagada)
* **Geometry Type:** LineString
* **Key Columns:** `name`, `highway`, `ref`
* **Gaps & Missing Values:** 50% of the features (1 out of 2) lack entries in the `ref` column. No missing values were found in the `name` or `highway` columns.
