with open('/Users/ghjk3695/Documents/Xlue-Style/style.md', 'r') as f:
    content = f.read()

pairs = []

pairs.append(('## \u76ee\u9304', '## Table of Contents'))

# §5.1 table header & rows
pairs.append(('| \u7528\u9014 | \u985e\u540d / max-width |', '| Usage | Class / max-width |'))
pairs.append(('|------|----------------|', '|-------|------------------|'))
pairs.append(('| \u6587\u5b57\u6bb5\u843d\uff08\u55ae\u6b04\uff09 | `max-w-3xl mx-auto` (768px) |',
              '| Text paragraphs (single column) | `max-w-3xl mx-auto` (768px) |'))
pairs.append(('| Section \u5bb9\u5668\uff08\u5361\u7247\uff09 | `max-w-4xl mx-auto` (896px) |',
              '| Section container (cards) | `max-w-4xl mx-auto` (896px) |'))
pairs.append(('| \u591a\u6b04\u5167\u5bb9 | `max-w-5xl mx-auto` (1024px) |',
              '| Multi-column content | `max-w-5xl mx-auto` (1024px) |'))
pairs.append(('| Footer / \u5927\u578b\u4f48\u5c40 | `max-w-6xl mx-auto` (1152px) |',
              '| Footer / large layout | `max-w-6xl mx-auto` (1152px) |'))
pairs.append(('| \u5c0e\u89bd\u5217 | `max-w-7xl mx-auto` (1280px) |',
              '| Navigation bar | `max-w-7xl mx-auto` (1280px) |'))

# §5.2
pairs.append(('### 5.2 Section \u9593\u8ddd\u6a19\u6e96', '### 5.2 Section Spacing Standard'))
pairs.append(('py-12 px-4   \u2192 \u6240\u6709\u4e3b\u8981 section\uff08\u4e0a\u4e0b 48px\uff0c\u5de6\u53f3 16px\uff09',
              'py-12 px-4   \u2192 all primary sections (48px vertical, 16px horizontal)'))
pairs.append(('p-8          \u2192 \u5361\u7247\u5167\u5bb9 padding\uff0832px \u56db\u908a\uff09',
              'p-8          \u2192 card content padding (32px all sides)'))
pairs.append(('p-4          \u2192 \u7dca\u6e4a\u5361\u7247 padding\uff0816px \u56db\u908a\uff09',
              'p-4          \u2192 compact card padding (16px all sides)'))

# §5.3
pairs.append(('### 5.3 \u5b50\u5143\u7d20\u9593\u8ddd', '### 5.3 Child Element Spacing'))
pairs.append(('| \u5834\u666f | \u985e\u540d |', '| Context | Class |'))
pairs.append(('|------|------|', '|---------|-------|'))
pairs.append(('| Section \u6a19\u984c\u8207\u5167\u5bb9\u4e4b\u9593 | `mb-8` |',
              '| Between section heading and content | `mb-8` |'))
pairs.append(('| \u6a19\u984c\u8207\u526f\u6a19\u4e4b\u9593 | `mb-4` / `mb-3` |',
              '| Between heading and sub-heading | `mb-4` / `mb-3` |'))
pairs.append(('| \u6bb5\u843d\u4e4b\u9593 | `space-y-4` / `space-y-6` |',
              '| Between paragraphs | `space-y-4` / `space-y-6` |'))
pairs.append(('| \u4e09\u6b04 Feature grid | `gap-6` |', '| Three-column feature grid | `gap-6` |'))
pairs.append(('| Badge + \u65e5\u671f\u5217 | `gap-3` |', '| Badge + date row | `gap-3` |'))
pairs.append(('| \u6309\u9215\u7d44 | `gap-4` |', '| Button group | `gap-4` |'))
pairs.append(('| Footer \u6b04\u4f4d\u9593 | `gap-8` |', '| Footer column gap | `gap-8` |'))

# §5.4
pairs.append(('### 5.4 Grid \u4f48\u5c40\u6a21\u5f0f', '### 5.4 Grid Layout Patterns'))
pairs.append(('// \u4e09\u6b04 Feature Cards', '// Three-column Feature Cards'))
pairs.append(('// \u96d9\u6b04 About \u8aaa\u660e', '// Two-column About section'))
pairs.append(('// Footer \u56db\u6b04\uff08\u54c1\u724c\u4f54 2\uff09', '// Footer four-column (brand takes 2)'))

# §5.5
pairs.append(('### 5.5 \u5c0e\u89bd\u5217\u9ad8\u5ea6', '### 5.5 Navigation Bar Height'))
pairs.append(('h-16  \u2192 64px\uff08\u56fa\u5b9a\u9ad8\u5ea6\uff09', 'h-16  \u2192 64px (fixed height)'))
pairs.append(('pt-20 \u2192 \u82f1\u96c4\u5340\u584a\u9802\u90e8 padding\uff0c\u88dc\u511f nav \u9ad8\u5ea6\uff0880px\uff09',
              'pt-20 \u2192 hero section top padding to compensate for nav height (80px)'))

# §5.6
pairs.append(('### 5.6 Xlue Health Demo \u4f48\u5c40\u7279\u6709\u898f\u7bc4', '### 5.6 Xlue Health Demo Layout Specifics'))
pairs.append(('Sidebar \u5bec\u5ea6       : 240px\uff08\u684c\u9762\uff09/ \u6536\u5408\u81f3 64px',
              'Sidebar width          : 240px (desktop) / collapsed to 64px'))
pairs.append(('\u4e3b\u5167\u5bb9\u5340           : calc(100vw - 240px)', 'Main content area      : calc(100vw - 240px)'))
pairs.append(('Panel \u6700\u5c0f\u9ad8\u5ea6     : 200px', 'Panel minimum height   : 200px'))
pairs.append(('Panel \u6a19\u984c\u9ad8\u5ea6     : 40px\uff08h-10\uff09', 'Panel header height    : 40px (h-10)'))
pairs.append(('Patient Queue \u5bec\u5ea6 : 320px', 'Patient Queue width    : 320px'))

# §6
pairs.append(('## 6. \u5713\u89d2\u8207\u9670\u5f71', '## 6. Radius & Shadows'))
pairs.append(('### 6.1 \u5713\u89d2\u898f\u7bc4', '### 6.1 Border Radius'))
pairs.append(('| \u5143\u4ef6 | \u985e\u540d | px \u5024 | CSS Token |', '| Component | Class | px | CSS Token |'))
pairs.append(('| \u5927\u578b\u5361\u7247\u3001\u5340\u584a\u5bb9\u5668 | `rounded-2xl` | 16px | `--radius-xl` |',
              '| Large cards, section containers | `rounded-2xl` | 16px | `--radius-xl` |'))
pairs.append(('| \u4e00\u822c\u5361\u7247 | `rounded-xl` | 12px | `--radius-lg` |', '| General cards | `rounded-xl` | 12px | `--radius-lg` |'))
pairs.append(('| \u6309\u9215 | `rounded-md` | ~6\u20138px | `--radius-md` |', '| Buttons | `rounded-md` | ~6\u20138px | `--radius-md` |'))
pairs.append(('| \u4eba\u7269\u982d\u50cf | `rounded-full` | 50% | \u2014 |', '| Person avatar | `rounded-full` | 50% | \u2014 |'))
pairs.append(('| Icon \u5bb9\u5668 | `rounded-xl` | 12px | `--radius-lg` |', '| Icon container | `rounded-xl` | 12px | `--radius-lg` |'))
pairs.append(('> Health Demo \u5168\u57df `--radius: 16px`\uff0c\u6bd4\u5b98\u7db2\u7565\u5927\uff0c\u5f37\u8abf\u5361\u7247\u908a\u7de3\u7684\u53cb\u597d\u611f\u3002',
              '> Health Demo sets `--radius: 16px` globally, slightly larger than the website, to give card edges a friendlier feel.'))
pairs.append(('### 6.2 \u9670\u5f71\u898f\u7bc4', '### 6.2 Shadows'))
pairs.append(('| \u5c64\u7d1a | \u5024 | CSS Token | \u7528\u9014 |', '| Level | Value | CSS Token | Usage |'))
pairs.append(('|------|-----|-----------|------|', '|-------|-------|-----------|-------|'))
pairs.append(('| **\u5361\u7247\u4e3b\u9670\u5f71** | `0 4px 12px rgba(0,0,0,0.15)` | `--shadow-card` | \u4eba\u7269\u5361\u3001\u91cd\u8981\u5361\u7247 |',
              '| **Card main shadow** | `0 4px 12px rgba(0,0,0,0.15)` | `--shadow-card` | Person cards, key cards |'))
pairs.append(('| **\u5361\u7247\u8f15\u9670\u5f71** | `0 2px 8px rgba(0,0,0,0.08)` | `--shadow-light` | \u65b0\u805e\u5361\u3001\u6b21\u8981\u5361\u7247 |',
              '| **Card light shadow** | `0 2px 8px rgba(0,0,0,0.08)` | `--shadow-light` | News cards, secondary cards |'))
pairs.append(('| **Icon \u5bb9\u5668\u9670\u5f71** | `shadow-lg` | \u2014 | Feature icon |',
              '| **Icon container** | `shadow-lg` | \u2014 | Feature icon |'))
pairs.append(('| **\u4eba\u7269\u982d\u50cf\u9670\u5f71** | `0 2px 8px rgba(0,0,0,0.08)` | `--shadow-light` | \u8207\u5361\u7247\u540c\u5c64\u7d1a |',
              '| **Person avatar** | `0 2px 8px rgba(0,0,0,0.08)` | `--shadow-light` | Same level as card |'))
pairs.append(('> \u539f\u5247\uff1a\u6240\u6709\u5361\u7247\u7686\u4f7f\u7528 **`border: none`** \u6383\u914d\u81ea\u8a02 box-shadow\uff0c**\u4e0d\u6df7\u7528 border + shadow**\u3002',
              '> Rule: All cards use **`border: none`** plus a custom box-shadow. **Never combine border + shadow.**'))

# §7
pairs.append(('## 7. \u5143\u4ef6\u98a8\u683c', '## 7. Component Styles'))
pairs.append(('### 7.1 \u5c0e\u89bd\u5217 (Navigation)', '### 7.1 Navigation Bar'))
pairs.append(('/* \u5b98\u7db2\u5c0e\u89bd\u5217 */', '/* Website navigation bar */'))
pairs.append(('- **Logo \u5207\u63db**\uff1a\u6eda\u52d5\u9032\u5165 Features section \u6642\uff0c\u4e3b logo \u6de1\u51fa\uff0cHealth logo \u6de1\u5165',
              '- **Logo switch**: When scrolling into the Features section, the primary logo fades out and the Health logo fades in'))
pairs.append(('- **Links**\uff1a`text-sm font-medium transition-colors`\uff0chover \u8272 `#00A7A2`',
              '- **Links**: `text-sm font-medium transition-colors`, hover color `#00A7A2`'))
pairs.append(('- **CTA Button**\uff1a`bg-[#007D7D] hover:bg-[#00A7A2] text-white`',
              '- **CTA Button**: `bg-[#007D7D] hover:bg-[#00A7A2] text-white`'))
pairs.append(('### 7.2 \u4e3b\u8981\u6309\u9215 (Primary Button)', '### 7.2 Primary Button'))
pairs.append(('### 7.3 \u6b21\u8981\u6309\u9215 (Secondary / Outline)', '### 7.3 Secondary Button (Outline)'))
pairs.append(('### 7.5 Mission / Contact CTA \u5361\u7247', '### 7.5 Mission / Contact CTA Card'))
pairs.append(('  /* \u7121 border\uff0c\u7121 shadow */', '  /* no border, no shadow */'))
pairs.append(('### 7.6 Feature Icon \u5bb9\u5668', '### 7.6 Feature Icon Container'))
pairs.append(('/* Icon \u8272\uff1awhite (#FFFFFF) */', '/* Icon color: white (#FFFFFF) */'))
pairs.append(('/* Icon \u5c3a\u5bf8\uff1a32\xd732px */', '/* Icon size: 32\xd732px */'))
pairs.append(('### 7.7 \u4eba\u7269\u5361\u7247 (Founder Card)', '### 7.7 Person Card (Founder Card)'))
pairs.append(('/* \u540d\u5b57\uff1afont-bold text-[#0D2B2B] text-lg */', '/* Name: font-bold text-[#0D2B2B] text-lg */'))
pairs.append(('/* \u63cf\u8ff0\uff1atext-[#5C6C6C] text-sm */', '/* Description: text-[#5C6C6C] text-sm */'))
pairs.append(('### 7.8 \u65b0\u805e\u5361\u7247 (News Card)', '### 7.8 News Card'))
pairs.append(('/* \u9023\u7d50\u8272\uff1a#007D7D\uff0chover\uff1a#00A7A2 */', '/* Link color: #007D7D, hover: #00A7A2 */'))
pairs.append(('### 7.9 Badge / \u5206\u985e\u6a19\u7c64', '### 7.9 Badge / Category Label'))
pairs.append(('### 7.10 \u5206\u9694\u7dda', '### 7.10 Divider'))
pairs.append(('| \u5143\u7d20 | \u6a23\u5f0f |', '| Element | Style |'))
pairs.append(('| \u80cc\u666f | `#F4F7F6` |', '| Background | `#F4F7F6` |'))
pairs.append(('| \u9802\u90e8\u908a\u6846 | `1px solid #D8E2E0` |', '| Top border | `1px solid #D8E2E0` |'))
pairs.append(('| \u4e3b\u6587\u5b57 | `#0E2E2E` |', '| Primary text | `#0E2E2E` |'))
pairs.append(('| \u6b21\u6587\u5b57 | `rgba(14,46,46,0.80)` |', '| Secondary text | `rgba(14,46,46,0.80)` |'))
pairs.append(('| \u5340\u584a\u6a19\u984c | `font-semibold` |', '| Section heading | `font-semibold` |'))
pairs.append(('| \u9023\u7d50 hover | \u52a0\u6df1\u81f3 `#0E2E2E` |', '| Link hover | Darken to `#0E2E2E` |'))
pairs.append(('| \u5167\u5bb9 padding | `py-12` |', '| Content padding | `py-12` |'))
pairs.append(('| Grid | 4\u6b04\uff0c\u54c1\u724c\u6b04\u4f54 2/4 |', '| Grid | 4 columns, brand column spans 2/4 |'))
pairs.append(('### 7.13 Xlue Health Demo \u2014 \u81e8\u5e8a Panel \u5143\u4ef6', '### 7.13 Xlue Health Demo \u2014 Clinical Panel Components'))

# §8
pairs.append(('## 8. \u52d5\u756b\u8207\u4e92\u52d5', '## 8. Animation & Interaction'))
pairs.append(('### 8.1 \u57fa\u790e\u904e\u6e21', '### 8.1 Base Transitions'))
pairs.append(('/* \u984f\u8272\u5207\u63db\uff08\u6240\u6709\u4e92\u52d5\u72c0\u614b\uff09 */', '/* Color switch (all interactive states) */'))
pairs.append(('/* \u901a\u7528\u5168\u5c6c\u6027\u904e\u6e21\uff08Logo \u5207\u63db\u7b49\uff09 */', '/* Universal all-property transition (logo switch, etc.) */'))
pairs.append(('/* \u5361\u7247 hover \u63d0\u5347 */', '/* Card hover lift */'))
pairs.append(('### 8.2 Logo \u5207\u63db\u52d5\u756b\uff08\u5b98\u7db2\uff09', '### 8.2 Logo Switch Animation (Website)'))
pairs.append(('\u5c0e\u89bd\u5217\u5728\u9032\u5165 Features section \u6642\uff0c\u4e3b logo \u8207 Health logo \u4e92\u76f8\u6de1\u5165\u6de1\u51fa\u4e26\u6709\u8f15\u5fae\u4f4d\u79fb\uff1a',
              'When the navbar enters the Features section, the primary logo and Health logo cross-fade with a subtle vertical shift:'))
pairs.append(('/* \u4e3b Logo\uff08\u975e features \u5340\u584a\uff09 */', '/* Primary Logo (outside features section) */'))
pairs.append(('/* Health Logo\uff08features \u5340\u584a\uff09 */', '/* Health Logo (inside features section) */'))
pairs.append(('### 8.3 \u5361\u7247 Hover \u6548\u679c', '### 8.3 Card Hover Effect'))
pairs.append(('### 8.4 \u6372\u52d5\u884c\u70ba', '### 8.4 Scroll Behavior'))
pairs.append(('- \u6240\u6709 anchor \u9023\u7d50\uff1a`scroll-behavior: smooth`', '- All anchor links: `scroll-behavior: smooth`'))
pairs.append(('- \u5c0e\u89bd\u5217\u6372\u52d5\u5049\u6e2c\u95be\u5024\uff1a`scrollY > 50px`', '- Navbar scroll detection threshold: `scrollY > 50px`'))
pairs.append(('- Section \u5049\u6e2c\uff1a`rect.top <= 100 && rect.bottom >= 100`', '- Section detection: `rect.top <= 100 && rect.bottom >= 100`'))
pairs.append(('### 8.5 Accordion \u52d5\u756b', '### 8.5 Accordion Animation'))

# §9
pairs.append(('## 9. \u97ff\u61c9\u5f0f\u65b7\u9ede', '## 9. Responsive Breakpoints'))
pairs.append(('\u63a1\u7528 Tailwind CSS \u9810\u8a2d\u65b7\u9ede\uff1a', 'Uses Tailwind CSS default breakpoints:'))
pairs.append(('| \u65b7\u9ede | \u524d\u7f6e | \u6700\u5c0f\u5bec\u5ea6 | \u4e3b\u8981\u884c\u70ba |', '| Breakpoint | Prefix | Min-width | Main behavior |'))
pairs.append(('|------|------|---------|---------|', '|------------|--------|-----------|---------------|'))
pairs.append(('| Mobile | \uff08\u7121\uff09 | 0px | \u55ae\u6b04\u3001\u6f22\u5821\u9078\u55ae |', '| Mobile | (none) | 0px | Single column, hamburger menu |'))
pairs.append(('| Small | `sm:` | 640px | \u6309\u9215\u4f75\u6392\uff08`sm:flex-row`\uff09 |', '| Small | `sm:` | 640px | Buttons in row (`sm:flex-row`) |'))
pairs.append(('| Medium | `md:` | 768px | \u591a\u6b04 Grid\u3001\u986f\u793a\u684c\u9762\u5c0e\u89bd |', '| Medium | `md:` | 768px | Multi-column grid, show desktop nav |'))
pairs.append(('| 2XL | `2xl:` | 1400px | Container \u6700\u5927\u5bec\u5ea6 |', '| 2XL | `2xl:` | 1400px | Container max-width |'))
pairs.append(('### 9.1 \u91cd\u8981\u97ff\u61c9\u5f0f\u6a21\u5f0f', '### 9.1 Key Responsive Patterns'))
pairs.append(('// \u5c0e\u89bd\u5217\uff1a\u624b\u6a5f\u6f22\u5821 \u2192 \u684c\u9762\u6c34\u5e73\u9078\u55ae', '// Navbar: mobile hamburger \u2192 desktop horizontal menu'))
pairs.append(('<div className="hidden md:block">   // \u684c\u9762\u7248\u5c0e\u89bd\u9023\u7d50', '<div className="hidden md:block">   // desktop nav links'))
pairs.append(('<div className="md:hidden">         // \u624b\u6a5f\u7248\u6f22\u5821\u6309\u9215', '<div className="md:hidden">         // mobile hamburger button'))
pairs.append(('// \u4e09\u6b04 Feature\uff1a\u624b\u6a5f\u55ae\u6b04 \u2192 \u684c\u9762\u4e09\u6b04', '// Three-column Feature: mobile single \u2192 desktop three-column'))
pairs.append(('// Hero \u6a19\u984c\uff1a\u624b\u6a5f 36px \u2192 \u684c\u9762 48px', '// Hero heading: mobile 36px \u2192 desktop 48px'))
pairs.append(('// \u6309\u9215\u7d44\uff1a\u624b\u6a5f\u76f4\u6392 \u2192 \u684c\u9762\u6a6b\u6392', '// Button group: mobile stacked \u2192 desktop inline'))

# §10
pairs.append(('## 10. CSS \u8b8a\u6578\u901f\u67e5\u8868', '## 10. CSS Token Reference'))
pairs.append(('\u8cbc\u5165\u4efb\u4f55\u65b0\u5e73\u53f0\u7684 `:root` \u5373\u53ef\u7e7c\u627f\u5b8c\u6574 Xlue \u54c1\u724c\u914d\u8272\uff1a',
              'Paste into the `:root` of any new platform to inherit the full Xlue brand palette:'))

# §11
pairs.append(('## 11. Tailwind \u5feb\u901f\u53c3\u7167', '## 11. Tailwind Quick Reference'))
pairs.append(('### 11.1 \u5e38\u7528\u8272\u5f69 Class', '### 11.1 Common Color Classes'))
pairs.append(('| \u984f\u8272 | Tailwind arbitrary |', '| Color | Tailwind arbitrary |'))
pairs.append(('| \u54c1\u724c\u4e3b\u8272 | `bg-[#007D7D]` / `text-[#007D7D]` |', '| Brand primary | `bg-[#007D7D]` / `text-[#007D7D]` |'))
pairs.append(('| \u54c1\u724c hover | `hover:bg-[#00A7A2]` / `hover:text-[#00A7A2]` |',
              '| Brand hover | `hover:bg-[#00A7A2]` / `hover:text-[#00A7A2]` |'))
pairs.append(('| \u4e3b\u6587\u5b57 | `text-[#0D2B2B]` |', '| Primary text | `text-[#0D2B2B]` |'))
pairs.append(('| \u6b21\u6587\u5b57 | `text-[#2C4444]` |', '| Secondary text | `text-[#2C4444]` |'))
pairs.append(('| \u8f14\u52a9\u6587\u5b57 | `text-[#5C6C6C]` |', '| Tertiary text | `text-[#5C6C6C]` |'))
pairs.append(('| L1 \u80cc\u666f | `bg-[#EFF4F4]` |', '| L1 background | `bg-[#EFF4F4]` |'))
pairs.append(('| Footer \u80cc\u666f | `bg-[#F4F7F6]` |', '| Footer background | `bg-[#F4F7F6]` |'))
pairs.append(('| \u908a\u6846 | `border-[#D8E2E0]` |', '| Border | `border-[#D8E2E0]` |'))
pairs.append(('### 11.2 \u5e38\u7528\u8907\u5408\u6a23\u5f0f', '### 11.2 Common Composite Styles'))
pairs.append(('// Section \u5bb9\u5668', '// Section container'))
pairs.append(('// \u54c1\u724c\u4e3b\u6309\u9215', '// Brand primary button'))
pairs.append(('// \u5167\u5bb9\u5361\u7247', '// Content card'))
pairs.append(('// Feature \u5340\u584a\u5bb9\u5668', '// Feature section container'))
pairs.append(('// \u6a19\u984c\u54c1\u724c\u6f38\u5c64', '// Heading brand gradient'))
pairs.append(('// \u5c0e\u89bd\u9023\u7d50', '// Nav link'))
pairs.append(('// \u56fa\u5b9a\u5c0e\u89bd\u5217', '// Fixed navbar'))
pairs.append(('// \u5206\u9694\u7dda', '// Divider'))
pairs.append(('// \u4eba\u7269\u982d\u50cf', '// Person avatar'))
pairs.append(('// \u5361\u7247\u9670\u5f71', '// Card shadow'))

# §12
pairs.append(('## 12. Xlue Health Demo \u7279\u6709\u898f\u7bc4', '## 12. Xlue Health Demo Specifics'))
pairs.append(('\u672c\u7bc0\u5f59\u6574 Xlue Health Demo\uff08\u81e8\u5e8a\u5de5\u4f5c\u4ecb\u9762\uff09\u4e2d\u89c0\u5bdf\u5230\u7684\u984d\u5916\u8a2d\u8a08\u898f\u7bc4\uff0c\u88dc\u5145\u5b98\u7db2 Style Guide \u672a\u8986\u84cb\u7684\u90e8\u5206\u3002',
              'This section consolidates additional design rules observed in Xlue Health Demo (the clinical workspace interface), supplementing areas not covered by the website Style Guide.'))
pairs.append(('### 12.1 InterfaceLayout \u7d50\u69cb', '### 12.1 Interface Layout Structure'))
pairs.append(('### 12.2 \u81e8\u5e8a\u8cc7\u6599\u984f\u8272\u898f\u7bc4', '### 12.2 Clinical Data Color Rules'))
pairs.append(('| \u72c0\u614b | \u984f\u8272 | \u8aaa\u660e |', '| Status | Color | Notes |'))
pairs.append(('|------|------|------|', '|--------|-------|-------|'))
pairs.append(('| \u6b63\u5e38 / \u901a\u904e | `#007D7D` | \u54c1\u724c\u4e3b\u8272 |', '| Normal / Passed | `#007D7D` | Brand primary |'))
pairs.append(('| \u8b66\u793a | `#B45309` (amber-700) | \u2014 |', '| Warning | `#B45309` (amber-700) | \u2014 |'))
pairs.append(('| \u5371\u6025 | `#B91C1C` (red-700) | \u2014 |', '| Critical | `#B91C1C` (red-700) | \u2014 |'))
pairs.append(('| \u8cc7\u8a0a | `#1D4ED8` (blue-700) | \u50c5\u9650\u7d14\u8cc7\u8a0a\u6027\u6a19\u8a18 |',
              '| Informational | `#1D4ED8` (blue-700) | Pure informational labels only |'))
pairs.append(('> \u6ce8\u610f\uff1a\u81e8\u5e8a\u8b66\u793a\u8272\u4f7f\u7528 amber/red\uff0c**\u4e0d\u4f7f\u7528** Xlue \u54c1\u724c\u8272\uff08\u907f\u514d\u6df7\u6de1\u56b4\u91cd\u7a0b\u5ea6\uff09\u3002',
              '> Note: Clinical alert colors use amber/red \u2014 **do not** use Xlue brand colors (avoids confusing severity levels).'))
pairs.append(('### 12.3 Screening Panel \u7b5b\u67e5\u986f\u793a', '### 12.3 Screening Panel Display'))
pairs.append(('- \u6b63\u5411\u7b5b\u67e5\u6307\u6a19\uff1a\u4ee5\u4eae\u773c\u6a19\u8a18\uff08badge + icon\uff09\uff0c\u907f\u514d\u907a\u6f0f',
              '- Positive screening indicators: highlighted with badge + icon to prevent missed findings'))
pairs.append(('- \u9670\u6027\u7d50\u679c\uff1a\u7070\u968e\u6216\u5f31\u5316\u6587\u5b57\uff0c\u964d\u4f4e\u8996\u89ba\u91cd\u91cf',
              '- Negative results: grayscale or weakened text, reduced visual weight'))
pairs.append(('- \u81e8\u754c\u5024\u986f\u793a\uff1a`font-mono` \u7b49\u5bec\u5b57\u9ad4\u78ba\u4fdd\u6578\u5024\u5c0d\u9f4a',
              '- Threshold display: `font-mono` monospace ensures numeric alignment'))
pairs.append(('### 12.4 Copilot Chat \u4ecb\u9762', '### 12.4 Copilot Chat Interface'))
pairs.append(('/* \u4f7f\u7528\u8005\u8a0a\u606f\u6ce1\u6ce1 */', '/* User message bubble */'))
pairs.append(('/* AI \u56de\u61c9\u8a0a\u606f\u6ce1\u6ce1 */', '/* AI response message bubble */'))

# §13
pairs.append(('## 13. \u7981\u6b62\u4e8b\u9805', '## 13. Do Nots'))
pairs.append(('\u4ee5\u4e0b\u884c\u70ba\u9055\u53cd Xlue \u8a2d\u8a08\u898f\u7bc4\uff0c**\u8acb\u52ff\u4f7f\u7528**\uff1a',
              'The following practices violate Xlue design standards \u2014 **do not use**:'))
pairs.append(('| \u7981\u6b62\u884c\u70ba | \u539f\u56e0 |', '| Prohibited | Reason |'))
pairs.append(('|---------|------|', '|------------|--------|'))
pairs.append(('| \u4f7f\u7528\u85cd\u8272\u3001\u7d2b\u8272\u3001\u6a58\u8272\u7b49\u975e\u54c1\u724c\u8272\uff08\u8b66\u793a\u7528\u9014\u9664\u5916\uff09 | \u7834\u58de\u9751\u8272\u54c1\u724c\u8b58\u5225 |',
              '| Using non-brand colors like blue, purple, or orange (except for alert purposes) | Breaks teal brand identity |'))
pairs.append(('| \u5728\u5361\u7247\u4e0a\u540c\u6642\u4f7f\u7528 border + shadow | \u8996\u89ba\u566a\u97f3\uff0c\u64c7\u4e00 |',
              '| Using border + shadow simultaneously on cards | Visual noise \u2014 choose one |'))
pairs.append(('| \u4f7f\u7528 `text-black` \u6216 `#000000` | \u6539\u7528 `#0D2B2B` \u6df1\u9751\u8272 |',
              '| Using `text-black` or `#000000` | Use `#0D2B2B` deep teal instead |'))
pairs.append(('| \u4f7f\u7528\u7d14\u767d `#FFFFFF` \u4f5c\u70ba\u5168\u7ad9\u80cc\u666f | \u6539\u7528 `#FAFAF8` \u6696\u8abf\u5e95\u8272 |',
              '| Using pure white `#FFFFFF` as the site-wide background | Use `#FAFAF8` warm off-white instead |'))
pairs.append(('| Section \u9593\u4f7f\u7528\u5927\u5e45\u80cc\u666f\u8272\u5207\u63db | \u4fdd\u6301 L0/L1 \u7684\u67d4\u548c\u5c64\u6b21 |',
              '| Large background-color shifts between sections | Maintain gentle L0/L1 layering |'))
pairs.append(('| \u8d85\u904e `text-5xl` \u7684\u5b57\u7d1a\uff08\u975e\u7279\u6b8a\u9801\u9762\uff09 | \u7dad\u6301\u8996\u89ba\u6bd4\u4f8b |',
              '| Font sizes larger than `text-5xl` (except special pages) | Preserve visual proportion |'))
pairs.append(('| \u4f7f\u7528\u5f37\u70c8\u9670\u5f71\uff08`shadow-2xl` \u4ee5\u4e0a\uff09 | \u7dad\u6301\u8f15\u76c8\u7684\u8996\u89ba\u91cd\u91cf |',
              '| Heavy shadows (`shadow-2xl` or stronger) | Maintain lightweight visual style |'))
pairs.append(('| \u5728\u6bb5\u843d\u6b63\u6587\u4f7f\u7528 `font-bold` | \u6b63\u6587\u50c5\u7528 normal\uff0cbold \u53ea\u7528\u65bc\u6a19\u984c |',
              '| Using `font-bold` in body paragraph text | Body uses normal weight; bold is for headings only |'))
pairs.append(('| \u65b0\u589e\u672a\u5be9\u6838\u7684\u52d5\u756b\u6548\u679c | \u91ab\u7642\u54c1\u724c\u9700\u7dad\u6301\u6c89\u7a69\u611f |',
              '| Adding unapproved animation effects | Medical brands require a calm, restrained feel |'))
pairs.append(('| \u4f7f\u7528 `rounded-none` \u65bc\u5361\u7247\u5143\u4ef6 | \u6240\u6709\u5361\u7247\u5fc5\u9808\u5e36\u5713\u89d2 |',
              '| Using `rounded-none` on card components | All cards must have rounded corners |'))
pairs.append(('| \u5728\u81e8\u5e8a\u4ecb\u9762\u4f7f\u7528\u54c1\u724c\u8272\u8868\u793a\u5371\u6025\u72c0\u614b | \u6df7\u6de1\u81e8\u5e8a\u56b4\u91cd\u7a0b\u5ea6\u8a9e\u610f |',
              '| Using brand color to indicate critical status in clinical interfaces | Confuses clinical severity semantics |'))

# Appendix
pairs.append(('## \u9644\u9304\uff1a\u4f86\u6e90\u8207\u76f8\u5bb9\u6027', '## Appendix: Sources & Compatibility'))
pairs.append(('| \u898f\u7bc4\u4f86\u6e90 | \u6db5\u84cb\u7522\u54c1 | \u512a\u5148\u7d1a |', '| Source | Products covered | Priority |'))
pairs.append(('|---------|---------|-------|', '|--------|-----------------|----------|'))
pairs.append(('| `Xlue/xlue-style.md` | \u5b98\u7db2\u3001\u901a\u7528 | \u57fa\u790e\u898f\u7bc4 |',
              '| `Xlue/xlue-style.md` | Website, general | Foundation spec |'))
pairs.append(('| `Xlue-Health-Demo/src/index.css` | Health \u81e8\u5e8a\u4ecb\u9762 | \u88dc\u5145\u8986\u84cb |',
              '| `Xlue-Health-Demo/src/index.css` | Health clinical interface | Supplemental override |'))
pairs.append(('| `Xlue-Health-Demo/tailwind.config.js` | Health \u914d\u7f6e | \u5de5\u5177\u914d\u7f6e |',
              '| `Xlue-Health-Demo/tailwind.config.js` | Health configuration | Tooling config |'))
pairs.append(('| `Xlue-Style/style.md`\uff08\u672c\u6587\u4ef6\uff09 | \u6240\u6709 Xlue \u7522\u54c1 | **\u7d71\u4e00\u898f\u7bc4** |',
              '| `Xlue-Style/style.md` (this document) | All Xlue products | **Unified spec** |'))
pairs.append(('> **\u7dad\u8b77\u8aaa\u660e**\uff1a\u672c\u6587\u4ef6\u61c9\u96a8\u8a2d\u8a08\u7cfb\u7d71\u6f14\u9032\u6301\u7e8c\u66f4\u65b0\u3002\u65b0\u589e\u984f\u8272\u6216\u5143\u4ef6\u524d\uff0c\u8acb\u78ba\u8a8d\u8207\u73fe\u6709\u54c1\u724c\u8272\u76e4\u7684\u5c0d\u6bd4\u5024\uff08WCAG AA \u6700\u4f4e 4.5:1\uff09\u53ca\u8996\u89ba\u4e00\u81f4\u6027\u3002  \n> \u5982\u6709\u8a2d\u8a08\u7591\u554f\uff0c\u8acb\u4ee5\u6b64\u6587\u4ef6\u70ba\u6700\u7d42\u4f9d\u64da\u3002',
              '> **Maintenance note**: This document should be updated continuously as the design system evolves. Before adding new colors or components, verify contrast ratios against the existing brand palette (WCAG AA minimum 4.5:1) and visual consistency.  \n> For any design questions, treat this document as the authoritative reference.'))

count = 0
not_found = []
for old, new in pairs:
    if old in content:
        content = content.replace(old, new, 1)
        count += 1
    else:
        not_found.append(old[:80])

with open('/Users/ghjk3695/Documents/Xlue-Style/style.md', 'w') as f:
    f.write(content)

import re
remaining = len(re.findall('[\u4e00-\u9fff]', content))
print(f'Applied: {count}/{len(pairs)} replacements')
print(f'Chinese chars remaining after translation: {remaining}')
if not_found:
    print(f'Not found ({len(not_found)}):')
    for x in not_found[:10]:
        print(f'  {x!r}')
