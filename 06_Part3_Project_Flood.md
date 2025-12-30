# Project 3: Flood Mapping with Radar (Detailed)

This is the most advanced and impactful project. We will use **Sentinel-1 Radar (SAR)** to map floods. This technology is used by the UN and Governments during disasters because it works **at Night** and **through Clouds**.

## The Objective

We want to map the extent of a flood event (e.g., Pakistan 2022 dataset).
The logic is simpler than you think: **Water is smooth.**

* **Radar Signal hits Land (Rough)** -> Bounces back to satellite -> Image looks **Bright**.
* **Radar Signal hits Water (Smooth)** -> Bounces away (Mirror effect) -> Image looks **Dark**.

So, we look for pixels that were **Bright (Land)** before the flood, but became **Dark (Water)** during the flood.

---

## Step 1: The Setup

We need to define the study area and the dates.

* **Before Flood**: A dry period (e.g., Jan 2022)
* **During Flood**: The peak flood period (e.g., Aug 2022)

```javascript
// A region in Sindh, Pakistan
var geometry = ee.Geometry.Polygon([
  [67.5, 26.0], [68.5, 26.0], [68.5, 27.0], [67.5, 27.0]
]);

Map.centerObject(geometry, 9);
```

---

## Step 2: Loading Sentinel-1

Sentinel-1 is a complex beast. We need to filter it carefully to get consistent data.

* `VV`: Vertical Transmit, Vertical Receive (Polarization). Good for water detection.
* `IW`: Interferometric Wide Swath. The standard mode for land.

```javascript
var collection = ee.ImageCollection('COPERNICUS/S1_GRD')
    .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
    .filter(ee.Filter.eq('instrumentMode', 'IW'));
```

---

## Step 3: Getting "Before" and "During" Images

We create two mosaics. A **Mosaic** stitches together multiple images to cover our whole area.

```javascript
// 1. Before Image (Dry Season)
var beforeFlood = collection
    .filterDate('2022-01-01', '2022-02-28') 
    .mosaic()
    .clip(geometry);

// 2. During Image (Flood Season)
var duringFlood = collection
    .filterDate('2022-08-20', '2022-08-31')
    .mosaic()
    .clip(geometry);
```

---

## Step 4: Smoothing (De-speckling)

Radar images have a salt-and-pepper noise called "Speckle". We must smooth it out to avoid false detections. We use a `focal_mean` filter (a blur).

```javascript
var smoothingRadius = 50; // 50 meters blur

var beforeFiltered = beforeFlood.select('VV').focal_mean(smoothingRadius, 'circle', 'meters');
var duringFiltered = duringFlood.select('VV').focal_mean(smoothingRadius, 'circle', 'meters');
```

---

## Step 5: Detecting Change

We compare the two images.
In Radar math (Decibels), subtraction or division is used to find ratio.
Here, we check if the value dropped significantly.

**The Threshold**: `1.25` is a common scientific threshold for this ratio.

* If `Before / During > 1.25`, it means the "Before" was much brighter than "During".
* This implies Land became Water.

```javascript
// Calculate Ratio: Before / During
var ratio = beforeFiltered.divide(duringFiltered);

// Apply Threshold
// Result is 1 (Flood) or 0 (No Flood)
var flooded = ratio.gt(1.25).selfMask();
```

---

## Step 6: Visualization

Let's verify our work.

1. **Layer 1**: The "Before/Dry" image (Greyscale).
2. **Layer 2**: The "Flooded" pixels (Bright Blue).

```javascript
// Radar visualized in Greyscale (Values usually -25 to 0)
Map.addLayer(beforeFiltered, {min: -25, max: 0}, 'Before Flood (Dry)', 0);

// Flood visualized in Blue
Map.addLayer(flooded, {palette: 'cyan'}, 'Flooded Areas');
```

## Conclusion

You have just built a disaster response tool!
Inspect the map. The cyan areas show where the Indus River overflowed and created a massive inland sea. This exact technique is used by the UN Spider program to generate emergency maps.
