# Project 1: Tracking Forest Loss (Detailed)

In this project, we will build a scientific-grade application to monitor deforestation. We will not just write code; we will understand *why* we are writing it.

## The Objective

We want to answer a simple question: **"Where exactly has the forest disappeared in the last 20 years?"**
To answer this, we need a dataset that has looked at trees every year. The *Hansen Global Forest Change* dataset is the gold standard for this.

---

## Step 1: Divide and Conquer

Coding is about breaking big problems into small steps.

1. **Where?** We need to define our study area (Region of Interest).
2. **What?** We need to load the Forest Change dataset.
3. **When?** The dataset already contains time information (Year of loss).
4. **How?** We will mask the data to show only the *loss* and visualize it with colors.

---

## Step 2: The Code (Explained Line-by-Line)

Copy the following code blocks into your Code Editor (`code.earthengine.google.com`).

### 2.1 Setting the Stage

First, we tell the map where to look. We are choosing a location in the Amazon Rainforest notorious for "fishbone" deforestation patterns.

```javascript
// Map.setCenter(longitude, latitude, zoom_level)
// Zoom level 1 is whole world, 15 is street level. 7 is good for a state/region.
Map.setCenter(-60.0, -3.0, 7); 
```

### 2.2 Loading the Data

We use the `ee.Image` constructor. The weird string `"UMD/hansen/global_forest_change_2023_v1_11"` is simple the **Asset ID**. Think of it like a URL or phone number for the dataset on Google's servers.

```javascript
var gfc = ee.Image("UMD/hansen/global_forest_change_2023_v1_11");

// Let's see what is inside! (Check the Console tab)
print("Hansen Data:", gfc);
```

*If you check the console, you will see bands like `treecover2000`, `loss`, `gain`, and `lossyear`. These are our ingredients.*

### 2.3 Visualizing the "Before" State

Before looking at destruction, let's look at the forest as it was in the year 2000.
We select the `treecover2000` band. It has values from 0 (No tree) to 100 (Dense forest).

```javascript
var treeCover = gfc.select(['treecover2000']);

// We use a palette from Black (0%) to Green (100%)
// This makes the dense Amazon look bright green.
Map.addLayer(treeCover, {min: 0, max: 100, palette: ['black', 'green']}, 'Forest Cover 2000');
```

### 2.4 The Magic: "Loss Year"

The band `lossyear` is very clever.

* If a pixel has a value of `0`, it means **NO LOSS** occurred.
* If a pixel has a value of `1`, it means loss occurred in **2001**.
* If a pixel has a value of `20`, it means loss occurred in **2020**.

We want to visualize this range.

```javascript
var lossYear = gfc.select(['lossyear']);
```

### 2.5 Masking (Transparency)

If we just display `lossYear` now, the map will be black because most pixels are `0` (no loss). We want to make those pixels **invisible** so we can see the map underneath.
We use the `.selfMask()` function.

* It looks at the value of the pixel.
* If value is `0` -> It makes transparency `0%` (Invisible).
* If value is `>0` -> It keeps it visible.

```javascript
var lossMasked = lossYear.selfMask();
```

### 2.6 The Final Visualization

We want to color-code the years.

* Old deforestation (early 2000s) -> **Yellow**
* New deforestation (recent years) -> **Red**
This helps us see the *progression* of damage.

```javascript
var lossVis = {
  min: 1,  // Start year 2001
  max: 23, // End year 2023
  palette: ['yellow', 'orange', 'red']
};

Map.addLayer(lossMasked, lossVis, 'Forest Loss Progression (2001-2023)');
```

---

## Step 3: Analysis

Run the code. Look at the red lines extending from the yellow lines.

* **Fishbone Pattern**: Roads are built (often yellow/older).
* **Expansion**: Farmers/Loggers move deeper into the forest from the road (orange/red).

This simple script visualizes terabytes of data to tell a powerful story about human impact.
