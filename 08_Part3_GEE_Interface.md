# Chapter 3.1: GEE Interface and Basics

We now move to the "Lab" part of the book. Google Earth Engine (GEE) is your tool.

## The Logic of Earth Engine

GEE is a "Client-Server" system.

* **The Client (You)**: You write JavaScript code in the browser.
* **The Server (Google)**: You send that code to Google. Google's supercomputers run it on petabytes of data.
* **The Result**: Google sends back just the map tiles (pictures) or statistics.

## Fundamental Objects

1. **ee.Image**: A single raster (e.g., one photo of Delhi).
2. **ee.ImageCollection**: A stack of rasters (e.g., all photos of Delhi from 2000-2020).
3. **ee.Geometry**: A vector shape (Point, Line, Polygon).
4. **ee.Feature**: A Geometry + Attributes (like a Shapefile row).
5. **ee.FeatureCollection**: A group of Features (like the whole Shapefile).

## Your First Script

Copy this into the Code Editor:

```javascript
// 1. Define a Point
var place = ee.Geometry.Point([77.2, 28.6]); // Delhi

// 2. Load an Image (SRTM Elevation)
var image = ee.Image("USGS/SRTMGL1_003");

// 3. Add to Map
Map.centerObject(place, 9);
Map.addLayer(image, {min: 0, max: 1000}, "Elevation");
```
