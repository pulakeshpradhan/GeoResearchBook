# Chapter 2.4: Designing the Methodology

The methodology is the "Recipe". It must be so clear that a stranger can bake your cake.

## 1. The Methodological Flowchart

A diagram is worth 1000 words. Draw standard shapes:

* **Ovals**: Start/End.
* **Rectangles**: Processes (e.g., "Atmospheric Correction").
* **Parallelograms**: Data I/O (e.g., "Sentinel-2 Image").
* **Diamonds**: Decisions (e.g., "Cloud Cover < 10%?").

**Structure**:
`[Data Input] -> [Pre-Processing] -> [Analysis] -> [Validation] -> [Output]`

## 2. Describing Data Sources (The Table)

Always use a table.

| Satellite | Sensor | Spatial Res | Temporal Res | Source | Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sentinel-2** | MSI | 10m | 5 Days | ESA | LULC Classification |
| **Landsat 8** | TIRS | 30m (100m) | 16 Days | USGS | LST Retrieval |
| **SRTM** | Radar | 30m | Static | NASA | Slope/Aspect |

## 3. Writing the Method (The "How")

Do not write a tutorial ("Click File -> Open"). Write the *science*.

* **Bad**: "I opened the image in ArcGIS and clicked the Buffer tool."
* **Good**: "A proximity analysis was conducted by generating a 500m Euclidean buffer around the major road network to assess the zone of influence."

## 4. Software and Tools

Mention the tools used.

* "The geospatial analysis was performed using **Google Earth Engine (GEE)**, utilizing its cloud computing capabilities for processing multi-temporal datasets."
* "Statistical correlations were computed using **Python (Pandas/Scikit-learn)**."
* "Final map composition was done in **QGIS 3.28**."
