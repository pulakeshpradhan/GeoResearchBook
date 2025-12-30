# Part 2: Writing the Structure

A research paper or thesis typically follows a standard structure.

## 1. Introduction

The introduction should follow the "Inverted Pyramid" style:

1. **Broad Concept**: distinct from the general topic (e.g., "Climate change is a global crisis...").
2. **Specific Problem**: Narrow down (e.g., "Urban areas are experiencing Heat Islands...").
3. **Local Context**: Why your study area? (e.g., "Delhi is facing extreme heatwaves...").
4. **Scientific Gap**: What is missing? (e.g., "Previous studies lacked high-resolution thermal analysis...").
5. **Objective**: What will *you* do? (e.g., "This study aims to quantifty UHI using Landsat 8").

**Key Terms**: Define your terms early. If you use "LST", define it as "Land Surface Temperature" the first time.

## 2. Study Area

You must describe *where* you are working.

* **Location**: Latitude/Longitude range.
* **Physiography**: Elevation, soil type, terrain.
* **Climate**: Average rainfall, temperature range (from literature or IMD data).
* **Socio-Economic**: Population, main industries (if relevant).
* **Map**: Always include a location map showing the study area relative to the country/state.

## 3. Methodology

This is the "Recipe" of your research. Another scientist should be able to reproduce your work reading this.

* **Data Sources**:
  * Satellite Data: Sentinel-2 (European Space Agency), Landsat 8 (USGS/NASA).
  * Vector Data: Administrative boundaries (Survey of India or GADM).
* **Software**: Google Earth Engine, ArcGIS, QGIS.
* **Flow Chart**: Create a diagram showing: `Input Data` -> `Preprocessing` -> `Analysis` -> `Output`.

**Example Text**:
> "The land surface temperature was derived using the Thermal Infrared Sensor (TIRS) band of Landsat 8 imagery. The images were pre-processed in Google Earth Engine to remove cloud cover using the 'QA_PIXEL' band..."
