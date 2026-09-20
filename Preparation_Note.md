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
