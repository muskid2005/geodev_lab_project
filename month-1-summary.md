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
