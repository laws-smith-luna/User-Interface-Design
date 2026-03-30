# Module 10: Visual Design

## Key Concept: Visual Design is Communication, Not Aesthetics

Visual design isn't about making things look pretty. It's about how your interface **communicates information** to the user.

When a user encounters a complex dialogue or screen they've never seen before, they need to figure out where the thing they're looking for is. They don't want to read every word. Visual design gives them **clues** about what to read and helps them get where they want to go as fast as possible.

### What Good Visual Design Does

- **Communicates structure and organization** - Great interfaces have a high-level purpose, with panels and elements that each have separate roles. Good visual design helps communicate this story, helping users quickly see what the main parts are and the role they play.
- **Helps users visually parse an interface into its parts** - Users should be able to quickly scan and understand the layout without reading everything.
- **Keeps things simple** - Minimizes clutter and information the user needs to sort through, letting them focus on the part relevant to their current goal, even when users may have different goals at different times.

**Bottom line:** Visual design principles let you use visual design to communicate effectively with your user about how to interact with your interface.

---

## Visual Design Defined

- Solving **communications problems** in ways that are both functionally effective and aesthetically pleasing
- Creating a **visual language** containing a vocabulary of design elements characterized by:
  - **Visual variables** - shape, size, position, orientation, color, texture, ...
  - **Organizational relations between elements** - balance, structure, proportion, ...
  - **Visual syntax** - rules for assembling elements within a design language

---

## Visual Design as Communication

- Goal: **efficiently and accurately** transmit information from system to user
- Visual variables and organization encode information
- Communication model: Message source -> Sender (Encoder) -> Channel (with noise) -> Receiver (Decoder) -> Destination

### Goals for Visual Design
1. Successfully **transmit** information
2. Present coherent and consistent design that reduces ambiguity and potential confusion
3. Reduce visual **search** time through layout and organization
4. Create desired **emotional** reactions through aesthetic choices

---

## Elegance and Simplicity

- Elegance derives from Latin *eligere*, "to select carefully"
- Judicious selection of elements and economy of expression revealing an intimate understanding of the problem
- Removing and combining superfluous elements until only the necessary remains

### Benefits of Simplicity
- **Approachability** - rapidly understood affordances, allowing glanceable understanding of possible interactions
- **Immediacy** - greater emotional impact because interactions can be quickly understood

### Reducing a Design to its Essence
- Make design simple, bold, and direct by removing inessential details and elements
  - Even essential elements may be suggested
1. Determine essential qualities and information to be conveyed
2. Critically examine each element and ask how design would suffer without it
3. Try removing elements. What happens?

### Trade-offs in Simplicity
- Example: macOS Finder toolbar evolution (2010 -> 2011 -> 2016 -> 2021) shows progressive simplification over time

---

## Guidelines for Visual Design

- Example: London Underground map redesign removed geographic accuracy (relative distances don't matter) to make the transit connections clearer and more usable

### Error: Excessive Skeuomorphism
- **Skeuomorphism** - making visual design resemble reality (like metaphors)
- Excessive skeuomorphism is distracting and wastes potential visual bandwidth that could encode meaningful information
- Trend towards "flat" interfaces

---

## Scale, Contrast, and Proportion

"Information consists of differences that make a difference." (Edward Tufte, *Envisioning Information*)

- Individual visual variables of design that encode information

### Terminology
- **Scale** - relative size or magnitude of element in comparison to related elements
- **Contrast** - visually noticeable distinctions along a common visual dimension
- **Proportion** - ratio and balance between elements
- **Emphasis** - contrasts can emphasize important elements or areas and add visual interest by creating tension and drama

### Principles of Scale, Contrast, and Proportion
- **Clarity** - contrasts should be clear and easily differentiated, not slight and subtle
- **Harmony** - proportions and ratios should be harmonious
- **Activity** - use contrasts to maintain orientation and context within design
- **Restraint** - contrasts should be conscious, strong, few in number, and never overwhelming

### Error: Excessive Typographic Contrast
- Example: dialog boxes with 5 different type sizes in 3 different fonts. Too many contrasts become noise rather than signal.

---

## Layers

- Contrasting color, value, texture can segregate information into separate layers
- Supports **overlapping** information in displays, allowing selective processing of specific sets of elements
- Allows different layers to be read and interpreted **separately**

### Creating Layers
1. Group items into categories based on intended use
2. Determine rank and importance of groups
3. Use perceptual variables (size, value, hue, etc.) to establish layering effect
4. Maximize differences between groups while minimizing differences within groups
5. Use **squint test** to ensure elements in group retain together but visually separated

- Example: Marshalling signals redesigned with color layers (gray figures, colored arrows) to separate the person from the instruction, making each layer independently readable

---

## Organization and Structure

- Organization needs to be **designed**
- Benefits:
  - **Unity** - ties together related elements so that they work together
  - **Integrity and readability** - offers structure that helps user to easily scan and make comparisons
  - **Control** - determines where user will focus attention in the design
- Gestalt -> psychology of perception

### Gestalt Principles

- **Proximity** - elements associated most strongly with nearby elements. Spacing creates grouping (e.g., circles parsed as 4 columns based on close vertical spacing, then as two sets of two columns based on horizontal spacing)
- **Similarity** - elements associated more strongly when they share common visual attributes than when they differ (e.g., filled vs unfilled circles parsed as rows based on fill similarity, despite closer column spacing)
- **Continuity** - preference for simplest physical explanation of complex figure (e.g., crossing lines parsed as two lines rather than 4 separate lines or 4 opposing angles)
- **Closure** - preference to interpret figures as complete, even when missing information (e.g., Kanizsa triangle, IBM logo with horizontal lines)
- **Area** - preference to interpret smaller overlapping elements as figure, larger as ground (e.g., FedEx arrow in negative space)
- **Symmetry** - preference to interpret ambiguous form as multiple symmetric elements (e.g., two overlapping diamonds rather than 3 separate shapes)

---

## Grouping

- Binding UI elements tightly together while distinguishing them from surrounding controls
- **"Showing" not "telling"**
- Can be achieved through:
  - Bounding boxes (not recommended)
  - Negative space and contrasts
  - Arrangement and alignment

### Use Fewer Borders
- Instead of borders, use: **negative space** (margin instead of border-bottom), **box shadows**, or **different backgrounds**

---

## Hierarchy

- Order groups based on perceptual prominence corresponding to intended reading sequence
- Can help solve "skimming" problems - structure helps people focus attention on key parts
- Example: old "Save As" dialog vs. newer "Save Web Page" dialog shows improved hierarchy

### Use Negative Space
- Directs attention to critical regions of display
1. Review design, prioritizing groups
2. Add extra space to ensure spatial separation and emphasis, particularly for important elements

### Creating Hierarchy: Color and Weight Instead of Size
- Use **bolder not bigger** for emphasis
- Use **lighter not smaller** for de-emphasis
- Avoids the problem of too many font sizes

### Signal Importance of Action
- Primary actions: filled/colored buttons (strongest visual weight)
- Secondary actions: outlined buttons
- Tertiary actions: text-only links (least visual weight)

---

## Emphasis (IxDF Reading)

Emphasis is a design strategy that directs viewer attention to specific elements by creating a **focal point**, an eye-catching area distinct from surrounding design components.

### Techniques for Creating Emphasis
- **Lines** - breaking established linear flow draws attention to the disruption point
- **Shapes** - using a different shape among similar ones instantly captures the eye
- **Colors** - color shifts create focal points; stronger contrasts demand more attention than subtle transitions
- **Textures** - embossing, drop shadows, surface variations highlight areas
- **Mass** - dark elements against bright backgrounds (and vice versa) emphasize through perceived "heaviness"

### Design Principles That Facilitate Emphasis
By strategically **breaking established patterns**, designers can emphasize elements:
- **Balance/Symmetry** - asymmetric arrangements highlight points of imbalance
- **Proximity** - isolating an element from a grouped set makes it stand out
- **Alignment** - breaking alignment patterns captures attention to misaligned items
- **Repetition** - varying a repeated element draws focus to the deviation
- **Contrast** - stark differences between areas direct eye movement
- **White space** - increasing surrounding space breaks visual flow and highlights content

### Key Rule
"Emphasis is relative" - elements only stand out against something else. Multiple emphasized areas saturate designs and confuse users. Commit to emphasizing key focal points (especially calls to action) without overwhelming the visual hierarchy.

---

## Principles

