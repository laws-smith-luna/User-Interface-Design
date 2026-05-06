# Module 10: Visual Design

**Week of 3/24/2026**
**Individual Assignment:** Visual Design Critique
**Group Assignment:** Interaction Design Critique and Iteration

---

## What Visual Design Is

- **Solving communications problems** in ways that are both functionally effective and aesthetically pleasing
- Creating a **visual language** with a vocabulary of design elements characterized by:
  - **Visual variables** — shape, size, position, orientation, color, texture…
  - **Organizational relations between elements** — balance, structure, proportion…
  - **Visual syntax** — rules for assembling elements within the design language

## Visual Design as Communication

- **Goal:** efficiently and accurately transmit information from system to user
- Visual variables and organization **encode** information
- Standard communication model applies: Message source → Sender (encoder) → Channel (with noise) → Receiver (decoder) → Destination

## Goals for Visual Design

1. Successfully **transmit** information
2. Present **coherent and consistent** design that reduces ambiguity and confusion
3. Reduce visual **search** time through layout and organization
4. Create desired **emotional** reactions through aesthetic choices

---

## Elegance & Simplicity

- **Elegance** comes from Latin *eligere*, "to select carefully"
- Judicious selection of elements + economy of expression that reveals an intimate understanding of the problem
- Remove and combine superfluous elements until **only the necessary remains**

### Benefits of Simplicity
- **Approachability** — rapidly understood affordances; glanceable understanding of possible interactions
- **Immediacy** — greater emotional impact because interactions can be quickly understood

### Trade-offs in Simplicity
- OSX Finder toolbar evolved from cluttered (c.2010) to progressively simpler (c.2021) — fewer icons, more space, clearer hierarchy
- Industry trend over a decade: aggressive removal of toolbar items as designers learned what users actually needed

### Reducing a Design to Its Essence
Make the design simple, bold, and direct by removing inessential details. Even essential elements may be *suggested* rather than fully drawn.

1. Determine the essential qualities and information to convey
2. Critically examine each element — how would the design suffer without it?
3. Try removing elements. What happens?

Example: road signs distill complex situations (lane merges, curves, additional lanes) into minimal stylized arrows.

### Guidelines from a Classic
The London Underground map evolution: early geographically-accurate maps were dense and hard to scan; the modern stylized topology map sacrificed geographic accuracy for instant readability.

### Error: Excessive Skeuomorphism
- **Skeuomorphism** = making visual design resemble physical reality (the visual sibling of metaphor)
- *Excessive* skeuomorphism is distracting and wastes potential visual bandwidth that could encode meaningful info
- Trend has moved toward **flat interfaces**

---

## Scale, Contrast, & Proportion

> "Information consists of differences that make a difference." — Edward Tufte, *Envisioning Information*

These are the individual visual variables that encode information.

### Terminology
- **Scale** — relative size or magnitude of an element compared to related elements
- **Contrast** — visually noticeable distinctions along a common visual dimension
- **Proportion** — ratio and balance between elements
- **Emphasis** — contrasts can emphasize important elements or areas, and add visual interest by creating tension and drama

### Principles
- **Clarity** — contrasts should be clear and easily differentiated, not slight or subtle
- **Harmony** — proportions and ratios should be harmonious
- **Activity** — use contrasts to maintain orientation and context within the design
- **Restraint** — contrasts should be conscious, strong, few in number, and never overwhelming

### Error: Excessive Typographic Contrasts
Too many fonts, sizes, and styles in one dialog (classic 1990s Mac dialogs) shouts at the user instead of guiding them.

---

## Layers

- Contrasting **color, value, texture** can segregate information into separate layers
- Supports **overlapping** information in displays, allowing selective processing of specific element sets
- Allows different layers to be read and interpreted **separately**
- Example: historical maps overlaying topology, building footprints, and political boundaries with different palettes

### Creating Layers
1. Group items into categories based on intended use
2. Determine rank and importance of groups
3. Use perceptual variables (size, value, hue, etc.) to establish the layering effect
4. Maximize differences *between* groups while minimizing differences *within* groups
5. Use the **squint test** — squint at the design to ensure elements in a group hold together while remaining visually separated from other groups

Example: airport marshalling signal redesign uses motion arrows in a contrasting color to layer dynamic information over the figure.

---

## Organization & Structure

Organization needs to be **designed**, not left to chance.

### Benefits
- **Unity** — ties together related elements so they work together
- **Integrity & readability** — structure helps users scan and make comparisons
- **Control** — determines where the user focuses attention

The underlying psychology: **Gestalt** — how perception builds wholes from parts.

### Gestalt Principles

- **Proximity** — elements are most strongly associated with nearby elements (column-vs-row parsing follows spacing)
- **Similarity** — elements with shared visual attributes are grouped (rows of filled circles read as rows even when columns are spaced closer)
- **Continuity** — preference for the simplest physical explanation (a "+" reads as two crossing lines, not 4 separate segments)
- **Closure** — figures are interpreted as complete even when missing information (IBM logo, Kanizsa triangle)
- **Area** — smaller overlapping element reads as figure, larger as ground (FedEx logo)
- **Symmetry** — ambiguous forms are interpreted as multiple symmetric elements (overlapping diamonds)

### Grouping
Bind UI elements tightly together while distinguishing them from surrounding controls. **Show, don't tell.** Achieved through:

- **Bounding boxes** (not recommended — heavy)
- **Negative space** and contrasts
- **Arrangement and alignment**

### Use Fewer Borders
Three preferred alternatives to literal borders:
- **Negative space** (whitespace)
- **Box shadows** for soft elevation
- **Different backgrounds** for distinct regions

---

## Hierarchy

Order groups based on perceptual prominence corresponding to the intended **reading sequence**.

- Helps solve "skimming" problems
- Structure focuses attention on key parts
- Without clear hierarchy, key points get lost
- Bold and weight changes help; *don't* reach for novelty fonts and red arrows

### Hierarchy in UIs
File-save dialogs evolved from flat lists with one type of control (early Save As) to dialogs with clear visual hierarchy — directory navigation, common locations sidebar, file type and name with distinct prominence.

### Use Negative Space
- Directs attention to critical regions of the display
1. Review the design and prioritize groups
2. Add extra space to ensure spatial separation and emphasis, especially for important elements

Example: image-preferences dialog rebalanced with more whitespace becomes much easier to scan even with the same controls.

### Creating Hierarchy: Color and Weight, Not Size
- **Bolder, not bigger** for emphasis
- **Lighter, not smaller** for de-emphasis
- Avoid the trap of using size as the only hierarchy signal — color and weight carry the same meaning at lower visual cost

### Signal Importance of Action
Buttons typically come in **primary / secondary / tertiary** treatments:

- **Primary** — filled, solid color (the action you want users to take)
- **Secondary** — outlined or ghost button
- **Tertiary** — text link or no chrome at all

Same hierarchy works on light and dark backgrounds — adjust contrast, keep the relative weight relationship.
