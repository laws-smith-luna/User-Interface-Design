# SWE 632 — Final Exam Study Guide

**Closed book. One attempt. No AI.** Study from this. `course-notes.md` is the deep reference; this is the cram doc.

Quiz yourself by covering the right column of each table or the items below each header.

---

## 0. The Spine — Cross-Cutting Themes

If you can rephrase a question in these terms, you can usually answer it.

1. **Bridge the two gulfs** — execution (knowing what to do) and evaluation (knowing what happened).
2. **Match the user's mental model** — the system image either matches the user's model or fights it.
3. **Watch, don't listen** — users can't tell you what they need; observe in context.
4. **Iterate** — never one-shot a design.
5. **Constraints prevent errors** — physical, cultural, semantic, logical.
6. **Visibility & signifiers** — make actions perceivable.
7. **Cognitive vs. social** — most of the course is cognitive (one user, one task). M14 flips to social.
8. **Designer ethics** — values encoded into design intent.

---

## 1. Norman (M2) — Must Know Cold

### Seven Stages of Action

| # | Stage | Question | Bucket |
|---|---|---|---|
| 1 | Goal | What do I want? | Goal |
| 2 | Plan | What alternatives? | Execution |
| 3 | Specify | Which action now? | Execution |
| 4 | Perform | How do I do it? | Execution |
| 5 | Perceive | What happened? | Evaluation |
| 6 | Interpret | What does it mean? | Evaluation |
| 7 | Compare | Did I accomplish my goal? | Evaluation |

**Mnemonic:** *Goals Plan Specify Perform, then Perceive Interpret Compare.* (1 goal, 3 execute, 3 evaluate.)

### Gulfs

- **Gulf of Execution** = intent → action. Bridged by: signifiers, constraints, mappings, conceptual model. **Feedforward.**
- **Gulf of Evaluation** = system state → understanding. Bridged by: feedback, conceptual model. **Feedback.**

### Six Fundamental Principles (Ch. 1)

| Principle | Question | Strategy |
|---|---|---|
| Affordances | What can I do? | Make actions possible |
| Signifiers | Where do I do it? | Make actions visible |
| Mappings | How do controls relate? | Spatial correspondence |
| Feedback | What happened? | Immediate, informative |
| Constraints | What can't I do? | Limit incorrect actions |
| Conceptual model | How does this work? | Clear system image |

### Seven Principles (Ch. 2 — adds Discoverability)

Discoverability + Feedback + Conceptual Model + Affordances + Signifiers + Mappings + Constraints. Discoverability is the meta-principle that emerges when the others succeed.

### Affordance vs. Signifier (Easily Confused)

- **Affordance** = *relationship* between object and person determining possible use. Property of both, not just object. Anti-affordance prevents action (glass).
- **Signifier** = perceivable indicator showing *where* the action goes. More important to designers.
- Hand-lettered "PUSH" signs = poor design (signifier compensating for missing one).

### Four Constraint Types

- **Physical** — key fits one way
- **Cultural** — red = stop
- **Semantic** — windshield faces forward
- **Logical** — one screw left, one hole left

### Anchors

- **Refrigerator** = wrong conceptual model (two knobs ≠ two compartments)
- **Mercedes seat control** = natural mapping (control shaped like seat)
- **Scissors** = good conceptual model (holes, sizes, visible operation)

### Slips vs. Mistakes (also M9)

- **Novices** make **mistakes** (wrong goal/plan) — top of cycle
- **Experts** make **slips** (right goal, wrong execution) — bottom of cycle

---

## 2. User-Centered Design (M3)

### Double Diamond

Challenge → **Discover** (diverge) → **Define** (converge) → **Develop** (diverge) → **Deliver** (converge) → Outcome.

Diamond 1 = right *problem*. Diamond 2 = right *solution*. Don't skip Diamond 1.

**Core values:** people-centered, communicate visually & inclusively, collaborate & co-create, iterate.

### Needfinding Goals

Qualitative data, behaviors/attitudes/aptitudes, domain context, vocabulary, how existing products are used, team credibility.

---

## 3. Contextual Inquiry (M4)

### Three Parts of Contextual Design

1. **Contextual inquiry** — gather data while users work
2. **Work modeling** — explicit, sharable models
3. **Work redesign** — design how work *will* happen (the core problem is *work design*, not tech design)

### Four Principles

1. **Context** — see work in environment
2. **Partnership** — users as co-investigators
3. **Interpretation** — Fact → Hypothesis → Implication → Design idea
4. **Focus** — pre-defined concerns guide probes

### CI vs. Traditional Methods

| Interviews/Surveys/Focus Groups | Contextual Inquiry |
|---|---|
| Remembered experience | Ongoing experience |
| Subjective | Objective |
| Limited by memory | Limited by observation |
| What users *say* they do | What users *actually* do |

### Why Asking About New Features Fails

- **Functional fixedness** (people understand world inside current structure)
- They suggest small additions, not redesigns
- They struggle with hypotheticals
- They'll happily make something up

### Novice Interviewer Mistakes

- Giving opinions
- Doing all the talking — aim for **20–25%** of words
- Failing to follow up — "Can you tell me more about that?"

### Focus Across Stages

- **Early** = broad / usefulness ("right thing?")
- **Late** = narrow / usability ("easy to use?")

---

## 4. Sketches & Prototypes (M5)

### Buxton: Sketches vs. Prototypes

| Sketches | Prototypes |
|---|---|
| Design exploration | UX engineering |
| **Right** design | Design **right** |
| Ideation | Iterative refinement |

### Sketch Properties

Anyone can sketch. Quick, inexpensive, **disposable**, just-in-time. Annotated.

### Wireframes

Outline boxes capturing emerging interaction designs. **Deliberately unfinished** — no finished graphics, colors, fonts.

**Four wireframe questions:** key interactions? supporting widgets? best layout? matches mental model?

### Prototype Types (which details left out?)

- **Horizontal** — broad, shallow
- **Vertical** — narrow, deep (realistic eval of few features)
- **T** — most low-depth, a few deep
- **Local** — one specific interaction

### Wizard of Oz

Simulate without building — hidden human handles response. Good et al. 1984: natural-command-line.

### Critique Rules

- **Designer:** state what you want feedback on; dispassionate; show alternatives
- **Critic:** comment on *design*, not designer; specific positives; ask for alternatives, don't prescribe

---

## 5. Think-Aloud Usability (M6)

### Steps in Order

1. Formulate goals
2. Design protocol/tasks/materials
3. Conduct study
4. Analyze data → assess performance, identify usability issues

### Participants

- Representative of target users; consider classes
- **4–5 participants catch ~80% of problems** (Nielsen & Morlich 1990); Krug suggests 3
- Can include UX experts

### Tasks

- Scenario + goal, but **NOT how to do it**
- Communicate end criterion + max time
- Avoid training unless target users would have it
- Evaluate the **design**, not the user

### Critical Incident Report Structure

1. **Problem statement** — summary + effect (no solution)
2. **User goals** — what they were trying to do
3. **Immediate intention** — what they were doing *at the moment*
4. **Possible causes** — speculation

Group similar incidents → identify underlying cause → brainstorm fixes.

### Usability Study vs. CI

| Usability Study | CI |
|---|---|
| Evaluation | Needfinding |
| Observation | Conversation |
| Critical incidents | Contextual data |
| Identifies issues | Informs design |

### Open vs. Bad Questions

- Bad: "Did you find it useful?" (yes/no, leading)
- Good: "How might the UI better support what you're trying to do?"

---

## 6. Site Design (M7)

### Course Pivot

Half 1 = learn from users. Half 2 = apply principles. Design space too big to user-test everything.

### Effective Site Design — Six Questions

A good site makes these obvious:

1. What site is this?
2. What page am I on?
3. What are the major sections?
4. What are my options at this level?
5. Where am I in the site?
6. How can I search?

### Navigation Tools

- **Persistent navigation** — main nav always accessible
- **Tabs** — binder/folder metaphor; partition content; hard to miss
- **Breadcrumbs** — trail showing path + current location
- **Progressive disclosure** — most-used first, advanced behind expand control

### Information Foraging (Pirolli & Card)

| Term | Meaning |
|---|---|
| Patch | A location (page, dialog) |
| Links | Connections between patches |
| Cues | Text/visuals on outgoing links |
| Information scent | Visible cues signaling page match |
| Diet | Info sources user will consider |

**Rate of gain = info value / cost.** Users maximize this. Search increases competition (first impressions are fast).

### Design Implications of IFT

1. Group related info together
2. Design effective cues
3. Match user mental model
4. Provide search for large spaces

### Metaphor vs. Idiom

| Metaphor | Idiom |
|---|---|
| Real-world model (desktop, recycle bin) | Consistent UI model with no real-world basis (cut/copy/paste, follow) |
| Intuitive | Learn once, apply broadly |
| **Tyranny of metaphor:** breaks at extremes (folders 10 deep) | No metaphor friction |

### Interaction Flow Guidelines

- Don't use dialogs to report normal behavior
- Separate commands from configuration
- Don't ask questions — give choices
- Provide defaults, show options
- Make dangerous choices hard to reach
- **Design for the probable, provide for the possible**

---

## 7. Interaction Design (M8)

### Fitts's Law

**Time decreases with target size, increases with distance.**

- Movements = ballistic + homing; homing dominates time and errors
- Bigger = faster
- Closer to cursor = faster (context menus)
- 1D constraint dramatically increases speed (scroll bars)
- **Edge of screen = infinite target** (Mac menu bar)

### Modes

A mode changes what a command does. **Inconsistent mapping** is the problem (Ctrl+S sometimes saves, sometimes sends). Especially dangerous for automatic System-1 actions.

**Guideline:** avoid; if needed, distinguish mode + show how to switch.

### Mobile

Smaller form factor; no cursor → rely on **static** hinting (no dynamic). Fingers occlude. Sensors enable new inputs (camera, mic, GPS, gyro, accelerometer, barometer, proximity, ambient light).

### Disabilities

- **Perception** — visual/auditory
- **Motion** — fine motor, weakness, fatigue
- **Cognition** — memory, planning, sequencing

Blind users: screenreaders at 400+ wpm. Need **alt-text** + **hierarchy** for skim-by-listening.

### Universal vs. Assistive Design

- **Assistive** = equivalent actions for disabled users
- **Universal** = normal actions usable by widest range
- **Curb cut** = universal design exemplar (helps wheelchairs AND suitcases, carts, bikes)

### Seven Principles of Universal Design

1. Equitable use
2. Flexibility in use
3. Simple and intuitive
4. Perceptible information
5. Tolerance for error
6. Low physical effort
7. Size and space for approach and use

---

## 8. Preventing Error (M9)

### Direct Manipulation (Shneiderman 1982)

> "Rapid incremental reversible operations whose impact on the objects of interest is immediately visible."

**Characteristics:** continuous representation, physical actions, continuous + reversible feedback. **Spreadsheets** = canonical example.

**Drawbacks:** few objects on screen, physically demanding, slow for large sequences, bad for repetitive expert tasks, gestures error-prone.

### Error Taxonomy (Memorize This)

```
Unsafe Acts
├── Unintended
│   ├── Slip (attentional): intrusion, omission, reversal, misordering, mistiming
│   └── Lapse (memory): omitting items, place-losing, forgetting intentions
└── Intended
    ├── Mistake
    │   ├── Rule-based (wrong rule applied)
    │   └── Knowledge-based (missing info)
    └── Violation: routine, exceptional, sabotage
```

### Slips vs. Mistakes — Where in the Action Cycle?

- **Mistakes** at Goal/Plan/Compare (top — wrong goal/plan)
- **Slips** at Specify/Perform/Perceive/Interpret (bottom — right goal, wrong execution)

### Canonical Examples

| Type | Example |
|---|---|
| Slip | Poured milk into coffee, then put coffee in fridge (right action, wrong object) |
| Strong habit intrusion | Drove to usual destination instead of new one |
| Omission | Picked up coat, phone rang, left without it |
| Mistimed check | Interrupted while tying shoes, can't resume |
| Memory lapse | Got pen out, distracted, left pen on desk |
| Rule-based mistake | Bouncers blocked exits during fire ("not following the rules") |
| Knowledge-based mistake | Driver feels ABS vibration, lifts foot, defeats ABS |
| Routine violation | Running a red light because everyone does |

### Preventing Error (Hierarchy)

- Good: **detect** errors
- Better: **show how to fix**
- **Best: prevent with constraints**

### Other Tools

- **Undo** — most powerful mitigation; not always possible (sending email)
- **Forcing functions** — ATM: take card *before* taking cash
- **Swiss cheese model** — accidents must penetrate multiple layers; add layers, shrink holes, alert when holes line up
- **Root cause** — keep asking *why* (F-22 crash: "pilot error" → pilot unconscious from oxygen failure)

### Tone of Feedback

- Don't make user feel stupid
- System takes blame
- Be positive, encouraging
- Helpful, not cute
- Avoid violent words ("illegal," "invalid")

---

## 9. Visual Design (M10)

### Visual Design = Communication

> "Information consists of differences that make a difference." — Tufte

Goal: **efficiently and accurately** transmit info from system to user. Visual variables + organization encode information.

### Four Goals

1. Successfully transmit information
2. Coherent and consistent design
3. Reduce visual search time
4. Create desired emotional reactions

### Scale, Contrast, Proportion — Four Principles

- **Clarity** — contrasts clear and easily differentiated
- **Harmony** — proportions harmonious
- **Activity** — use contrasts to maintain orientation
- **Restraint** — strong, few, never overwhelming

### Gestalt Principles (Memorize)

| Principle | Meaning | Example |
|---|---|---|
| Proximity | Nearby = grouped | Spacing forms columns vs. rows |
| Similarity | Shared attributes = grouped | Filled vs. open circles read as rows |
| Continuity | Simplest physical explanation | "+" reads as 2 lines, not 4 segments |
| Closure | Complete despite missing info | IBM logo, Kanizsa triangle |
| Area | Smaller = figure, larger = ground | FedEx arrow |
| Symmetry | Ambiguous = multiple symmetric | Overlapping diamonds |

### Layers

Contrasting color/value/texture segregate info into separate readable layers. **Squint test** — squint to see if groups hold together.

### Hierarchy

- Order groups by perceptual prominence = reading sequence
- **Bolder, not bigger** for emphasis
- **Lighter, not smaller** for de-emphasis
- Color and weight do hierarchy work at lower visual cost than size
- Buttons: **Primary** (filled) / **Secondary** (outlined) / **Tertiary** (text link)

### Grouping — Use Fewer Borders

Prefer: negative space, box shadows, different backgrounds. Bounding boxes are heavy.

### Emphasis (IxDF)

A focal point — eye-catching area distinct from surroundings.

**Techniques:** lines, shapes, colors, textures, mass.

**By breaking patterns:** balance/symmetry, proximity, alignment, repetition, contrast, white space.

**Key rule: emphasis is relative.** Multiple emphasized areas saturate and confuse.

### Skeuomorphism

Visual sibling of metaphor (resembling physical reality). **Excessive** = distracting, wastes bandwidth. Trend → flat interfaces.

---

## 10. Icons & Design Languages (M11)

### Four Types of Iconic Representation

| Type | Meaning | Example |
|---|---|---|
| Similar | Visually analogous | Right-turn sign |
| Example | Exemplifies concept | Airplane = airport, scissors = cut |
| Symbolic | Abstract concept | Lightning = electricity |
| Arbitrary | Must be learned | Radioactive, biohazard |

### Four Principles of Icon Design

1. **Immediacy** — perceived effortlessly (bold, clear, balanced)
2. **Generality** — represents a class, not an individual (bathroom icons strip personal features)
3. **Cohesiveness** — set shares visual variables
4. **Characterization** — calls to mind distinctive features (hanger for closet)

### Abstraction Trade-off

Simplifying realistic icons makes them clearer **up to a point**, then loses meaning.

### Design Languages

Describes how to express ideas in the interface. Tied to Nielsen's **consistency and standards**.

- **Elements** — visual building blocks (view controls, source indicators, action buttons)
- **Syntax** — how elements compose (task, placeholder, toolbar, list)

**Goals:** colors, typography, organization, multi-resolution/device, universal design.

**Why it matters:** idioms create user expectations; branding creates associations (a photography site that looks like ESPN sends mixed signals).

---

## 11. Information Visualization (M12)

### Why Viz Amplifies Cognition

1. Increases memory + processing
2. Reduces search
3. Detects patterns visually
4. Enables perceptual inference
5. Uses attention for monitoring
6. Encodes info in manipulable medium

### Anchors

- **John Snow, 1854** — Broad Street cholera, plotted deaths on map, removed pump handle
- **Minard's Napoleon** — army size + path + direction + temperature + time

### Visualization Pipeline

Raw Data → [Data Transformations] → Data Tables → [Visual Mappings] → Visual Structures → [View Transformations] → Views

Closed by **human interaction** at every stage, driven by user **task**.

### Data Types

- **Nominal** — unordered (gender, hair color)
- **Ordinal** — ordered, no meaningful differences (likert)
- **Quantitative** — numeric (height, distance)

### Data Transformations

- **Classing/binning** — Q → O (histograms)
- **Sorting** — N → O
- **Descriptive stats** — mean, median, max

### Visual Structure Components

1. **Spatial substrate** — axes (unstructured / N / O / Q)
2. **Marks** — points (0D), lines (1D), areas (2D), volumes (3D)
3. **Mark properties:**
   - Spatial: position, size, orientation
   - Object: grayscale, color, texture, shape

### Effectiveness by Data Type (Memorize)

| Property | Q | O | N |
|---|---|---|---|
| Position | ✓ | ✓ | ✓ |
| Size | best | best | weak |
| Grayscale | weak | good | weak |
| Color, texture, shape | weak | weak | best |

### Animation

Encoding data **as a function of time** is usually weak (hard to compare). Animate **transitions between user states** instead.

### Common Viz Types

**Time-series / multi-component:**
- Stacked graph (visual summation)
- Small multiples (better than overlays)

**Geographic:**
- Choropleth (color by area)
- Cartogram (distorts geography for size + color)

**Hierarchies/networks:**
- Node-link, dendrogram, treemap, force-directed, arc diagram, adjacency matrix

---

## 12. Principles for Visualization (M13)

### Tufte's Principles of Graphical Excellence

A good viz should:

1. Show the data
2. Get viewer thinking about substance, not method
3. Avoid distortion
4. Pack many numbers into small space
5. Make large data sets coherent
6. Encourage comparison
7. Reveal data at several levels of detail
8. Serve a clear purpose (description, exploration, tabulation, decoration)

### Data-Ink

- **Data-ink** = non-redundant ink encoding data
- **Data-ink ratio** = data-ink / total ink
- = 1 − proportion that could be erased without loss

**Principles:**
- Above all, show the data
- Erase non-data-ink (within reason)
- Erase redundant data-ink
- **Chartjunk** — decorative distractions

### Distortions = Design Variation Without Data Variation

### Common Ways Viz Mislead (Memorize)

- **Truncated axes** — exaggerate small differences
- **Inconsistent scales** — dual axes, non-linear
- **Cherry-picked time ranges**
- **Inappropriate chart types** (3D pies)
- **Area vs. length** — doubled radius = quadrupled area
- **Missing context** — no baseline
- **Correlation ≠ causation**
- **Aggregation bias** — Simpson's paradox

### Shneiderman's Mantra (Memorize)

> "Overview first, zoom and filter, then details-on-demand."

**Tasks:** Overview, Zoom, Filter, Details on demand, Relate, History, Extract.

### Heuristics

- Match encoding to data type (Q/O/N)
- Reduce cognitive load — let perception do the work
- Avoid 3D unless data is genuinely 3D
- Color: categorical / sequential / diverging
- Label directly; avoid legend chases

---

## 13. Community Design (M14)

### Course Pivot

Cognitive psychology → social psychology. User-to-user interactions are **shaped and enabled by the UI** and can be designed.

### Definition (Kraut & Resnick)

Virtual spaces where people converse, exchange info/resources, learn, play. Break barriers of **time, space, scale**.

### Cognitive vs. Community Design

| Most of course | Community design |
|---|---|
| Task performance | Community behavior |
| Cognitive psychology | Social psychology |

### Four Dimensions of Socio-Technical Design

1. **Community structure** — size, homogeneity, subgroups, ties
2. **Content/tasks/activities** — self-disclosure vs. anonymity, professional vs. UGC, welcoming, independent vs. interdependent
3. **Feedback/rewards/sanctions** — informal vs. structured; intangible (status) vs. tangible (privileges, prizes)
4. **Roles/rules/access control/visibility** — specialized roles, behavior rules, decision procedures, access controls, moderators, **visibility of bad behavior + punishment**

### Four Challenges

1. Starting a new community
2. Encouraging contribution
3. Encouraging commitment
4. Regulating behavior

### Anchor: Facebook Reactions

- **Like** = positive, avoids negative judgment
- **Dislike** would turn it into voting
- **Reactions** (Like, Love, Haha, Yay, Wow, Sad, Angry) = expressive without thumbs-down
- Lesson: small UI choices have big behavioral consequences

---

## 14. Challenge 1 — Starting a Community

### Difficulties

- Communicating value
- Visibility
- Competition

### Carving a Niche

- Pick scope by **topic** or **pre-existing group**
- Mixed-topic = lower value
- Subdivide spaces — but **NOT** prematurely (empty rooms feel worse than crowded)

### Critical Mass

Costs ~fixed per user; value increases with N. **Critical mass** = where benefits dwarf costs. Why use Facebook? Because everyone else does.

### Bootstrapping

- Incentives (Epinions paid early reviewers — but pay-stop demotivates)
- Discounts/free services (less problematic)
- Viral spread (invite-a-friend)

### Early Adopter Benefits

- Permanent discounts
- Status (cool-finder identity)
- Scarce, claimable resources (usernames, low member numbers)

### Competition Tactics

- Reduce startup costs (OAuth/SSO)
- Cross-posting
- Advertising — *"the aura of inevitability is a powerful weapon"*

---

## 15. Challenge 2 — Encouraging Contribution

### Contribution Gap Causes

- Too much work, not enough workers
- Users don't know how to help
- Tasks aren't appealing

### Visibility

- Lists of needed contributions (Wikipedia: 125,000 articles need citations)
- Track work as it's done (FB profile changes in newsfeed)
- **Personal appeals** work best when: simple, stresses benefits, from high-status / likable member

### Requesting

- **Social proof** — others have already complied (ESP game: "over a million labels")
- **Specific challenging goals** — "rate 16 movies on MovieLens this week"
- **Group goals + deadline + frequent feedback** (fundraising thermometer)

### Motivation

- **Intrinsic** — activity is its own end
- **Extrinsic** — activity is a means to an end
- WoW: enjoy slaying monsters (intrinsic) vs. enjoy the level (extrinsic)

### Rewards (Extrinsic)

- **Reputation/status** — changes how others treat you
- **Privileges** — opens new actions (commit rights on OSS)
- **Tangible** — money, prizes

### Perverse Incentives

- Wrong incentives → counterfeit actions (rewards for invites → fake invites)
- Quantity-based rewards get gamed
- **Status/privileges gamed less than tangible rewards** — value disappears once gamed
- Less transparent / more unpredictable criteria → less gaming

### Intrinsic vs. Extrinsic Trade-off

- Extrinsic **can reduce** intrinsic motivation (less likely to donate blood when paid)
- Tangible incentives diminish intrinsic motivation when they reduce **autonomy** and **competence** (perceived as controllers)

### Comparative Feedback (Leaderboards)

Motivating to beat competitors. **But also demotivating:**
- Reminds you how much time was "wasted"
- May feel done enough
- Discouraging when top is unattainable

### Collective Outcomes Motivate When

- More committed to the group
- Group is smaller
- Members feel they make a unique contribution
- Contributions are **complementary or contingent** (not substitutes)

---

## 16. Challenge 3 — Encouraging Commitment

### Why It Matters

Committed users work harder, stick with it, sustain through problems, enforce norms.

### Three Types (Memorize)

| Type | Stance | Grounded in |
|---|---|---|
| Affective | "I want to" | Closeness/attachment to members |
| Normative | "I ought to" | Obligation to the group |
| Need-based / continuance | "I must" | Net cost of leaving |

A user can have more than one at once.

### Two Sub-types of Affective

- **Identity-based** — attachment to community **as a whole**, mission
- **Bonds-based** — attachment to **specific people**

### Encouraging Identity-based

- Cluster similar members (FB group for Mason SWE)
- Explicit name + tagline ("free encyclopedia anyone can edit")
- Subgroup identity → larger-community identity
- Make community fate/goals/purpose explicit
- Joint, interdependent tasks (WoW guilds)
- Highlight an out-group (Wikipedia vs. Britannica)
- Anonymity raises group identity

### Encouraging Bonds-based

- Recruit members with existing ties (Piazza for a course)
- Friend-of-friend interactions
- Profile photos + recent activity
- DMs / personal conversation
- Repeat-encounter mechanisms
- Profile pages with self-disclosure → interpersonal liking
- Pseudonymous self-disclosure for sensitive info

### Encouraging Normative

- Highlight community purpose + success
- Testimonials from committed members
- Prime reciprocity (cancer survivors who keep posting after remission)
- Highlight chances to return favors

### Encouraging Need-based

Match experiences to motivations. Know community needs. Motivational mix varies (info, companionship, social support, fun).

---

## 17. Challenge 4 — Regulating Behavior

### Damage Types

- **Trolls** — disruption for satisfaction
- **Manipulators** — want particular outcome (Wikipedia POV pushers)
- **Low-quality contributors** — waste community attention

### Limiting Bad Behavior

**Pre-screening / moderation:**
- Pre-screen content before posting
- Effectiveness factors:
  - **Redirect** inappropriate posts (vs. delete)
  - Consistently applied criteria + appeals
  - Moderation seen as **impartial**

**Post-hoc tools:**
- Reversion tools (Wikipedia)
- Filters / influence limiters (downrank vs. delete)
- Activity quotas (anti-spam)
- Gags and bans

### Encouraging Voluntary Compliance

Cheap default; norms work best when members regulate themselves.

- Make norms clear and salient by displaying examples of **appropriate** behavior
- Publicly contrast inappropriate vs. appropriate
- Show formal feedback given to violators (transparency)
- Display statistics about normative behavior ("X days since last workplace injury")

---

## 18. Designer Ethics & Dark Patterns

### Existential Values

- What are your values? (facilitating tasks, broadening access, expressing truth, refraining from collecting data)
- How do they align with business?
- How do you encode them into design intent?

### Six Dark Patterns (Memorize Cold)

| Pattern | What it does | Example |
|---|---|---|
| **Sneaking** | Auto-add to transaction | Greeting card surprise in cart |
| **Urgency** | Fake time pressure | Countdown timer that resets |
| **Misdirection** | Visual hierarchy/wording steers choice | Confirmshaming ("No thanks, I like full price") |
| **Scarcity** | Fake low availability | "Only 3 left in stock" |
| **Obstruction** | Easy in, hard out | Call to cancel |
| **Forced action** | Required signup to access | "Continue with Facebook" gating browsing |

**Mnemonic:** *S U M S O F* (Sneaking, Urgency, Misdirection, Scarcity, Obstruction, Forced action).

### Benevolent Intent

User needs above all, business goals balanced. Hard to achieve, but necessary.

---

## 19. Easily-Confused Pairs (Self-Quiz)

| Concept A | Concept B | Distinction |
|---|---|---|
| Affordance | Signifier | Affordance = possibility; signifier = perceivable indicator |
| Slip | Mistake | Slip = right goal/wrong execution; mistake = wrong goal/plan |
| Rule-based mistake | Knowledge-based mistake | Rule applied wrong vs. info missing |
| Lapse | Slip | Memory failure vs. attention failure |
| Metaphor | Idiom | Real-world model vs. learned UI model |
| Horizontal proto | Vertical proto | Broad/shallow vs. narrow/deep |
| CI | Usability study | Needfinding vs. evaluation |
| Assistive | Universal | Equivalent action vs. broadest user range |
| Identity-based | Bonds-based | Community as whole vs. specific people |
| Affective | Normative | "Want to" vs. "ought to" |
| Choropleth | Cartogram | Color by area vs. area distorted |
| Stacked graph | Small multiples | Visual summation vs. side-by-side |
| Skeuomorphism | Metaphor | Visual sibling — skeuo is the visual form |
| Intrinsic | Extrinsic | Activity is the end vs. means to an end |
| Discoverability | Feedback | Can user find action? vs. Can user see what happened? |
| Gulf of Execution | Gulf of Evaluation | Intent → action vs. state → understanding |

---

## 20. Canonical Examples (Anchors for Recall)

| Example | What it shows |
|---|---|
| Refrigerator (Norman) | Wrong conceptual model |
| Mercedes seat control | Natural mapping |
| Scissors | Good conceptual model |
| Door with PUSH sign | Failed signifiers |
| Curb cut | Universal design |
| F-22 crash (oxygen) | Root cause beyond "pilot error" |
| ATM (card before cash) | Forcing function |
| Bouncers blocking exits in fire | Rule-based mistake |
| ABS brake driver | Knowledge-based mistake |
| Spreadsheet | Direct manipulation |
| FedEx logo | Gestalt area (figure/ground) |
| IBM logo / Kanizsa triangle | Gestalt closure |
| London Underground map | Simplification (sacrificed geography) |
| OSX Finder (2010 → 2021) | Trend toward simplicity |
| John Snow, 1854 cholera | InfoViz amplifying cognition |
| Minard, Napoleon in Russia | Multi-variable viz |
| NYT Rent vs. Buy | Interactive viz, Shneiderman's mantra |
| Nobel Prizes 1901–1974 | Small multiples |
| 2020 weighted electoral map | Cartogram correcting bias |
| Facebook Reactions | Small UI choice → big behavioral effect |
| Wikipedia "free encyclopedia anyone can edit" | Identity-based commitment |
| Piazza for a class | Bonds-based commitment via existing ties |
| ESP game ("over a million labels") | Social proof |
| WoW guilds | Joint interdependent tasks |
| Epinions paying reviewers | Bootstrapping (and intrinsic-motivation trap) |
| "X days since last workplace injury" | Make norms salient |
| Confirmshaming "No thanks, I like full price" | Misdirection dark pattern |

---

## 21. Last-Pass Cheat List (The Night Before)

If you can recite these from memory, you'll do fine.

1. **Seven stages of action** (Goal, Plan, Specify, Perform, Perceive, Interpret, Compare) and the two **gulfs**
2. **Six fundamental principles** + the **seventh (Discoverability)**
3. **Affordance ≠ signifier**
4. **Four constraint types** (physical, cultural, semantic, logical)
5. **Double Diamond** — Discover/Define/Develop/Deliver
6. **CI four principles** (context, partnership, interpretation, focus)
7. **CI vs. usability** comparison
8. **Buxton sketches vs. prototypes**
9. **Prototype types** (horizontal, vertical, T, local) + **Wizard of Oz**
10. **4–5 participants catch 80%** of issues
11. **Critical incident report** (problem statement, user goal, immediate intention, possible cause)
12. **Six site-design questions**
13. **Information foraging** vocabulary + rate-of-gain formula
14. **Metaphor vs. idiom**
15. **Fitts's Law** and screen-edge as infinite target
16. **Universal design** vs. assistive; **curb cut**; seven principles
17. **Error taxonomy** — slip/lapse/mistake (rule/knowledge)/violation
18. **Slips vs. mistakes** in action cycle
19. **Forcing functions, undo, swiss cheese model, root cause**
20. **Tone of feedback** — system takes blame
21. **Six gestalt principles** + the **squint test**
22. **Hierarchy via color and weight, not size**; primary/secondary/tertiary buttons
23. **Emphasis is relative**
24. **Four icon types** + **four icon principles**
25. **Design language** = elements + syntax (consistency & standards)
26. **Visualization pipeline** (Raw → Tables → Structures → Views)
27. **Effectiveness table** — position is the universal winner
28. **Tufte's data-ink ratio** + **chartjunk**
29. **Shneiderman's mantra** — overview, zoom, filter, details-on-demand
30. **Eight ways viz mislead**
31. **Four community design dimensions** + **four challenges**
32. **Three types of commitment** (affective [identity/bonds], normative, need-based)
33. **Intrinsic vs. extrinsic** + crowding-out effect
34. **Six dark patterns** (S-U-M-S-O-F)
35. **Cognitive (most of course) vs. social (M14)** — the framing pivot

---

**Final note for the exam:** when stuck, ask which of the cross-cutting themes the question is really about. Almost every answer reduces to: *which gulf, what mental model, what observation, what constraint, what visibility, what motivation.*
