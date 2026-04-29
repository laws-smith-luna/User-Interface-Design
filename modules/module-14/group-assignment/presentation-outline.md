# Final Presentation — 10 Minutes

**Team:** Laws Smith, Kevin Le, Samana Hussain
**Format:** Recorded PowerPoint with built-in narration (Slide Show → Record)
**Required:** Demo the high-fidelity prototype (recorded video embedded as a slide)

> **Note for the team:** Each speaker records their own slides in the shared `.pptx`. Speaking time is split as evenly as possible (~3:00 each, ~10:00 total). One person (Laws) owns the master deck and integrates everyone's recordings.

---

## Recording Approach

PowerPoint's **Slide Show → Record** feature records narration per-slide. Workflow:
1. Laws builds the deck shell with all slides + speaker notes filled in (already done via `build_deck.py`)
2. Each person records narration for their assigned slides directly in the shared file
3. Demo is pre-recorded as an MP4 and embedded on the demo slide
4. Final export: File → Export → Create a Video (MP4)

**Pros of this approach:** No live coordination needed, can re-take individual slides, demo is rock-solid, total upload is one file.

---

## Slide-by-Slide Outline

### `[Laws — ~3:00 total]`

#### Slide 1 — Title (0:15)
- Project name, tagline, team names

#### Slide 2 — Section Divider 01: The Project
- Brief lead-in to the section

#### Slide 3 — The Problem (0:45)
- Existing tools are scattered, demand manual input, only update after-the-fact
- The save-able window is mid-week, before the overspend
- That's the window we set out to address

#### Slide 4 — Our Solution (1:00)
- Per-category monthly budgets, translated into daily spending pace
- Real-time alerts when a category drifts off course
- Dashboard, Budgets, Transactions, Alerts, Settings
- Hero screenshot from final UI

#### Slide 5 — Project Origin & Initial Design (1:00)
- Started as Laws's M3 individual assignment ("Design a New Consumer Software Product")
- Real-time, all-inclusive budgeting was the personal need driving the concept
- Formalized into the Sarah scenario in the M5 wireframes
- Hero image: hand-drawn M5 wireframes

**↳ Handoff to Kevin**

---

### `[Kevin — ~3:15 total]`

#### Slide 6 — Section Divider 02: First Budget Buddy Iterations
- Brief lead-in

#### Slide 7 — Iteration 2: M6 Usability Study (1:15)
- Converted Laws's M5 wireframes into interactive HTML, ran think-aloud with 4 participants
- 5 usability issues identified, top three: no purchase preview, vague transaction labels, confusing budget-creation flow
- Findings drove M8

#### Slide 8 — Iteration 3: M8 Interaction Iteration (1:00)
- Three usability fixes from M6: Plan-a-Purchase preview, merchant-specific transaction labels, clearer budget-creation flow
- Before/after of Plan-a-Purchase preview

#### Slide 9 — Iteration 4: M9 Interaction Critique (1:00)
- Self-critique against Site Design / Interaction Techniques / Preventing Error
- Top fixes: active bottom-nav indicator, budget-creation confirmation step, daily-pace context on budget cards

**↳ Handoff to Samana**

---

### `[Samana — ~3:00 total]`

#### Slide 10 — Section Divider 03: Refinement & Demo
- Brief lead-in

#### Slide 11 — Iterations 5 & 6: M10 + M13 (1:15)
- M10: dead-end tabs fixed, contextual quick actions, back-button consistency
- M13: critical alerts now visually dominant, budget aggregate at top, threshold indicators on donuts, severity tags on alert cards
- Tied to Mullet & Sano hierarchy and Tufte data-encoding principles

#### Slide 12 — Demo (1:15)
- Embedded MP4 walking through the 3 core tasks: check budget before a purchase, create a new budget with confirmation, re-categorize a transaction
- Voiceover narrates what the user sees and why it works

#### Slide 13 — Reflection & Next Steps (0:30)
- Outside frameworks beat team intuition
- Visual design is where perceived quality lives
- Next: real data integration, predictive alerts, accessibility audit, primary user research

#### Slide 14 — Thanks / Q&A placeholder (0:15)

---

## Time Budget Summary

| Speaker | Slides | Time |
|---|---|---|
| Laws | 1–5 | ~3:00 |
| Kevin | 6–9 | ~3:15 |
| Samana | 10–13 | ~3:00 |
| (closing slide) | 14 | ~0:15 |
| (section divider transitions) | 2, 6, 10 | ~0:30 |
| **Total** | | **~10:00** |

---

## Production Checklist

- [x] Laws builds master deck shell with all slides + speaker notes (via `build_deck.py`)
- [ ] Decide on visual template (current: GMU-neutral dark/teal/green)
- [ ] Each person drafts speaker notes for their slides before recording
- [ ] Record demo MP4 separately (screen recording with voiceover) and embed
- [ ] Each person records their slides with PowerPoint's per-slide record
- [ ] Laws does a full playback to check transitions, audio levels, total time
- [ ] Export final MP4 (File → Export → Create a Video)
- [ ] Confirm Canvas submission format (PPTX vs MP4 vs both) and deadline
