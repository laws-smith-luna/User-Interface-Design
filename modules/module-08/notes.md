# Module 8: Interaction Design

**Week of March 17, 2026**

---

## Lecture Notes

### Command Interactions

How can a user invoke a command? Common examples:
- Menus
- Buttons
- Toolbar
- Dialog box
- Keyboard shortcut
- Gesture
- Voice commands

### Signifiers

The visual cues that communicate what UI elements can do. Example: "Is this a button? Or a link?" When styling is ambiguous, users can't tell what's interactive.

**Goals of signifiers:**
- Show which UI elements can be manipulated
- Show how they can be manipulated
- Help users get started
- Guide data entry
- Suggest default choices
- Support error recovery

### Clarity of Wording

- Choose words carefully
- Speak the user's language
- Avoid vague, ambiguous terms
- Be as specific as possible
- Clearly represent domain concepts

### Likely & Useful Defaults

- Default text, if relevant (e.g., date)
- Default cursor position
- Avoid requirements to retype & re-enter data

### Modes

Modes vary the effect of a command based on the state of the system.

**Examples:**
- Caps lock
- Insert / overtype mode
- vi / emacs command modes
- Keyboard entry used for controlling game and chatting

### Avoid Physical Awkwardness

- Switching between input devices takes time
- Avoid forcing users to constantly switch between input devices (e.g., keyboard & mouse)
  - E.g., effective tab order between fields
- Avoid awkward keyboard combinations

### Fitt's Law

The time required to move to a target **decreases** with target **size** and **increases** with **distance** to the target.

- Movements typically consist of:
  - One large quick movement to target (**ballistic** movement)
  - Fine-adjustment movement (**homing** movements)
- Homing movements are generally responsible for most of movement time & errors
- Applies to rapid pointing movements, not slow continuous movements

### Design Implications of Fitt's Law

- Making controls **larger** reduces time to invoke actions
- Locating controls closer to user **cursor** reduces time
  - E.g., context menus
- **Constraining** movement to one dimension dramatically increases speed of actions
  - E.g., scroll bars are 1D
- Positioning a button or control along the **edge** of the screen acts as a barrier to movement, substantially reducing homing time & errors

### Challenges with Modes

Modes create inconsistent mapping:
- E.g., Ctrl+S sometimes saves, sometimes sends email
- Especially dangerous for frequent interactions that become highly automatic System 1 actions

**Guidelines:**
- Avoid modes when possible
- If necessary, clearly distinguish which mode the user is in and how to change it

### Mobile Devices

- Mobile devices often have smaller form factor than desktop / laptop OS
- Can design a separate UI
- Or may build a **fluid** UI that rescales for different display sizes

### Where's the Cursor?

- No cursor on many mobile devices
- Cannot use dynamic hinting to determine which elements can be interacted with
  - May require more use of static hinting
- Fitt's law still applies
  - Fingers are less sensitive, hard to select small buttons, occlude elements

### Alternative Inputs

- Modern mobile devices often have a wide range of sensors which can be used for input
  - Camera
  - Microphone
  - Accelerometer
  - Three-axis gyro
  - GPS
  - Barometer
  - Proximity sensor
  - Ambient light sensor
- Enables new interaction techniques

### Augmented Reality

Overlaying generated content on top of a view of the real world.

### Supporting Users with Disabilities

- **Perception** - visual & auditory impairments
  - Blindness or visual impairments
  - Color blindness
  - Deafness & hearing limitations
- **Motion** - muscle control impairments
  - Difficulties with fine muscle control
  - Weakness & fatigue
- **Cognition** - difficulties with mental processes
  - Difficulties remembering
  - Difficulties with conceptualizing, planning, sequencing actions

### Blindness and Visual Impairments

- Users use screenreader to listen to screen elements
- Reads all of the text on the page
  - Through practice, learn to listen to text at 400+ words per minute
- Important to have **alt-text**
  - Images should have labels that explain them
- Important to have **hierarchy**
  - Rather than visually skimming page, skims page by listening to section heads to determine which level to navigate to next

### Universal Design

- How can users with physical disabilities be supported in user interactions?
- Good: **assistive design** - offering equivalent actions for disabled users that cannot take normal actions
- Better: **universal design** - designing interactions so broadest set of users across age, ability, status in life can use normal actions

**Example - Curb cut:**
- Initially designed for **accessibility** - support for disabled & wheelchairs
- But potentially benefits **all users** of public spaces - people w/ suitcases, hand carts, roller blades, bikes, etc.
- The curb cut is a great example of universal design because it:
  - Provides unintended benefits to the broader population
  - Benefits a wide range of users, not just those with disabilities
  - Is an example of inclusivity and accessibility for all

### 7 Principles of Universal Design

1. **Equitable use** - The design is useful and marketable to people with diverse abilities
2. **Flexibility in use** - The design accommodates a wide range of individual preferences and abilities
3. **Simple and intuitive** - Use of the design is easy to understand, regardless of the user's experience, knowledge, language skills, or current concentration level
4. **Perceptible information** - The design communicates necessary information effectively to the user, regardless of ambient conditions or the user's sensory abilities
5. **Tolerance for error** - The design minimizes hazards and the adverse consequences of accidental or unintended actions
6. **Low physical effort** - The design can be used efficiently and comfortably and with a minimum of fatigue
7. **Size and space for approach and use** - Appropriate size and space is provided for approach, reach, manipulation, and use regardless of user's body size, posture, or mobility

---

## Readings & Materials

- [Fitts' Law - IxDF](https://ixdf.org/literature/topics/fitts-law)
