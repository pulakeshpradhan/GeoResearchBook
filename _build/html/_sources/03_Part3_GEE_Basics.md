# Part 3: Analysis (Google Earth Engine)

This section covers the technical implementation of your research using Google Earth Engine (GEE). It assumes no prior coding knowledge.

## Why GEE?

Traditional GIS requires downloading huge files. GEE processes data in the cloud.

## Basic Javascript for GEE

**1. The "Hello World"**

```javascript
print("Research Started!");
```

**2. Variables**
Containers for data.

```javascript
var city = "Bhubaneswar";
var population = 1000000;
```

**3. Loading an Image**

```javascript
var image = ee.Image("USGS/SRTMGL1_003"); // Digital Elevation Model
Map.addLayer(image, {min:0, max:1000}, "Elevation");
```

**4. Loading a Collection**
A stack of images.

```javascript
var collection = ee.ImageCollection("COPERNICUS/S2_SR");
```

**5. Filtering**
Narrowing down the data.

* `.filterBounds(geometry)`: Space
* `.filterDate('2023-01-01', '2023-05-01')`: Time
* `.filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))`: Quality

In the next chapters, we will perform complete analyses for **Forest Loss**, **Urban Heat Islands**, and **Flood Mapping**.
