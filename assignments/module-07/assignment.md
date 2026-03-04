# Module 7 Individual Assignment - Course Catalog & Registration System

**Due:** Monday (submit PDF on Canvas)
**Type:** Individual (must be your own work)

## Requirements

Design a course catalog and registration system with sketches showing key screens and user interactions.

**Must support:**
1. Browsing course catalog
2. Registering for classes
3. Waitlists
4. Building a plan of courses over multiple semesters to fulfill degree requirements

**Deliverable:** Annotated sketches explaining how users interact with the system, submitted as PDF.

## Relevant Module 7 Principles to Apply
- Hierarchy (catalog organized by department, level, etc.)
- Information foraging / scent (clear cues for finding courses)
- Progressive disclosure (overview first, details on demand)
- Effective site design (the 6 questions)
- Task structure and sequencing
- Breadcrumbs / navigation
- Anticipating likely next actions
- Interaction flow guidelines

## Design Brainstorm

### Overall Layout

Split-panel design with two main areas:
- **Left panel: Course Catalog** (browse, search, filter, register)
- **Right panel: Degree Plan** (multi-semester timeline, requirements tracker, schedule view)

Panels use expand/collapse behavior. Clicking one expands it while the other shrinks. The collapsed panel still shows key info at a glance so both tasks stay connected.

Search bar at the top of the catalog panel, always visible. Can search by course name, number, or professor. Results replace the filtered list, but active filters still apply on top of search.

---

### Screen 1: Catalog Panel (Expanded)

**Filters (top or sidebar):**
- Semester (most important, top-level)
- Department
- Level (100, 200, 300, etc.)
- Modality (synchronous / asynchronous)
- Time of day (morning / afternoon / evening)
- Days of week (MWF / TR / single day)
- Open seats / availability toggle
- "Fulfills requirement" filter (connects to degree plan, e.g., "show CS electives only")

**Class cards (at a glance):**
- Course number and name
- Professor
- Days / time
- Modality
- Seats available
- Requirement badge for YOUR major (e.g., "Core Requirement", "CS Elective")

**Class card (expanded / detail view - progressive disclosure):**
- Syllabus link
- Course description / learning objectives
- Key assignments
- Prerequisites

**Actions on each card:**
- "Register" button (adds to current semester schedule)
- "Add to Plan" button (adds to a future semester in degree plan)

---

### Screen 2: Registration Status (Color System)

When adding a class to your schedule:
- **Green** = clear, no conflicts, registered successfully
- **Yellow** = conflict exists (time overlap with another class, missing prerequisite). Class is still added but flagged with a warning tooltip: "Time conflict with CS 632 on Tuesdays" or "Requires CS 330 first"
- **Red** = class is full, automatically added to waitlist

Inline confirmation banner after registering: "Added to Spring 2026 schedule" (no dialog popup, follows interaction flow guideline).

---

### Screen 3: Waitlist Flow

- When adding a full class (red), user is automatically placed on the waitlist
- Class card shows "Waitlisted - Position #3"
- Notification (bell icon or email) when a spot opens
- User has a time window (24 hours) to confirm or they lose the spot
- Waitlisted classes still appear on schedule/plan but visually distinct (red border or dimmed)

---

### Screen 4: Degree Plan Panel (Expanded)

**Requirements tracker (top of panel):**
- Shows all degree requirements for your major
- Uses icons/shapes (not colors) to differentiate from registration status:
  - Filled circle/checkmark = completed
  - Half-filled circle = planned but not yet taken
  - Empty circle = not planned at all
- Clicking an unfulfilled requirement filters the catalog to show only qualifying classes

**Semester timeline (below tracker):**
- Semesters stacked vertically, earliest at top, latest at bottom
- Each semester is a row with class chips laid out horizontally
- Class chips show course number/name and requirement badge

**Prerequisite visualization:**
- If a class is placed in a semester before its prerequisite, it gets a yellow warning: "Requires CS 330 first"
- Small "prereq" tag on class chips that links to what's needed

---

### Screen 5: Schedule Toggle (Weekly Calendar View)

- Toggle button on the degree plan panel to switch between:
  - **Timeline view** (all semesters, vertical stack)
  - **Schedule view** (weekly calendar for a selected semester)
- Calendar shows time blocks for each class with days across the top
- Conflicts are visually obvious (overlapping blocks highlighted in yellow)
- Helps users see their actual week before committing to registration

---

### Drop/Remove Flow

- X button on any class card to remove from schedule or plan
- Registered class: confirmation prompt "Drop CS 632? This will remove you from the class."
- Waitlisted class: removes from waitlist immediately, no confirmation needed
- Planned (future) class: removes from plan immediately, no confirmation needed

---

### Principles Applied

| Design Element | Module 7 Principle |
|---|---|
| Split panel with expand/collapse | Progressive disclosure |
| Filters narrowing results | Hierarchy, information foraging |
| Requirement badges on class cards | Information scent (strong cues) |
| Search bar always visible | Effective site design (Q6: How can I search?) |
| Green/yellow/red registration status | Idiom (traffic light pattern, learned once) |
| Requirement tracker filtering catalog | Anticipating likely next actions |
| Semester timeline layout | Task structure and sequencing |
| Schedule toggle | Flexibility and efficiency |
| Inline confirmations, no dialogs | Interaction flow guidelines |
| "Fulfills requirement" filter | Bridging both panels / reducing foraging cost |

---

## Next Steps

1. **Sketch the 5 screens** (paper or digital): main split-panel view, catalog expanded, degree plan expanded, schedule toggle, and waitlist/registration states
2. **Annotate each sketch** explaining how users interact (use the principles table above)
3. **Show transitions** between screens (arrows or numbered flow showing how user moves between views)
4. **Export as PDF** and submit on Canvas by Monday
