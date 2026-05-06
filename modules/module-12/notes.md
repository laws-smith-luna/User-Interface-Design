# Module 12 - Information Visualization

**Start:** 4/7/2026
**Topic:** Information Visualization
**Individual Assignment:** Critique an Information Visualization

## Opening Case: John Snow and the 1854 London Cholera Outbreak

- Broad Street, London, 1854: 500+ deaths in 10 days, many within hours
- Disease widely suspected to be airborne; 75%+ of inhabitants fled
- John Snow (English physician) investigated cause
- Built a visualization overlaying death counts on a map of London
- Pattern revealed: strong concentration around a pump on Broad Street
- Convinced city board to remove the pump handle and close the well -> epidemic ended
- Solved centuries-old question of cholera transmission via water
- Helped found modern epidemiology

### Why Snow's Visualization Worked
1. **Appropriate context for cause and effect** - plotted data on a map that included the well location, revealing proximity as cause
2. **Quantitative comparisons** - tested alternative hypotheses (e.g., brewery had fewer nearby deaths)
3. **Considered alternatives and contrary cases** - investigated outlier deaths far from the pump and traced them back to it

## Module Goal
Learn how information visualization amplifies cognition by leveraging the visual processing system to gain insights and solve problems.

## Notes

### Amplifying Cognition
Information visualization can amplify cognition by:
1. Increasing the **memory** and **processing** resources available to users
2. Reducing the **search** for information
3. Using visual representations to enhance the detection of **patterns**
4. Enabling **perceptual** inference
5. Using perceptual **attention** mechanisms for monitoring
6. Encoding information in a **manipulable** medium

### Classic Example: Minard's Map of Napoleon's Russian Campaign (1812)
Famous multi-variable visualization showing the campaign to move Napoleon's army into Russia - encodes army size, geographic path, direction, temperature, and time in one image.

### Designing an Information Visualization (Pipeline)
Raw Data -> [Data Transformations] -> Data Tables -> [Visual Mappings] -> Visual Structures -> [View Transformations] -> Views
- Loop closed by **Human Interaction** at every stage
- Driven by user's **task**

### Types of Raw Data
- **Nominal** - unordered set *without* a quantitative value (gender, hair color)
- **Ordinal** - *ordered* set, no meaning assigned to differences (very unhappy -> very happy)
- **Quantitative** - *numeric* value (height, weight, distance)

### Data Transformations
- **Classing / binning:** Quantitative -> Ordinal (map ranges to classes; histograms count items per class)
- **Sorting:** Nominal -> Ordinal (add order to sets)
- **Descriptive statistics:** mean, average, median, max, min...

### Visual Structures (3 components)
1. **Spatial substrate** - axes that divide space (unstructured, nominal, ordinal, quantitative); composition via multiple orthogonal axes (2D scatterplot, 3D)
2. **Marks** - Points (0D), Lines (1D), Areas (2D), Volumes (3D)
3. **Marks' graphical properties** - Spatial (position, size, orientation) and Object (grayscale, color, texture, shape)

### Effectiveness of Graphical Properties
Different properties work better for Quantitative (Q), Ordinal (O), or Nominal (N) data:
- **Position** - good for all (Q, O, N)
- **Size** - best for Q/O
- **Grayscale** - good for O
- **Color, texture, shape** - best for N
- Filled circle = good fit; open circle = poor fit

### Animation
- Visualization can change over time
- Encoding data as a function of time often **not effective** - hard to make direct comparisons
- More effective: animate **transitions** between user-configured states (before -> after)

### Common Visualization Types

**Time series / multi-component:**
- **Stacked Graph** - supports visual summation of multiple components
- **Small Multiples** - separate comparison of data series; better legibility than overlaying in one plot

**Geographic:**
- **Choropleth Map** - groups data by area, maps to color
- **Cartogram** - encodes two variables with size & color (distorts geography)
- **Election-style maps** - color by category per region

**Hierarchies / networks:**
- **Node Link Diagram** - tree/graph structure
- **Dendrogram** - leaf nodes on edge of circle (radial hierarchy)
- **Treemaps** - nested rectangles, area encodes value
- **Force-directed Layout** - edges as springs, finds least-energy configuration
- **Arc Diagram** - identifies cliques & bridges with right node order
- **Adjacency Matrix** - grid showing connections between nodes
