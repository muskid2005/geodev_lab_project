# My GeoDev Lab Africa project
- Which wards in Shomolu LGA, Lagos state are more than 5km from a health facility?
- Built over twelve months with GeoDev Lab Africa, Cohort One.
- See project-brief.md for the full brief


# WEEK 1 project brief

## The question

Which areas in Pedro Gbagada, Lagos State are more than 5km from a health facility?

## Study Area
Pedro Gbagada, Lagos State, Nigeria.

## The data I need

1. Nigeria Ward Level boundaries - GRID 3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-wards-v1-0/about - 128 mb
2. Nigeria LGA boundaries  - GRID 3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about - 2.6 mb
3. Nigeria State boundaries - GRID 3 - https://data.grid3.org/datasets/GRID3::grid3-nga-operational-state-boundaries-/about - 645 kb
4. Health Facilities Location in Pedro Bagada, Lagos State, Nigeria - GRID 3 - https://data.grid3.org/datasets/GRID3::grid3-nga-health-facilities-v2-0/about - 4.7 mb
5. Road Data OSM via QuickOSM plugin extracted for my study area


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


# Week 3 Data Preparation Note

## 1. CRS Chosen

**CRS:** WGS 84 / UTM Zone 31N (EPSG:32631)

**Why:** Lagos falls within UTM Zone 31N, and a projected CRS makes it easier to calculate distances and areas because measurements are in metres.

## 2. What I Reprojected

I reprojected:

* Settlement data
* Lagos study-area boundary

Both were reprojected to **WGS 84 / UTM Zone 31N (EPSG:32631)** so that the datasets use the same working coordinate system.

## 3. What I Clipped

I used the **Lagos boundary/study area** as the clipping boundary.

The settlement data was clipped to the Lagos study area so that only features within the area of interest would be used for analysis.

## 4. Five Quality Checks

### CRS consistency

**Result:** The working layers were checked to ensure they use the same projected CRS.

**Decision:** Passed. The working CRS is EPSG:32631.

### Geometry validity

**Result:** The available vector layers were checked for obvious invalid or broken geometries.

**Decision:** No obvious geometry problems were identified.

### Study-area extent

**Result:** The data was checked against the Lagos study-area boundary.

**Decision:** Passed for the available data. Features outside the study area were excluded through clipping.

### Attribute completeness

**Result:** The available settlement data was checked to confirm that the required information was present.

**Decision:** Some required data could not be fully obtained and was flagged for follow-up.

### Data/source availability

**Result:** Several sources were tested. Settlement Data Grid 3 returned a download failure, Humanitarian data mainly provided points, QuickOSM did not return the expected dataset, and the ArcGIS API returned a connection error.

**Decision:** These issues were flagged rather than using unsuitable replacement data.

## 5. Problems Found

The main problem was obtaining the required settlement dataset. Settlement Data Grid 3 failed to download, while other attempted sources did not provide the required dataset in the expected form.

These issues were **flagged for follow-up** rather than treated as successfully resolved.

## 6. Analysis-Ready File

The analysis-ready data is stored in my local pc at:

`"C:\Users\HELLO\Documents\GIS DATA\GEODev_Lab\task1\residential.gpkg"`

The final GeoPackage contains the prepared spatial data for the study area.


# Month 1 Summary: Spatial Analysis Report

## Research Question
Which settlements fall within a 200-meter buffer of waterways across administrative wards in Oyo State?

## Spatial Operation
- **Operation Run:** 200-Meter Buffer & Spatial Intersection
- **Reasoning:** A 200m buffer was generated around the waterway network to establish the hazard exposure zone. An intersection/spatial join was then performed with the settlement and ward layer to extract only the settlement features falling directly within this distance threshold for localized risk assessment.

## Expectations vs. Results
- **Pre-Analysis Expectations:** Expected roughly 1,500 to 2,000 settlements to intersect the 200m waterway buffer given the settlement density along river corridors in Oyo.
- **Actual Results & 4-Way Verification:**
  1. **Visual Map Check:** Confirmed visually on the map canvas that selected settlement points lie strictly within the 200m buffered waterway polygon zones.
  2. **Row Count Check:** Out of **11,557** total recorded settlement features, exactly **1,730** features fell within the 200m buffer.
  3. **Manual Feature Verification:** Inspected individual settlements by hand in the attribute table; coordinates and spatial locations accurately match the buffer overlap.
  4. **Empty Geometry Check:** Filtered and verified that there are **0** empty or null geometries in the output layer.

## Surprises / Findings
- A significant proportion (~15%) of the total settlements in the region are situated within the 200m buffer zone, highlighting high vulnerability to potential riverine flooding.
- Certain wards exhibited clustered settlement patterns right along stream edges rather than uniform distribution across the ward boundaries.

## Data Gaps
- Detailed river flow/discharge rates and historical flood extent polygons to refine the risk boundary beyond a fixed Euclidean distance buffer.
- Population density data at the settlement level to estimate the actual number of individuals at risk within the 200m buffer zone.


# Month 2 (Week 5) : Preparation of environment, and early Python 
- week 5: I setup python, vs code and terminal, hello.py runs.

