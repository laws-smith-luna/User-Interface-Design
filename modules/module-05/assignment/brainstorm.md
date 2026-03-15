# Module 5 - Wireframes for Consumer App (Brainstorm)

## App Purpose

A comprehensive expense tracking and budgeting app that consolidates bank accounts, credit cards, and spending into one central location. Uses LLM-powered auto-categorization, real-time push notifications, and proactive budget warnings to help users stay on track — without the manual effort of existing tools.

## Scenario

**User:** Sarah, 28, just started a new job and wants to take control of her finances.

**Goal:** Sarah just got paid and wants to connect her accounts, see where last month's money went, set up a monthly budget, and configure alerts — so she can identify and cut unnecessary spending this month.

## Wireframe Pages

### Page 1: Onboarding / Account Connection
- Welcome screen with clear value prop ("All your money, one place")
- "Connect Your Accounts" button front and center
- List of supported banks/cards with search
- User selects their bank, authenticates
- **Annotation:** User's goal is to link everything quickly without friction. Minimal steps to get started — no lengthy profile setup first.

### Page 2: Dashboard / Spending Overview
- Top: total balance across all accounts
- Middle: last month's spending breakdown (pie chart or bar chart by category)
- Categories auto-labeled by LLM (Groceries, Dining, Subscriptions, Transport, etc.)
- Bottom: quick stats — "You spent $X more on dining than last month"
- **Annotation:** User's goal is to get an instant picture of where money went. The LLM categorization means Sarah doesn't have to manually tag 100+ transactions.

### Page 3: Budget Setup
- Pre-populated category list based on actual spending history
- Each category shows: last month's actual spend + suggested budget
- Slider or input to adjust each budget amount
- Running total at top shows income vs. total budgeted
- "Smart Suggest" button that auto-fills reasonable budgets based on spending patterns
- **Annotation:** User's goal is to set realistic limits. Pre-populated suggestions reduce the cold-start problem — Sarah doesn't have to guess numbers from scratch.

### Page 4: Smart Insights / Unnecessary Expenses
- LLM-flagged items: subscriptions Sarah may have forgotten, duplicate charges, spending spikes
- Each insight is a card with: what it found, how much it costs, and a suggested action
- Example: "Netflix + Hulu + Disney+ = $45/mo — consider consolidating?"
- Example: "Gym membership — no transactions at gym locations in 60 days"
- Swipe to dismiss or tap to take action
- **Annotation:** User's goal is to find easy wins for cutting spending. The LLM does the detective work so Sarah doesn't have to comb through statements manually.

### Page 5: Notification & Alert Settings
- Toggle categories for real-time purchase alerts
- Set threshold warnings ("Alert me when Dining hits 80% of budget")
- Frequency options: real-time, daily digest, weekly summary
- Preview of what a push notification looks like
- **Annotation:** User's goal is to stay informed without being overwhelmed. Customizable alerts let Sarah choose her comfort level — proactive feedback without notification fatigue.

## Why This Design Is Better Than Current Approaches

- **vs. YNAB:** No manual transaction entry or "envelope" mental model to learn — LLM handles categorization automatically
- **vs. Mint/Rocket Money:** Proactive, real-time insights instead of passive end-of-month reports you check too late
- **vs. bank apps:** Consolidated view across ALL accounts instead of checking 3-4 separate apps
- **vs. spreadsheets:** Zero manual data entry — accounts sync automatically and budgets are pre-suggested based on real data
- The core advantage: **intelligent automation** (LLM categorization + smart insights) combined with **proactive alerts** means users stay engaged instead of abandoning the app after two weeks
