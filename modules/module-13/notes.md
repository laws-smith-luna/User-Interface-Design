# Module 13 - Principles for Information Visualization

**Start:** 4/14/2026
**Topic:** Principles for Information Visualization
**Individual Assignment:** Design an Information Visualization

## Module Overview
Principles for designing effective information visualizations, and how visualizations can be used to mislead.

## Objectives
1. Apply the principle of **data-ink minimization** to improve a visualization (CLO 3)
2. Critically examine a visualization to identify ways it may **mislead users** (CLO 3)
3. Apply principles of **interactive information visualization** to design effective interactivity (CLO 1)

## Notes

### Tufte's Principles of Graphical Excellence
A good visualization should:
1. **Show the data**
2. Induce the viewer to think about the **substance** rather than the methodology
3. Avoid **distorting** what the data have to say
4. Present **many numbers in a small space**
5. Make large data sets **coherent**
6. Encourage the eye to **compare** different pieces of data
7. Reveal data at **several levels of detail** - overview to fine structure
8. Serve a reasonably clear **purpose**: description, exploration, tabulation, or decoration

### Distortions in Visualizations
- Visualizations may distort the underlying data, making it harder for the reader to understand the truth
- Use of **design variation** to falsely communicate **data variation** (style changes that aren't backed by real changes in the data)

### Examples of Excellence
- **Nobel Prizes Awarded in Science, 1901-1974** - small multiples-style line chart packing 7 decades x 5 countries into a small space; lets the eye compare trajectories (US surge post-WWII, Germany's early dominance and decline)
- **Weighted Electoral Map (2020)** - tile cartogram where each square = 1 electoral vote; corrects geographic-area maps that visually overweight large, low-population states. Encodes both party (color) and electoral weight (count of tiles)

### Data-Ink (Tufte)
- **Data-ink** = non-redundant ink encoding data information
- **Data-ink ratio** = data-ink / total ink used to print the graphic
  - = proportion of the graphic's ink devoted to non-redundant display of data
  - = 1.0 - proportion of the graphic that can be erased without loss

### Design Principles for Data-Ink
(a.k.a. aesthetics & minimalism / elegance & simplicity)
- **Above all else, show the data**
- **Erase non-data-ink**, within reason - often not valuable, distracting
- **Erase redundant data-ink** - redundancy not usually useful
- "Chartjunk" - decorative elements that distract from the data

### Misleading Visualizations
Common ways visualizations mislead:
- **Truncated axes** - exaggerate small differences by not starting Y at 0
- **Inconsistent scales** - dual axes or non-linear scales
- **Cherry-picked time ranges** - hide trends by choosing favorable windows
- **Inappropriate chart types** - 3D pie charts distort area perception
- **Area vs. length encoding** - doubling a radius quadruples area
- **Missing context** - no baseline, no comparison
- **Correlation implying causation**
- **Aggregation bias** - Simpson's paradox

### Interactive Visualizations
- Users follow an iterative process of making **sense** of data - answers lead to new questions
- Interactivity lets the user constantly change the display to answer new questions
- A good viz should offer the **best view of the data moment to moment** as the desired view changes

### Information Visualization Tasks (Shneiderman)
Mantra: **"Overview first, zoom and filter, then details-on-demand."**
- **Overview** - gain an overview of the entire collection
- **Zoom** - zoom in on items of interest
- **Filter** - filter out uninteresting items
- **Details on Demand** - select an item or group and get details
- **Relate** - view relationships between items
- **History** - support undo, replay, progressive refinement
- **Extract** - allow extraction of sub-collections through queries

### Example: NYT "Is It Better to Rent or Buy?" (2014)
- Interactive calculator by Mike Bostock, Shan Carter, Archie Tse
- User drags sliders for home price, length of stay, mortgage rate, etc.
- Output updates live: "If you can rent a similar home for less than $X/month, then renting is better."
- Demonstrates filter + details-on-demand + extract - the user steers the visualization to answer their own question

### Design Heuristics
- Match visual encoding to data type (Q/O/N) - see Module 12
- Reduce cognitive load - let perception do the work
- Avoid 3D unless data is genuinely 3D
- Use color purposefully (categorical vs. sequential vs. diverging palettes)
- Label directly when possible instead of relying on a legend
