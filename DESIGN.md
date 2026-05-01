# Design System Strategy: The Analytical Architect

## 1. Overview & Creative North Star
This design system is built upon the Creative North Star of **"The Analytical Architect."** 

Business consultancy is often bogged down by cluttered spreadsheets and dry templates. This system rejects the "generic dashboard" aesthetic in favor of a high-end editorial experience. We aim to convey authority through sophisticated typography and architectural depth rather than rigid lines. By leveraging intentional asymmetry, generous white space, and a "layered paper" philosophy, we transform complex data into a curated narrative. The goal is to make the user feel they are not just looking at a mobile app, but a bespoke intelligence report.

> **Implementation Note:** All layouts must be built using Bootstrap 5 grid system while preserving editorial asymmetry through spacing and column distribution.

---

## 2. Colors & Surface Philosophy
The palette is rooted in a deep, authoritative `primary` (#1A237E) and a growth-oriented `secondary` (#2E7D32). However, the luxury of the system is found in the "Neutral Greys" and how they are layered.

### The "No-Line" Rule
To maintain a premium feel, **1px solid borders are strictly prohibited** for sectioning or containment. Boundaries must be defined through background color shifts.

- Place a `surface_container_low` element against a `surface` background to define a region. 
- Use tonal transitions to guide the eye, creating a "frameless" UI that feels infinite and modern.

> **Bootstrap Mapping:**
- Use `bg-*` utility classes combined with custom CSS variables
- Avoid `border`, `border-top`, `hr`, etc.

---

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of premium materials. 

- **Base Layer:** `surface` (#faf9f9)
- **Primary Content Area:** `surface_container_low`
- **Elevated Interactive Cards:** `surface_container_highest` or `surface_container_lowest`

> **Bootstrap Mapping:**
- Base layout: `container` or `container-fluid`
- Structure: `row` + `col-*`
- Nesting achieved via padding (`p-4`, `p-5`) and background layers

---

### The "Glass & Gradient" Rule

- **CTAs & Heroes:** Use subtle linear gradients transitioning from `primary` to `primary_container` at 135deg
- **Glassmorphism:** Use backdrop blur with opacity

> **Bootstrap Mapping:**
- Use custom classes (`.btn-primary-gradient`)
- Combine with `position-sticky`, `backdrop-filter`, and `bg-opacity-*`

---

## 3. Typography
We utilize a pairing of **Manrope** for editorial impact and **Inter** for data precision.

> **Bootstrap Integration:**
- Override default Bootstrap font stack
- Use utility classes (`fw-bold`, `fs-*`, `lh-*`)

### Usage
- **Headlines:** Custom classes (`.display-architect`)
- **Body:** Bootstrap default with overrides
- **Labels:** `text-muted` or custom token (`on_surface_variant`)

---

## 4. Elevation & Depth

Depth is achieved through **Tonal Layering**, not heavy shadows.

- Use layering instead of shadow
- Use ambient shadows only when necessary

> **Bootstrap Mapping:**
- Avoid default `shadow`, `shadow-sm`, etc.
- Use custom shadow utilities with low opacity

---

## 5. Components

### Buttons

- **Primary:** Gradient background
- **Secondary:** Transparent + ghost border
- **Interaction:** Increase shadow, not color shift

> **Bootstrap Mapping:**
- Extend `.btn` classes
- Avoid default `.btn-primary`

---

### Data Visualization

- Thin, precise elements
- Avoid heavy visuals

> **Implementation Tip:**
- Integrate with Chart.js but override styles

---

### Cards & Lists

- No dividers
- Use spacing and background alternation

> **Bootstrap Mapping:**
- Use `d-flex`, `gap-*`, `py-*`
- Avoid `list-group` default borders

---

### Input Fields

- Minimalist
- Bottom border on focus only

> **Bootstrap Mapping:**
- Override `.form-control`
- Remove borders, apply focus state

---

## 6. Layout Strategy (NEW)

### Grid Philosophy with Bootstrap

Even with Bootstrap, avoid rigid symmetry.

- Break the grid intentionally:
  - Example: `col-md-7` + `col-md-5`
- Use offsets:
  - `offset-md-1`
- Mix alignment:
  - `text-start` + `text-end`

### Spacing Rules

- Prefer:
  - `p-4`, `p-5`, `py-5`
- Avoid tight layouts
- White space = hierarchy

---

## 7. Responsive Behavior (NEW)

Design must be **mobile-first**.

- Use:
  - `col-12 col-md-6 col-lg-4`
- Stack elements vertically on mobile
- Maintain breathing space on all breakpoints

> Never sacrifice spacing for density.

---

## 8. Do’s and Don’ts

### Do
- Use asymmetry with Bootstrap grid
- Use spacing instead of borders
- Use gradients strategically
- Keep UI breathable

### Don't
- Don't use Bootstrap defaults blindly
- Don't use `card` component as-is (override it)
- Don't use `hr` or borders
- Don't create dense layouts

---

## 9. Implementation Layer (NEW - CRITICAL)

### Required Stack

- Bootstrap 5 (CDN or local)
- Custom CSS (design tokens)
- Google Fonts (Manrope + Inter)

---

### Base HTML Structure

```html
<div class="container py-5">
  <div class="row">
    <div class="col-md-7">
      <!-- Main content -->
    </div>
    <div class="col-md-5">
      <!-- Secondary content -->
    </div>
  </div>
</div>