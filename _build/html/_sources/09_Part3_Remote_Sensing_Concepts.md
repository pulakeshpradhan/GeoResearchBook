# Chapter 3.2: Remote Sensing Concepts

To interpret satellite images scientifically, one must grasp the underlying physics of **Electromagnetic Radiation (EMR)**.

## The Electromagnetic Spectrum

Satellites measure reflected or emitted energy.

* **Visible (0.4 - 0.7 µm)**: Blue, Green, Red. Used for true-color visualization.
* **Near Infrared - NIR (0.7 - 1.1 µm)**: The "Vegetation Band". Healthy chlorophyll reflects NIR strongly (the "Red Edge").
* **Shortwave Infrared - SWIR (1.1 - 3.0 µm)**: Sensitive to moisture content in soil and vegetation. Also differentiates clouds from snow.
* **Thermal Infrared - TIR (3.0 - 14.0 µm)**: Measures emitted heat. Used for LST.
* **Microwave (1mm - 1m)**: Active Radar (SAR). Can penetrate clouds (e.g., Sentinel-1).

### Atmospheric Windows

Not all radiation reaches the surface. The atmosphere absorbs specific wavelengths (Water vapor, CO2, Ozone). Satellites are designed to operate in "Atmospheric Windows"—spectral ranges where the atmosphere is transparent.

## The 4 Resolutions

Scientific data quality is defined by four resolutions:

1. **Spatial Resolution**: The size of the ground area represented by one pixel.
    * *High Res*: < 5m (WorldView, Planet).
    * *Medium Res*: 10m - 30m (Sentinel-2, Landsat).
    * *Coarse Res*: > 250m (MODIS).
    * *Trade-off*: Higher resolution usually means smaller file size/swath width.

2. **Spectral Resolution**: The number and width of spectral bands.
    * *Panchromatic*: 1 broad band (Black & White).
    * *Multispectral*: 3-15 bands (Landsat/Sentinel).
    * *Hyperspectral*: Hundreds of narrow bands (Hyperion). Distinction between specific mineral types.

3. **Radio-metric Resolution**: The sensitivity of the sensor (Bit Depth).
    * *8-bit*: 0-255 values.
    * *12-bit*: 0-4095 values (Landsat 8).
    * *Why it matters*: Higher radiometric resolution allows detection of subtle differences in brightness (e.g., distinguishing details in dark shadows).

4. **Temporal Resolution**: The revisit time.
    * *Sentinel-2*: 5 days.
    * *Landsat*: 16 days.
    * *MODIS*: Daily (High temporal, low spatial).

## Spectral Indices

Mathematical combination of bands to highlight features.

### Normalized Difference Vegetation Index (NDVI)

$$NDVI = \frac{NIR - Red}{NIR + Red}$$

* **Range**: -1 to +1.
* **Science**: Plants absorb Red (for photosynthesis) and reflect NIR (structure).

### Normalized Difference Water Index (MNDWI)

$$MNDWI = \frac{Green - SWIR}{Green + SWIR}$$

* **Science**: Water absorbs SWIR strongly but reflects Green. Better than NDWI for urban areas.
