# Design Language: 3Waves Software

## Company Description

3Waves Software is a product I work on that operates in the military tech space. Our primary product is a flight simulation add-on. The design language below reflects the choices we've made for our public-facing website.


## Design Language Elements

### 1. Display Heading

**Purpose:** Display headings are the first text element a visitor sees when landing on a page section. They capture attention immediately and communicate the primary message of each section. Used for hero banners and major section introductions.

**Style:** Barlow Semi Condensed, weight 700, sized fluidly from 3rem to 5rem using CSS `clamp()`. Color is primary white (`#E6EDF3`). Line height is tight at 1.2 to keep multi-line headings compact and impactful. The semi-condensed width lets us use large sizes without overwhelming the layout.


### 2. Eyebrow Label

**Purpose:** Small text placed above a heading to categorize or contextualize the content below it. It signals to the reader what type of content follows before they reach the main heading (e.g., "CAPABILITIES", "PLATFORM SUPPORT"). Borrows from defense industry documentation conventions where section classifications appear above titles.

**Style:** Inter, weight 600, 0.8rem, fully uppercase with wide letter-spacing (0.2em). Color is the brand cyan (`#00B4D8`). The combination of small size, uppercase, and generous letter-spacing makes it visually distinct from both headings and body text, creating a clear hierarchy without competing for attention.


### 3. Body Text

**Purpose:** The primary reading text for descriptions, explanations, and general content. Needs to be highly readable at length since visitors may be reading technical product descriptions or integration details.

**Style:** Inter, weight 400, sized fluidly from 1rem to 1.125rem. Color is secondary text (`#B1BAC4`), which is intentionally softer than the primary white used for headings. This contrast difference reinforces the visual hierarchy. Line height is 1.7-1.8 for comfortable reading on dark backgrounds, where tighter spacing can feel claustrophobic.


### 4. Technical/Monospace Text

**Purpose:** Used for version numbers, file names, API references, system specifications, and download details. Sets technical content apart from marketing copy, signaling to the reader that this is precise, literal information (not descriptive prose).

**Style:** JetBrains Mono, weight 400, slightly smaller than body text. This font carries over from our desktop application's dashboard UI, creating a visual connection between the website and the product itself. Used inline or in small blocks, never for long-form reading.


### 5. Navigation Bar

**Purpose:** Provides persistent access to all major sections of the site. Stays visible as users scroll so they can reorient or jump to a different section at any time. The visual treatment keeps it present without blocking content.

**Style:** Fixed position at the top of the viewport. Background uses the base dark color (`#0A0E14`) at 85% opacity with a 20px backdrop blur, so content scrolls behind it with a frosted-glass effect. Nav links are Inter weight 500, 0.9rem. The active page link is highlighted with cyan text and a subtle cyan background tint (`rgba(0, 180, 216, 0.1)`). Hover transitions use a 0.3s ease-out curve.


### 6. Primary Button

**Purpose:** The main call-to-action element. Used for downloads, contact forms, and key user flows. Designed to stand out against the dark background and draw the eye toward the action we want visitors to take.

**Style:** Outlined by default with a 1px cyan (`#00B4D8`) border and cyan text. On hover, the button fills with a solid cyan background and the text shifts to dark. Text is uppercase, Inter weight 600, with 0.08em letter-spacing. Padding is generous (14px vertical, 32px horizontal) to create a comfortable click target. Border radius is 6px for a slightly rounded feel that softens the otherwise technical aesthetic. Transition is 0.3s ease-out.


### 7. Content Card

**Purpose:** Groups related information into a distinct, scannable unit. Used for feature highlights, product summaries, and download items. The card format lets visitors quickly compare items side by side and pick what's relevant to them.

**Style:** Background is a raised surface color (`#1C2128`) with a 1px subtle border (`#21262D`). Border radius is 12-16px, noticeably rounder than buttons, which gives the cards a softer, more approachable feel within the technical design. On hover, cards lift upward with a `translateY(-4px)` transform and gain a deeper shadow (`0 20px 40px rgba(0, 0, 0, 0.5)`), providing clear interactive feedback. Internal padding uses the standard spacing scale (1.5-2rem).


### 8. Section Container/Spacing

**Purpose:** Controls the rhythm and breathing room between major content sections. Generous spacing prevents the dark interface from feeling dense or overwhelming, and gives each section visual weight and separation without needing explicit dividers.

**Style:** Max content width is 1200px (1400px for wide layouts), centered with auto margins. Vertical section padding scales fluidly from 5rem to 10rem using `clamp()`. Internal spacing follows a consistent scale: 0.5rem (xs), 1rem (sm), 1.5rem (md), 2rem (lg), 3rem (xl), 4rem (2xl), 6rem (3xl). This scale is used consistently across all components for alignment.


### 9. Status Indicator

**Purpose:** Communicates system state or availability at a glance (e.g., "Operational", "Update Available", deployment status). In a defense context, operators need to read status quickly and accurately. Color alone carries the meaning, reinforced by a glow effect that draws peripheral attention.

**Style:** Green (`#2EA565`) for positive/operational states, red (`#E04E52`) for warnings or issues. Each color has a lighter variant for text labels and a translucent glow version for background effects. The glow is achieved with box-shadow rather than background color, keeping the element's footprint small while still being noticeable. Green glow: `rgba(46, 165, 101, 0.25)`. Red glow: `rgba(224, 78, 82, 0.2)`.


### 10. Link/Interactive Text

**Purpose:** Indicates clickable text within body content or navigation. Needs to be clearly distinguishable from static text without disrupting reading flow.

**Style:** Cyan (`#00B4D8`) is used consistently for all interactive text, creating a strong learned association: cyan means clickable. On hover, the color brightens to `#00C9F0` and an underline appears. In navigation contexts, the hover state adds a subtle background tint instead of an underline. Transitions are 0.15s (fast) so the response feels immediate.


### 11. Glow/Accent Effect

**Purpose:** Adds visual emphasis and depth to key elements without using traditional drop shadows, which feel out of place on dark interfaces. The glow effect ties into the technical/tactical aesthetic and creates a sense of energy around important elements.

**Style:** Implemented as box-shadow with the brand cyan at low opacity: `0 0 40px rgba(0, 180, 216, 0.1)`. Used on hero elements, featured cards, and active states. A pulsing animation variant is used sparingly for elements that need sustained attention (like a live status dot). The glow reinforces the cyan brand color throughout the interface without adding new colors.


### 12. Footer

**Purpose:** Provides secondary navigation, legal information, and company details. Serves as a visual anchor at the bottom of the page and a final touchpoint for visitors who've scrolled through all content.

**Style:** Background is the deepest dark (`#0A0E14`), matching the nav bar to bookend the page. Text uses the tertiary color (`#7D8590`) at 0.875rem, intentionally de-emphasized. Links follow the standard cyan interactive pattern but at reduced size. A 1px top border in the subtle border color (`#21262D`) provides a clean separation from the content above. Layout uses a multi-column grid with generous spacing.


## How This Design Language Supports the Brand

The design language communicates three things about 3Waves Software that matter to our audience:

**Technical credibility.** The dark color scheme, monospace font for technical content, and restrained color palette borrow from themes common in military tech interfaces. The look is precise and purposeful, not flashy, which is what users in this space expect.

**Color as brand signal.** The blue-cyan accent palette gives the interface a "future technology" feel that highlights the tech space we operate in. Cyan also carries associations with safety and reliability, which reinforces trust in the product. It's a deliberate choice to connect the brand with both innovation and dependability.

**Consistency and reliability.** Every element follows the same spacing scale, color tokens, and transition timing. The cyan accent is used for one purpose (interactivity), status colors are used for one purpose (system state), and the typography hierarchy is predictable. This consistency mirrors what operators need from the software itself: predictable, reliable behavior.
