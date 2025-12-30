# Project 2: Urban Heat Island Analyzer (Detailed)

In this project, we explore the connection between urban development and temperature. This is crucial for planning livable cities in a warming world.

## The Objective

We want to prove that concrete and asphalt make cities hotter, while parks and lakes keep them cool.
We will calculate the **Land Surface Temperature (LST)** of your city using the Landsat 8 satellite.

---

## Step 1: Understanding the Sensor

Cameras usually capture Red, Green, and Blue light. But Landsat 8 has a special "Thermal Infrared Sensor" (TIRS). It measures **HEAT** radiation, not light.

* **Band 10 (ST_B10)**: This band records the temperature of the ground.

---

## Step 2: The Code (Explained Line-by-Line)

### 2.1 Choose Your City

Let's pick New Delhi, India, known for extreme heatwaves. You can change these coordinates to your own city!

```javascript
// Creates a point geometry
var city = ee.Geometry.Point([77.2090, 28.6139]);

// Centers the map on the city
Map.centerObject(city, 11);
```

### 2.2 Finding the Right Images

We need images from **Summer**, because that is when the heat island effect is strongest.
We also need images with **No Clouds**, because clouds block the thermal sensor (they are cold).

```javascript
var dataset = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
    .filterBounds(city)                         // Only images covering Delhi
    .filterDate('2023-04-01', '2023-06-30')     // April to June (Peak Summer)
    .filter(ee.Filter.lt('CLOUD_COVER', 10));   // Keeping it clear
    
print("Number of images found:", dataset.size());
```

### 2.3 Selecting and Reducing

We might find 5 or 6 images. Let's take the **Median** of all of them. This creates a "typical" summer day image and removes any stray noise.
We specifically select band `ST_B10` (Surface Temperature Band 10).

```javascript
var thermal = dataset.select('ST_B10').median();
```

### 2.4 Converting to Celsius (The Math Part)

The satellite doesn't give us "Celsius" directly. It gives us a "Digital Number" (DN). We simply follow the math formula provided in the USGS Landsat User Manual.

**Formula**:

1. `Kelvin = (DN * 0.00341802) + 149.0`
2. `Celsius = Kelvin - 273.15`

In Earth Engine coding:

```javascript
// Step A: Apply scale factor to get Kelvin
var kelvin = thermal.multiply(0.00341802).add(149.0);

// Step B: Convert Kelvin to Celsius
var celsius = kelvin.subtract(273.15);
```

### 2.5 Visualizing the Heat

We need a color palette that makes sense:

* **Blue/Cyan**: Cool areas (25°C - 35°C) -> Water, Parks
* **Yellow**: Warm areas (35°C - 40°C) -> Residential
* **Red**: Hot areas (40°C +) -> Industrial, Concrete, Airport

```javascript
var visParams = {
  min: 30, // Minimum expected temp
  max: 48, // Maximum expected temp (Delhi gets HOT!)
  palette: ['blue', 'cyan', 'yellow', 'orange', 'red']
};

Map.addLayer(celsius, visParams, 'Land Surface Temperature (C)');
```

---

## Step 3: Exploration

Run the script.
Now, use the **Inspector Tab** (Top Right) and click around the map.

1. Click on a **Park** (like Lodhi Gardens). The temperature might be ~35°C.
2. Click on the **Airport** (Palam) or a dense **Concrete/Asphalt** area. The temperature might be ~45°C.

**Conclusion**: That 10°C difference is the Urban Heat Island effect. Planting more trees is the solution!
