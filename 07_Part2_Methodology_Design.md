# Chapter 2.3: Methodology Design

The Methodology section allows reproducibility. It must be detailed enough that another researcher could repeat your experiment exactly.

## Research Design

Define your overall approach:

1. **Exploratory**: When the problem is not clearly defined (e.g., "Identifying potential drivers of unknown forest die-back").
2. **Descriptive**: "Snapshot" of a situation (e.g., "Mapping current flood extents").
3. **Explanatory**: Testing cause-and-effect (e.g., "Does road construction *cause* deforestation?").

## Data Acquisition (Primary vs. Secondary)

### 1. Primary Data

Data collected first-hand by the researcher.

* **Field Surveys**: Ground Truth points collected using GPS (vital for classification accuracy assessment).
* **Questionnaires**: Socio-economic data.
* **Lab Analysis**: Soil pH, Water quality samples.

### 2. Secondary Data (Remote Sensing)

Data collected by others (Satellites/Agencies).

| Dataset | Sensor | Resolution | Purpose | Source |
| :--- | :--- | :--- | :--- | :--- |
| **Sentinel-2** | MSI | 10m/20m | Land Use/Vegetation | ESA (Copernicus) |
| **Landsat 8/9** | OLI/TIRS | 30m/100m | Long-term Trends/LST | USGS |
| **Sentinel-1** | SAR (C-band) | 10m | Flood/All-weather | ESA |
| **SRTM / ALOS** | Radar | 30m / 12.5m | Elevation/Slope (DEM) | NASA / JAXA |
| **CHIRPS** | Rain Gauge+Sat | 0.05° | Rainfall Trends | UCSB |

## Methodological Workflow (The Flowchart)

Every methodology needs a graphical workflow. Standard stages:

1. **Pre-processing**: Geometric correction, Atmospheric correction (Top-of-Atmosphere -> Surface Reflectance), Cloud Masking.
2. **Processing**: Calculation of indices (NDVI/NDWI), Image Classification (Random Forest/SVM), Statistical extraction.
3. **Post-processing**: Accuracy Assessment (Confusion Matrix), Map Layout, Graph plotting.
