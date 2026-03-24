# Module 9 Group Assignment - Laws' Weaknesses (3 of 7)

## Weakness 1: Bottom navigation never indicates the active section

**Screenshot:** [Screenshot of Dashboard screen showing bottom nav with no highlighted item]

The bottom navigation bar contains five items (Home, Budgets, Transactions, Alerts, Settings), but none of them visually highlight to show the user which section they are currently viewing. When looking at the Dashboard, the Home icon is not highlighted. When viewing the Transactions list, the Transactions icon looks the same as every other tab. Krug emphasizes in *Don't Make Me Think* that navigation must always communicate where the user currently is, similar to a "You Are Here" marker on a map. Without this feedback, users lose their sense of place in the app. This is especially problematic after an interruption, since there is no visual cue to remind them where they left off.

**Screenshot:** [Screenshot of updated bottom nav with active tab highlighted]

The active bottom navigation item is now visually highlighted with a colored icon and label (blue for the active section) while inactive items remain gray. This provides continuous location feedback so the user always knows which section of the app they are viewing, regardless of how they navigated there or how long they've been away.

---

## Weakness 2: No confirmation step before creating a budget

**Screenshot:** [Screenshot of New Budget form screen with "Create Budget" button]

Tapping "Create Budget" on the form immediately commits the action with no review or confirmation step. If the user accidentally selects the wrong category, enters the wrong dollar amount, or picks the wrong alert threshold, the budget is created instantly. The success screen that follows shows a summary of what was created, but it offers no "Edit" or "Undo" option to correct a mistake. Norman argues in Chapter 5 of *The Design of Everyday Things* that for actions with meaningful consequences, the system should request confirmation to help catch mistakes before they become committed errors. Setting a monthly budget is a financial decision that shapes how the app tracks and alerts the user going forward, so an accidental misconfiguration could go unnoticed for weeks.

**Screenshot:** [Screenshot of new confirmation/review step before budget creation]

A review step now appears after the user taps "Create Budget," showing a summary of the category, amount, start date, and alert threshold with a clear "Confirm" button and a "Go Back" option. This gives the user a chance to catch mistakes before the budget is finalized. The success screen also now includes an "Edit Budget" link so the user can still correct it without deleting and recreating.

---

## Weakness 3: Dashboard budget bars give no spending pace context

**Screenshot:** [Screenshot of Dashboard budget overview showing colored bars with dollar amounts but no pace indicator]

The Budget Overview section on the Dashboard shows colored progress bars and how much money remains in each category, but it provides no context about whether the user's spending pace is sustainable for the rest of the month. For example, the Food budget shows "$47.32 left" with a yellow bar, but the user has no way of knowing whether that amount needs to last 2 days or 15 days without doing the math themselves. The principle of visibility of system status from the Interaction Techniques lecture says the system should always keep users informed about what is going on through appropriate feedback. A budget tracker that only shows raw remaining dollars without relating it to time forces users to calculate their own spending rate, which defeats the purpose of the tool.

**Screenshot:** [Screenshot of updated Dashboard with daily spending allowance and days remaining]

The Budget Overview cards now include a line below each progress bar showing the number of days remaining in the month and the daily spending allowance (e.g., "$47.32 left, 2 days remaining, ~$23.66/day"). This gives users immediate context about whether their current pace is sustainable. The color coding also now factors in pace: a budget with plenty of money but only a few days left stays green, while a budget with the same amount but two weeks remaining turns yellow to signal that spending should slow down.
