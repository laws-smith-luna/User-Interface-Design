# Module 5: Sketching and Prototyping

## Sketches vs. Prototypes (Buxton)

| Buxton Design Exploration Sketches | Low-Fidelity Design Refinement Prototypes |
|------------------------------------|-------------------------------------------|
| For **design** | For **UX engineering** |
| Getting the **right design** | Getting the **design right** |
| Experimenting, exploring, being creative | Following the UX process |
| **Goal:** Support ideation to find a great design solution | **Goal:** Support iterative refinement of a given design |

## Properties of Sketches

- **Everyone** can sketch; you do not have to be artistic
- Sketches are **quick** and inexpensive to create; do not inhibit early exploration
- Sketches are disposable; no **investment** in sketch itself
- Sketches are timely; made in-the-moment, **just-in-time**

## Sketches Include Annotations

- Annotations explain what is going on in each part of a sketch and how it works
- Example: Hand-drawn wireframes with written notes describing cursor behavior, interaction states, and visual feedback

## UI Storyboards

Elements of a UI storyboard:
- Hand-sketched pictures annotated with a few words
- Sketch of user activity before or after interacting w/ system
- Sketches of devices & screens
- Connections with system (e.g., database connection)
- Physical user actions
- Cognitive user action in "thought balloons"

## Wireframes

- Lines & outlines ("wireframes") of boxes & other shapes
- Capturing emerging interaction designs
- Schematic designs to define screen content & visual flow
- Illustrate approximate visual layout, behavior, transitions emerging from task flows
- **Deliberately unfinished:** do not contain finished graphics, colors, or fonts

### Creating a Wireframe

Key questions to ask:
1. What are the key interactions needed to support the design?
2. What widgets support these interactions?
3. What are the best ways to lay them out?
4. How do these relate to conceptual design & user's mental model?

## Design Critiques

### Designer: Frame the Discussion

- State **explicitly** what you want comments on:
  - Overall idea?
  - Usability?
  - Specific interaction design?
  - Visual design?
- Take a **dispassionate** stance (this is hard!)
  - Show alternatives where possible
  - Why? To objectively assess and improve the design

### Critic: How to Avoid Deaf Ears

- Comments about the **design**, not the designer
- Point out positive aspects — be **specific**
  - Not: "I like this, but..."
  - Better: "The layout effectively communicates the hierarchical nature of the data. However..."
- Ask for **alternatives** instead of offering solutions
  - Not: "You should really change X"
  - Instead: "Have you considered alternatives for X?"

## Prototyping

How do you know your system design is right before you invest the time to build it? **Prototyping!**

- Evaluation performed **before** investing resources in building finished product
- Early version of system constructed much **faster** & with less expense
- Used to evaluate & **refine** design ideas

### Types of Prototypes

Which details do you leave out?

- **Horizontal:** broad in features, less depth
  - Explore overall concept of app, but not specific workflows
- **Vertical:** lots of depth, but only for a few features
  - Enables testing limited range of features w/ realistic user evals
- **T:** most of UI realized at low depth, few parts realized in depth
  - Combination of vertical & horizontal
- **Local:** focused prototype on **specific** interaction detail

### Wizard of Oz

- Goal: **simulate** actual system without building it
  - Want user to interact **as if** they were interacting w/ real system
  - Helps explore how users would interact w/ novel interaction if it were to exist
- Example: natural command line (Good et al 1984)
  - Users typed in commands to interact w/ computer
  - Commands intercepted by hidden human who interpreted commands & executed them
