# Xlue Design System & Style Guide

> **版本：1.1** ｜ 更新日期：2026-03-04
> 適用範圍：Xlue 官方網站、Xlue Health Demo、子平台、Web 應用程式、合作方整合介面
> 來源整合：`Xlue/xlue-style.md` + `Xlue-Health-Demo` 實際產品分析

---

## 目錄

1. [品牌定調](#1-品牌定調)
2. [色彩系統](#2-色彩系統)
3. [字形與字體](#3-字形與字體)
4. [字級排版規範](#4-字級排版規範)
5. [間距與佈局](#5-間距與佈局)
6. [圓角與陰影](#6-圓角與陰影)
7. [元件風格](#7-元件風格)
8. [動畫與互動](#8-動畫與互動)
9. [響應式斷點](#9-響應式斷點)
10. [CSS 變數速查表](#10-css-變數速查表)
11. [Tailwind 快速參照](#11-tailwind-快速參照)
12. [Xlue Health Demo 特有規範](#12-xlue-health-demo-特有規範)
13. [禁止事項](#13-禁止事項)

---

## 1. 品牌定調

Xlue 是一家 Carnegie Mellon University spin-off，專注於 **Health Foundation Models**。視覺風格應傳達：

| 特質 | 視覺語言 |
|------|---------|
| 醫療信賴感 | 深邃墨綠青色、簡潔無冗餘 |
| 前沿科技感 | 漸層文字、精準排版 |
| 學術嚴謹性 | 高對比文字、充裕留白 |
| 開放生態感 | 柔和背景色、模組化卡片 |
| 臨床實用性（Health Demo）| 密集資訊、清晰層級、快速掃視 |

### 1.1 產品線區分

| 產品 | 定位 | 主要視覺差異 |
|------|------|------------|
| **Xlue 官網** | 行銷、品牌展示 | 大留白、漸層標題、Hero 區塊 |
| **Xlue Health Demo** | 臨床工作介面 | Side Panel、資訊密度高、Sidebar Navigation |
| **Xlue Copilot** | AI 對話輔助 | 聊天介面、浮動視窗 |

---

## 2. 色彩系統

### 2.1 核心品牌色盤

| 名稱 | Hex | HSL | CSS Token | 用途 |
|------|-----|-----|-----------|------|
| **Brand Primary** | `#007D7D` | `180 100% 25%` | `--color-primary` / `--primary` | 按鈕、連結、強調色 |
| **Brand Hover** | `#00A7A2` | `178 100% 32%` | `--color-primary-hover` | 互動懸停態 |
| **Brand Light** | `#009C9C` | `180 100% 31%` | `--color-primary-light` | 次要按鈕 hover |
| **Brand Dark** | `#005A5A` | `180 100% 18%` | `--color-primary-dark` | 漸層深端、footer |
| **Gradient Start** | `#00948A` | `177 100% 29%` | `--color-gradient-start` | 標題漸層起點 |
| **Gradient End** | `#3A5A56` | `174 22% 29%` | `--color-gradient-end` | 標題漸層終點 |

### 2.2 背景色分層

| 層級 | Hex | HSL | CSS Token | 說明 |
|------|-----|-----|-----------|------|
| **L0 全站背景** | `#FAFAF8` | `60 8% 98%` | `--bg-l0` / `--background` | `<body>` 底色，微暖白 |
| **L1 卡片 / 區塊** | `#EFF4F4` | `180 20% 95%` | `--bg-l1` / `--surface-900` | 內容卡片、Mission、Contact CTA |
| **L2 頁腳背景** | `#F4F7F6` | `165 11% 96%` | `--bg-l2` | Footer 底色 |
| **L3 純白卡片** | `#FFFFFF` | — | `--bg-card` / `--card` | 人物卡、彈窗、表格 |

> **Xlue Health Demo 補充**：臨床介面的 sidebar 使用 L3（`#FFFFFF`），主內容區使用 L0，panel 區塊使用 L1。

### 2.3 文字色階

| 用途 | Hex | HSL | CSS Token |
|------|-----|-----|-----------|
| **主文字** | `#0D2B2B` | `180 50% 10%` | `--text-primary` / `--foreground` |
| **次文字** | `#2C4444` | `180 30% 22%` | `--text-secondary` / `--muted-foreground` |
| **輔助文字** | `#5C6C6C` | `180 9% 40%` | `--text-tertiary` |
| **弱化文字** | `rgba(14,46,46,0.80)` | — | `--text-weak` |

### 2.4 線框 / 分隔色

| 用途 | Hex / Value | CSS Token |
|------|-------------|-----------|
| **主要 border** | `#D8E2E0` | `--border-default` / `--border` |
| **深色面 border** | `rgba(255,255,255,0.08)` | `--border-dark` |

### 2.5 Feature Icon 漸層組合

三欄 feature card 的 icon 背景依序使用以下漸層，保持品牌一致性：

```css
/* Card 1 — Clinical & Payer */
background: linear-gradient(135deg, #007D7D, #005A5A);

/* Card 2 — Patient-Centered */
background: linear-gradient(135deg, #008A8A, #006A6A);

/* Card 3 — Pharma & Life Science */
background: linear-gradient(135deg, #009C9C, #007A7A);
```

### 2.6 Badge 色彩

```css
/* 預設狀態 */
background-color: rgba(0, 125, 125, 0.20);
color: #007D7D;
border-color: rgba(0, 125, 125, 0.40);

/* Hover 態 */
background-color: rgba(0, 156, 156, 0.20);
color: #009C9C;
border-color: rgba(0, 156, 156, 0.40);
```

### 2.7 Sidebar Colors（Xlue Health Demo 特有）

```css
/* Sidebar 背景 */
--sidebar-background: #FFFFFF;
--sidebar-foreground: #0D2B2B;
--sidebar-primary:    #007D7D;
--sidebar-accent:     #EFF4F4;
--sidebar-border:     #D8E2E0;
```

---

## 3. 字形與字體

### 3.1 字體堆疊

Xlue 官網採用**系統原生字體堆疊**（Tailwind CSS 預設）；Xlue Health Demo 及未來品牌升級則以 **Inter** 為首選：

```css
/* 官網 / 預設 */
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

/* Health Demo / 升級版（Inter 優先）*/
font-family:
  "Inter",
  ui-sans-serif,
  system-ui,
  Avenir,
  Helvetica,
  Arial,
  sans-serif;

/* 等寬 / 代碼 */
font-family: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
```

> **設計哲學**：以系統字體確保全平台渲染一致性，避免字型載入延遲影響首頁感知效能。Health Demo 使用 Inter 以確保臨床資訊在密集排版下的可讀性。

### 3.2 字體角色分配

| 角色 | 主要字體 | 備選 |
|------|---------|------|
| 標題 Display | **Inter** | Manrope |
| 一般內文 Body | **Inter** | DM Sans |
| 臨床資料 / 數值 | **Inter** | — |
| 等寬 / 代碼 | **JetBrains Mono** | Fira Code |

---

## 4. 字級排版規範

### 4.1 尺度對照表

| 層級 | Tailwind 類名 | px 值 | font-weight | line-height | 用途 |
|------|--------------|-------|-------------|-------------|------|
| **Display H1** | `text-5xl` desktop / `text-4xl` mobile | 48 / 36px | `font-bold` 700 | `leading-tight` 1.25 | 首頁英雄標題 |
| **H2 Section** | `text-3xl` | 30px | `font-bold` 700 | `leading-tight` | 各 section 主標題 |
| **H2 Card** | `text-2xl` | 24px | `font-bold` 700 | `leading-tight` | 卡片主標題（Mission、News） |
| **H3 Feature** | `text-lg` | 18px | `font-bold` 700 | `leading-normal` | Feature card 標題 |
| **H4 Sub** | `text-xl` | 20px | `font-semibold` 600 | `leading-normal` | About 副標題 |
| **Body Large** | `text-lg` | 18px | `font-normal` 400 | `leading-relaxed` 1.625 | 段落正文 |
| **Body Base** | `text-base` | 16px | `font-normal` 400 | `leading-normal` 1.5 | 說明文字 |
| **Body Small** | `text-sm` | 14px | `font-normal` / `font-medium` | — | 導覽連結、標籤、footer |
| **Caption** | `text-xs` | 12px | `font-normal` | — | 輔助標記、metadata |

### 4.2 行高規範

| 類型 | Tailwind | 數值 | 適用 |
|------|----------|------|------|
| 壓縮 | `leading-tight` | 1.25 | 大標題 H1/H2 |
| 標準 | `leading-normal` | 1.5 | 介面文字 |
| 寬鬆 | `leading-relaxed` | 1.625 | 段落正文 |

### 4.3 標題品牌漸層寫法

```html
<!-- 主要標題漸層（較深沉） -->
<span style="
  background: linear-gradient(to right, #00948A, #3A5A56);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
">Revolutionizing Medicine</span>

<!-- Feature section 品牌漸層（較亮） -->
<span style="
  background: linear-gradient(to right, #007D7D, #009C9C);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
">The Health Foundation Model</span>
```

```tsx
/* Tailwind/TSX 寫法 */
<span className="bg-gradient-to-r from-[#00948A] to-[#3A5A56] bg-clip-text text-transparent">
  Revolutionizing Medicine
</span>
```

### 4.4 特殊字串樣式

| 情境 | 類名 |
|------|------|
| 新聞分類標籤 | `uppercase tracking-wide text-sm font-medium` |
| Nav 連結 | `text-sm font-medium transition-colors` |
| Section 眉標（eyebrow） | `uppercase tracking-widest text-xs font-medium` |
| Footer 區塊標題 | `font-semibold` |
| Footer 內文 | `text-sm leading-relaxed` |

---

## 5. 間距與佈局

### 5.1 頁面寬度容器

```css
/* 全局根容器（官網 App.css / #root） */
#root {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
}
```

| 用途 | 類名 / max-width |
|------|----------------|
| 文字段落（單欄） | `max-w-3xl mx-auto` (768px) |
| Section 容器（卡片） | `max-w-4xl mx-auto` (896px) |
| 多欄內容 | `max-w-5xl mx-auto` (1024px) |
| Footer / 大型佈局 | `max-w-6xl mx-auto` (1152px) |
| 導覽列 | `max-w-7xl mx-auto` (1280px) |

### 5.2 Section 間距標準

```
py-12 px-4   → 所有主要 section（上下 48px，左右 16px）
p-8          → 卡片內容 padding（32px 四邊）
p-4          → 緊湊卡片 padding（16px 四邊）
```

### 5.3 子元素間距

| 場景 | 類名 |
|------|------|
| Section 標題與內容之間 | `mb-8` |
| 標題與副標之間 | `mb-4` / `mb-3` |
| 段落之間 | `space-y-4` / `space-y-6` |
| 三欄 Feature grid | `gap-6` |
| Badge + 日期列 | `gap-3` |
| 按鈕組 | `gap-4` |
| Footer 欄位間 | `gap-8` |

### 5.4 Grid 佈局模式

```tsx
// 三欄 Feature Cards
<div className="grid grid-cols-1 md:grid-cols-3 gap-6">

// 雙欄 About 說明
<div className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-12 items-start">

// Footer 四欄（品牌佔 2）
<div className="grid grid-cols-1 md:grid-cols-4 gap-8">
```

### 5.5 導覽列高度

```
h-16  → 64px（固定高度）
pt-20 → 英雄區塊頂部 padding，補償 nav 高度（80px）
```

### 5.6 Xlue Health Demo 佈局特有規範

```
Sidebar 寬度       : 240px（桌面）/ 收合至 64px
主內容區           : calc(100vw - 240px)
Panel 最小高度     : 200px
Panel 標題高度     : 40px（h-10）
Patient Queue 寬度 : 320px
```

---

## 6. 圓角與陰影

### 6.1 圓角規範

| 元件 | 類名 | px 值 | CSS Token |
|------|------|-------|-----------|
| 大型卡片、區塊容器 | `rounded-2xl` | 16px | `--radius-xl` |
| 一般卡片 | `rounded-xl` | 12px | `--radius-lg` |
| 按鈕 | `rounded-md` | ~6–8px | `--radius-md` |
| Badge / Tag | `rounded-full` | 9999px | `--radius-full` |
| 人物頭像 | `rounded-full` | 50% | — |
| Icon 容器 | `rounded-xl` | 12px | `--radius-lg` |

> Health Demo 全域 `--radius: 16px`，比官網略大，強調卡片邊緣的友好感。

### 6.2 陰影規範

| 層級 | 值 | CSS Token | 用途 |
|------|-----|-----------|------|
| **卡片主陰影** | `0 4px 12px rgba(0,0,0,0.15)` | `--shadow-card` | 人物卡、重要卡片 |
| **卡片輕陰影** | `0 2px 8px rgba(0,0,0,0.08)` | `--shadow-light` | 新聞卡、次要卡片 |
| **Icon 容器陰影** | `shadow-lg` | — | Feature icon |
| **人物頭像陰影** | `0 2px 8px rgba(0,0,0,0.08)` | `--shadow-light` | 與卡片同層級 |

> 原則：所有卡片皆使用 **`border: none`** 搭配自訂 box-shadow，**不混用 border + shadow**。

---

## 7. 元件風格

### 7.1 導覽列 (Navigation)

```css
/* 官網導覽列 */
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

- **Logo 切換**：滾動進入 Features section 時，主 logo 淡出，Health logo 淡入
- **Links**：`text-sm font-medium transition-colors`，hover 色 `#00A7A2`
- **CTA Button**：`bg-[#007D7D] hover:bg-[#00A7A2] text-white`

### 7.2 主要按鈕 (Primary Button)

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

### 7.3 次要按鈕 (Secondary / Outline)

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

### 7.5 Mission / Contact CTA 卡片

```css
.mission-card {
  background-color: #EFF4F4;
  border-radius: 16px;
  padding: 3rem;
  text-align: center;
  /* 無 border，無 shadow */
}
```

### 7.6 Feature Icon 容器

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
/* Icon 色：white (#FFFFFF) */
/* Icon 尺寸：32×32px */
```

### 7.7 人物卡片 (Founder Card)

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
/* 名字：font-bold text-[#0D2B2B] text-lg */
/* 描述：text-[#5C6C6C] text-sm */
```

### 7.8 新聞卡片 (News Card)

```css
.news-card {
  background-color: #EFF4F4;
  border-radius: 16px;
  padding: 1.5rem;
  border: none;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
/* 連結色：#007D7D，hover：#00A7A2 */
```

### 7.9 Badge / 分類標籤

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

### 7.10 分隔線

```css
.divider { border-top: 1px solid #D8E2E0; }
```

### 7.11 Footer

| 元素 | 樣式 |
|------|------|
| 背景 | `#F4F7F6` |
| 頂部邊框 | `1px solid #D8E2E0` |
| 主文字 | `#0E2E2E` |
| 次文字 | `rgba(14,46,46,0.80)` |
| 區塊標題 | `font-semibold` |
| 連結 hover | 加深至 `#0E2E2E` |
| 內容 padding | `py-12` |
| Grid | 4欄，品牌欄佔 2/4 |

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

### 7.13 Xlue Health Demo — 臨床 Panel 元件

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

## 8. 動畫與互動

### 8.1 基礎過渡

```css
/* 顏色切換（所有互動狀態） */
transition: color 0.2s, background-color 0.2s, border-color 0.2s;

/* 通用全屬性過渡（Logo 切換等） */
transition: all 0.5s ease-in-out;

/* 卡片 hover 提升 */
transition: box-shadow 0.2s, transform 0.2s;
```

### 8.2 Logo 切換動畫（官網）

導覽列在進入 Features section 時，主 logo 與 Health logo 互相淡入淡出並有輕微位移：

```css
/* 主 Logo（非 features 區塊） */
.logo-main { transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out; }
.logo-main.hidden { opacity: 0; transform: translateY(-8px); }

/* Health Logo（features 區塊） */
.logo-health { transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out; }
.logo-health.visible { opacity: 1; transform: translateY(0); }
```

### 8.3 卡片 Hover 效果

```css
.card-interactive:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  transform: translateY(-2px);
}
```

### 8.4 捲動行為

- 所有 anchor 連結：`scroll-behavior: smooth`
- 導覽列捲動偵測閾值：`scrollY > 50px`
- Section 偵測：`rect.top <= 100 && rect.bottom >= 100`

### 8.5 Accordion 動畫

```css
accordion-down: 0.2s ease-out;
accordion-up:   0.2s ease-out;
```

---

## 9. 響應式斷點

採用 Tailwind CSS 預設斷點：

| 斷點 | 前綴 | 最小寬度 | 主要行為 |
|------|------|---------|---------|
| Mobile | （無） | 0px | 單欄、漢堡選單 |
| Small | `sm:` | 640px | 按鈕併排（`sm:flex-row`） |
| Medium | `md:` | 768px | 多欄 Grid、顯示桌面導覽 |
| Large | `lg:` | 1024px | — |
| XL | `xl:` | 1280px | — |
| 2XL | `2xl:` | 1400px | Container 最大寬度 |

### 9.1 重要響應式模式

```tsx
// 導覽列：手機漢堡 → 桌面水平選單
<div className="hidden md:block">   // 桌面版導覽連結
<div className="md:hidden">         // 手機版漢堡按鈕

// 三欄 Feature：手機單欄 → 桌面三欄
<div className="grid grid-cols-1 md:grid-cols-3 gap-6">

// Hero 標題：手機 36px → 桌面 48px
<h1 className="text-4xl md:text-5xl font-bold">

// 按鈕組：手機直排 → 桌面橫排
<div className="flex flex-col sm:flex-row gap-4 justify-center">
```

---

## 10. CSS 變數速查表

貼入任何新平台的 `:root` 即可繼承完整 Xlue 品牌配色：

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

## 11. Tailwind 快速參照

### 11.1 常用色彩 Class

| 顏色 | Tailwind arbitrary |
|------|-------------------|
| 品牌主色 | `bg-[#007D7D]` / `text-[#007D7D]` |
| 品牌 hover | `hover:bg-[#00A7A2]` / `hover:text-[#00A7A2]` |
| 主文字 | `text-[#0D2B2B]` |
| 次文字 | `text-[#2C4444]` |
| 輔助文字 | `text-[#5C6C6C]` |
| L1 背景 | `bg-[#EFF4F4]` |
| Footer 背景 | `bg-[#F4F7F6]` |
| 邊框 | `border-[#D8E2E0]` |

### 11.2 常用複合樣式

```tsx
// Section 容器
"py-12 px-4"

// 品牌主按鈕
"bg-[#007D7D] hover:bg-[#00A7A2] text-white rounded-md font-medium transition-colors"

// 內容卡片
"bg-[#EFF4F4] rounded-2xl p-8"

// Feature 區塊容器
"section-health p-8 max-w-4xl mx-auto"

// 標題品牌漸層
"bg-gradient-to-r from-[#00948A] to-[#3A5A56] bg-clip-text text-transparent"

// 導覽連結
"text-foreground hover:text-[#00A7A2] px-3 py-2 text-sm font-medium transition-colors rounded-md"

// 固定導覽列
"fixed top-0 w-full bg-background/90 backdrop-blur-md z-50 h-16 border-b border-[#D8E2E0]"

// 分隔線
"border-t border-[#D8E2E0]"

// 人物頭像
"w-24 h-24 rounded-full overflow-hidden border-2 border-white shadow-[0_2px_8px_rgba(0,0,0,0.08)]"

// 卡片陰影
"border-0 shadow-[0_4px_12px_rgba(0,0,0,0.15)] rounded-2xl"

// Badge
"uppercase tracking-wide bg-[#007D7D]/20 text-[#007D7D] border border-[#007D7D]/40 rounded-full text-xs font-medium px-3 py-1 transition-colors hover:bg-[#009C9C]/20 hover:text-[#009C9C]"
```

---

## 12. Xlue Health Demo 特有規範

本節彙整 Xlue Health Demo（臨床工作介面）中觀察到的額外設計規範，補充官網 Style Guide 未覆蓋的部分。

### 12.1 InterfaceLayout 結構

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

### 12.2 臨床資料顏色規範

| 狀態 | 顏色 | 說明 |
|------|------|------|
| 正常 / 通過 | `#007D7D` | 品牌主色 |
| 警示 | `#B45309` (amber-700) | — |
| 危急 | `#B91C1C` (red-700) | — |
| 資訊 | `#1D4ED8` (blue-700) | 僅限純資訊性標記 |

> 注意：臨床警示色使用 amber/red，**不使用** Xlue 品牌色（避免混淆嚴重程度）。

### 12.3 Screening Panel 篩查顯示

- 正向篩查指標：以亮眼標記（badge + icon），避免遺漏
- 陰性結果：灰階或弱化文字，降低視覺重量
- 臨界值顯示：`font-mono` 等寬字體確保數值對齊

### 12.4 Copilot Chat 介面

```css
/* 使用者訊息泡泡 */
.chat-user {
  background-color: #007D7D;
  color: #FFFFFF;
  border-radius: 16px 16px 4px 16px;
  padding: 0.75rem 1rem;
  max-width: 80%;
  align-self: flex-end;
}

/* AI 回應訊息泡泡 */
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

## 13. 禁止事項

以下行為違反 Xlue 設計規範，**請勿使用**：

| 禁止行為 | 原因 |
|---------|------|
| 使用藍色、紫色、橘色等非品牌色（警示用途除外） | 破壞青色品牌識別 |
| 在卡片上同時使用 border + shadow | 視覺噪音，擇一 |
| 使用 `text-black` 或 `#000000` | 改用 `#0D2B2B` 深青色 |
| 使用純白 `#FFFFFF` 作為全站背景 | 改用 `#FAFAF8` 暖調底色 |
| Section 間使用大幅背景色切換 | 保持 L0/L1 的柔和層次 |
| 超過 `text-5xl` 的字級（非特殊頁面） | 維持視覺比例 |
| 使用強烈陰影（`shadow-2xl` 以上） | 維持輕盈的視覺重量 |
| 在段落正文使用 `font-bold` | 正文僅用 normal，bold 只用於標題 |
| 新增未審核的動畫效果 | 醫療品牌需維持沉穩感 |
| 使用 `rounded-none` 於卡片元件 | 所有卡片必須帶圓角 |
| 在臨床介面使用品牌色表示危急狀態 | 混淆臨床嚴重程度語意 |

---

## 附錄：來源與相容性

| 規範來源 | 涵蓋產品 | 優先級 |
|---------|---------|-------|
| `Xlue/xlue-style.md` | 官網、通用 | 基礎規範 |
| `Xlue-Health-Demo/src/index.css` | Health 臨床介面 | 補充覆蓋 |
| `Xlue-Health-Demo/tailwind.config.js` | Health 配置 | 工具配置 |
| `Xlue-Style/style.md`（本文件） | 所有 Xlue 產品 | **統一規範** |

> **維護說明**：本文件應隨設計系統演進持續更新。新增顏色或元件前，請確認與現有品牌色盤的對比值（WCAG AA 最低 4.5:1）及視覺一致性。  
> 如有設計疑問，請以此文件為最終依據。
