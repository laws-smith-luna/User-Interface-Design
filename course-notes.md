# SWE 632 — User Interface Design and Development

**Course:** George Mason University, Spring 2026
**Instructor:** Prof. Zhicong Lu
**Student:** Laws Smith

This is the consolidated study document for the whole semester. Module-by-module notes still live in `modules/module-XX/notes.md`. This file is the single place to read across the course or to grep for a concept.

---

## Cross-Cutting Themes

A handful of ideas show up everywhere, restated in each module's vocabulary.

- **Bridge the two gulfs.** Gulf of Execution (knowing what to do) and Gulf of Evaluation (knowing what happened). Norman frames it in M2; M7's site-design questions ("what site is this, where am I, what can I do here?") are gulf-of-execution questions; M9's error-prevention work is gulf-of-evaluation work.
- **Match the user's mental model.** M2 (conceptual models, refrigerator example), M7 (information scent, metaphor vs. idiom), M8 (signifiers, modes), M11 (icons matching cultural conventions). Every module circles back to "the user has a model in their head; the system image either matches it or fights it."
- **Don't trust what people say, watch what they do.** M3 (user-centered design), M4 (contextual inquiry: actions vs. words), M6 (think-aloud usability). Functional fixedness, novice-interviewer mistakes, retrospective-recall limits all point at the same thing.
- **Iterate.** M3 (double diamond), M5 (sketch-then-prototype), M6 (usability cycle), M9 (root cause), M14 (the project itself iterates across modules).
- **Constraints prevent errors.** M2 (four constraint types: physical, cultural, semantic, logical), M9 (forcing functions, undo, swiss cheese model), M14 (access control as a regulator).
- **Visibility and signifiers.** M2 (affordances vs. signifiers), M7 (effective site design questions), M8 (button vs. link ambiguity), M11 (icons), M14 (showing membership / norms).
- **Cognitive psychology vs. social psychology.** Most of the course is cognitive (one user, one task, one interface). M14 flips the lens: when users interact with each other through the system, social-psychology principles apply.
- **Designer ethics.** Surfaces explicitly in M14 (existential values, dark patterns), but threads through M9 (tone of error messages, blaming the user) and M8 (universal design).

---

# Module 2 — Human Cognition

Norman's *Design of Everyday Things*, Chapters 1–2. The cognitive foundation for the rest of the course.

## Seven Stages of Action

Action breaks into **execution** and **evaluation**.

- **One for goals:** 1) Goal — what do I want?
- **Three for execution:** 2) Plan — what alternatives? 3) Specify — which action now? 4) Perform — how do I do it?
- **Three for evaluation:** 5) Perceive — what happened? 6) Interpret — what does it mean? 7) Compare — did I accomplish my goal?

**Gulfs:**
- **Gulf of Execution:** gap between intent and available actions. Bridged by signifiers, constraints, mappings, conceptual model.
- **Gulf of Evaluation:** gap between system state and user understanding. Bridged by feedback, conceptual model.
- **Feedforward** = info about how to do; **Feedback** = info about what happened.

**Goal-driven** action starts top-down (form a goal, plan); **event-driven** starts bottom-up (something in the world prompts action).

**Root cause:** keep asking "why?" Person buys drill → wants hole → wants shelf → wants to organize books.

## Six Fundamental Principles

1. **Affordances** — the *relationship* between object and person that determines possible use. Not a property; depends on both. Anti-affordance prevents action (glass blocks passage).
2. **Signifiers** — perceivable indicators that communicate appropriate behavior. Where the action goes. More important than affordances for designers. Hand-lettered "PUSH" signs on doors signal poor design.
3. **Mappings** — relationship between controls and effects. Natural mapping uses spatial analogy (Mercedes seat control shaped like a seat). Spatial, cultural/biological, gestalt.
4. **Feedback** — must be immediate (0.1s delay is bad), informative, prioritized, appropriate. Too much feedback → ignored. Identical sounds across devices → confusion.
5. **Conceptual model** — simplified explanation of how something works. Doesn't need to be complete, just useful. The **system image** is what communicates the model. Refrigerator example: two knobs suggest one-per-compartment (wrong) but actually adjust thermostat + air distribution.
6. **Constraints** (four kinds):
   - **Physical** — key fits one way
   - **Cultural** — red = stop
   - **Semantic** — windshield faces forward
   - **Logical** — one screw left + one hole left

| Principle | Question | Strategy |
|---|---|---|
| Affordances | What can I do? | Make actions possible |
| Signifiers | Where do I do it? | Make actions visible |
| Mappings | How do controls relate? | Spatial correspondence |
| Feedback | What happened? | Immediate, informative |
| Constraints | What can't I do? | Limit incorrect actions |
| Conceptual model | How does this work? | Clear system image |

---

# Module 3 — User-Centered Design

## Double Diamond

Two diamonds. The first finds the right *problem*, the second finds the right *solution*. Each diamond diverges (broaden) then converges (narrow). Don't jump to solving — make sure you're solving the right problem first.

| Phase | Diamond | Mode |
|---|---|---|
| **Discover** | 1 | Diverge |
| **Define** | 1 | Converge |
| **Develop** | 2 | Diverge |
| **Deliver** | 2 | Converge |

Flow: Challenge → Discover → Define → Develop → Deliver → Outcome.

**Core values:** be people-centered, communicate visually & inclusively, collaborate & co-create, iterate.

**Supporting layers:** engagement (stakeholders), leadership (innovation conditions), methods bank (practical techniques).

## Needfinding (Design Research)

Identify, articulate, understand user needs by:
- Gathering qualitative data
- Exploring behaviors, attitudes, aptitudes
- Understanding domain (technical/business/environmental context, vocabulary, social aspects)
- Understanding how existing products are used
- Building team credibility to inform decisions

---

# Module 4 — Contextual Inquiry

## Contextual Design (Three Parts)

1. **Contextual inquiry** — gather data from users while they work
2. **Work modeling** — build sharable models of the work
3. **Work redesign** — design how the work *will* happen; the core problem is *work design*, not technology design

## Approach

**Actions speak louder than words.** Users can't reliably tell you what would help them. Have conversations *in the context* of the work.

## Four Principles

1. **Context** — see work in its environment
2. **Partnership** — users are co-investigators, not subjects
3. **Interpretation** — assign meaning explicitly (Fact → Hypothesis → Implication → Design idea)
4. **Focus** — pre-defined set of concerns guiding probes

## CI vs. Traditional Methods

| Interviews / Surveys / Focus Groups | Contextual Inquiry |
|---|---|
| Remembered experience | Ongoing experience |
| Subjective | Objective |
| Limited by memory | Limited by observation |
| What users *say* they do | What users *actually* do |

## Do's and Don'ts

- **Go to the workplace.**
- **Seek concrete data.** Not "what do you dislike about ordering?" Instead: "show me how you place an order, tell me what you like and don't like as we go."
- **Avoid summary information.**

## Partnership

Build an equitable relationship. Not interviewer-interviewee, master-apprentice, expert-novice, or host-guest. Share control, ask open-ended questions ("What are you doing?" "Why?"), let user lead, listen, watch non-verbal cues.

## Focus

Focus is a *perspective*, not a script. It steers conversation, can expand, and reveals as well as conceals. Probe surprises and contradictions. Challenge focus assumptions, don't validate them. Avoid expert blind spot.

**Focus across stages:** early = broad/usefulness ("are we building the right thing?"); late = narrow/usability ("is the artifact easy to use?").

## Conducting a Session

- Phase 2: transition to actually watching them work, ask them to think aloud, agree they can decline interruptions
- Phase 3: take notes, follow focus, validate interpretations

## Why Asking About New Features Fails

- **Functional fixedness** — people understand their world inside its current structure
- They suggest small additions, fixes, transferred features — rarely redesigns
- They struggle with hypotheticals
- They'll happily make something up

## Information You Want

- Underlying **goals**
- Current **behavior** — how they spend time, priorities, problems, inefficiencies, feelings about experiences

## Novice Interviewer Mistakes

- Giving opinions (people want to please you, you'll bias them)
- Doing all the talking — aim for **20–25%** of word count
- Failing to follow up — when stuck, "Can you tell me more about that?"

---

# Module 5 — Sketching and Prototyping

## Sketches vs. Prototypes (Buxton)

| Sketches (design exploration) | Prototypes (design refinement) |
|---|---|
| For design | For UX engineering |
| Get the *right* design | Get the design *right* |
| Experiment, explore | Follow the UX process |
| Ideation | Iterative refinement |

## Sketch Properties

- Anyone can sketch — no artistic skill required
- Quick, inexpensive — don't inhibit early exploration
- Disposable — no investment in any one sketch
- Just-in-time — made in the moment

Sketches include **annotations** explaining how things work.

## UI Storyboards

Hand-sketched, annotated panels showing user activity, devices, screens, system connections, physical actions, and cognitive actions ("thought balloons").

## Wireframes

Outline boxes/shapes capturing emerging interaction designs. Schematic — define content and visual flow. **Deliberately unfinished:** no finished graphics, colors, or fonts.

**Creating a wireframe** — ask:
1. What are the key interactions?
2. What widgets support them?
3. Best layout?
4. How does this match the user's mental model?

## Design Critiques

**As designer:** state explicitly what you want feedback on; take a dispassionate stance; show alternatives.

**As critic:** comment on the *design*, not the designer. Be specific about what works ("the layout communicates hierarchy" not "I like this"). Ask for alternatives ("have you considered…?") instead of prescribing solutions.

## Prototyping

Evaluate before investing in the full build.

**Types** (which details do you leave out?):
- **Horizontal** — broad in features, shallow depth
- **Vertical** — narrow in features, deep depth (realistic eval of a few features)
- **T** — most of UI low depth, a few parts deep
- **Local** — focused on one specific interaction

## Wizard of Oz

Simulate the system without building it. User interacts as if it's real; a hidden human handles the response. (Good et al. 1984: natural-command-line — typed commands intercepted by a human interpreter.)

---

# Module 6 — Think-Aloud Usability Evaluations

## Why

- Insights into user needs/preferences
- Identify and rectify UI issues
- Improve experience and satisfaction

## Study Goals

Where are you in the process? Possible goals: explore new idea, validate approach, find issues, evaluate a new feature/corner case, study a specific user class, compare against competitors.

## Participants

- Representative of target users; consider classes (analyst vs. admin)
- Novices vs. experts; can also include UX experts
- **4–5 participants catch ~80% of problems** (Nielsen & Morlich 1990); Krug suggests 3
- More participants → more data but slower/more expensive

## Preparing

- Be clear: you're evaluating the **design**, not the user
- **Tasks:** scenario + goal, but *not* how to do it; communicate end criterion + max time
- **Training:** avoid unless target users would also have it

## Post-Study Questions

Use open-ended. Bad: "Did you find it useful?" (yes/no, leading). Good: "How might the UI better support what you're trying to do?" "What was most challenging?" "What did you like best?"

## Critical Incident Analysis

Identify moments where something went wrong. Document:
- Exact point in the task
- Detailed observation of behavior + comments

Don't include: general impressions, participant background.

**Reporting:**
- **Problem statement:** summary + effect on user (no solution!)
- **User goals:** what they were trying to do
- **Immediate intention:** what they were trying to do *at the moment* of the problem
- **Possible causes:** speculation

## Critical Incidents → Usability Issues

Group similar incidents within and across sessions, identify underlying cause, brainstorm fixes.

## Usability Study vs. Contextual Inquiry

| Usability Study | Contextual Inquiry |
|---|---|
| Evaluation | Needfinding |
| Observation | Conversation |
| Identifies critical incidents | Gathers contextual data |
| Identifies usability issues | Informs design |

## Steps in Order

1. Formulate goals
2. Design protocol, tasks, materials
3. Conduct study
4. Analyze data → assess performance, identify usability issues

---

# Module 7 — Site Design

The course shifts from *learning from users* to *applying principles*. The design space is too large to user-test every decision; principles let you make informed choices and prioritize what to test.

## Hierarchy and Navigation

- Sites are hierarchical; pages live at different levels
- Signal: which hierarchies exist, which navigation belongs to which subtree, where the user is
- **Persistent navigation:** main nav always accessible
- **Tabs:** binder/folder metaphor; partition content; hard to miss
- **Breadcrumbs:** trail showing path + current location
- **Progressive disclosure:** layer info — most-used first, advanced behind a "Customize" or expand control

## Effective Site Design Questions

A good site makes these obvious:
1. What site is this? (site ID)
2. What page am I on?
3. What are the major sections?
4. What are my options at this level?
5. Where am I in the site?
6. How can I search?

## Site Design Goals

- How do users learn whether they can do what they want?
- How do they find what they're looking for?
- How do you balance competing objectives?

## Challenges

Sites lack the spatial cues physical spaces have:
- No sense of scale (50 pages? 50,000?)
- No sense of direction (which way did I come from?)
- No sense of location (where am I now?)
- Nowhere to check that something *isn't* present

Without those cues users get lost, frustrated, leave.

## Key Design Dimensions

- Organization of content into pages
- Organization within pages
- Navigation between pages

**Goals:** reduce time/cost to reach content; reduce irrelevant info read.

## Information Foraging

Users navigate like animals foraging for food. Maximize prey caught, minimize time hunting.

- **Patch** — a location (page, dialog)
- **Links** — connections between patches
- **Cues** — text/visuals on outgoing links
- **Information scent** — visible cues that signal whether a page matches the goal
- **Diet** — info sources the user is willing to consider
- **Rate of gain = info value / cost** — users maximize this ratio

**Design implications:**
1. Group related info together
2. Design effective cues (better cues → better navigation)
3. Match user mental model
4. Provide search for large spaces

**Search increases competition** — users arrive from search engines, form first impressions fast, leave if scent is weak.

## Metaphor vs. Idiom

**Metaphor** — uses existing real-world mental model (desktop, recycle bin, folders).
- *Pros:* intuitive, eases mapping tasks to actions
- *Cons (tyranny of metaphor):* ties UI to physical-world workings, adds overhead, breaks at extremes (folders 10 deep), users expect metaphor consistency

**Idiom** — consistent UI mental model with no real-world metaphor (open/close/save, cut/copy/paste, follow/subscribe). Learn once, apply broadly.

## Task Structure

- Some tasks need a sequence (must select shipping before seeing price)
- Want user control + flexibility, but don't overwhelm with options
- Trade-offs: control vs. structure, flexibility vs. efficiency, minimalism vs. completeness

## Long Tasks

- Break into sequences to reduce memory load
- Don't interrupt with unrelated tasks
- Provide subtask closure
- Example: airline booking flow (find → choose → travelers → options → seats → pay → finish)

## Anticipate Likely Next Actions

Surface options for likely next steps. "Save As" defaulting to current project folder.

## Interaction Flow Guidelines

- Don't use dialogs to report normal behavior
- Separate commands from configuration
- Don't ask questions — give choices
- Provide defaults, show options
- Make dangerous choices hard to reach
- Design for the probable, provide for the possible

---

# Module 8 — Interaction Design

## Command Interactions

Many ways to invoke a command: menu, button, toolbar, dialog, keyboard shortcut, gesture, voice.

## Signifiers (revisited)

Visual cues showing what's interactive. "Is this a button or a link?" When ambiguous, users can't tell what to click.

**Goals:** show what can be manipulated, how to manipulate it, help users get started, guide data entry, suggest defaults, support error recovery.

## Clarity of Wording

Speak the user's language. Avoid vague terms. Be specific. Represent domain concepts clearly.

## Likely Defaults

- Default text (e.g., today's date)
- Default cursor position
- Don't make users re-type or re-enter

## Modes

A mode changes what a command does. Examples: Caps Lock, insert/overtype, vi/emacs command modes, game-vs-chat keyboard.

**Problems:** inconsistent mapping (Ctrl+S sometimes saves, sometimes sends). Especially dangerous for automatic System-1 actions.

**Guidelines:** avoid modes when possible; if needed, distinguish current mode clearly + show how to switch.

## Avoid Physical Awkwardness

- Switching input devices is slow — keep tab order good
- Avoid awkward keyboard combinations

## Fitts's Law

Time to acquire a target **decreases with target size, increases with distance**.

- Movements: large **ballistic** + fine **homing**
- Homing dominates time and errors
- Applies to rapid pointing, not slow continuous

**Design implications:**
- Bigger controls = faster
- Closer to cursor = faster (context menus)
- 1D constraint dramatically increases speed (scroll bars)
- Edge of screen acts as a barrier — fastest possible target (Mac menu bar)

## Mobile

- Smaller form factor — separate UI or fluid responsive
- No cursor → no dynamic hinting → rely on static hinting
- Fitts's law still applies; fingers are imprecise and occlude

## Alternative Inputs

Mobile sensors enable new interactions: camera, mic, accelerometer, gyro, GPS, barometer, proximity, ambient light. Plus AR overlays.

## Disabilities

- **Perception** — visual/auditory (blindness, color blindness, hearing)
- **Motion** — fine motor control, weakness, fatigue
- **Cognition** — memory, planning, sequencing

**Blind users** rely on screenreaders (400+ wpm). Need:
- **Alt-text** on images
- **Hierarchy** — section headings let them skim by listening

## Universal Design

- **Assistive design** = equivalent actions for disabled users
- **Universal design** = normal actions usable by widest range of people

**Curb-cut example:** designed for wheelchairs, used by everyone (suitcases, carts, bikes). Universal design benefits the broader population.

## Seven Principles of Universal Design

1. **Equitable use**
2. **Flexibility in use**
3. **Simple and intuitive**
4. **Perceptible information**
5. **Tolerance for error**
6. **Low physical effort**
7. **Size and space for approach and use**

---

# Module 9 — Preventing Error

## Direct Manipulation

Shneiderman 1982: "rapid incremental reversible operations whose impact on the objects of interest is immediately visible."

**Characteristics:** continuous representation, physical actions (not syntax), continuous + reversible feedback.

**Benefits:** supports exploration (try, see, change mind), immediate feedback, easy goal-vs-actual comparison.

**Drawbacks:** few objects on screen, physically demanding, slow for large action sequences, repetitive tasks suffer (good for novices, bad for expert efficiency), some gestures error-prone.

Spreadsheets are the canonical example.

## When IFT Breaks Down

Information Foraging Theory assumes patches and topology are fixed. When user actions transform application state (clicking "Send"), the patch model breaks.

## Norman's Key Design Principles

- Put knowledge in the world, not in the head
- Use natural and artificial constraints
- Bridge the two gulfs:
  - **Execution:** make options readily available
  - **Evaluation:** provide feedback

## Error Types

**Mistakes vs. slips:** novices make more *mistakes* (wrong goal/plan), experts make more *slips* (right goal, wrong execution). Mistakes happen at Goal/Plan/Compare; slips happen at Specify/Perform/Perceive/Interpret.

### Unsafe Acts (taxonomy)

- **Unintended:**
  - **Slip** (attentional): intrusion, omission, reversal, misordering, mistiming
  - **Lapse** (memory): omitting items, place-losing, forgetting intentions
- **Intended:**
  - **Mistake** — rule-based (wrong rule applied) or knowledge-based (missing info)
  - **Violation** — routine, exceptional, sabotage

### Examples

- **Slip:** poured milk into coffee, then put coffee in the fridge. Right action, wrong object.
- **Strong habit intrusion:** drove to your usual destination instead of the new one
- **Omission:** picked up coat, phone rang, left without coat
- **Mistimed check:** interrupted while tying shoes, can't resume
- **Memory lapse:** got a pen out, got distracted, left pen on the desk
- **Rule-based mistake:** nightclub bouncers blocking exits during a fire because patrons "weren't following the rules"
- **Knowledge-based mistake:** driver feels ABS vibration, thinks brakes are broken, lifts foot, defeats ABS
- **Routine violation:** running a red light because everyone does

## Interruptions

Major source of error. Even a perfectly-designed interface can fail when the user takes a phone call or comes back the next day.

**Designing for interruptions:**
- Help user resume — remember where they were
- Reduce step count
- Use forcing functions (ATM: take card *before* taking cash)

## Undo

One of the most powerful error-mitigation tools. Not always possible (sending email).

## Designing for Error

### Understand Causes

- Ambiguous system state
- No effective conceptual model
- Inappropriate procedures

Design for users as they exist, not as you wish they'd behave.

### Root Cause

Keep asking *why*. F-22 crash: "pilot error" → pilot was unconscious from oxygen failure.

### Add Constraints

- Format constraints on form fields
- Separate easily-confused controls
- Split items across screens or modules

### Feedback

- Early, consistent, visible, in user focus
- Confirmation requests for costly errors (use sparingly)

### Tone of Feedback

- Don't make the user feel stupid
- System takes the blame
- Be positive, encouraging
- Helpful, not cute
- Avoid violent/negative/threatening words ("illegal," "invalid")

### Fix Errors

- Good: detect errors
- Better: show how to fix
- **Best: prevent with constraints**

### Swiss Cheese Model

Accidents must penetrate multiple layers of defense. Reduce by adding layers, shrinking holes, alerting when holes line up.

---

# Module 10 — Visual Design

## What Visual Design Is

- **Solving communications problems** in ways that are functionally effective and aesthetically pleasing
- A **visual language** with three components:
  - **Visual variables** — shape, size, position, orientation, color, texture
  - **Organizational relations** — balance, structure, proportion
  - **Visual syntax** — rules for assembling elements

## Visual Design as Communication

Goal: **efficiently and accurately** transmit information from system to user. Visual variables and organization encode the information. Standard sender-channel-receiver model applies; noise is anything that interferes with the encoding being decoded as intended.

## Goals

1. Successfully **transmit** information
2. Coherent and **consistent** design (reduces ambiguity/confusion)
3. Reduce visual **search** time through layout and organization
4. Create desired **emotional** reactions through aesthetic choices

## Elegance & Simplicity

- *Elegance* from Latin *eligere* — "to select carefully"
- Judicious selection of elements + economy of expression revealing intimate understanding of the problem
- Remove and combine superfluous elements until **only the necessary remains**

### Benefits of Simplicity

- **Approachability** — rapidly understood affordances; glanceable understanding of possible interactions
- **Immediacy** — greater emotional impact because interactions can be quickly understood

### Trade-offs in Simplicity

OSX Finder evolved from cluttered (c. 2010) to progressively simpler (c. 2021). Industry trend over a decade: aggressive removal of toolbar items as designers learned what users actually needed.

### Reducing a Design to Its Essence

1. Determine essential qualities/info to convey
2. Examine each element — how would the design suffer without it?
3. Try removing elements — what happens?

Even essential elements may be *suggested* rather than fully drawn (road signs distill complex situations into stylized arrows).

### Error: Excessive Skeuomorphism

- **Skeuomorphism** = making visual design resemble physical reality (visual sibling of metaphor)
- *Excessive* skeuomorphism is distracting and wastes visual bandwidth that could encode meaningful info
- Trend toward **flat interfaces**

## Scale, Contrast, & Proportion

> "Information consists of differences that make a difference." — Edward Tufte, *Envisioning Information*

### Terminology

- **Scale** — relative size of an element vs. related elements
- **Contrast** — visually noticeable distinctions along a common dimension
- **Proportion** — ratio and balance between elements
- **Emphasis** — contrasts emphasize important elements; add tension and drama

### Principles

- **Clarity** — contrasts should be clear and easily differentiated, not slight/subtle
- **Harmony** — proportions and ratios should be harmonious
- **Activity** — use contrasts to maintain orientation and context
- **Restraint** — contrasts should be conscious, strong, few in number, never overwhelming

**Error: excessive typographic contrasts** — too many fonts/sizes/styles in one dialog shouts instead of guiding.

## Layers

Contrasting color, value, and texture can segregate information into separate **layers** that overlap on the same display and can be read separately.

### Creating Layers

1. Group items into categories by intended use
2. Determine rank and importance of groups
3. Use perceptual variables (size, value, hue) to establish layering
4. Maximize differences *between* groups, minimize differences *within* groups
5. **Squint test** — squint at the design to confirm groups hold together but stay visually separated

## Organization & Structure

Organization needs to be **designed**, not left to chance.

**Benefits:** unity (related elements work together), integrity & readability (easy scanning), control (focuses user attention).

The underlying psychology: **Gestalt** — how perception builds wholes from parts.

### Gestalt Principles

- **Proximity** — elements associate most strongly with nearby elements (column vs. row parsing follows spacing)
- **Similarity** — elements with shared visual attributes group together (rows of filled circles read as rows even when columns are closer)
- **Continuity** — preference for the simplest physical explanation (a "+" reads as two crossing lines, not 4 segments)
- **Closure** — figures interpreted as complete even when missing info (IBM logo, Kanizsa triangle)
- **Area** — smaller overlapping element reads as figure, larger as ground (FedEx logo)
- **Symmetry** — ambiguous forms interpreted as multiple symmetric elements (overlapping diamonds)

### Grouping

Bind UI elements tightly together while distinguishing them from surrounding controls. **Show, don't tell.** Achieved through:

- Bounding boxes (not recommended — heavy)
- Negative space and contrasts
- Arrangement and alignment

### Use Fewer Borders

Preferred alternatives to literal borders:
- **Negative space**
- **Box shadows** (soft elevation)
- **Different backgrounds** for distinct regions

## Hierarchy

Order groups by perceptual prominence corresponding to intended **reading sequence**.

- Helps solve "skimming" problems
- Structure focuses attention on key parts
- Without clear hierarchy, key points get lost
- Bold and weight changes help; novelty fonts and red arrows hurt

### Use Negative Space

Directs attention to critical regions:
1. Review design, prioritize groups
2. Add extra space for spatial separation and emphasis, especially for important elements

### Color and Weight, Not Size

- **Bolder, not bigger** for emphasis
- **Lighter, not smaller** for de-emphasis
- Don't make size the only hierarchy signal — color and weight carry the same meaning at lower visual cost

### Signal Importance of Action

Buttons in **primary / secondary / tertiary** treatments:

- **Primary** — filled, solid color (the action you want users to take)
- **Secondary** — outlined or ghost
- **Tertiary** — text link or no chrome

Same hierarchy works on light and dark backgrounds — adjust contrast, keep the relative weight relationship.

---

# Module 11 — Icons and Design Languages

## Icons

**Benefits:** identification (recognizable) and expression (engagement).

**Types of iconic representation:**
- **Similar** — visually analogous (right-turn sign)
- **Example** — exemplifies the concept (airplane = airport, scissors = cut)
- **Symbolic** — abstract concept (lightning = electricity)
- **Arbitrary** — must be learned (radioactive, biohazard)

**Abstraction:** simplifying realistic icons makes them clearer up to a point, then it loses meaning. (Calculator example progressing from photo to icon.)

**Four Principles of Icon Design:**
1. **Immediacy** — perceived effortlessly (bold, clear, balanced)
2. **Generality** — represents a class, not an individual (bathroom icons strip personal features)
3. **Cohesiveness** — icons in a set share visual variables
4. **Characterization** — calls to mind distinctive features (hanger for closet)

## Design Languages

How do you make consistent visual choices across an entire app?

**A design language** describes how to express ideas in the interface. Often communicated through Human Interface Guidelines. Tied to Nielsen's "consistency and standards" heuristic.

### Components

**Elements** — individual visual building blocks: view controls, source indicators, detail displays, action buttons.

**Syntax** — how elements compose into structures:
- **Task** — form/input area
- **Placeholder** — loading state
- **Toolbar** — navigation
- **List** — repeated items (inboxes)

### Evolution Example

Google 2004 → 2016 (Material Design): from text-heavy/sparse to cards-with-shadows, clear hierarchy, consistent icons, navigation drawers.

### Common Layout Patterns

Heatmap studies show consistent placements: nav top, logo top-left, search top-right, hero, footer, etc. These conventions create user expectations.

### Why It Matters

- **Idioms** — users expect what other elements suggest
- **Branding** — appearance creates associations (a photography site that looks like ESPN sends mixed signals)

### Design-Language Goals

Offer guidance on:
- **Colors** — palettes
- **Typography** — fonts, sizes, hierarchy
- **Organization**
- Multiple resolutions/devices
- Universal design (visually impaired, color blind)

---

# Module 12 — Information Visualization

## Opening Case: John Snow, 1854 London

Broad Street cholera outbreak, 500+ deaths in 10 days. Snow plotted death counts on a London map and saw the cluster around the Broad Street pump. City removed the handle, epidemic ended. Founded modern epidemiology.

**Why his viz worked:**
1. Plotted on the right context (a map including the well) — proximity revealed cause
2. Quantitative comparisons (brewery had fewer nearby deaths)
3. Considered alternatives and contrary cases (outliers traced back to the pump)

## Amplifying Cognition

Visualization amplifies cognition by:
1. Increasing memory + processing resources
2. Reducing search
3. Detecting patterns visually
4. Enabling perceptual inference
5. Using attention for monitoring
6. Encoding info in a manipulable medium

**Classic example:** Minard's Napoleon-in-Russia map (army size, path, direction, temperature, time — all in one image).

## Visualization Pipeline

Raw Data → [Data Transformations] → Data Tables → [Visual Mappings] → Visual Structures → [View Transformations] → Views

Closed at every stage by **human interaction**, driven by the user's **task**.

## Data Types

- **Nominal** — unordered (gender, hair color)
- **Ordinal** — ordered, no meaningful differences (very-unhappy → very-happy)
- **Quantitative** — numeric (height, distance)

## Data Transformations

- **Classing/binning** — Q → O (histograms)
- **Sorting** — N → O
- **Descriptive stats** — mean, median, max

## Visual Structures

1. **Spatial substrate** — axes (unstructured, N, O, Q); composed via orthogonal axes (2D scatter, 3D)
2. **Marks** — points (0D), lines (1D), areas (2D), volumes (3D)
3. **Mark properties:**
   - Spatial — position, size, orientation
   - Object — grayscale, color, texture, shape

## Effectiveness by Data Type

- **Position** — good for Q, O, N
- **Size** — best for Q, O
- **Grayscale** — good for O
- **Color, texture, shape** — best for N

## Animation

Encoding data *as a function of time* is usually weak — hard to compare. More effective: animate **transitions** between user-configured states.

## Common Types

**Time-series / multi-component:**
- **Stacked graph** — visual summation
- **Small multiples** — separate side-by-side comparisons (better than overlays)

**Geographic:**
- **Choropleth** — color by area
- **Cartogram** — distorts geography to encode size + color
- **Election maps** — color by region

**Hierarchies / networks:**
- **Node-link diagram** — tree/graph
- **Dendrogram** — radial leaf hierarchy
- **Treemap** — nested rectangles, area = value
- **Force-directed layout** — edges as springs
- **Arc diagram** — cliques + bridges with right ordering
- **Adjacency matrix** — grid of connections

---

# Module 13 — Principles for Information Visualization

## Tufte's Principles of Graphical Excellence

A good viz should:
1. Show the data
2. Get the viewer thinking about substance, not method
3. Avoid distortion
4. Pack many numbers into small space
5. Make large data sets coherent
6. Encourage comparison
7. Reveal data at several levels of detail (overview to fine)
8. Serve a clear purpose: description, exploration, tabulation, decoration

## Distortions

Use of **design variation** to falsely communicate **data variation** (style changes that aren't backed by real data changes).

## Examples of Excellence

- **Nobel Prizes 1901–1974** — small-multiples-style line chart packing 7 decades × 5 countries; eye compares trajectories
- **Weighted Electoral Map (2020)** — tile cartogram, each square = 1 electoral vote; fixes geographic-area bias

## Data-Ink

- **Data-ink** = non-redundant ink encoding data
- **Data-ink ratio** = data-ink / total ink
- = proportion of graphic devoted to non-redundant data display
- = 1 − proportion that could be erased without loss

**Principles:**
- Above all, show the data
- Erase non-data-ink (within reason)
- Erase redundant data-ink
- "Chartjunk" — decorative distractions

## Misleading Visualizations

- **Truncated axes** — exaggerate small differences
- **Inconsistent scales** — dual axes, non-linear
- **Cherry-picked time ranges**
- **Inappropriate chart types** (3D pies)
- **Area vs. length encoding** — doubled radius = quadrupled area
- **Missing context** — no baseline/comparison
- **Correlation implying causation**
- **Aggregation bias** (Simpson's paradox)

## Interactive Visualizations

Sense-making is iterative — answers raise new questions. Interactivity gives the user **the best view of the data moment to moment** as their question evolves.

## Shneiderman's Mantra

> "Overview first, zoom and filter, then details-on-demand."

**Tasks:**
- **Overview** — entire collection
- **Zoom** — items of interest
- **Filter** — remove uninteresting
- **Details on demand** — pick one + see specifics
- **Relate** — see relationships
- **History** — undo/replay/refinement
- **Extract** — sub-collections via queries

## Example: NYT "Rent or Buy?" (2014)

Bostock/Carter/Tse interactive calculator. Sliders (price, stay length, rate). Live output ("if you can rent for less than $X, rent"). Filter + details + extract — user steers to answer their own question.

## Heuristics

- Match encoding to data type (Q/O/N)
- Reduce cognitive load — let perception do the work
- Avoid 3D unless data is genuinely 3D
- Use color purposefully (categorical / sequential / diverging)
- Label directly; avoid legend chases when possible

---

# Module 14 — Community Design

The course pivots from individual cognition to social psychology. When users interact through the system, the design problem changes shape.

## Why Community Design Matters

Many influential platforms succeed because **users contribute content that benefits the community**, not just because individuals accomplish goals. Without community-generated content, Facebook, Stack Overflow, and Amazon reviews wouldn't exist.

## Motivating Example

A site to share favorite news stories with friends. Discovery, informedness, publisher money. Sounds simple. **What could possibly go wrong?** (Trolling, misinformation, polarization, abandonment, low contribution…)

## Definition

**(Kraut & Resnick):** virtual spaces where people converse, exchange info or resources, learn, play.

- Supported by tech platforms (email, wikis, comments, social networks, automated feedback)
- Public or internal
- Break the barriers of time, space, and **scale** that limit offline interactions

## Examples

Usenet, Facebook, Netflix, Amazon, Stack Overflow, Cisco Support Community, Kickstarter, Wikipedia, Linux, change.org, Carcinoid Cancer Online Support Group, Piazza.

## Designing Online Communities

User-to-user interactions are **shaped and enabled by the UI**. They can be designed — they're not just emergent.

## Example: Facebook Reactions

- **Goal:** incentivize positive interactions, not negative judgments
  - Solution: **Like button** (approval)
- **Problem:** how to express response to a *bad* event without turning Likes into a vote?
  - A **Dislike** button would let users vote on each other
  - **Reactions** (Like, Love, Haha, Yay, Wow, Sad, Angry) — expressive without being a thumbs-down
- **Lesson:** small UI choices have big behavioral consequences

## Cognitive vs. Social

| Most of the course | Community design |
|---|---|
| Designing for **task performance** | Designing for **community behavior** |
| **Cognitive psychology** | **Social psychology** |

## Four Dimensions of Socio-technical System Design

1. **Community structure** — size, homogeneity of interests, subgroup structures, relationship to existing social ties
2. **Content, tasks, activities, external communication** — self-disclosure vs. anonymity, professional vs. user-generated content, welcoming activities, independent vs. interdependent tasks, invite/share
3. **Feedback, rewards, sanctions** — informal vs. structured (ratings); intangible (status) vs. tangible (privileges, prizes)
4. **Roles, rules, access control, visibility** — specialized roles (welcomer, dispute handler), behavior rules, decision/conflict procedures, access controls (sometimes paid), moderators, **visibility of bad behavior + punishment**

## Four Challenges

1. Starting a new community
2. Encouraging contribution
3. Encouraging commitment
4. Regulating behavior

---

## Challenge 1: Starting a New Community

### Difficulties

- **Communicating value** — does the community offer what users want?
- **Visibility** — do users even know it exists?
- **Competition** — why here instead of somewhere bigger?

### Carving a Niche

- Pick scope by **topic/activities** (Twins fans) or **pre-existing group** (GMU alumni)
- Mixed-topic scopes reduce value (most content irrelevant)
- Subdivide spaces — but **not** prematurely; empty rooms feel worse than crowded ones. Subdivide *after* it's active.

### Design Techniques for Subdivided Spaces

- Navigation aids highlighting active spaces
- Recommender systems for sub-spaces
- Schedule of "expected active times" for synchronous spaces

### Competition

- Switching costs (new profile, new system, content rediscovery)
- Awareness costs of following multiple communities

**Techniques:**
- Reduce startup costs (OAuth/SSO)
- Content sharing / cross-posting
- Advertising + celebrity endorsements — *"the aura of inevitability is a powerful weapon"*

### Critical Mass

Communities fail if:
- Not enough members
- No shared purpose

**Why people use Facebook:** because everyone else does. Cost of joining is fixed per user; value increases with N. **Critical mass** = where benefits dwarf costs.

### Bootstrapping

A community needs a series of states where early-user activity attracts more.

- **Incentives** (Epinions paid early reviewers — but pay-stop demotivates and crowds out intrinsic motivation)
- **Discounts/free services** (less problematic)
- **Viral spread** (invite-a-friend)

### Making Membership Visible to Non-members

- Post membership to existing networks
- Cross-post activity (Twitter → FB)
- Referral benefits

### Early Adopter Benefits

- Permanent discounts
- Status of being an early adopter (cool-finder identity)
- Scarce, claimable resources (usernames, URLs, low member numbers)

---

## Challenge 2: Encouraging Contribution

### Contribution Gap

Communities rely on user-created resources (YouTube videos, Wikipedia articles, reviews). Gap between work needed and work done. Causes:
- Too much work, not enough workers
- Users don't know how to help
- Users don't find tasks appealing

### Visibility of Requests

- **Lists of needed contributions** (Wikipedia: 125,000 articles need citations)
- **Track work as it's done** (FB profile changes in newsfeed)
- **Personal appeals** — best when:
  - Request is simple
  - Stresses benefits of contributing
  - Comes from high-status member (Jimmy Wales asking for Wikipedia support)
  - Comes from likable requestors

### Requesting Contributions

- **Social proof** — others have already complied (ESP game: "over a million labels created")
- **Specific, challenging goals** ("rate 16 movies on MovieLens this week")

### Group Goals

- Group goal + specific deadline (Wikipedia Featured Article application, software release cycle)
- Frequent feedback (fundraising thermometer)

### Motivation

- **Intrinsic** — activity is its own end
- **Extrinsic** — activity is a means to an end
- WoW example: enjoy slaying monsters (intrinsic) vs. enjoy the level/status (extrinsic)

### Comparative Feedback (Leaderboards)

- Motivating to beat competitors
- **But also demotivating:**
  - Reminds you how much time you've "wasted"
  - May feel done enough
  - Discouraging when top is unattainable (top-10 in a community of thousands)

### Rewards (Extrinsic Motivation)

- **Reputation/status** — changes how others treat you
- **Privileges** — opens new actions (commit rights on OSS)
- **Tangible** — money, prizes, charitable donations

### Perverse Incentives

- Wrong incentives → counterfeit actions (rewards for invites → fictitious-entity invites)
- Quantity-based rewards get gamed (Mechanical Turk uses automated quality checks)
- **Status/privileges are gamed less than tangible rewards** — value disappears once gamed
- Less transparent / more unpredictable criteria reduce gaming

### Intrinsic vs. Extrinsic Trade-offs

- Extrinsic rewards **can reduce** intrinsic motivation (people donate blood less when paid)
- Extrinsic must outweigh the loss in intrinsic to be net valuable
- Tangible incentives diminish intrinsic motivation when they reduce **autonomy** and **competence** by being perceived as **controllers**

### Collective Outcomes

Group benefits motivate when:
- More committed to the group
- Group is smaller
- Members feel they make a unique contribution
- Contributions are **complementary or contingent**, not substitutes

---

## Challenge 3: Encouraging Commitment

### Why It Matters

Committed users work harder, contribute more, stick with it, sustain the group through problems, enforce norms.

### Three Types

| Type | Stance | Grounded in |
|---|---|---|
| **Affective** | "I want to" | Closeness/attachment to members |
| **Normative** | "I ought to" | Obligation to the group |
| **Need-based / continuance** | "I must" | Net cost of leaving |

A user can have more than one type at once.

### Two Sub-types of Affective Commitment

- **Identity-based** — attachment to the **community as a whole**, mission
- **Bonds-based** — attachment to **specific people**

### Encouraging Identity-based Commitment

- Cluster similar members in homogeneous spaces (FB group for Mason SWE)
- Explicit name + tagline ("the free encyclopedia anyone can edit")
- Subgroup identity boosts larger-community identity (FB-group membership → FB commitment)
- Make community fate/goals/purpose explicit
- Joint, interdependent tasks (WoW guilds)
- Highlight an out-group (Wikipedia vs. Britannica)
- Anonymity raises group identity (reduces individual ego)

### Encouraging Bonds-based Commitment

- Recruit members with existing ties (Piazza for a course)
- Friend-of-friend interactions
- Profile photos + recent activity
- DMs / personal conversation
- Repeat-encounter mechanisms (places, spaces, friend feeds)
- Profile pages with self-disclosure → interpersonal liking
- Pseudonymous self-disclosure for sensitive info (weight in a weight-loss community)

### Normative Commitment

Feeling of obligation to be loyal and act on the community's behalf.

**Encouraging:**
- Highlight community purpose + success
- Testimonials from other committed members
- Prime reciprocity (cancer survivors who keep posting after remission)
- Highlight chances to return favors (review someone's commit who reviewed yours)

### Need-based Commitment

Net benefits ≥ costs.
- **Benefits:** info, social support, companionship, reputation
- **Costs:** time, effort, frustration

**Encouraging:** match experiences to motivations; know the community's needs; OSS code fests satisfy both friendship and planning needs. Motivational mix varies (info exchange, companionship, social support, fun).

---

## Challenge 4: Regulating Behavior

### Community Norms

- Communities develop norms; communities differ on what's normative
- Examples: personal insults, neutral perspective on Wikipedia vs. opinionated Huffington Post
- Conflicts: flame wars, edit wars

### Damage Types

- **Trolls** — disruption for satisfaction
- **Manipulators** — want the community to produce a particular outcome (Wikipedia POV pushers)
- **Low-quality contributors** — waste community attention

### Limiting Bad Behavior

**Pre-screening / moderation:**
- Pre-screen content before posting
- **Effectiveness factors:**
  - Redirect inappropriate posts elsewhere (vs. delete)
  - Consistently applied criteria + appeals
  - Moderation seen as impartial

**Post-hoc tools:**
- Reversion tools (Wikipedia)
- Filters / influence limiters (downrank vs. delete)
- Activity quotas (anti-spam)
- Gags and bans

### Encouraging Voluntary Compliance

Norms work best when members regulate themselves:
- Make norms clear and salient by displaying examples of *appropriate* behavior
- Publicly contrast inappropriate vs. appropriate
- Show formal feedback given to violators (transparency)
- Display statistics about normative behavior ("X days since last workplace injury")

**Practical takeaway:** voluntary compliance is the cheap default; enforcement handles what voluntary can't reach. Both layers are needed.

---

## Designer Ethics & Dark Patterns

### Existential Values

Questions every designer should ask:
- What are your values? (Facilitating user tasks, broadening access, expressing truth + hiding misinformation, refraining from collecting data)
- How do they align with business directives?
- How do you encode them into your design intent?

### Ill or Misdirected Intent

When business needs are prioritized over user needs, the result is harmful intent. Most prominent example: **dark patterns**.

### Dark Patterns

Anti-patterns where the interface manipulates users into taking actions they otherwise wouldn't, often without realizing.

1. **Sneaking** — auto-add items to a transaction (greeting card surprise in the cart)
2. **Urgency** — fake countdown timers ("offer ends in 00:59:48")
3. **Misdirection** — confirmshaming, biased visual hierarchy ("No thanks, I like full price")
4. **Scarcity** — "only 3 left in stock"
5. **Obstruction** — easy to sign up, hard to cancel (call this number)
6. **Forced action** — required signup or "Continue with Facebook" gating browsing

### Benevolent Intent

The goal: user needs above all, business goals balanced. Hard to achieve, but necessary.

---

# Final Exam — Module 15

Closed book, one attempt, no AI. Don't even open this file during it.
