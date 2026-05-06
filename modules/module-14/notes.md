# Module 14 - Community Design

**Start:** 4/21/2026
**Topic:** Community Design
**Individual Assignment:** Fix Twitter
**Group Assignment:** Final Project Presentation and Writeup

## Module Overview

So far this course has focused on individual users working to accomplish goals in isolation. But many of the most influential software stories owe their success to having a community behind them: Facebook, Stack Overflow, Amazon product reviews. What these systems share is that their success is governed not just by a user accomplishing a personal goal, but by users choosing to engage with the software in ways that **generate content that benefits the community as a whole**. Without community-generated content, none of those products would exist.

This module covers how to design online communities. It builds on insights from social psychology to examine the key problems all communities face and principles for solving them. We'll look at common community interfaces (e.g. leaderboards), what goes on behind Wikipedia pages to make it successful, and **dark patterns** - design anti-patterns where sites influence users into actions they wouldn't otherwise take, or might not even realize they're taking. The throughline is learning to think about community design *responsibly* and to build communities that offer benefits for all.

## Objectives
1. Identify the key problems online communities face
2. Apply community design principles grounded in social psychology to address those problems
3. Recognize and critique dark patterns in community-driven software

## Notes

### Why Community Design Matters
- A user accomplishing a personal goal is no longer the only success metric
- The system depends on users **contributing content** that benefits others
- Examples of community-driven products:
  - **Facebook** - social graph + user-generated posts
  - **Stack Overflow** - Q&A content written by users for users
  - **Amazon reviews** - purchase decisions driven by other buyers' content
- Without community contributions, these platforms have nothing to offer

### Motivating Example: Crowdsourced News-Sharing App
A site that lets users share favorite news stories with friends:
- Help users discover stories more relevant to their interests
- Help users become more informed by reading more news
- Raise money from publishers who want more readers

Sounds like a simple app with great potential. **What could possibly go wrong?**
(Foreshadows community-design failure modes: trolling, misinformation, polarization, abandonment, low contribution, etc.)

### What Are Online Communities?
- **Definition (Kraut & Resnick):** virtual spaces where people come together to converse, exchange information or resources, learn, play
- Supported by technology platforms: email, wikis, comments, social networks, automated feedback
- May be **public** (open community) or **internal** (inside a company)
- Break the barriers of **time, space, and scale** that limit offline interactions

### Examples of Online Communities
Usenet, Facebook, Netflix, Amazon, Stack Overflow, Cisco Support Community, Kickstarter, Wikipedia, Linux, change.org, Carcinoid Cancer Online Support Group, Piazza
- Range across: open vs. closed, commercial vs. volunteer, support vs. content vs. activism

### Designing Online Communities
- Interactions among users are **shaped and enabled by the user interface**
- These interactions **can be designed** - they're not just emergent
- The interface mediates the user ↔ other-users relationship

### Example: Facebook Reactions
- **Goal:** incentivize positive, supportive interactions over negative, judgmental ones
  - Solution: **Like button** that expresses approval
- **Problem:** how to express response to a *bad* event (e.g. friend posts about a loss)?
  - A simple **Dislike** button risks turning likes into **voting** (negative judgment of content/people)
  - Solution: **Reactions** (Like, Love, Haha, Yay, Wow, Sad, Angry) - expressive without becoming a thumbs-down vote
- Lesson: small UI choices have big behavioral consequences in communities

### Community Design vs. Task Design
| Most of course | Community design |
|----------------|------------------|
| Designing for **task performance** | Designing for successful **community behavior** |
| Methods/principles from **cognitive psychology** of user-interface interactions | Methods/principles from **social psychology** of human-human interactions |

### Dimensions of Socio-technical System Design
Four dimensions a designer can manipulate:

**1. Community structure**
- Size of community
- Homogeneity of member interests
- Presence of subgroup structures
- Relationship of membership to existing social ties

**2. Content, tasks, activities, external communication**
- Presence of self-disclosure (e.g. user profiles) vs. anonymity; visibility internally or externally
- Presence of professionally generated content, imported/exported from other communities
- Welcoming activities & safe spaces for exploration
- Tasks that are independent or interdependent, embedded in social experiences
- Ability to invite friends & share content

**3. Feedback, rewards, sanctions**
- Feedback telling members how to behave - may be informal or structured (e.g. ratings)
- Give or take away something valuable:
  - **Intangible** - approval, status
  - **Tangible** - community privileges, prizes

**4. Roles, rules, access control, & visibility**
- Members may have specialized roles (welcomers for newcomers, dispute handlers)
- Rules & guidelines for behavior
- Procedures for decision-making & conflict resolution
- Access controls limiting who can join & what actions can be taken; may require money for certain actions
- Moderators regulating behavior
- Communication choices on **visibility of bad behavior & punishment**

### Challenges in Community Design
1. **Starting a new community** - especially dealing with newcomers
2. **Encouraging commitment** - keeping members coming back
3. **Encouraging contribution** - getting members to actually produce content
4. **Regulating behavior** - norms, moderation, sanctions

---

## Challenge 1: Starting a New Community

### Difficulties Starting a Community
- **Communicating value to users** - does the community offer services or experiences users want?
- **Visibility** - do users even know it exists?
- **Competition** - why spend time *here* rather than another community that already has more users and activity?

### Carving Out a Useful Niche
- **Picking a scope:**
  - By **topic and activities** (e.g. Minnesota Twins fan community)
  - Around a **pre-existing group** (e.g. GMU alumni group)
- **Mixed-topic scopes reduce community value** - if most content isn't relevant, why pay attention?
- **Subdivide spaces into more relevant sub-spaces**
  - But avoid **inactive/dead spaces** - empty rooms feel worse than crowded ones
  - **Subdivide *after* it's active**, rather than creating too many empty spaces upfront

### Design Techniques for Subdivided Spaces
- **Navigation aids that highlight active spaces** (so users find where the action is)
- **Recommender systems** for spaces (point users at sub-spaces they'd enjoy)
- **Schedule of "expected active times"** for spaces with synchronous activity (e.g. "Tuesday 7pm chat")
- Example: chatroom directory showing rooms in "Social Issues and Politics" with member counts visible

### Competing for a Niche
- New communities often **compete with an existing community** (e.g. enterprise social network competing with FB and LinkedIn)
- **Switching costs:** creating a new profile, learning a new system, re-finding content
- **Awareness costs** of following multiple communities (cognitive load of split attention)

### Techniques for Competition
- **Reduce startup costs** (e.g. shared IDs/profiles via OAuth, SSO)
- **Content sharing** (cross-posting, importing existing content)
- **Advertising & celebrity endorsements** - "the aura of inevitability is a powerful weapon"

### Critical Mass and Effects of Scale
Communities may fail if:
- Not enough members to provide content & interaction opportunities
- Lack of a shared purpose about the scope of activity and membership

**Why do users use Facebook?**
- Because **everyone else** uses Facebook
- The more users join, the greater the value the space provides to each individual
- Cost of joining is roughly **fixed per user**, but value to each user **increases with the number of others** (network effect)

**Critical mass** = the point at which the benefits of increasing network size dwarf the costs.

### Bootstrapping Communities
A community needs a **series of states** in which the activity of early users is sufficient to attract more users.

Techniques:
- **Incentives** - e.g. Epinions paid early users for reviews
  - Caveat: paying can be **demotivating once it stops** (replaces intrinsic with extrinsic motivation)
- **Discounts & free services** (less problematic than direct payment)
- **Viral membership spread** (e.g. invite-a-friend mechanics)

### Making Membership Visible to Non-members
Tactics to convert outside attention into new members:
- **Post membership** to existing social network sites (badges, profile links)
- **Post activity** to existing social networks (e.g. cross-posting Twitter feed to Facebook)
- **Referral benefits** for members who bring others in

### Early Adopter Benefits
Reward people for joining before there's much value yet:
- **Permanent discounts** for early adopters
- **Status of being an early adopter** of an "undiscovered" community (cool-finder identity)
- **Scarce, claimable resources** - usernames, URLs, low member numbers

---

## Challenge 2: Encouraging Contribution

### Challenges of Contribution
- Communities rely on **resources created by the community** (YouTube videos, Wikipedia articles, Stack Overflow answers, Amazon reviews)
- There's often a **contribution gap** between work to be done and work being done:
  - Too much work, not enough workers
  - Users **don't know how** to help
  - Users **don't find the task appealing**

### Visibility of Requests for Contributions
- **Make lists of needed contributions easily visible**
  - e.g. Wikipedia surfaces 125,000 articles that need citations
- **Let users track and follow work as it's done**
  - e.g. Facebook posts profile changes to the newsfeed
- **Personal appeals to specific members** to contribute
  - Most effective when:
    - Request is **simple**
    - **Stresses benefits** of the contribution
    - Comes from a **high-status community member** (e.g. Jimmy Wales requesting Wikipedia support)
    - Comes from **likable requestors**

### Requesting Contributions
- **Social proof** - users are more likely to comply when others have already complied
  - e.g. ESP game announces "over a million labels have already been created"
- Provide **specific & highly challenging goals**
  - e.g. "rate 16 movies on MovieLens in the next week"

### Group Goals
- **Goals for the group coupled with a specific deadline**
  - e.g. apply for Featured Article status on Wikipedia
  - e.g. release cycle on a software project
- **Offer frequent feedback** about performance with respect to the goal
  - e.g. fundraising thermometer

### Increasing Motivation for Contributions
- **Intrinsic motivation** - the activity is an **end** in itself
- **Extrinsic motivation** - the activity is a **means** to an end
- Example: slaying monsters in *World of Warcraft*
  - Intrinsic - enjoy the task or the camaraderie
  - Extrinsic - enjoy the **status** of a higher-level character

### Comparative Feedback (Leaderboards)
- Can be especially **motivating** to beat competitors
  - e.g. leaderboards & lists of top contributors
- But can also be **demotivating**:
  - Reminded how much time was "wasted" on the site
  - May feel they've **already done enough**
  - Discouraging when success is **unattainably high** (e.g. leaderboard of 10 in a population of thousands)

### Enhancing Extrinsic Motivation with Rewards
Rewards increase extrinsic motivation:
- **Reputation & status** - changes how others interact with the user
- **Privileges** - opens new actions
  - e.g. commit privileges on an open-source project
- **Tangible rewards** - money, prizes, charitable donations to causes

### Perverse Incentives: Gaming the System
- Rewards may create **wrong incentives**, leading to **counterfeit actions**
  - e.g. rewards for inviting new members → invitations to fictitious entities
- Gaming is **especially a problem when rewards are based on quantity rather than quality**
  - e.g. Amazon Mechanical Turk uses automated quality checks
- **Status & privileges** lead to **less gaming** than tangible rewards - status becomes meaningless once gamed
- **Less transparent / more unpredictable reward criteria reduce gaming**

### Trade-offs Between Intrinsic & Extrinsic Motivation
- **Extrinsic rewards can reduce intrinsic motivation**
  - e.g. people are *less likely* to donate blood when offered compensation
- Extrinsic rewards must **outweigh the loss in intrinsic motivation** to be net valuable
- **Tangible incentives diminish intrinsic motivation** when they reduce feelings of **autonomy** and **competence** by being perceived as **controllers** of behavior

### Collective Outcomes
- Benefits may accrue to individuals based on success achieved by the **group**
- Group benefits are motivating when:
  - Members are **more committed to the group**
  - The **group is smaller**
  - People feel they can make a **unique contribution**
  - Contributions by others are **complementary or contingent** rather than **substitutes** (your work matters, doesn't get duplicated)

---

## Challenge 3: Encouraging Commitment

### Why Committed Users Matter
Committed users:
- Work harder, say more, do more
- Provide content that others value
- **Stick with** the community
- **Care enough to sustain the group through problems**
- Are more likely to **enforce norms & regulate behavior**

### Three Types of Commitment
| Type | Stance | What it's grounded in |
|------|--------|----------------------|
| **Affective** | "I **want** to continue" | Closeness & attachment to members of the community |
| **Normative** | "I **ought** to continue" | Feelings of rightness or obligation to the group |
| **Need-based / continuance** | "I **must** continue" | Incentive structure & net cost of leaving |

A user can have **more than one type** of commitment at the same time.

### Two Sub-types of Affective Commitment
- **Identity-based commitment**
  - Feeling of being part of the community and helping fulfill its mission
  - Attachment to the **community as a whole**
- **Bonds-based commitment**
  - Feeling close to **individual members** of the group
  - Attachment to **specific people**

### Encouraging Identity-based Commitment
- **Recruit/cluster similar members into homogeneous spaces**
  - e.g. FB group for Mason SWE master's students
- **Explicit name & tagline articulating shared interests**
  - e.g. Wikipedia: "the free encyclopedia anyone can edit"
- **Increase subgroup identity** - belonging to a subgroup increases commitment to the larger community
  - e.g. being part of an FB group increases commitment to FB itself
- **Make community fate, goals, or purpose explicit**
  - e.g. "want Wikipedia to succeed"
- **Joint, interdependent tasks** that require multiple members to succeed
  - e.g. guilds in *World of Warcraft*
- **Highlight an out-group** (rivalry / contrast)
  - e.g. "want Wikipedia to be Britannica's quality or better"
- **Make group members anonymous** - reduces individual ego, raises group identity

### Encouraging Bonds-based Commitment
- **Recruit members with existing ties** to current members
  - e.g. Piazza for a course (classmates already know each other)
- **Facilitate interactions with friends-of-friends**
- **Display photos and info** about individual members + recent activity
- **Opportunities to engage in personal conversation** (DMs, threads)
- **Mechanisms increasing the likelihood of repeat encounters** with the same people
  - Places, spaces, groups, friend feeds
- **User profile pages** that increase self-disclosure & interpersonal liking
  - e.g. profiles with personal contact info
- **Pseudonymous self-disclosure** when info is sensitive
  - e.g. revealing daily weight in a weight-loss community

### Normative Commitment
**Definition:** feeling that one has obligations to the community to be **loyal** and to **act on its behalf**.

#### Encouraging Normative Commitment
- **Highlight community's purpose & success** at achieving that purpose
- **Testimonials about other members' normative commitment** (modeling)
- **Prime norms of reciprocity** by highlighting normative obligations
  - e.g. cancer survivors who participate in a forum after their own cancer is in remission
- **Highlight opportunities to return favors** to other users
  - e.g. someone reviews your commit → review one of theirs

### Need-based Commitment
- Commitment that depends on **net benefits** experienced from the community
- **Benefits:** information, social support, companionship, reputation
- **Costs:** time, effort, frustration
- Members remain (need-based) when **benefits exceed costs**

#### Encouraging Need-based Commitment
- **Provide experiences that match motivations** for participation
- Requires **knowing the community's needs**
  - e.g. code fests for OSS projects satisfy *both* friendship needs *and* planning support
- Motivational mix varies by community type (info exchange, companionship, social support, fun) - design accordingly

---

## Challenge 4: Regulating Behavior

### Community Norms
- Communities develop **norms** about what is/isn't acceptable behavior
- Communities **differ** on which behaviors are normative
  - e.g. personal insults
  - e.g. neutral perspective on Wikipedia vs. viewpoint-driven posts on Huffington Post
- Conflicts between members:
  - Flame wars
  - Edit wars on Wikipedia

### How Individuals Can Damage a Community
- **Trolls** - derive satisfaction from disrupting the community
- **Manipulators** - want the community to produce a particular outcome
  - e.g. Wikipedia members who want a page to show a particular viewpoint
- **Low-quality contributors** - waste community attention with content nobody benefits from

### Limiting Effects of Bad Behavior
**Pre-screening / moderation:**
- Moderate content creation through pre-screening **before** posting
- Techniques to increase moderation effectiveness:
  - **Redirect** inappropriate posts to other places (vs. just deleting)
  - **Consistently applied criteria**, with a chance to argue a case & appeal procedures
  - Moderation by community members **seen as impartial**

**Post-hoc tools:**
- **Reversion tools** - e.g. Wikipedia lets pages be reverted to past versions
- **Filters or influence limiters** (downrank vs. delete)
- **Activity quotas** - limit spam-like activity
- **Gags and bans** on bad actors

### Encouraging Voluntary Compliance
Norms are most effective when members regulate themselves:
- **Make norms clear and salient** by publicly displaying examples of **appropriate** behavior
- **Publicly contrast inappropriate vs. appropriate** behavior in context of the norm
  - e.g. surfaced examples of uncivil comments on Wikipedia
- **Display formal feedback** given to norm-violators (transparency about consequences)
- **Display statistics highlighting prevalence of normative behaviors**
  - e.g. "X days since last workplace injury" sign

---

### Examples to Examine
- **Leaderboards** as a community interface mechanism
- **Wikipedia** - what happens behind the article pages that makes the community function

---

## Designer Ethics & Dark Patterns

### Existential Values
Questions every designer should ask themselves:
- **What are your values as a designer?**
  - Focus on facilitating user tasks
  - Broadening access to technology
  - Expressing truth to users and hiding misinformation
  - Refraining from collecting (excess) data
- **How do those values align with the business directives of your company?**
- **How will you encode your values into your intent, and reconcile that with the business?**

### Ill or Misdirected Intent
- Balancing user needs with business needs is **tricky**
- When business needs are prioritized, the result is **harmful or misdirected intent**
- Most prominent example: **Dark Patterns**

### Dark Patterns
Anti-patterns where the interface manipulates users into taking actions they otherwise wouldn't, often without realizing.

#### 1. Sneaking
Adding things to a transaction the user didn't ask for.
- Example: a checkout cart that auto-includes a "Greeting Card Service - $3.99" item without it being requested

#### 2. Urgency
Creating artificial time pressure.
- Example: countdown timer "OFFER ENDS IN 00:59:48" on a JustFab landing page (resets every visit)

#### 3. Misdirection
Visual hierarchy/wording that steers users toward a particular choice.
- Example: "Yes! I'd like the discount" as a big red button vs. "No thanks, I like full price" - guilt-shaming the dismiss option (a.k.a. *confirmshaming*)

#### 4. Scarcity
Making the user think availability is running out.
- Example: "Only 3 left in stock" displayed next to size selector

#### 5. Obstruction
Making it hard to do something the user *wants* to do (often, leave).
- Example: subscription site that requires **calling a phone number** to cancel, while signing up takes one click - "(855) SAVAGEX (open 24/7)"

#### 6. Forced Action
Requiring users to do something they don't want to in order to access content.
- Example: gating browsing behind required sign-up or "Continue with Facebook"

### Moving Forward: Benevolent Intent
- A **benevolent or "thoughtful" intent** is what we should strive for
- The user's needs are considered **above all else**
- Business goals are balanced, but **designing for the user is a core value**
- Difficult to achieve, but necessary
