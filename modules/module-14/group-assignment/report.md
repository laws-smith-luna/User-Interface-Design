# Budget Buddy: Final Project Report

Course: SWE 632, User Interface Design and Development
Team: Laws Smith, Kevin Le, Samana Hussain
Semester: Spring 2026

---

## 1. Project Name & Value Proposition

Project name: Budget Buddy

Value proposition: a mobile budgeting app that helps people stay on track with monthly category budgets by surfacing not just *how much they have left* but *whether their pace is sustainable*, with real-time alerts when spending drifts off course.

## 2. Team Members and Roles

All three of us contributed to every phase of the project. There was no single lead on any phase. The table below summarizes the specific work each person did across the semester.

| Name | Project contributions |
|---|---|
| Laws Smith | M2 filter feature and GitHub Pages deployment; M4 heuristic eval (GitHub); two of four M6 usability interviews and post-task summaries; M8 budget-creation-flow fix and integration/hosting of the combined deliverable; M9 weaknesses 1–3; M10 weaknesses 1–4; M13 weaknesses 4–5 |
| Kevin Le | M2 initial code, repo setup, and use cases 1–4; M4 heuristic eval (booking.com); co-developed M6 usability tasks and ran interview A with post-task summary; M8 Plan-a-Purchase preview; M9 weaknesses 4–5; M10 weaknesses 5–6; M13 weaknesses 1–3 |
| Samana Hussain | M2 clear-completed button; M4 heuristic eval (Canva); M6 interview D with post-task summary; M8 transaction-label fix; M9 weaknesses 6–7; M10 weakness 7; M13 weaknesses 6–10 |

## 3. Problem / Solution Overview

People want to be better at budgeting either to cut costs or save for the future, but existing apps are scattered across disconnected tools, demand too much manual categorization, and mostly only update users after the money has already been spent. Budget Buddy targets the window in between, where a budget can still help shape both long-term savings and day-to-day spending. It tracks per-category monthly budgets, translates remaining dollars into a daily spending pace, and surfaces alerts when a category drifts off course early enough to course-correct rather than after the damage is done.

## 4. Needfinding

Budget Buddy started not from a formal needfinding study but from a personal need that Laws articulated in his Module 3 individual assignment, *Design a New Consumer Software Product*. He had tried Quicken, Mint, YNAB, Rocket Money, and a rotation of bank apps over the years and found that none of them were both real-time and all-inclusive in the way he wanted. The M3 writeup framed the gap directly: existing tools force users to maintain too many disconnected spaces, require too much manual categorization, and only update users *after* money has been spent. Kevin and Samana joined the concept as a group project from there.

### 4a. Interviews

We did not run formal pre-design interviews with recruited participants for Budget Buddy. The Module 4 contextual inquiry was an individual methodology exercise on different domains (restaurant search, etc.), and the interviews we ran in Module 6 were for usability evaluation of an existing design rather than needfinding. Our user-side input was therefore informal and came from two sources:

- Personal experience with existing tools. Laws had used Quicken, Mint, YNAB, Rocket Money, and several bank apps and could speak directly to the gaps between them. None of them combined real-time spending feedback, automatic categorization that the user actually trusted, and a single consolidated view of money in one place. That gap is the founding insight of the product.
- Prior informal conversations. Laws's framing in M3 drew on prior conversations with friends and family over the years about budgeting and which trackers worked or fell short. We treated this prior context as background rather than as primary research data.

### 4b. Synthesis

Synthesis happened through scenario formalization rather than affinity mapping of interview transcripts. Laws's Module 5 individual wireframes formalized the M3 concept into the Sarah scenario, a 28-year-old saving for a vacation who needs to make in-the-moment spending decisions before a purchase rather than after. The scenario gave the team a single, testable user story to design and evaluate against from M6 onward, and three themes fell out of it that shaped every design decision that followed:

- Budgets are most useful before a purchase, not after. Existing tools mostly surface spending after the fact, but the moment when a user can actually change behavior is the moment of decision. This shaped the Dashboard-as-home-base structure and the later Plan-a-Purchase preview added in M8.
- Raw remaining dollars aren't actionable on their own. "$47 left" doesn't tell you whether to skip lunch. Pace context (days remaining, daily allowance) is what makes the number useful. This drove the M9 changes to budget cards.
- Trust depends on accurate categorization. If transactions land in the wrong bucket, per-category budgets are silently wrong, and the whole tool stops being useful. This drove the merchant-specific labels in M8 and the re-categorize task included in the M6 study.

The M3 writeup itself flagged that "the key assumption is that people want proactive, real-time feedback, but this needs to be confirmed with needfinding." We did not run that confirmatory study within the scope of the course, and a future version of this project would benefit from a dedicated needfinding phase before scaling up the design.

## 5. Design Evolution

### 5a. Final Solution

Budget Buddy is a mobile-first personal budget tracker organized around five sections: a Dashboard summarizing the month, a Budgets list, a Transactions feed, an Alerts inbox, and Settings. The Dashboard is the home base. It shows each category's progress as a donut chart with a clear alert threshold, the daily spending allowance for the rest of the month, a feed of recent transactions, and a prioritized list of alerts when categories are at risk.

Key flows:

- See the month at a glance from the Dashboard.
- Drill into a category to see transactions and adjust the budget.
- Add a transaction quickly via the Quick Actions card.
- Get alerted when a category is trending over budget early enough to act.

The final design is the result of six evaluation cycles and reflects three load-bearing decisions:

1. Pace, not just balance. Module 9's review revealed that showing "$47.32 left" is useless without knowing whether that has to last 2 days or 15. The Dashboard now shows a daily allowance alongside each remaining balance, addressing the *visibility of system status* principle directly.

2. Confirmation for committed actions. Module 9 also surfaced that creating a budget was a one-tap commit with no review. We added a confirmation step modeled on Norman's argument that meaningful actions warrant a deliberate confirmation (Ch. 5, *The Design of Everyday Things*).

3. Visual hierarchy that matches importance. Module 13's visual-design critique identified that severity in alerts was encoded only by border color, that donut charts had no threshold indicator, and that there was no top-level budget aggregate on the Dashboard. The final design layers explicit text labels onto color cues, surfaces a budget aggregate at the top, and adds threshold indicators on each donut, driven by Mullet & Sano's principle that contrasts should be conscious, strong, and few.

### 5b. Tasks

The three core tasks tested in our Module 6 usability study, and which the final prototype is built around, are:

#### Task 1: Check your budget before a purchase

- Description: Sarah is running errands at the end of the month. She set budgets earlier to save for a vacation, including limits on clothing and food. She sees a shirt she likes for $36, opens the app, and finds her clothing budget has only $15.33 left for the month, so she decides against the shirt. Later, hungry, she checks her food budget ($47.32 left), buys lunch for $21.63, and gets an immediate push notification confirming $25.69 remaining for the rest of the month.
- Why it matters to the user base: most existing budget tools only show spending *after* the fact. The whole premise of Budget Buddy is to make the budget useful in the moment of decision, when the user can still choose not to buy. This task represents the app's primary value proposition.
- Annotated task flow: *(Dashboard → Clothing Budget detail → back → Food Budget detail → updated balance after purchase + push notification)*

#### Task 2: Create a new budget with an alert

- Description: the user starts a new monthly savings budget ($500/month) for an upcoming vacation, sets an alert threshold, and confirms the budget is created.
- Why it matters: users will create and adjust budgets regularly as their goals change. The flow needs to be quick enough for casual use but careful enough to prevent setup mistakes (wrong category, wrong amount, wrong threshold) that would silently break the alerting system.
- Annotated task flow: *(Budgets list → "+ New Budget" → New Budget form → review/confirm step → Budget Created success → back to Budgets list)*

#### Task 3: Review and re-categorize a transaction

- Description: the user notices an Amazon transaction that was auto-categorized incorrectly, finds it in the transactions feed, and reassigns it to the right category.
- Why it matters: auto-categorization is never perfect. If users can't quickly fix a miscategorized transaction, their per-category budgets become unreliable, and the whole tool loses trust. This task represents the app's self-healing maintenance loop.
- Annotated task flow: *(Dashboard → Transactions → Amazon transaction (Uncategorized) → Transaction Detail → Re-categorize → Save → back to Transactions)*

### 5c. Design Evolution Visualizations

For each iteration we describe the evaluation technique used, what was learned, and how the design changed in response. The full set of weaknesses identified in each iteration lives in that iteration's deliverable PDF (linked in each subsection). The report focuses on a few representative changes per iteration to show the evolution.

#### Iteration 1: Module 5 Wireframes (initial prototype)

> **Image:** Hand-drawn wireframes of the original Budget Buddy concept. The at-a-glance Dashboard greets Sarah and lists upcoming bills (Rent $2,000 due in 3 days), budget status ($47.32 left in food for February), and over-spending alerts ($2.37 overspent on utilities); the Clothing Budget donut shows $15.33 of $300 left for the month; the Food Budget donut shows $47.32 of $400 left.
>
> **Source:** `modules/module-05/assignment/Module 5 - Wireframes.pdf`, pages 1–2.

Budget Buddy began here as Laws's individual M5 assignment. The hand-drawn wireframes laid out the original concept: a personal-finance app organized around per-category monthly budgets, anchored by the Sarah scenario showing the in-the-moment-of-decision use case the product is built around. The wireframes covered the Dashboard, individual budget detail screens (Clothing, Food) with donut charts and remaining balances, a push-notification flow after a purchase, and the post-purchase updated budget view. The evaluation here was scenario-driven design rather than a structured critique. The main thing learned was that grounding the design in a single concrete scenario (Sarah, end of month, deciding whether to buy a shirt) concretized the value proposition and gave the team a single user story to design and evaluate against from M6 onward. The Sarah scenario, donut charts, push notifications, and per-category budget structure all originated here and survived to the final design.

#### Iteration 2: Module 6 Usability Study

> **Image:** Interactive HTML wireframe of the Food Budget screen as shown to participants — donut chart, "$47.32 remaining" callout, spent vs. budget totals ($352.68 of $400), and a recent-transactions list — captured before any of the M8 fixes were applied.
>
> **Source:** `modules/module-06/group-assignment/budget_wireframes.html` (open in browser and screenshot the Food Budget screen), or pull the equivalent screen from `modules/module-06/group-assignment/Module 6 - Usability Study - Laws Smith, Kevin Le, Samana Hussain.pdf`.

The first group iteration on Budget Buddy. We converted Laws's M5 hand-drawn wireframes into interactive HTML wireframes with facilitator-operated Wizard of Oz navigation between 11 screens, then ran a four-participant think-aloud usability study (participants A, B, C, D) covering three tasks: check budget before a purchase, create a new budget with an alert, and re-categorize a transaction. Each member ran at least one session, took critical-incident notes, and contributed to the synthesis of five usability issues. The most consequential findings were that users had no way to *preview* how a purchase would affect a budget (they could only see the impact after the fact), transaction labels were too vague to verify against real-world activity ("Lunch" instead of "Chipotle"), and the budget-creation flow had several confusing moments around alert thresholds and button styling. These findings fed directly into the M8 interaction iteration.

#### Iteration 3: Module 8 Interaction Iteration

> **Image:** Before/after pair of the budget detail screen. Before: only "$47.32 remaining" with no way to test a hypothetical purchase. After: a "Plan a Purchase" card lets the user enter a hypothetical amount (e.g. $36.00) and immediately see the projected remaining balance with an "Almost at your limit!" warning when the purchase would push the category close to its threshold.
>
> **Source:** `modules/module-08/group-assignment/Interaction Design Iteration.pdf`, the Usability Issue #1 before/after pair.

> TO DO (Kevin) — paragraph covering the M8 iteration. Address the three usability fixes from the M6 study (Plan-a-Purchase preview, merchant-specific transaction labels, budget-creation-flow clarity). Note the evaluation technique (re-design pass against the 5 usability issues), what was learned, and how the design changed in response. Pick whichever 1–2 fixes you want to highlight in the paragraph; the full set lives in the PDF.

#### Iteration 4: Module 9 Interaction Design Critique & Iteration

> **Image:** Before/after pair of the budget creation flow. Before: tapping "Create Budget" commits the budget instantly with no review. After: a confirmation step appears summarizing the chosen category, monthly amount, start date, and alert threshold, with explicit "Confirm" and "Go Back" buttons before the budget is finalized.
>
> **Source:** `modules/module-09/group-assignment/Module09 – Interaction Design Critique and Iteration.pdf`, weakness 2 before/after pair.

> TO DO (Kevin) — paragraph covering the M9 iteration. The evaluation was a self-critique of Budget Buddy against the Site Design, Interaction Techniques, and Preventing Error principle sets, identifying 7 weaknesses with cited principles. Pick 2–3 representative weaknesses to summarize (your weaknesses were 4–5; Laws's were 1–3; Samana's were 6–7) and describe what was learned and how the design changed. Full list of 7 lives in the PDF.

#### Iteration 5: Module 10 Interaction Design Critique & Iteration

> **Image:** Before/after pair of a budget detail screen's back button. Before: "← Home" returns the user to the Dashboard, breaking the expected hierarchy. After: "← Budgets" returns to the Budgets list, matching where the user came from and matching standard mobile-nav conventions.
>
> **Source:** `modules/module-10/group-assignment/Module10 – Interaction Design Critique and Iteration.pdf`, weakness 3 before/after pair.

> TO DO (Samana) — paragraph covering the M10 iteration. The evaluation was a second round of principle-driven critique, this round emphasizing Consistency & Standards, error prevention, and information scent. We identified 7 more weaknesses. Pick 2–3 representative ones to summarize (your weakness was 7; Laws's were 1–4; Kevin's were 5–6) and describe what was learned and how the design changed. Full list lives in the PDF.

#### Iteration 6: Module 13 Visual Design Critique & Iteration

> **Image:** Before/after pair of the Dashboard alerts area. Before: critical alerts are sized and weighted the same as routine notifications, so a budget about to overflow blends visually with low-priority status updates. After: critical alerts are scaled up, given heavier visual weight, and elevated in the layout so they read as more important at a glance, applying Mullet & Sano's principle that visual hierarchy should match informational hierarchy.
>
> **Source:** `modules/module-13/group-assignment/Visual Design Critique and Iteration.pdf`, weakness 6 before/after pair (Samana's contribution).

> TO DO (Samana) — paragraph covering the M13 iteration. This is the iteration you contributed the most to (5 of 10 weaknesses). The evaluation was a visual-design and information-visualization critique against Mullet & Sano (visual hierarchy, contrast, layering, Gestalt) and Tufte (data-ink, encoding-to-data-type matching). Pick 2–3 representative weaknesses to summarize. Yours were 6–10 (alerts not visually dominant enough, color contrast, depth in flat cards, no clickable indication, no previous-month transactions). Kevin's were 1–3 (no budget aggregate, no donut threshold indicator, no transactions filter). Laws's were 4–5 (transaction magnitude bars, alert severity tags). Full list lives in the PDF.

## 6. Final Prototype Implementation

### 6a. Tools Used

| Tool | Purpose | Pros | Cons |
|---|---|---|---|
| HTML / CSS / JavaScript | High-fidelity interactive mockup | No platform install; fast iteration; demonstrable in any browser; easy version control | Not a real mobile app; interactions are simulated, no persistence between sessions |
| AI-assisted code generation (Claude) | Translating design changes from sketch and spec into working markup | Fast turnaround on visual revisions; freed time for design thinking | Required careful review; generated code occasionally introduced unintended visual changes outside the requested fix |
| Git + GitHub | Source control for iterations and team coordination | Auditable history of every design change; easy rollback | Binary screenshots and PDFs grow the repo size |

### 6b. Wizard of Oz Techniques

The mockup simulates several behaviors that would require real backend infrastructure:

- Transaction data is hard-coded in the HTML. Adding a new transaction in the prototype does not persist between sessions.
- Alerts are pre-populated from a fixed dataset rather than generated from real spending behavior.
- The daily-allowance calculation uses a static "today's date" baked into the page rather than the real current date.

### 6c. Hard-Coded Techniques

- All budget categories, amounts, and thresholds are static in the HTML.
- Navigation between screens is implemented by toggling CSS visibility, not real routing.
- The before and after mockups are separate files rather than a single app with a versioned UI.

## 7. Reflection & Next Steps

### 7a. Main Learnings

From the design thinking process:

- The biggest gains came from cycles where we evaluated against an outside framework (Nielsen heuristics, Krug, Norman, Mullet & Sano) rather than relying on team intuition. Every iteration that started with "what principle is this violating?" produced clearer fixes than ones that started with "what should we change?"
- Iteration is not free. By M10 we were re-discovering issues we had already caught, a sign that we needed to consolidate fixes between rounds rather than treat each module's critique as fresh ground.

From our specific project:

- Budget tracking sits in a crowded space (Mint, YNAB, Rocket Money, every bank app). Our differentiator emerged through iteration: spending pace, not just spending balance. That was not obvious in the M5 wireframes or even after the M6 usability study.
- Visual design was where the biggest perceived-quality gains happened. M9 and M10 fixed real interaction bugs, but M13's visual changes are what made the app feel like something we would want to use.

> TO DO (Kevin)
>
> 1–2 sentences on what stood out to you across the project.

> TO DO (Samana)
>
> 1–2 sentences on what stood out to you across the project.

### 7b. If We Had More Time

- Real data integration. Plaid or a CSV import so the budget pace calculations work on actual spending rather than canned data.
- Predictive alerts. Instead of alerting after a threshold is crossed, surface "at this pace you'll be over by the 25th" warnings earlier.
- Customizable categories and rollover. Users with non-standard spending patterns (variable income, irregular categories) need flexibility we didn't get to.
- Accessibility audit. We addressed color-blindness in the alert cards in M13, but a full screen-reader pass and tap-target-size review would close gaps we know exist.
- Primary user research. The needfinding gap noted in §4c is the biggest open question. Specific studies that would shape the next version: how many push notifications are helpful before they cause too much stress, what makes a budgeting app stay in someone's daily routine versus get abandoned after a few weeks, the mental models people use for budgeting and saving money, which common expenses are easiest to cut to get initial buy-in for a new budget, and pricing research on whether users would pay a subscription, accept ads, or expect a freemium model.
