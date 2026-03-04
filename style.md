# Xlue Design System & Style Guide

> **Version: 1.2** | Updated: 2026-03-04
> Scope: Xlue official website, Xlue Health Demo, sub-platforms, web applications, partner integration interfaces
> Sources: `Xlue/xlue-style.md` + live product analysis of `Xlue-Health-Demo`

---

## Table of Contents

1. [Brand Identity](#1-brand-identity)
2. [Color System](#2-color-system)
3. [Typefaces & Fonts](#3-typefaces--fonts)
4. [Typography Scale](#4-typography-scale)
5. [Spacing & Layout](#5-spacing--layout)
6. [Radius & Shadows](#6-radius--shadows)
7. [Component Styles](#7-component-styles)
8. [Animation & Interaction](#8-animation--interaction)
9. [Responsive Breakpoints](#9-responsive-breakpoints)
10. [CSS Token Reference](#10-css-token-reference)
11. [Tailwind Quick Reference](#11-tailwind-quick-reference)
12. [Xlue Health Demo Specifics](#12-xlue-health-demo-specifics)
13. [Do Nots](#13-do-nots)
14. [Logo System](#14-logo-system)
15. [Icon System](#15-icon-system)

---

## 1. Brand Identity

Xlue is a Carnegie Mellon University spin-off focused on **Health Foundation Models**. The visual language must communicate:

| Quality | Visual Language |
|---------|----------------|
| Clinical trustworthiness | Deep teal, clean and uncluttered |
| Cutting-edge technology | Gradient text, precise typography |
| Academic rigor | High-contrast text, generous whitespace |
| Open ecosystem | Soft backgrounds, modular cards |
| Clinical usability (Health Demo) | Information-dense, clear hierarchy, fast scanning |

### 1.1 Product Line Differentiation

| Product | Role | Key Visual Differences |
|---------|------|------------------------|
| **Xlue Website** | Marketing & brand showcase | Large whitespace, gradient headlines, hero section |
| **Xlue Health Demo** | Clinical workspace interface | Side panels, high information density, sidebar navigation |
| **Xlue Copilot** | AI-assisted clinical chat | Chat UI, floating window |

---

## 2. Color System

### 2.1 Core Brand Palette

| Name | Hex | HSL | CSS Token | Usage |
|------|-----|-----|-----------|-------|
| **Brand Primary** | `#007D7D` | `180 100% 25%` | `--color-primary` / `--primary` | Buttons, links, accents |
| **Brand Hover** | `#00A7A2` | `178 100% 32%` | `--color-primary-hover` | Interactive hover state |
| **Brand Light** | `#009C9C` | `180 100% 31%` | `--color-primary-light` | Secondary button hover |
| **Brand Dark** | `#005A5A` | `180 100% 18%` | `--color-primary-dark` | Gradient deep end, footer |
| **Gradient Start** | `#00948A` | `177 100% 29%` | `--color-gradient-start` | Heading gradient from |
| **Gradient End** | `#3A5A56` | `174 22% 29%` | `--color-gradient-end` | Heading gradient to |

### 2.2 Background Layers

| Layer | Hex | HSL | CSS Token | Description |
|-------|-----|-----|-----------|-------------|
| **L0 Global** | `#FAFAF8` | `60 8% 98%` | `--bg-l0` / `--background` | `<body>` base, warm off-white |
| **L1 Cards / Sections** | `#EFF4F4` | `180 20% 95%` | `--bg-l1` / `--surface-900` | Content cards, Mission, Contact CTA |
| **L2 Footer** | `#F4F7F6` | `165 11% 96%` | `--bg-l2` | Footer background |
| **L3 Pure White Cards** | `#FFFFFF` | — | `--bg-card` / `--card` | Person cards, modals, tables |

> **Xlue Health Demo note**: The clinical interface sidebar uses L3 (`#FFFFFF`), the main content area uses L0, and panel blocks use L1.

### 2.3 Text Colors

| Usage | Hex | HSL | CSS Token |
|-------|-----|-----|----------|
| **Primary text** | `#0D2B2B` | `180 50% 10%` | `--text-primary` / `--foreground` |
| **Secondary text** | `#2C4444` | `180 30% 22%` | `--text-secondary` / `--muted-foreground` |
| **Tertiary text** | `#5C6C6C` | `180 9% 40%` | `--text-tertiary` |
| **Muted text** | `rgba(14,46,46,0.80)` | — | `--text-weak` |

### 2.4 Borders & Dividers

| Usage | Hex / Value | CSS Token |
|-------|-------------|----------|
| **Default border** | `#D8E2E0` | `--border-default` / `--border` |
| **Border on dark surface** | `rgba(255,255,255,0.08)` | `--border-dark` |

### 2.5 Feature Icon Gradients

The three feature card icons use the following gradients sequentially to maintain brand consistency:

```css
/* Card 1 — Clinical & Payer */
background: linear-gradient(135deg, #007D7D, #005A5A);

/* Card 2 — Patient-Centered */
background: linear-gradient(135deg, #008A8A, #006A6A);

/* Card 3 — Pharma & Life Science */
background: linear-gradient(135deg, #009C9C, #007A7A);
```

### 2.6 Badge Colors

```css
/* Default state */
background-color: rgba(0, 125, 125, 0.20);
color: #007D7D;
border-color: rgba(0, 125, 125, 0.40);

/* Hover state */
background-color: rgba(0, 156, 156, 0.20);
color: #009C9C;
border-color: rgba(0, 156, 156, 0.40);
```

### 2.7 Sidebar Colors (Xlue Health Demo only)

```css
/* Sidebar background */
--sidebar-background: #FFFFFF;
--sidebar-foreground: #0D2B2B;
--sidebar-primary:    #007D7D;
--sidebar-accent:     #EFF4F4;
--sidebar-border:     #D8E2E0;
```

---

## 3. Typefaces & Fonts

### 3.1 Font Stack

The Xlue website uses the **native system font stack** (Tailwind CSS default); Xlue Health Demo and future brand upgrades prefer **Inter**:

```css
/* Website / default */
font-family:
  ui-sans-serif,
  system-ui,
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  Roboto,
  "Helvetica Neue",
  Arial,
  "Noto Sans",
  sans-serif;

/* Health Demo / upgraded (Inter preferred) */
font-family:
  "Inter",
  ui-sans-serif,
  system-ui,
  Avenir,
  Helvetica,
  Arial,
  sans-serif;

/* Monospace / code */
font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
```

> **Design philosophy**: System fonts guarantee consistent rendering across all platforms and eliminate font-load latency that degrades perceived performance on the homepage. Health Demo uses Inter to ensure clinical data remains readable at high information density.

### 3.2 Font Role Assignment

| Role | Primary | Fallback |
|------|---------|----------|
| Display / Heading | **Inter** | Manrope |
| General body copy | **Inter** | DM Sans |
| Clinical data / values | **Inter** | — |
| Monospace / code | **JetBrains Mono** | Fira Code |

---

## 4. Typography Scale

### 4.1 Size Reference Table

| Level | Tailwind class | px | font-weight | line-height | Usage |
|-------|---------------|-----|-------------|-------------|-------|
| **Display H1** | `text-5xl` desktop / `text-4xl` mobile | 48 / 36px | `font-bold` 700 | `leading-tight` 1.25 | Homepage hero heading |
| **H2 Section** | `text-3xl` | 30px | `font-bold` 700 | `leading-tight` | Section main headings |
| **H2 Card** | `text-2xl` | 24px | `font-bold` 700 | `leading-tight` | Card headings (Mission, News) |
| **H3 Feature** | `text-lg` | 18px | `font-bold` 700 | `leading-normal` | Feature card titles |
| **H4 Sub** | `text-xl` | 20px | `font-semibold` 600 | `leading-normal` | About sub-headings |
| **Body Large** | `text-lg` | 18px | `font-normal` 400 | `leading-relaxed` 1.625 | Body paragraphs |
| **Body Base** | `text-base` | 16px | `font-normal` 400 | `leading-normal` 1.5 | Descriptive copy |
| **Body Small** | `text-sm` | 14px | `font-normal` / `font-medium` | — | Nav links, labels, footer |
| **Caption** | `text-xs` | 12px | `font-normal` | — | Auxiliary marks, metadata |

### 4.2 Line-Height Reference

| Type | Tailwind | Value | Use |
|------|----------|-------|-----|
| Tight | `leading-tight` | 1.25 | Large headings H1/H2 |
| Normal | `leading-normal` | 1.5 | Interface text |
| Relaxed | `leading-relaxed` | 1.625 | Body paragraphs |

### 4.3 Brand Gradient Text Syntax

```html
<!-- Primary heading gradient (deeper, subdued) -->
<span style="
  background: linear-gradient(to right, #00948A, #3A5A56);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
">Revolutionizing Medicine</span>

<!-- Feature section gradient (brighter) -->
<span style="
  background: linear-gradient(to right, #007D7D, #009C9C);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
">The Health Foundation Model</span>
```

```tsx
/* Tailwind / TSX syntax */
<span className="bg-gradient-to-r from-[#00948A] to-[#3A5A56] bg-clip-text text-transparent">
  Revolutionizing Medicine
</span>
```

### 4.4 Special Text Styles

| Context | Class names |
|---------|-------------|
| News category label | `uppercase tracking-wide text-sm font-medium` |
| Nav link | `text-sm font-medium transition-colors` |
| Section eyebrow | `uppercase tracking-widest text-xs font-medium` |
| Footer section heading | `font-semibold` |
| Footer body copy | `text-sm leading-relaxed` |

---

## 5. Spacing & Layout

### 5.1 Page Width Containers

```css
/* Global root container (website App.css / #root) */
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
}
```

| Usage | Class / max-width |
|-------|------------------|
| Text paragraphs (single column) | `max-w-3xl mx-auto` (768px) |
| Section container (cards) | `max-w-4xl mx-auto` (896px) |
| Multi-column content | `max-w-5xl mx-auto` (1024px) |
| Footer / large layout | `max-w-6xl mx-auto` (1152px) |
| Navigation bar | `max-w-7xl mx-auto` (1280px) |

### 5.2 Section Spacing Standard

```
py-12 px-4   → all primary sections (48px vertical, 16px horizontal)
p-8          → card content padding (32px all sides)
p-4          → compact card padding (16px all sides)
```

### 5.3 Child Element Spacing

| Context | Class |
|---------|-------|
| Between section heading and content | `mb-8` |
| Between heading and sub-heading | `mb-4` / `mb-3` |
| Between paragraphs | `space-y-4` / `space-y-6` |
| Three-column feature grid | `gap-6` |
| Badge + date row | `gap-3` |
| Button group | `gap-4` |
| Footer column gap | `gap-8` |

### 5.4 Grid Layout Patterns

```tsx
// Three-column Feature Cards
<div className="grid grid-cols-1 md:grid-cols-3 gap-6">

// Two-column About section
<div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-start">

// Footer four-column (brand takes 2)
<div className="grid grid-cols-1 md:grid-cols-4 gap-8">
```

### 5.5 Navigation Bar Height

```
h-16  → 64px (fixed height)
pt-20 → hero section top padding to compensate for nav height (80px)mpensate for nav height (80px)
```

### 5.6 Xlue Health Demo Layout Specifics

```
Sidebar width          : 240px (desktop) / collapsed to 64px
Main content area      : calc(100vw - 240px)
Panel minimum height   : 200px
Panel header height    : 40px (h-10)
Patient Queue width    : 320px
```

---

## 6. Radius & Shadows

### 6.1 Border Radius

| Component | Class | px | CSS Token |
|-----------|-------|-----|-----------|
| Large cards, section containers | `rounded-2xl` | 16px | `--radius-xl` |
| General cards | `rounded-xl` | 12px | `--radius-lg` |
| Buttons | `rounded-md` | ~6-8px | `--radius-md` |
| Badge / Tag | `rounded-full` | 9999px | `--radius-full` |
| Person avatar | `rounded-full` | 50% | — |
| Icon container | `rounded-xl` | 12px | `--radius-lg` |

> Health Demo sets `--radius: 16px` globally, slightly larger than the website, to give card edges a friendlier feel.

### 6.2 Shadows

| Level | Value | CSS Token | Usage |
|-------|-------|-----------|-------|
| **Card main shadow** | `0 4px 12px rgba(0,0,0,0.15)` | `--shadow-card` | Person cards, key cards |
| **Card light shadow** | `0 2px 8px rgba(0,0,0,0.08)` | `--shadow-light` | News cards, secondary cards |
| **Icon container** | `shadow-lg` | — | Feature icon |
| **Person avatar** | `0 2px 8px rgba(0,0,0,0.08)` | `--shadow-light` | Same level as card |

> Rule: All cards use **`border: none`** plus a custom box-shadow. **Never combine border + shadow.**

---

## 7. Component Styles

### 7.1 Navigation Bar

```css
/* Website navigation bar */
nav {
  position: fixed;
  top: 0;
  width: 100%;
  height: 64px;
  background: rgba(250,250,248,0.90);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid #D8E2E0;
  z-index: 50;
}
```

- **Logo switch**: When scrolling into the Features section, the primary logo fades out and the Health logo fades in
- **Links**: `text-sm font-medium transition-colors`, hover color `#00A7A2`
- **CTA Button**: `bg-[#007D7D] hover:bg-[#00A7A2] text-white`

### 7.2 Primary Button

```css
.btn-primary {
  background-color: #007D7D;
  color: #FFFFFF;
  padding: 0.625rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  transition: background-color 0.2s;
}
.btn-primary:hover { background-color: #00A7A2; }

/* Large CTA */
.btn-primary--lg {
  padding: 0.875rem 2rem;
  font-size: 1rem;
}
```

### 7.3 Secondary Button (Outline)

```css
.btn-secondary {
  background-color: transparent;
  color: #007D7D;
  border: 1.5px solid #007D7D;
  padding: 0.625rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.2s;
}
.btn-secondary:hover {
  background-color: rgba(0,125,125,0.06);
  border-color: #00A7A2;
  color: #00A7A2;
}
```

### 7.4 Section Health (Feature BG)

```css
.section-health {
  background: hsl(180 20% 95%);  /* #EFF4F4 */
  color: #0D2B2B;
  border-radius: 16px;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.06);
  padding: 3rem;
}
```

### 7.5 Mission / Contact CTA Card

```css
.mission-card {
  background-color: #EFF4F4;
  border-radius: 16px;
  padding: 3rem;
  text-align: center;
  /* no border, no shadow */
}
```

### 7.6 Feature Icon Container

```css
.feature-icon {
  width: 64px;
  height: 64px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
  margin: 0 auto 1rem;
}
/* Icon color: white (#FFFFFF) */
/* Icon size: 32x32px */
```

### 7.7 Person Card (Founder Card)

```css
.person-card {
  background-color: #FFFFFF;
  border-radius: 16px;
  padding: 2rem;
  text-align: center;
  border: none;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
.person-card__avatar {
  width: 96–128px;
  height: 96–128px;
  border-radius: 50%;
  border: 2px solid #FFFFFF;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
/* Name: font-bold text-[#0D2B2B] text-lg */
/* Description: text-[#5C6C6C] text-sm */
```

### 7.8 News Card

```css
.news-card {
  background-color: #EFF4F4;
  border-radius: 16px;
  padding: 1.5rem;
  border: none;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
/* Link color: #007D7D, hover: #00A7A2 */
```

### 7.9 Badge / Category Label

```css
.badge {
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  background-color: rgba(0,125,125,0.20);
  color: #007D7D;
  border: 1px solid rgba(0,125,125,0.40);
  border-radius: 4–9999px;
  padding: 0.2rem 0.6rem;
  transition: all 0.2s;
}
```

### 7.10 Divider

```css
.divider { border-top: 1px solid #D8E2E0; }
```

### 7.11 Footer

| Element | Style |
|---------|-------|
| Background | `#F4F7F6` |
| Top border | `1px solid #D8E2E0` |
| Primary text | `#0E2E2E` |
| Secondary text | `rgba(14,46,46,0.80)` |
| Section heading | `font-semibold` |
| Link hover | Darken to `#0E2E2E` |
| Content padding | `py-12` |
| Grid | 4 columns, brand column spans 2/4 |

### 7.12 Form Input

```css
.input {
  font-size: 0.9375rem;
  padding: 0.625rem 1rem;
  border: 1.5px solid #D8E2E0;
  border-radius: 8px;
  background-color: #FFFFFF;
  color: #0D2B2B;
  transition: border-color 0.2s, box-shadow 0.2s;
}
.input:focus {
  border-color: #007D7D;
  box-shadow: 0 0 0 3px rgba(0,125,125,0.12);
  outline: none;
}
```

### 7.13 Xlue Health Demo — Clinical Panel Components

```css
/* Patient Info Card */
.patient-info-card {
  background: #FFFFFF;
  border-radius: 16px;
  padding: 1rem;
  border: 1px solid #D8E2E0;
}

/* Sidebar Navigation Item */
.sidebar-item {
  color: #2C4444;
  padding: 0.5rem 0.75rem;
  border-radius: 8px;
  font-size: 0.875rem;
  transition: background-color 0.15s, color 0.15s;
}
.sidebar-item:hover   { background-color: #EFF4F4; }
.sidebar-item.active  { background-color: rgba(0,125,125,0.10); color: #007D7D; font-weight: 500; }

/* Panel Header */
.panel-header {
  height: 40px;
  display: flex;
  align-items: center;
  padding: 0 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: #0D2B2B;
  border-bottom: 1px solid #D8E2E0;
}
```

---

## 8. Animation & Interaction

### 8.1 Base Transitions

```css
/* Color switch (all interactive states) */
transition: color 0.2s, background-color 0.2s, border-color 0.2s;

/* Universal all-property transition (logo switch, etc.) */
transition: all 0.5s ease-in-out;

/* Card hover lift */
transition: box-shadow 0.2s, transform 0.2s;
```

### 8.2 Logo Switch Animation (Website)

When the navbar enters the Features section, the primary logo and Health logo cross-fade with a subtle vertical shift:

```css
/* Primary Logo (outside features section) */
.logo-main { transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out; }
.logo-main.hidden { opacity: 0; transform: translateY(-8px); }

/* Health Logo (inside features section) */
.logo-health { transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out; }
.logo-health.visible { opacity: 1; transform: translateY(0); }
```

### 8.3 Card Hover Effect

```css
.card-interactive:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}
```

### 8.4 Scroll Behavior

- All anchor links: `scroll-behavior: smooth`
- Navbar scroll detection threshold: `scrollY > 50px`
- Section detection: `rect.top <= 100 && rect.bottom >= 100`

### 8.5 Accordion Animation

```css
accordion-down: 0.2s ease-out;
accordion-up:   0.2s ease-out;
```

---

## 9. Responsive Breakpoints

Uses Tailwind CSS default breakpoints:

| Breakpoint | Prefix | Min-width | Main behavior |
|------------|--------|-----------|---------------|
| Mobile | (none) | 0px | Single column, hamburger menu |
| Small | `sm:` | 640px | Buttons in row (`sm:flex-row`) |
| Medium | `md:` | 768px | Multi-column grid, show desktop nav |
| Large | `lg:` | 1024px | — |
| XL | `xl:` | 1280px | — |
| 2XL | `2xl:` | 1400px | Container max-width |

### 9.1 Key Responsive Patterns

```tsx
// Navbar: mobile hamburger → desktop horizontal menu
<div className="hidden md:block">   // desktop nav links
<div className="md:hidden">         // mobile hamburger button

// Three-column Feature: mobile single → desktop three-column
<div className="grid grid-cols-1 md:grid-cols-3 gap-6">

// Hero heading: mobile 36px → desktop 48px
<h1 className="text-4xl md:text-5xl font-bold">

// Button group: mobile stacked → desktop inline
<div className="flex flex-col sm:flex-row gap-4 justify-center">
```

---

## 10. CSS Token Reference

Paste into the `:root` of any new platform to inherit the full Xlue brand palette:

```css
:root {
  /* ── Brand Colors ── */
  --color-primary:        #007D7D;   /* hsl(180 100% 25%) */
  --color-primary-hover:  #00A7A2;   /* hsl(178 100% 32%) */
  --color-primary-light:  #009C9C;   /* hsl(180 100% 31%) */
  --color-primary-dark:   #005A5A;   /* hsl(180 100% 18%) */
  --color-gradient-start: #00948A;   /* gradient from     */
  --color-gradient-end:   #3A5A56;   /* gradient to       */

  /* ── Background Layers ── */
  --bg-l0:   #FAFAF8;   /* body — warm off-white    */
  --bg-l1:   #EFF4F4;   /* cards / section surfaces */
  --bg-l2:   #F4F7F6;   /* footer background        */
  --bg-card: #FFFFFF;   /* pure white card          */

  /* ── Shadcn / Tailwind Aliases ── */
  --background:       60 8% 98%;    /* #FAFAF8 */
  --foreground:       180 50% 10%;  /* #0D2B2B */
  --primary:          180 100% 25%; /* #007D7D */
  --primary-foreground: 0 0% 100%;  /* #FFFFFF */
  --card:             0 0% 100%;    /* #FFFFFF */
  --card-foreground:  180 50% 10%;
  --muted-foreground: 180 30% 22%;  /* #2C4444 */
  --border:           165 14% 87%;  /* #D8E2E0 */
  --ring:             178 100% 32%; /* #00A7A2 */
  --surface-900:      180 20% 95%;  /* #EFF4F4 */
  --teal-400:         180 100% 25%; /* #007D7D */

  /* ── Text ── */
  --text-primary:   #0D2B2B;
  --text-secondary: #2C4444;
  --text-tertiary:  #5C6C6C;
  --text-weak:      rgba(14,46,46,0.80);

  /* ── Borders ── */
  --border-default: #D8E2E0;
  --border-dark:    rgba(255,255,255,0.08);

  /* ── Shadows ── */
  --shadow-card:  0 4px 12px rgba(0,0,0,0.15);
  --shadow-light: 0 2px  8px rgba(0,0,0,0.08);

  /* ── Radius ── */
  --radius-sm:   6px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-full: 9999px;
  --radius:      16px;   /* Health Demo global */

  /* ── Sidebar (Health Demo) ── */
  --sidebar-background: #FFFFFF;
  --sidebar-foreground: #0D2B2B;
  --sidebar-primary:    #007D7D;
  --sidebar-accent:     #EFF4F4;
  --sidebar-border:     #D8E2E0;
}
```

---

## 11. Tailwind Quick Reference

### 11.1 Common Color Classes

| Color | Tailwind arbitrary |
|-------|-------------------|
| Brand primary | `bg-[#007D7D]` / `text-[#007D7D]` |
| Brand hover | `hover:bg-[#00A7A2]` / `hover:text-[#00A7A2]` |
| Primary text | `text-[#0D2B2B]` |
| Secondary text | `text-[#2C4444]` |
| Tertiary text | `text-[#5C6C6C]` |
| L1 background | `bg-[#EFF4F4]` |
| Footer background | `bg-[#F4F7F6]` |
| Border | `border-[#D8E2E0]` |

### 11.2 Common Composite Styles

```tsx
// Section container
"py-12 px-4"

// Brand primary button
"bg-[#007D7D] hover:bg-[#00A7A2] text-white rounded-md font-medium transition-colors"

// Content card
"bg-[#EFF4F4] rounded-2xl p-8"

// Feature section container
"section-health p-8 max-w-4xl mx-auto"

// Heading brand gradient
"bg-gradient-to-r from-[#00948A] to-[#3A5A56] bg-clip-text text-transparent"

// Nav link
"text-foreground hover:text-[#00A7A2] px-3 py-2 text-sm font-medium transition-colors rounded-md"

// Fixed navbar
"fixed top-0 w-full bg-background/90 backdrop-blur-md z-50 h-16 border-b border-[#D8E2E0]"

// Divider
"border-t border-[#D8E2E0]"

// Person avatar
"w-24 h-24 rounded-full overflow-hidden border-2 border-white shadow-[0_2px_8px_rgba(0,0,0,0.08)]"

// Card shadow
"border-0 shadow-[0_4px_12px_rgba(0,0,0,0.15)] rounded-2xl"

// Badge
"uppercase tracking-wide bg-[#007D7D]/20 text-[#007D7D] border border-[#007D7D]/40 rounded-full text-xs font-medium px-3 py-1 transition-colors hover:bg-[#009C9C]/20 hover:text-[#009C9C]"
```

---

## 12. Xlue Health Demo Specifics

This section consolidates additional design rules observed in Xlue Health Demo (the clinical workspace interface), supplementing areas not covered by the website Style Guide.

### 12.1 Interface Layout Structure

```
┌─────────────────────────────────────────┐
│           Top Navigation (h-16)         │
├──────────┬──────────────────────────────┤
│ Sidebar  │      Main Content Area       │
│  240px   │    (flex, overflow-auto)     │
│          ├────────────┬─────────────────┤
│          │  Patient   │  Clinical Panel │
│          │  Queue     │  (tab-based)    │
│          │  320px     │                 │
└──────────┴────────────┴─────────────────┘
```

### 12.2 Clinical Data Color Rules

| Status | Color | Notes |
|--------|-------|-------|
| Normal / Passed | `#007D7D` | Brand primary |
| Warning | `#B45309` (amber-700) | — |
| Critical | `#B91C1C` (red-700) | — |
| Informational | `#1D4ED8` (blue-700) | Pure informational labels only |

> Note: Clinical alert colors use amber/red — **do not** use Xlue brand colors (avoids confusing severity levels).

### 12.3 Screening Panel Display

- Positive screening indicators: highlighted with badge + icon to prevent missed findings
- Negative results: grayscale or weakened text, reduced visual weight
- Threshold display: `font-mono` monospace ensures numeric alignment

### 12.4 Copilot Chat Interface

```css
/* User message bubble */
.chat-user {
  background-color: #007D7D;
  color: #FFFFFF;
  border-radius: 16px 16px 4px 16px;
  padding: 0.75rem 1rem;
  max-width: 80%;
  align-self: flex-end;
}

/* AI response message bubble */
.chat-ai {
  background-color: #EFF4F4;
  color: #0D2B2B;
  border-radius: 16px 16px 16px 4px;
  padding: 0.75rem 1rem;
  max-width: 80%;
  align-self: flex-start;
  border: 1px solid #D8E2E0;
}
```

---

## 13. Do Nots

The following practices violate Xlue design standards — **do not use**:

| Prohibited | Reason |
|------------|--------|
| Using non-brand colors like blue, purple, or orange (except for alert purposes) | Breaks teal brand identity |
| Using border + shadow simultaneously on cards | Visual noise — choose one |
| Using `text-black` or `#000000` | Use `#0D2B2B` deep teal instead |
| Using pure white `#FFFFFF` as the site-wide background | Use `#FAFAF8` warm off-white instead |
| Large background-color shifts between sections | Maintain gentle L0/L1 layering |
| Font sizes larger than `text-5xl` (except special pages) | Preserve visual proportion |
| Heavy shadows (`shadow-2xl` or stronger) | Maintain lightweight visual style |
| Using `font-bold` in body paragraph text | Body uses normal weight; bold is for headings only |
| Adding unapproved animation effects | Medical brands require a calm, restrained feel |
| Using `rounded-none` on card components | All cards must have rounded corners |
| Using brand color to indicate critical status in clinical interfaces | Confuses clinical severity semantics |

---

## 14. Logo System

### 14.1 Logo Asset Inventory

All brand logo files are stored in `assets/logos/`. Use this directory as the canonical source — do not copy SVG code inline or download alternatives from the web.

| File | Dimensions | Format | Description | Primary context |
|------|-----------|--------|-------------|----------------|
| `logo-main.svg` | 148 × 75 px | SVG | **Full logo**: constellation mark + "Xlue" wordmark (teal→deep-teal gradient) | Website nav, hero, marketing materials |
| `logo-health.svg` | 148 × 76 px | SVG | **Health variant**: full logo + heart/ECG icon + "Health" sub-brand text | Xlue Health Demo nav, health-product contexts |
| `logo-mark.svg` | 116 × 54 px | SVG | **Constellation mark only**: the dot-cluster brand symbol, no text | Favicons, app icons, tight spaces, loading indicators |
| `logo-wordmark.svg` | 134 × 48 px | SVG | **Wordmark only**: "Xlue" text in gradient, no constellation | Co-branding, light-background embeds, co-marketing |
| `logo-final.png` | 1536 × 1024 px | PNG | **High-res full logo** raster | Print, pitch decks, presentations |
| `logo-finance.png` | 1024 × 1024 px | PNG | **Finance vertical** logo variant | Xlue Finance product contexts |
| `logo-legal.png` | 1024 × 1024 px | PNG | **Legal vertical** logo variant | Xlue Legal product contexts |

---

### 14.2 Logo Anatomy

The Xlue logo is composed of three independent elements:

```
  •  •  •  •         ← Constellation Mark (brand symbol)
     •  •    •          The ascending dot cluster represents AI
   •    •  •             signal / data intelligence growth.

  X  l  u  e         ← Wordmark
                        Custom-drawn letterforms.
                        Gradient: #008F91 (teal) → #1F4C4C (deep teal)

  ♥ ECG             ← Health Sub-brand Mark (logo-health.svg only)
  H e a l t h          Appears only in the Xlue Health product suite.
```

**Constellation dot colors:**
- Teal dots: `#008F91` (brand primary)
- Deep teal dots: `#1F4C4C` (brand dark)
- Dots ascend and grow in size left→right, communicating AI signal growth

**Wordmark gradient (embedded in SVG):**
```css
/* linearGradient applied to the wordmark path */
stop 0%:   #008F91 (opacity 0.7)   /* teal, right side */
stop 69%:  #1F4C4C                  /* deep teal, left side */
/* Direction: right-to-left across the letterforms */
```

---

### 14.3 Logo Color Variants

| Variant | Background | File to use | Notes |
|---------|-----------|-------------|-------|
| **Full color** (default) | White / `#FAFAF8` | `logo-main.svg` | Always preferred |
| **Full color on teal bg** | `#EFF4F4` or `#007D7D` | `logo-main.svg` | Works on brand backgrounds |
| **Reversed / white** | Dark `#0D2B2B` | Apply `filter: brightness(0) invert(1)` | For dark-background contexts |
| **Grayscale** | Any | Apply `filter: grayscale(1)` | Co-branding neutral treatment |

> **Never** manually recolor the constellation dots or wordmark SVG paths. Use the CSS `filter` approach for mono or reversed rendering.

---

### 14.4 Clear Space & Minimum Size

Maintain clear space equal to at least the cap-height of the "X" letterform (~12 px at default size) on all four sides of the logo.

```
  ┌─────────────────────────────┐
  │  [clear]                    │
  │  [clear]  LOGO  [clear]     │
  │  [clear]                    │
  └─────────────────────────────┘
  Minimum clear zone ≈ 12 px at default render size
```

| Context | Minimum rendered width |
|---------|------------------------|
| Digital — full logo | 80 px |
| Digital — mark only (`logo-mark.svg`) | 24 px |
| Print — full logo | 25 mm |
| Favicon (16 × 16 px) | Use `logo-mark.svg` |

---

### 14.5 Logo Usage in Code

**React / Next.js (recommended):**
```tsx
import Image from 'next/image';
import logoMain from '@/assets/logos/logo-main.svg';
import logoHealth from '@/assets/logos/logo-health.svg';
import logoMark from '@/assets/logos/logo-mark.svg';

// Website nav — standard size
<Image src={logoMain} alt="Xlue" width={148} height={75} />

// Health Demo nav
<Image src={logoHealth} alt="Xlue Health" width={148} height={76} />

// Compact mark (tight spaces / favicon rendering)
<Image src={logoMark} alt="Xlue" width={116} height={54} />
```

**Navigation scroll-triggered logo switch (website):**
```tsx
// Primary logo fades out when scroll enters the Features section;
// Health logo fades in. Both logos must be in the DOM simultaneously.
<div className={`transition-all duration-500 ${
  isInFeatures
    ? 'opacity-0 -translate-y-1 pointer-events-none'
    : 'opacity-100 translate-y-0'
}`}>
  <Image src={logoMain} alt="Xlue" width={148} height={75} />
</div>
<div className={`absolute top-0 left-0 transition-all duration-500 ${
  isInFeatures
    ? 'opacity-100 translate-y-0'
    : 'opacity-0 translate-y-1 pointer-events-none'
}`}>
  <Image src={logoHealth} alt="Xlue Health" width={148} height={76} />
</div>
```

---

### 14.6 Logo Do Nots

| Prohibited | Reason |
|------------|--------|
| Stretching or distorting the logo aspect ratio | Destroys brand geometry |
| Rendering the full logo below 80 px wide | Constellation dots become illegible |
| Manually recoloring dot fills or wordmark paths in the SVG | Use CSS filters; never edit SVG source fills |
| Using `logo-health.svg` in non-health contexts | Health sub-brand mark carries clinical positioning |
| Placing the logo on busy photo backgrounds without a protective white zone | Destroys contrast and legibility |
| Using the raster PNGs (`logo-final.png` etc.) in web UI | Always prefer SVG for web — infinite resolution, smaller size |
| Adding drop shadows or outer glows to the logo | The constellation has its own visual depth; external effects clash |
| Placing the logo inside a colored badge or pill shape | Creates unintended framing and dilutes brand authority |

---

## 15. Icon System

### 15.1 Icon Library

Both the Xlue website and Xlue Health Demo exclusively use **[Lucide React](https://lucide.dev)** as the icon library.

```bash
npm install lucide-react
```

```tsx
import { Search, Shield, Brain } from 'lucide-react';
```

> **No other icon library** should be mixed in. Do not use Heroicons, FontAwesome, Phosphor, or Material Icons alongside Lucide.

---

### 15.2 Approved Icon Inventory

#### Xlue Website

| Lucide name | Component | Semantic role |
|------------|-----------|---------------|
| `Search` | `Features.tsx` | AI search capability |
| `Shield` | `Features.tsx` | Privacy / security |
| `Brain` | `Features.tsx` | Foundation model / AI |
| `ArrowRight` | `Contact.tsx`, `About.tsx` | CTA / directional navigation |
| `Stethoscope` | `Footer.tsx` | Health product identity |

#### Xlue Health Demo — Copilot / AI

| Lucide name | Component | Semantic role |
|------------|-----------|---------------|
| `Sparkles` | `CopilotPanel`, `CopilotMessageItem`, `CopilotChat` | AI / Copilot identity |
| `Brain` | `DeepResearchThinking` | Deep research AI |
| `MessageSquare` | `ChatHistorySidebar`, `CopilotChat` | Chat history |
| `ClipboardCopy` | `CopilotPanel` | Copy AI output |
| `History` | `CopilotPanel` | View chat history |
| `RotateCcw` | `CopilotPanel` | Reset conversation |
| `Send` | `CopilotPanel`, `CopilotChat` | Submit message |
| `Lightbulb` | `DeepResearchThinking` | Insight / reasoning step |
| `CheckCircle2` | `DeepResearchThinking`, `CopilotActionCard` | Completed step |
| `Loader2` | `DeepResearchThinking` | Loading / in-progress |
| `Eye` | `CopilotActionCard` | View detail |
| `Undo2` | `CopilotActionCard` | Undo action |
| `ChevronRight` / `ChevronDown` / `ChevronUp` | Multiple | Expand / collapse / navigate |
| `ExternalLink` | `CopilotCitations` | Open source link |
| `Quote` | `CopilotCitations` | Citation reference |

#### Xlue Health Demo — Clinical Panels

| Lucide name | Component | Semantic role |
|------------|-----------|---------------|
| `AlertTriangle` | Screening panels | Positive finding / alert |
| `CheckCircle2` | Screening panels | Negative / normal result |
| `AlertCircle` | `MedicationList` | Medication warning |
| `Activity` | Screening, `PatientInfoCard` | Vitals / physiological activity |
| `User` | `PatientInfoCard`, `PatientQueue` | Patient identity |
| `Calendar` | `PatientInfoCard`, `VisitInfoPanel`, `MedicationList` | Date / schedule |
| `UserCircle` | `ProvidersPanel` | Provider identity |
| `Pill` | `ProvidersPanel`, `VisitInfoPanel`, `MedicationPanel`, `MedicationList` | Medication |
| `Building2` | `ProvidersPanel` | Institution / facility |
| `Stethoscope` | `VisitInfoPanel`, `ProcedurePanel`, `DiagnosisPanel` | Clinical examination |
| `FileText` | `VisitInfoPanel`, `DeepResearchThinking` | Clinical notes / documents |
| `Search` | `DeepResearchThinking` | Knowledge retrieval |
| `DollarSign` | `ChargesPanel` | Charges |
| `Receipt` | `ChargesPanel` | Billing receipt |
| `Clock` | `PatientQueue` | Waiting time |
| `Syringe` | `OrdersPanel` | Injection / infusion order |
| `Package` | `OrdersPanel` | Supply order |
| `Plus` | `ChatHistorySidebar` | New chat |
| `Trash2` | `ChatHistorySidebar` | Delete chat |
| `X` | `ChatHistorySidebar` | Close panel |

---

### 15.3 Icon Sizing Convention

| Context | Class | px | Notes |
|---------|-------|----|-------|
| Feature icon (website hero, inside gradient container) | `w-8 h-8` | 32 px | White color, `strokeWidth={1.5}` at this size |
| Navigation / standard interactive | `w-5 h-5` | 20 px | Default for most UI icons |
| Compact / inline with text | `w-4 h-4` | 16 px | Inside tight components, badges |
| Clinical status indicator | `w-4 h-4` | 16 px | Alert / check icons in panels |
| CTA arrow | `w-5 h-5` | 20 px | `ArrowRight`, `ExternalLink` |
| Copilot / AI identity (`Sparkles`, `Brain`) | `w-6 h-6` | 24 px | Prominent heading / identity positions |

> Use `strokeWidth={1.5}` (instead of the default `2`) for icons rendered at 28 px or larger to avoid visual heaviness.

---

### 15.4 Icon Color Convention

| Context | Color | Tailwind class |
|---------|-------|----------------|
| Feature icons (inside gradient container) | White | `text-white` |
| Navigation / interactive actions | Brand primary | `text-[#007D7D]` |
| CTA arrows | Brand primary or inherited text | `text-[#007D7D]` |
| Clinical normal / passed | Brand primary | `text-[#007D7D]` |
| Clinical warning | Amber-700 | `text-amber-700` |
| Clinical critical | Red-700 | `text-red-700` |
| Informational | Blue-700 | `text-blue-700` |
| Disabled / muted | Tertiary text | `text-[#5C6C6C]` |
| Copilot AI identity (`Sparkles`) | Brand primary | `text-[#007D7D]` |

---

### 15.5 Icon Usage Patterns

**Feature icon container (website):**
```tsx
<div
  className="w-16 h-16 rounded-xl shadow-lg flex items-center justify-center"
  style={{ background: 'linear-gradient(135deg, #00948A, #3A5A56)' }}
>
  <Brain className="w-8 h-8 text-white" strokeWidth={1.5} />
</div>
```

**Clinical status icons:**
```tsx
// Positive / alert finding
<AlertTriangle className="w-4 h-4 text-amber-700" />

// Normal / negative result
<CheckCircle2 className="w-4 h-4 text-[#007D7D]" />

// Critical finding
<AlertTriangle className="w-4 h-4 text-red-700" />
```

**Copilot AI identity badge:**
```tsx
<div className="flex items-center gap-2">
  <Sparkles className="w-6 h-6 text-[#007D7D]" />
  <span className="font-semibold text-[#0D2B2B]">Xlue Copilot</span>
</div>
```

**CTA button with arrow:**
```tsx
<button className="flex items-center gap-2 bg-[#007D7D] hover:bg-[#00A7A2] text-white px-6 py-3 rounded-md transition-colors">
  Learn More
  <ArrowRight className="w-5 h-5" />
</button>
```

---

---

## Appendix: Sources & Compatibility

| Source | Products covered | Priority |
|--------|-----------------|----------|
| `Xlue/xlue-style.md` | Website, general | Foundation spec |
| `Xlue-Health-Demo/src/index.css` | Health clinical interface | Supplemental override |
| `Xlue-Health-Demo/tailwind.config.js` | Health configuration | Tooling config |
| `Xlue-Style/style.md` (this document) | All Xlue products | **Unified spec** |

> **Maintenance note**: This document should be updated continuously as the design system evolves. Before adding new colors or components, verify contrast ratios against the existing brand palette (WCAG AA minimum 4.5:1) and visual consistency.  
> For any design questions, treat this document as the authoritative reference.
