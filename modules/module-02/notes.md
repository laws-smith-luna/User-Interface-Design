# Module 2: Human Cognition and Design Principles

## The Seven Stages of Action

From Norman's *The Design of Everyday Things* (Chapter 2)

### Overview

There are two parts to an action:
1. **Executing** the action
2. **Evaluating** the results

Both require understanding how the item works and what results it produces.

### The Seven Stages

**One for Goals:**
1. **Goal** - Form the goal (What do I want to accomplish?)

**Three for Execution:**
2. **Plan** - Plan the action (What are the alternative action sequences?)
3. **Specify** - Specify an action sequence (What action can I do now?)
4. **Perform** - Perform the action sequence (How do I do it?)

**Three for Evaluation:**
5. **Perceive** - Perceive the state of the world (What happened?)
6. **Interpret** - Interpret the perception (What does it mean?)
7. **Compare** - Compare the outcome with the goal (Is this okay? Have I accomplished my goal?)

### Key Concepts

**Gulf of Execution**
- The gap between what users want to do and what actions they can take
- Bridged through: signifiers, constraints, mappings, conceptual model

**Gulf of Evaluation**
- The gap between system state and user's understanding of it
- Bridged through: feedback, conceptual model

**Feedforward vs Feedback**
- **Feedforward**: Information that helps answer questions of execution (doing) - accomplished through signifiers, constraints, mappings
- **Feedback**: Information that aids understanding what has happened

### Goal-Driven vs Event-Driven Behavior

- **Goal-driven**: Action cycle starts from the top by establishing a new goal
- **Event-driven (data-driven)**: Action cycle starts from the bottom, triggered by something in the world

### Root Cause Analysis

Always ask "Why?" to find the ultimate goal. Example:
- Person buys a drill → They want a hole → They want to hang shelves → They want to organize books

### Seven Fundamental Design Principles

Derived from the seven stages of action:

1. **Discoverability** - Possible to determine what actions are available and current state
2. **Feedback** - Full, continuous information about action results and current state
3. **Conceptual Model** - Design projects all information needed to understand the system
4. **Affordances** - Proper affordances exist to make desired actions possible
5. **Signifiers** - Effective use ensures discoverability and intelligible feedback
6. **Mappings** - Relationship between controls and actions follows good mapping principles
7. **Constraints** - Physical, logical, semantic, and cultural constraints guide actions

---

## Norman's Fundamental Principles of Interaction

From Norman's *The Design of Everyday Things* (Chapter 1)

### Discoverability

Results from appropriate application of five psychological concepts:
- Affordances
- Signifiers
- Constraints
- Mappings
- Feedback

Plus the most important: **Conceptual Model**

---

### 1. Affordances

**Definition**: The relationship between a physical object and a person that determines how the object could possibly be used.

- A chair affords sitting (and lifting, for those strong enough)
- Glass affords transparency and support, but blocks passage
- **Anti-affordance**: Prevention of interaction (e.g., glass blocking passage)

**Key Points**:
- Affordance is a *relationship*, not a property
- Depends on both the object's properties AND the agent's capabilities
- Affordances exist even if not visible
- For designers, visibility of affordances is critical

**Example**: A flat plate on a door affords pushing. Knobs afford turning, pushing, pulling. Slots are for inserting things.

---

### 2. Signifiers

**Definition**: Any mark, sound, or perceivable indicator that communicates appropriate behavior to a person.

**Relationship to Affordances**:
- Affordances determine what actions are *possible*
- Signifiers communicate *where* the action should take place
- We need both

**Types**:
- **Deliberate/Intentional**: A "PUSH" sign on a door
- **Accidental/Unintentional**: A worn path through grass showing where people walk

**Key Points**:
- Signifiers are more important to designers than affordances
- When you see hand-lettered signs on doors explaining how to use them, you're looking at poor design
- Perceived affordances often act as signifiers (but can be ambiguous)

**Example**: Arrows and icons on a touch screen signify permissible operations.

---

### 3. Mappings

**Definition**: The relationship between controls and their effects; borrowed from mathematics meaning the relationship between elements of two sets.

**Natural Mapping**: Taking advantage of spatial analogies for immediate understanding.
- Move control up → object moves up
- Arrange light switches in same pattern as ceiling lights
- Car seat control shaped like a seat

**Types of Natural Mappings**:
- **Spatial**: Layout of controls matches layout of items controlled
- **Cultural/Biological**: Moving hand up = more, down = less
- **Gestalt Principles**: Grouping and proximity for controls and feedback

**Key Points**:
- Related controls should be grouped together
- Controls should be close to the item being controlled
- What's "natural" can vary by culture

**Example**: Mercedes-Benz seat controls shaped like a seat - move front of control up to raise front of seat.

---

### 4. Feedback

**Definition**: Communicating the results of an action to the user.

**Requirements**:
- Must be **immediate** (even 0.1 second delay is disconcerting)
- Must be **informative** (not just beeps/lights)
- Must be **prioritized** (unimportant = unobtrusive, important = attention-grabbing)
- Must be **appropriate** (not too much, not too little)

**Problems with Poor Feedback**:
- Simple beeps/lights tell you something happened but not what
- Too much feedback causes people to ignore all of it
- Identical sounds from different devices cause confusion

**Examples**:
- Elevator buttons that don't light up → people press repeatedly
- Dishwasher beeping at 3am → inappropriate timing
- Operating room alarms creating dangerous cacophony

---

### 5. Conceptual Models

**Definition**: A simplified explanation of how something works. Doesn't need to be complete or accurate, just useful.

**Mental Models**: Conceptual models that reside in people's minds representing their understanding of how things work.

**Key Points**:
- People form models from the device itself, other people, or manuals
- Wrong models lead to difficulties
- Major clues come from: signifiers, affordances, constraints, mappings

**The System Image**: What the user can perceive from the product's appearance and behavior. This is what communicates the conceptual model to users.

**Classic Example - The Refrigerator Problem**:
- Two compartments (freezer, fresh food) with two controls
- Suggested model: Each control = one compartment (WRONG)
- Reality: One thermostat, one cooling unit; controls adjust temperature AND air distribution
- Result: Nearly impossible to set correctly

**Good Example - Scissors**:
- Holes clearly for fingers (affordance + signifier)
- Hole sizes constrain which fingers fit
- Operation visible and obvious
- Conceptual model is immediately clear

---

### 6. Constraints

**Four Types**:

1. **Physical**: Limit possible operations (e.g., key only fits one way)
2. **Cultural**: Conventions learned through culture (e.g., red = stop)
3. **Semantic**: Meaning constrains possibilities (e.g., windshield faces forward)
4. **Logical**: Use reasoning to determine alternatives (e.g., only one screw left, one hole left)

---

### Summary Table

| Principle | Question It Answers | Design Strategy |
|-----------|---------------------|-----------------|
| Affordances | What can I do? | Make actions possible |
| Signifiers | Where do I do it? | Make actions visible |
| Mappings | How do controls relate to actions? | Spatial correspondence |
| Feedback | What happened? | Immediate, informative response |
| Constraints | What can't I do? | Limit incorrect actions |
| Conceptual Model | How does this work? | Clear system image |

---

*Sources:*
- *Norman, D. A. (2013). The Design of Everyday Things, Chapter 1: The Psychopathology of Everyday Things*
- *Norman, D. A. (2013). The Design of Everyday Things, Chapter 2: The Psychology of Everyday Actions*
