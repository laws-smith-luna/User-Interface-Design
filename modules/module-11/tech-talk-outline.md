# Tech Talk: Angular

**Total time: ~14 minutes** | Split across 2-3 presenters

---

## 1. Introduction & What is Angular (~2 min)

- Angular is a **full front-end framework** built and maintained by Google for building dynamic web applications
- Written in **TypeScript** (not optional, it's baked in)
- **History:**
  - AngularJS (1.x) launched in 2010, was one of the first major JS frameworks
  - Angular 2 launched in 2016 as a **complete rewrite** (different language, different architecture, basically a new framework)
  - AngularJS hit end-of-life in December 2021, no longer maintained
  - Modern Angular (2+) is what we're talking about today
- **What problem does it solve?**
  - Traditional web pages reload the entire page on every interaction
  - Angular lets you build **single-page applications (SPAs)** where the page updates dynamically without full reloads
  - It gives you a complete, opinionated toolkit out of the box: routing, forms, HTTP, testing, all included

---

## 2. Key Compelling Use Case (~2 min)

- Angular's sweet spot is **large-scale, complex web applications** with big teams
- Why it works well for this:
  - TypeScript catches bugs early and makes code easier to navigate in large codebases
  - Opinionated structure means every Angular project looks similar, so new team members can ramp up faster
  - Built-in dependency injection makes it easy to swap out services for testing or different environments
  - The Angular CLI generates consistent boilerplate so teams don't argue about project structure
- **Real-world examples:**
  - Google uses it across many products (Google Cloud Console, Firebase Console)
  - Microsoft uses it for Office Online and Xbox web experiences
  - Deutsche Bank, Forbes, Upwork, Samsung all use Angular
  - It's especially popular in **enterprise and financial** applications where structure and maintainability matter more than speed of prototyping

---

## 3. Demo App Walkthrough (~4 min)

*Pick a simple existing demo app (to-do list works well). Walk through these key steps:*

### Setting up a project
- `ng new my-app` creates the full project scaffold
- Angular CLI sets up TypeScript config, testing framework, dev server, everything
- Run `ng serve` and the app is live at localhost:4200

### Creating a component
- `ng generate component todo-list` creates four files: the component class (.ts), template (.html), styles (.css), and test (.spec.ts)
- Components are the building blocks, each one owns a piece of the UI
- Show the `@Component` decorator: selector, template, styles

### Data binding
- **One-way binding:** `{{ title }}` in the template displays a value from the component class
- **Two-way binding:** `[(ngModel)]` on an input field keeps the input and the variable in sync automatically
- Show adding a new to-do: type in the input, the variable updates, click a button, it adds to the list

### Handling user input
- `(click)="addTodo()"` binds a button click to a method
- `*ngFor="let todo of todos"` loops through the list and renders each item
- Show completing/deleting a to-do to demonstrate event handling

### "Angular makes this easier" moments
- The CLI does all the wiring for you (no manual imports, no build config)
- Two-way binding means no manual DOM manipulation
- The component structure keeps everything organized even as the app grows

---

## 4. Design & Architecture Overview (~3 min)

### Components & Templates
- Components are the core abstraction. Each one is a TypeScript class with an HTML template and CSS styles
- Components nest inside each other to build the full UI (like a tree)
- Templates use Angular's own syntax: `{{ }}` for interpolation, `[ ]` for property binding, `( )` for event binding

### Data Binding
- **Interpolation:** `{{ value }}` displays data in the template
- **Property binding:** `[src]="imageUrl"` binds an HTML attribute to a variable
- **Event binding:** `(click)="handler()"` listens for DOM events
- **Two-way:** `[(ngModel)]="name"` combines property and event binding for form inputs

### Directives & Pipes
- **Structural directives** change the DOM layout: `*ngIf`, `*ngFor`, `*ngSwitch`
- **Attribute directives** change appearance/behavior: `ngClass`, `ngStyle`
- **Pipes** transform displayed values: `{{ date | date:'short' }}`, `{{ price | currency }}`

### Services & Dependency Injection
- Services are classes that handle logic that doesn't belong in a component (API calls, shared state, business rules)
- Angular's DI system automatically provides services where they're needed
- You declare a service once and inject it into any component's constructor
- This makes testing easy: swap in a mock service without changing the component

### Routing
- The Angular Router maps URL paths to components
- Supports nested routes, lazy loading (load modules only when the user navigates to them), and route guards (authentication checks before navigation)

---

## 5. Status & Adoption (~1 min)

- **Open source** under the MIT license, maintained by the Angular team at Google
- **Current version:** Angular 19 (released November 2024)
- **Release cycle:** Major version every 6 months. Each version gets 6 months of active support + 12 months of long-term support (security and critical fixes only)
- **Community size:**
  - ~3-4 million weekly npm downloads
  - ~96k GitHub stars
  - Large ecosystem of third-party libraries (Angular Material, NgRx, PrimeNG)

---

## 6. Nearest Competitors (~1.5 min)

| | Angular | React | Vue | Svelte |
|---|---|---|---|---|
| **Type** | Full framework | UI library | Progressive framework | Compiler-based |
| **Language** | TypeScript (required) | JS or TS (optional) | JS or TS (optional) | JS or TS (optional) |
| **Built-in tooling** | Everything included | Bring your own | Middle ground | SvelteKit |
| **Learning curve** | Steepest | Moderate | Gentlest | Low |
| **Bundle size** | Largest | Medium | Smaller | Smallest |
| **Best for** | Large enterprise apps | Flexible, any scale | Quick ramp-up | Performance-critical |

- **React** is the most popular overall but is just a library. You need to pick your own router, state manager, form library, etc. More flexibility, but more decisions.
- **Vue** is easier to learn and good for smaller teams, but its ecosystem is smaller.
- **Svelte** compiles to vanilla JS at build time (no virtual DOM), resulting in tiny bundles, but it's newer and the community is smaller.

---

## 7. When to Use It / When Not To (~0.5 min)

### Use Angular when:
- Building a **large, long-lived** application with a big team
- You want **everything included** out of the box (no decision fatigue)
- Your team already knows **TypeScript** or wants enforced type safety
- You need **enterprise features** like dependency injection, strong testing support, and consistent project structure

### Skip Angular when:
- Building a **small or simple** website (it's overkill)
- You need to **prototype fast** (the learning curve and boilerplate slow you down)
- Your team wants **more flexibility** in choosing libraries and patterns
- **Bundle size** is a top priority (Svelte or Vue will be lighter)

### One-liner summary:
Angular is the "batteries-included" framework. Pick it when structure and scalability matter more than speed and simplicity.

---

*AI Disclosure: Outline and research notes prepared with assistance from Claude (Anthropic). All presentation content reviewed and delivered by team members.*
