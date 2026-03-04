# Module 7: Site Design

**Week of March 3, 2026**
**Individual Assignment:** Design a Course Catalog and Registration System

---

## Lecture Notes

### Course Transition: From User Research to Design Principles

The first half of the course focused on learning from users directly:
- How users work, what their problems are
- Designing and testing new ideas
- Methods like contextual inquiries and usability evaluations
- Emphasis on interacting with real users to truly understand them

**The problem:** The design space is too vast to run every decision through a user study. Even Google's famous A/B tests for interface colors take time and effort. You have to prioritize user studies for the most important issues or for evaluating designs that are already partly fleshed out.

### Decisions That Need Principles

Before you can run meaningful user studies, you make countless decisions about:
- How software is organized into windows, screens, pages, and panels
- What steps users take to accomplish their goals
- How users identify and resolve errors
- How users discover what they can do with the software in the first place

### Role of Design Principles

- **Not a replacement** for empirical user studies
- Help make more informed decisions by identifying potential problems
- Give you a framework for thinking through and resolving those problems
- Principles help you make good low-level decisions; user studies tell you at a high level what users need
- They won't tell you if your software supports the right task, but they help you execute better on the tasks you've chosen

---

## Readings & Materials

- [Information Foraging - NN/g](https://www.nngroup.com/articles/information-foraging/)

---

## Key Concepts

### Hierarchy

- Information in sites is hierarchical
  - Different pages at different levels of hierarchy
  - May be different navigation elements that lead into different subtrees
- Important to signal:
  - What hierarchies are present
  - Which navigation elements are part of the same hierarchy
  - Where the user currently is on each hierarchy

### Persistent Navigation

- Provides constant, convenient access to main navigation options
- Stays visible across pages so users always know how to get around

### Tabs

- Metaphor: tab dividers in a three-ring binder or folders in a file drawer
- Partition content into sections
- Advantages:
  - Easily understood and self-evident
  - Usually hard to miss
- Example: Amazon's department/category tabs

### Breadcrumbs

- Offer a trail of where the user has been and how they got there
- Show the hierarchy of the information space
- Show current location within that hierarchy

### Progressive Disclosure

- A.k.a. "details on demand"
- Separate information and commands into layers
- Present the most frequently used information and commands first
- Example: Word's bullet/numbering dialog showing basic options first, with a "Customize" button for advanced settings

### Effective Site Design

A good site design makes the answers to these questions obvious:

1. **What site is this?** (Site ID)
2. **What page am I on?** (Page name)
3. **What are the major sections of this site?** (Sections)
4. **What are my options at this level?** (Local navigation)
5. **Where am I in the site?** ("You are here" indicators)
6. **How can I search?**

### Site Design Goals

Three core questions to address:
- How do you help users understand if it's possible to do what they'd like to do?
- How do you help users find what they're looking for?
- How do you balance tradeoffs between competing objectives in site design?

### Challenges in Site Design

- Sometimes a large space for users to navigate to find information
- **No spatial sense of scale** - 50 pages? 500? 50,000?
- **No sense of direction** - Which way did I just go?
- **No sense of location** - No spatial anchoring of where I am now and how that relates to where I could go
- **No place to check if something is not present or supported**

When a site lacks location/spatial awareness/direction:
- Causes confusion and frustration
- Users have difficulty determining their current location in the site structure
- Users feel lost or disoriented
- Without clear navigational aids and breadcrumbs, users may leave the site

### Key Design Dimensions

- Organization of content into pages/screens
- Organization of content within pages/screens
- Ways in which users navigate between pages/screens

**Key design goals:**
- Reduce the time/cost for users to reach content
- Reduce the irrelevant information users must read

### Planning

- Help users determine what they **can** do
  - Is this the right site for my goals? Is this the right page where I should spend my time?
- Support users in how they **determine** what to do
  - If this is the right place, how do I reach my goal?

### Information Foraging

A mathematical model describing navigation, based on the analogy of animals foraging for food:
- Animals forage in different patches (locations)
- Goal: maximize chances of finding prey while minimizing time spent in the hunt
- **Information foraging:** navigating through an information space (patches) to maximize chances of finding information (prey) in minimal time

### Information Environment

- Represented as a **topology**: information **patches** connected by traversable **links**
- Examples:
  - Web pages connected by links
  - Menu options and dialogs connected by commands
  - Locations on a map, connected by search, scroll, and move interactions

**Key terms:**
- **Patch** - a space in the environment where a user is located (e.g., a page, a dialog)
- **Links** - connections between patches offered by the information environment
- **Cues** - information features associated with outgoing links from a patch (e.g., text label on a hyperlink)
- **Information scent** - the visible cues (titles, images, link text, above-the-fold content) that signal whether a page matches user goals. Users follow "scent" to decide which links to click, similar to how animals follow scent trails to food.
- **Diet** - the set of information sources a user is willing to consider (analogous to food types an animal hunts)
- User must choose which link, of all possible links to traverse, has the best chance of reaching their prey
- Core formula: **Rate of gain = Information value / Cost of obtaining it** - users maximize this ratio

### Design Implications of Information Foraging Theory

1. **Organize information into functionally related groups** - If information required is already on the same page, no need to go elsewhere
2. **Design effective cues** - Help users predict what will be found by traversing links. Better cues lead to better ability to navigate to correct pages
3. **Match expectations of user's mental model** - Cues are interpreted relative to the user's mental model
4. **Provide search** - In large spaces, faster to search than traverse links

### Search Increases Competition

- Users often enter sites through search engines, looking for a site that will accomplish their goals
- Users form first impressions of sites rapidly
- Users will try another site if they perceive the value of continuing to forage in the current patch is low

### Metaphors

One way to communicate what an interface can do is through metaphors to the real world. Uses existing mental models from the real world (e.g., Windows desktop with icons, recycle bin, folders).

**Advantages:**
- Uses understanding of familiar objects and their functions (file cabinets, desks, telephones)
- Provides **intuitive** understanding of possible affordances and eases mapping tasks to actions
  - Open a folder, throw file in trash, momentum scrolling

**Disadvantages ("Tyranny of metaphor"):**
- Ties interactions closely to workings of the physical world
- Adds useless overhead in extra steps, wastes visual bandwidth
- Taken literally, becomes nonsensical (e.g., nesting folders 10 levels deep)
- People will expect your app to work consistently with the metaphor, which can be limiting

### Alternative: Idioms

A consistent mental model of how something works, without needing a direct real-world metaphor.

- E.g., Files: open / close / save / save as
- Offers intuitive understanding of affordances and interactions
- Provides consistent vocabulary for describing interactions
- Only have to learn it **once**
- Might have originated in the real world, but thought of in terms of mental model for UI interactions

**Examples of idioms:**
- Email
- Clipboard: cut / copy / paste
- Format painter
- Newsfeed
- Follow item / Subscribe

### Task Structure

- In some cases, users must take actions in a specific sequence
- Must input some information before being able to access subsequent information
  - E.g., must select a shipping method before seeing a final price
- To the extent possible, want to leave users in control of task (user control and freedom)
- But also don't want to distract users by making unrelated decisions in random order (flexibility and efficiency of use)
- Don't want to overwhelm users with too many options at one time (minimalist design)
- Good designs need to balance these tradeoffs

### Separate Long Tasks into Sequences

- Reduce short-term memory demands by having users work on one aspect of a larger task at a time
- Don't interrupt users in the middle with unrelated tasks
- Provide closure of each subtask at the end
- Example: American Airlines booking flow (Find Flights > Choose Flights > Travelers > Trip Options > Select Seats > Review & Pay > Finish)

### Design for Flexibility and Efficiency

- Users may take paths never envisioned by the designer
- Use studies to identify different task flows, then design flexible support for each
- Can enforce task dependencies (e.g., must choose flights before entering traveler info) while still allowing flexibility within steps

### Anticipate Likely Next Actions

- Based on typical observed task flows, surface options for users to take likely next steps
- Example: "Save As" dialogs that open to the current project folder, or offer to create a new folder if one doesn't exist

### Interaction Flow Guidelines

- Don't use dialogs to report normal behavior
- Separate commands from configuration
- Don't ask questions, give users choices
- Give users default input, show possible options
- Make dangerous choices hard to reach
- Design for the probable, provide for the possible
