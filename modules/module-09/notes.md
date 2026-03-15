# Module 9: Preventing Error

**Week of March 24, 2026**

---

## Lecture Notes

### Direct Manipulation

"Rapid incremental reversible operations whose impact on the objects of interest is immediately visible" (Shneiderman, 1982)

**Characteristics:**
- Continuous Representation of the Object of Interest
- Physical Actions instead of complex syntax
- Continuous feedback and reversible, incremental actions

**Benefits:**
- Supports exploration
  - Don't plan long sequence of actions: pick an action, try it, can change mind if want to do something else instead
- Provides immediate feedback
  - Can quickly see what outcome of actions are in manipulating the world
  - Easy to compare desired state of the world to actual state of the world

**Drawbacks:**
- Only a small number of objects on screen at once
- It can be physically demanding on the user
- Can be relatively slow
  - If the user needs to perform a large number of actions, it may be impractical
- Repetitive tasks are not well supported
  - e.g. can be better for novices to learn, but harder for experts to exploit
- Some gestures can be error prone

**Example - Spreadsheets:** Direct manipulation of cells, formulas, and data in a grid interface.

### Information Foraging Theory Perspective

- Information Foraging Theory (IFT) perspective
  - User exploring patches topology in search of prey
  - Always making a decision about whether a patch is the right place to hunt and changing as new information arrives
- Breaks down when user actions transform the state of the application
  - Patches and topology no longer fixed
  - Visiting a configuration of the system by clicking "Send" on the email editor is not an undoable action

### Motivation

- User is trying to do a task, manipulating a [model] of world
- Hard to plan out long sequence of actions in advance
- Gulf of execution: hard to know if took correct action
- Gulf of evaluation: hard to understand if successfully manipulated world
- Hard to compare hidden world to desired world

### Norman's Key Design Principles

- Put the knowledge required to operate the technology in the world
- Use the power of natural and artificial constraints
- Bridge the two Gulfs: the Gulf of Execution and the Gulf of Evaluation
  - Execution: Make options readily available
  - Evaluation: Provide feedback

### Key Questions

- What is the cost of an error?
  - Is it low cost or high cost?
  - Is it undoable?
- What feedback is necessary for user to realize the system is not in the desired state?

---

## Designing for Error

- Humans are not automatons and will never behave like automatons
- Easy to design for the situation in which everything goes well
- But important to think about what might go wrong and how the interaction design can ameliorate issues

### Error & the Seven Stages of Action

- **Novices** are more likely to make mistakes than slips, and **experts** are more likely to make slips
- Mistakes occur at the Goal/Plan/Compare level (top of action cycle)
- Slips occur at the Specify/Perform/Perceive/Interpret level (bottom of action cycle)

### Psychological Types of Unsafe Acts

**Unsafe acts** break down into:

- **Unintended action:**
  - **Slip** (attentional failures): Intrusion, Omission, Reversal, Misordering, Mistiming
  - **Lapse** (memory failures): Omitting planned items, Place-losing, Forgetting intentions
- **Intended action:**
  - **Mistake**: Rule-based mistakes (misapplication of good rule, application of bad rule), Knowledge-based mistakes (many verbal forms)
  - **Violation**: Routine violation, Exceptional violations, Acts of sabotage

### Slips

- Attentional failure - user **intended** to do correct action, but did not actually execute action
- Example: I poured some milk into my coffee and then put the coffee cup into the refrigerator. This is the correct action applied to the wrong object.

### Strong Habit Intrusion

- Performance of some well-practiced activity in familiar surroundings
- Intention to depart from custom
- Failure to make an appropriate check
- Example: start trip to frequent destination, forget going somewhere else

### Omissions

- May be interrupted, forgetting intention to act
- "I picked up my coat to go out when the phone rang. I answered it and then went out of the front door without my coat."

### Mistimed Checks

- Highly automated System 1 activity that is interrupted
- Error in resuming activity because usually unconscious
- Example - interrupted in the middle of tying shoes

### Memory Lapse

- Failing to do all steps of a procedure, repeating steps, forgetting the outcome of an action, forgetting the goal or plan
- Often caused by interruption
  - Time between when plan was formulated and plan was executed leads to forgetting plan
  - Take a pen out to sign form, get interrupted talking to someone, leave it on desk rather than put it back in bag

### Mistakes

- User **formulated** the wrong goal or plan
  - Executing action will not achieve goal
- Rule based: appropriately diagnosed situation, but chose erroneous course of action
  - Example: Night club attendees blocked from leaving during fire because bouncers thought they were breaking rules
- Knowledge based: does not have correct information
  - Example: Skidding driver feels brake vibrations, believes indicates malfunctioning brakes and takes foot off brake, stopping ABS

### Deliberate Violations

- Error occurred because user **intended** the erroneous output
- Routine violation - user always intends to do it
  - Noncompliance is so frequent it is ignored
  - E.g., running a red light
- Exceptional - only in some cases
- Sabotage - intended destruction

### Interruptions

- Interruptions are a frequent cause of error
- User may be using your interface perfectly, with the correct plan to get to their goal
  - What happens if, in the middle of the task, they answer a phone call?
  - Or if they run out of time, and come back the next day?

### Designing for Interruptions

- Help user resume task, by remembering where they were in task, what steps have been completed, and what steps remain
- Reduce the number of steps
- Use forcing functions to force users to do forgettable action (e.g., take card from **before** picking up cash)

### Undo

- Having an option to undo actions is one of the most powerful mechanisms to mitigate errors
- However, this is not always possible, e.g. sending an email

---

## Preventing & Recovering from Error

### Understand the Causes of Errors

- What errors occur? What type are they? How can they be prevented?
- Frequent contributing factors
  - Ambiguous or unclear information about the state of the system
  - Lack of an effective conceptual model
  - Inappropriate procedures
- Must design for users as they exist, rather than users as you'd like them to behave

### Root Cause Analysis

- Keep asking **why** to determine causes for erroneous actions, and the causes of these causes
- Example
  - 2010 F-22 crash that killed pilot
  - Official cause: pilot error - pilot failed to take corrective action
  - Why did the pilot not take the action?
    - Pilot was not receiving oxygen and was probably unconscious

### Adding Constraints to Block Errors

- Add specific constraints on actions
  - e.g. forcing formatting in form fields
- Separate controls/fields so that those which are easily confused are far apart
- Separate items into different screens or modules

### Offer Feedback for User Actions

- Feedback helps keep users on track in accomplishing goals
- Provide feedback early
- Provide feedback consistently
- Make feedback visible, noticeable, legible, located w/in users focus of attention
- Requesting confirmation can be used to prevent costly errors (but use sparingly)

### Tone of Feedback

- Establishes relationship with user
- Important not to make user feel "stupid"
- Make the system take blame for errors
- Be positive, to encourage
- Provide helpful messages, not cute messages
- Avoid violent, negative, demeaning, threatening terms (e.g., illegal, invalid)

### Show Users How to Fix Errors

- Good: detecting user errors
- Better: directly showing how errors can be fixed
- (Best: using constraints to prevent errors from ever occurring)

### Swiss Cheese Model

- Accidents must penetrate levels of system defenses
- Reduce accidents by:
  - Adding more layers
  - Reduce the size and number of holes
  - Alert users when holes line up

---

## Readings & Materials

- Norman, Ch. 5: Human Error? No, Bad Design
