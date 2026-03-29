# Module 10 Group Assignment - Laws' Weaknesses (4 of 7)

## Weakness 1: Alerts and Settings navigation tabs are non-functional dead ends

**Screenshot:** [Screenshot of bottom nav showing Alerts and Settings tabs with no response when tapped]

The bottom navigation bar includes five tabs (Home, Budgets, Transactions, Alerts, Settings), but tapping Alerts or Settings produces no response. There is no screen change, no loading state, no feedback of any kind. Norman describes this gap as the "gulf of evaluation" in *The Design of Everyday Things*, where the user cannot tell whether their action had any effect. When a button looks tappable but does nothing, users are left wondering whether the app is broken or whether they missed the tap target.

**Screenshot:** [Screenshot of new Alerts screen showing recent budget alerts with timestamps]

The Alerts and Settings tabs now navigate to dedicated screens. The Alerts screen displays a chronological list of budget notifications with timestamps, and the Settings screen provides access to profile and notification preferences. Users now receive immediate visual feedback when tapping any navigation item.

---

## Weakness 2: Dashboard Quick Actions duplicates the bottom navigation bar

**Screenshot:** [Screenshot of Dashboard showing Quick Actions card with "View Budgets", "Transactions", "Settings" alongside the bottom nav showing the same items]

The Dashboard's Quick Actions card contains three buttons: "View Budgets," "Transactions," and "Settings." All three are already accessible from the bottom navigation bar visible on every screen. In chapter 7 of *Don't Make Me Think*, Krug states that you should try to promote everything on the homepage. Applying Krug's advice to the Dashboard, the Quick Actions section should surface context-specific shortcuts rather than repeat navigation the user already has. The duplication wastes screen space and creates an unnecessary decision point between two identical paths to the same destination.

**Screenshot:** [Screenshot of updated Dashboard with Quick Actions showing "Add Transaction", "Adjust Budgets", "View Spending Report"]

The Quick Actions card now offers contextual shortcuts that complement the bottom navigation: "Add Transaction," "Adjust Budgets," and "View Spending Report." These are actions a user returning to their dashboard would actually want to do quickly, rather than generic navigation available one tap away on the bottom bar.

---

## Weakness 3: Back button on budget detail screens is mislabeled

**Screenshot:** [Screenshot of Clothing Budget detail screen showing "← Home" back button at the top]

The Clothing Budget, Food Budget, and Updated Food Budget detail screens all display a back button labeled "← Home" that navigates to the Dashboard. However, a user viewing a budget detail screen would expect to return to the Budgets list, not the Dashboard. This violates Consistency and Standards. Users expect the back button to return them to the previous logical level in the navigation hierarchy, which is the Budgets list. Labeling it "Home" forces extra navigation steps to get back to the budget list.

**Screenshot:** [Screenshot of updated Clothing Budget detail screen showing "← Budgets" back button]

The back button on all budget detail screens now reads "← Budgets" and navigates to the Budgets list. This matches the user's mental model of the hierarchy and lets users move between the list and detail views without being routed through the Dashboard.

---

## Weakness 4: Category dropdown does not prevent creating duplicate budgets

**Screenshot:** [Screenshot of Create New Budget form with "Clothing" selected, no warning that a Clothing budget already exists]

The Create New Budget form lets users select any category from the dropdown, including categories that already have an active budget. If a user selects "Clothing" (which already has a $300/month budget), the form proceeds without any warning. In chapter 5 of *The Design of Everyday Things*, Norman states that there should be sensibility checks so that small errors like this do not snowball into bigger issues down the line. The user does not intend to create a conflicting budget, but the interface offers no guardrail to catch this slip before it becomes a committed error.

**Screenshot:** [Screenshot of updated form showing warning banner when selecting a category with an existing budget]

The category dropdown now displays a warning banner when the user selects a category with an existing budget (e.g., "You already have a Clothing budget at $300/mo. Creating another will replace it."). This gives the user the information they need to decide whether to proceed or pick a different category, preventing accidental duplicates while still allowing intentional replacement.
