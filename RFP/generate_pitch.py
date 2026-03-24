"""Generate a 15-minute pitch PowerPoint for The Arc Mercer proposal."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Brand colors
DARK_BLUE = RGBColor(0x1B, 0x2A, 0x4A)
ACCENT_BLUE = RGBColor(0x2E, 0x86, 0xC1)
LIGHT_BLUE = RGBColor(0xD6, 0xEA, 0xF8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
MED_GRAY = RGBColor(0x66, 0x66, 0x66)
LIGHT_GRAY = RGBColor(0xF2, 0xF2, 0xF2)
GREEN = RGBColor(0x27, 0xAE, 0x60)
ORANGE = RGBColor(0xE6, 0x7E, 0x22)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)


def add_bg(slide, color=DARK_BLUE):
    """Fill slide background with a solid color."""
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_shape_bg(slide, left, top, width, height, color):
    """Add a colored rectangle shape."""
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_textbox(slide, left, top, width, height, text, font_size=18,
                color=DARK_GRAY, bold=False, alignment=PP_ALIGN.LEFT, font_name="Calibri"):
    """Add a text box with formatted text."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.name = font_name
    p.alignment = alignment
    return tf


def add_bullet_list(tf, items, font_size=16, color=DARK_GRAY, bold_prefix=False, spacing=Pt(6)):
    """Add bullet items to a text frame."""
    for i, item in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.space_after = spacing
        p.font.size = Pt(font_size)

        if bold_prefix and ": " in item:
            prefix, rest = item.split(": ", 1)
            run1 = p.add_run()
            run1.text = "• " + prefix + ": "
            run1.font.size = Pt(font_size)
            run1.font.color.rgb = color
            run1.font.bold = True
            run1.font.name = "Calibri"
            run2 = p.add_run()
            run2.text = rest
            run2.font.size = Pt(font_size)
            run2.font.color.rgb = color
            run2.font.bold = False
            run2.font.name = "Calibri"
        else:
            p.text = "• " + item
            p.font.color.rgb = color
            p.font.name = "Calibri"


def section_header_bar(slide, text):
    """Add a colored header bar at the top of a content slide."""
    add_shape_bg(slide, Inches(0), Inches(0), SLIDE_W, Inches(1.1), DARK_BLUE)
    add_textbox(slide, Inches(0.8), Inches(0.2), Inches(11), Inches(0.7),
                text, font_size=32, color=WHITE, bold=True)


# ─── SLIDE 1: Title ───
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
add_bg(slide, DARK_BLUE)
add_shape_bg(slide, Inches(0), Inches(2.5), SLIDE_W, Inches(3.2), ACCENT_BLUE)

add_textbox(slide, Inches(1), Inches(0.6), Inches(11), Inches(0.6),
            "IoTeye Inc.", font_size=24, color=LIGHT_BLUE, bold=False)
add_textbox(slide, Inches(1), Inches(2.7), Inches(11), Inches(1.2),
            "Employee Engagement &\nRecognition Platform", font_size=44, color=WHITE, bold=True)
add_textbox(slide, Inches(1), Inches(4.2), Inches(11), Inches(0.5),
            "Proposal for The Arc Mercer", font_size=24, color=WHITE, bold=False)
add_textbox(slide, Inches(1), Inches(6.2), Inches(11), Inches(0.5),
            "March 2026  |  Basking Ridge, NJ  |  www.ioteyeinc.com", font_size=16, color=LIGHT_BLUE)


# ─── SLIDE 2: Agenda ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Agenda")

items = [
    "1.  About IoTeye Inc.",
    "2.  Understanding Your Challenge",
    "3.  Our Solution — Platform Overview",
    "4.  Key Features Deep Dive",
    "5.  Paycom Integration & SSO",
    "6.  Accessibility & Mobile-First Design",
    "7.  Phased Implementation Timeline",
    "8.  Pricing Options",
    "9.  Why IoTeye — Next Steps",
]
tf = add_textbox(slide, Inches(1.5), Inches(1.6), Inches(10), Inches(5),
                 "", font_size=22, color=DARK_GRAY)
for i, item in enumerate(items):
    if i == 0:
        p = tf.paragraphs[0]
    else:
        p = tf.add_paragraph()
    p.text = item
    p.font.size = Pt(22)
    p.font.color.rgb = DARK_GRAY
    p.font.name = "Calibri"
    p.space_after = Pt(10)


# ─── SLIDE 3: About IoTeye ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "About IoTeye Inc.")

add_textbox(slide, Inches(0.8), Inches(1.4), Inches(5.5), Inches(0.5),
            "Who We Are", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(0.8), Inches(2.0), Inches(5.5), Inches(4.5),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "Remote software company — Basking Ridge, NJ",
    "5+ years building special care software",
    "1,000+ consumers across our platforms",
    "Core domain: Special Care sector",
    "Full-stack SaaS expertise: design → deploy → support",
], font_size=16, spacing=Pt(10))

add_textbox(slide, Inches(7), Inches(1.4), Inches(5.5), Inches(0.5),
            "Our Products", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(7), Inches(2.0), Inches(5.8), Inches(4.8),
                 "", font_size=15, color=DARK_GRAY)
add_bullet_list(tf, [
    "SpringBoard: Multi-agency route management & operations platform (route optimization, fleet mgmt, Twilio SMS, multi-tenant)",
    "BrainBook: AI-powered platform with Next.js/React/TypeScript, Supabase auth, AI agents, voice I/O, desktop & web",
    "Guardian: Multi-agency notification system — SMS, push notifications, reply tracking, iOS & Android apps",
], font_size=15, bold_prefix=False, spacing=Pt(14))


# ─── SLIDE 4: Understanding the Challenge ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Understanding Your Challenge")

add_textbox(slide, Inches(0.8), Inches(1.4), Inches(11), Inches(0.5),
            "The Arc Mercer's Current State", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(0.8), Inches(2.1), Inches(5.5), Inches(4),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "Manual recognition processes — inconsistent, hard to track",
    "Multiple programs (Residential, Day Programs) operating in silos",
    "Frontline staff with varying technical literacy",
    "No centralized system for nominations or point tracking",
    "No connection to Paycom HRIS for employee data",
], font_size=16, spacing=Pt(10))

add_textbox(slide, Inches(7), Inches(1.4), Inches(5.5), Inches(0.5),
            "What You Need", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(7), Inches(2.1), Inches(5.5), Inches(4),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "Centralized, web-based recognition platform",
    "Program-based competition engine",
    "Multi-stream point system with audit trails",
    "Rewards marketplace for merchandise & gift cards",
    "Paycom integration & SSO",
    "Mobile-first, accessible to all staff",
], font_size=16, spacing=Pt(10))


# ─── SLIDE 5: Solution Overview ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Our Solution — Platform Overview")

add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11), Inches(0.5),
            "Custom-Built SaaS — Tailored for The Arc Mercer", font_size=22, color=ACCENT_BLUE, bold=True)

# Architecture layers
layers = [
    ("React + TypeScript PWA", "Mobile-first responsive design, offline capable", ACCENT_BLUE),
    ("Supabase (PostgreSQL)", "Auth, real-time subscriptions, Row Level Security", RGBColor(0x1A, 0x5C, 0x8A)),
    ("Python (FastAPI)", "Paycom SFTP sync, gift card APIs, scheduled jobs", RGBColor(0x14, 0x73, 0x5A)),
    ("AWS Cloud", "ECS Fargate, CloudFront, S3, WAF, CloudWatch", RGBColor(0xE6, 0x7E, 0x22)),
]

y_pos = Inches(2.0)
for label, desc, color in layers:
    shape = add_shape_bg(slide, Inches(1.5), y_pos, Inches(10), Inches(1.0), color)
    add_textbox(slide, Inches(2), y_pos + Inches(0.08), Inches(4), Inches(0.45),
                label, font_size=20, color=WHITE, bold=True)
    add_textbox(slide, Inches(2), y_pos + Inches(0.48), Inches(9), Inches(0.45),
                desc, font_size=14, color=WHITE)
    y_pos += Inches(1.15)

add_textbox(slide, Inches(0.8), Inches(6.5), Inches(11), Inches(0.5),
            "Security: AES-256 at rest  |  TLS 1.3 in transit  |  WCAG AAA  |  Full audit logging",
            font_size=14, color=MED_GRAY, alignment=PP_ALIGN.CENTER)


# ─── SLIDE 6: Nomination Engine ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Program-Based Competition Engine")

add_textbox(slide, Inches(0.8), Inches(1.4), Inches(5.5), Inches(0.5),
            "Nominations", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(0.8), Inches(2.0), Inches(5.5), Inches(4),
                 "", font_size=15, color=DARK_GRAY)
add_bullet_list(tf, [
    "3 award types: Employee of the Month, Rising Star, Team Impact",
    "Step-by-step guided form with large buttons",
    "Auto-populated nominee list by program",
    "Limit: 1 nomination per candidate/month, 5 total/month",
    "Friendly feedback when limits reached",
], font_size=15, spacing=Pt(10))

add_textbox(slide, Inches(7), Inches(1.4), Inches(5.5), Inches(0.5),
            "QA Queue & Programs", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(7), Inches(2.0), Inches(5.5), Inches(4),
                 "", font_size=15, color=DARK_GRAY)
add_bullet_list(tf, [
    "Admin dashboard: Approve / Return for Edits / Decline",
    "Points awarded only upon admin approval",
    "Batch operations for high-volume periods",
    "Filter by program, award type, date, status",
    "Hierarchical grouping: Residential → Group Homes, Day Programs → Campus, Senior, OTC, Janitorial",
    "Programs synced from Paycom automatically",
], font_size=15, spacing=Pt(10))


# ─── SLIDE 7: Points & Engagement ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Point Allocation & Engagement Tracking")

# Point streams table
add_textbox(slide, Inches(0.8), Inches(1.4), Inches(6), Inches(0.5),
            "Multi-Stream Point Accrual", font_size=22, color=ACCENT_BLUE, bold=True)

streams = [
    ("Point Stream", "Trigger"),
    ("Employee / Rising Star / Team Impact (Approved)", "QA queue approval"),
    ("TAC Meeting Attendance", "Admin check-in"),
    ("Newsletter Trivia", "Correct answer"),
    ("Birthday / Anniversary", "Automated (Paycom sync)"),
    ("Leadership Bestowal", "Manual award"),
]

y = Inches(2.0)
for i, (stream, trigger) in enumerate(streams):
    bg_color = ACCENT_BLUE if i == 0 else (LIGHT_GRAY if i % 2 == 0 else WHITE)
    txt_color = WHITE if i == 0 else DARK_GRAY
    add_shape_bg(slide, Inches(0.8), y, Inches(7), Inches(0.45), bg_color)
    add_textbox(slide, Inches(0.9), y + Inches(0.02), Inches(4.5), Inches(0.4),
                stream, font_size=13, color=txt_color, bold=(i == 0))
    add_textbox(slide, Inches(5.5), y + Inches(0.02), Inches(2.2), Inches(0.4),
                trigger, font_size=13, color=txt_color, bold=(i == 0))
    y += Inches(0.45)

add_textbox(slide, Inches(0.8), y + Inches(0.2), Inches(7), Inches(0.4),
            "All point values are admin-configurable — no code changes needed",
            font_size=14, color=GREEN, bold=True)

# Audit
add_textbox(slide, Inches(8.5), Inches(1.4), Inches(4.5), Inches(0.5),
            "Audit & Transparency", font_size=22, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(8.5), Inches(2.0), Inches(4.5), Inches(4),
                 "", font_size=15, color=DARK_GRAY)
add_bullet_list(tf, [
    "Immutable transaction log for every point change",
    "Timestamp, actor, action, amount, reason",
    "Filterable by employee, program, date, type",
    "Export to CSV for external review",
    "Anomaly highlighting for oversight",
    "Top-down bestowal with instant notifications",
], font_size=15, spacing=Pt(10))


# ─── SLIDE 8: Rewards Marketplace ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Rewards Marketplace")

add_textbox(slide, Inches(0.8), Inches(1.4), Inches(5.5), Inches(0.5),
            "Digital Storefront", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(0.8), Inches(2.0), Inches(5.5), Inches(4),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "Visual catalog with images, point costs, descriptions",
    "Categories: Branded Merchandise, Cafeteria Meals, Digital Gift Cards",
    "Real-time point balance displayed during browsing",
    "One-tap redemption with confirmation",
    "Order history for employees",
], font_size=16, spacing=Pt(10))

add_textbox(slide, Inches(7), Inches(1.4), Inches(5.5), Inches(0.5),
            "Admin Fulfillment Tools", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(7), Inches(2.0), Inches(5.5), Inches(4),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "Inventory management (add/edit items, stock levels)",
    "Low-stock alerts, out-of-stock auto-hiding",
    "Order queue: Pending → Processing → Fulfilled",
    "Employee notifications on status changes",
    "Digital gift card: API-based instant delivery",
    "Gift card fees: 3-5% vendor markup (pass-through)",
], font_size=16, spacing=Pt(10))


# ─── SLIDE 9: Paycom & SSO ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Paycom Integration & SSO")

add_textbox(slide, Inches(0.8), Inches(1.4), Inches(5.5), Inches(0.5),
            "Paycom HRIS Integration", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(0.8), Inches(2.0), Inches(5.5), Inches(2.5),
                 "", font_size=15, color=DARK_GRAY)
add_bullet_list(tf, [
    "Primary: SFTP nightly file export (CSV/XML)",
    "Python ETL service parses & syncs to Supabase",
    "Auto-provision new hires, deactivate terminations",
    "Sync: Employee ID, name, email, program, hire date, DOB",
    "Discrepancy reports flagged for HR review",
    "Optional: REST API enhancement (if subscription supports)",
], font_size=15, spacing=Pt(8))

# Architecture mini-diagram as text
add_shape_bg(slide, Inches(0.8), Inches(4.8), Inches(5.5), Inches(2.2), LIGHT_GRAY)
add_textbox(slide, Inches(1.0), Inches(4.9), Inches(5.2), Inches(2.0),
            "Paycom → SFTP Export → AWS S3 → Python ETL\n          ↓\n    Supabase (PostgreSQL)\n          ↓\n    React Front End (Live Data)",
            font_size=13, color=DARK_GRAY, font_name="Consolas")

add_textbox(slide, Inches(7), Inches(1.4), Inches(5.5), Inches(0.5),
            "Single Sign-On (SSO)", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(7), Inches(2.0), Inches(5.5), Inches(4.5),
                 "", font_size=15, color=DARK_GRAY)
add_bullet_list(tf, [
    "Supabase Auth: SAML 2.0, OAuth 2.0, OIDC",
    "Initial: Google Workspace SSO (current provider)",
    "Future: Microsoft Entra ID — zero-downtime migration",
    "Both providers can run in parallel during transition",
    "Fallback: email/password for part-time staff",
    "Employee clicks 'Sign In' → Google login → done",
], font_size=15, spacing=Pt(10))


# ─── SLIDE 10: Accessibility & UX ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Accessibility & Mobile-First Design")

add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11), Inches(0.5),
            'Design philosophy: "Could someone who only uses their phone for calls and texts do this?"',
            font_size=18, color=MED_GRAY, bold=True, alignment=PP_ALIGN.CENTER)

# Two columns
col1_items = [
    "Large touch targets: 48×48px minimum",
    "WCAG AAA contrast (7:1 ratio)",
    "Icon-driven navigation — not text-dependent",
    "6th grade reading level for all text",
    "Progressive disclosure — one action per screen",
    "Keyboard navigable, screen reader compatible",
]
col2_items = [
    "Progressive Web App (PWA) — no app store needed",
    "Works on any smartphone, 320px+ screens",
    "Low-bandwidth friendly, lazy-loaded images",
    "Bottom nav: Home, Nominate, Store, Points, Profile",
    "Touch-optimized: swipe, pull-to-refresh",
    "Accessibility audit before each phase launch",
]

add_textbox(slide, Inches(0.8), Inches(2.0), Inches(5.5), Inches(0.5),
            "Universal Design", font_size=22, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(0.8), Inches(2.6), Inches(5.5), Inches(4),
                 "", font_size=15, color=DARK_GRAY)
add_bullet_list(tf, col1_items, font_size=15, spacing=Pt(10))

add_textbox(slide, Inches(7), Inches(2.0), Inches(5.5), Inches(0.5),
            "Mobile-First PWA", font_size=22, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(7), Inches(2.6), Inches(5.5), Inches(4),
                 "", font_size=15, color=DARK_GRAY)
add_bullet_list(tf, col2_items, font_size=15, spacing=Pt(10))


# ─── SLIDE 11: Dashboards ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Dashboards — Employee & Leadership")

add_textbox(slide, Inches(0.8), Inches(1.4), Inches(5.5), Inches(0.5),
            "Employee Dashboard", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(0.8), Inches(2.0), Inches(5.5), Inches(4),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "Points balance — large, centered display",
    "Recent point activity feed",
    "Nomination status tracker",
    "\"Quick Nominate\" action button",
    "Birthday/Anniversary recognition feed",
], font_size=16, spacing=Pt(12))

add_textbox(slide, Inches(7), Inches(1.4), Inches(5.5), Inches(0.5),
            "Leadership Dashboard", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(7), Inches(2.0), Inches(5.5), Inches(4),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "Participation metrics by program",
    "Trend charts (weekly/monthly activity)",
    "QA queue status — pending nominations count",
    "Top nominators & nominees leaderboard",
    "Point economy: issued vs. redeemed",
], font_size=16, spacing=Pt(12))


# ─── SLIDE 12: Phased Timeline ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Phased Implementation — 26 Weeks")

phases = [
    ("Phase 1: Foundation", "Weeks 1–10", "Nominations, Paycom sync, SSO, manual points, QA queue",
     ACCENT_BLUE, Inches(1.5), Inches(4.8)),
    ("Phase 2: Engagement", "Weeks 11–18", "Employee & leadership dashboards, automated tracking, notifications",
     RGBColor(0x14, 0x73, 0x5A), Inches(5.3), Inches(3.5)),
    ("Phase 3: Marketplace", "Weeks 19–26", "Rewards store, gift card integration, fulfillment tools",
     ORANGE, Inches(8.8), Inches(3.5)),
]

y_base = Inches(2.0)
for label, weeks, desc, color, x_start, width in phases:
    # Timeline bar
    add_shape_bg(slide, x_start, y_base, width, Inches(0.6), color)
    add_textbox(slide, x_start + Inches(0.2), y_base + Inches(0.05), width - Inches(0.3), Inches(0.5),
                f"{label}  ({weeks})", font_size=16, color=WHITE, bold=True)
    y_base += Inches(0.8)

# Details below
y_detail = Inches(4.8)
details = [
    ("Phase 1 Deliverables", [
        "Nomination portal (3 award types)",
        "QA queue (approve/return/decline)",
        "Paycom SFTP sync",
        "Google Workspace SSO",
        "Manual point bestowal + audit trail",
    ], ACCENT_BLUE),
    ("Phase 2 Deliverables", [
        "Employee dashboards",
        "Leadership analytics",
        "Automated birthday/anniversary awards",
        "TAC attendance & trivia tracking",
        "Push/email notifications",
    ], RGBColor(0x14, 0x73, 0x5A)),
    ("Phase 3 Deliverables", [
        "Digital rewards storefront",
        "Physical & digital fulfillment",
        "Gift card instant delivery",
        "Inventory management",
        "Complete platform go-live",
    ], ORANGE),
]

x_pos = Inches(0.8)
for title, items, color in details:
    add_textbox(slide, x_pos, y_detail, Inches(3.8), Inches(0.4),
                title, font_size=16, color=color, bold=True)
    tf = add_textbox(slide, x_pos, y_detail + Inches(0.4), Inches(3.8), Inches(2.5),
                     "", font_size=13, color=DARK_GRAY)
    add_bullet_list(tf, items, font_size=13, spacing=Pt(4))
    x_pos += Inches(4.2)


# ─── SLIDE 13: Pricing — Option A ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Pricing — Option A: Source-Code Ownership")

add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11), Inches(0.5),
            "The Arc Mercer owns all source code, database, and IP",
            font_size=18, color=GREEN, bold=True)

# Implementation cost table
headers = [("Phase", Inches(4)), ("Hours", Inches(1.5)), ("Cost", Inches(1.5))]
rows_data = [
    ("Phase 1: Nominations, Paycom, SSO, Infrastructure", "~480 hrs", "$45,000"),
    ("Phase 2: Dashboards, Tracking, Notifications", "~310 hrs", "$30,000"),
    ("Phase 3: Marketplace, Gift Cards, Fulfillment", "~280 hrs", "$35,000"),
    ("Total Implementation", "~1,070 hrs", "$110,000"),
]

y = Inches(1.9)
x_base = Inches(1.5)
# Header row
for j, (h, w) in enumerate(headers):
    x = x_base + sum(hw[1] for hw in headers[:j])
    add_shape_bg(slide, x, y, w, Inches(0.45), ACCENT_BLUE)
    add_textbox(slide, x + Inches(0.1), y + Inches(0.02), w - Inches(0.2), Inches(0.4),
                h, font_size=14, color=WHITE, bold=True)
y += Inches(0.45)

for i, (phase, hours, cost) in enumerate(rows_data):
    bg = LIGHT_GRAY if i % 2 == 0 else WHITE
    is_total = (i == len(rows_data) - 1)
    for j, (val, w) in enumerate(zip([phase, hours, cost], [h[1] for h in headers])):
        x = x_base + sum(hw[1] for hw in headers[:j])
        add_shape_bg(slide, x, y, w, Inches(0.45), DARK_BLUE if is_total else bg)
        add_textbox(slide, x + Inches(0.1), y + Inches(0.02), w - Inches(0.2), Inches(0.4),
                    val, font_size=13, color=WHITE if is_total else DARK_GRAY, bold=is_total)
    y += Inches(0.45)

add_textbox(slide, Inches(1.5), y + Inches(0.1), Inches(7), Inches(0.4),
            "Blended rate: ~$103/hr — well below $150-250/hr industry standard",
            font_size=14, color=GREEN, bold=True)

# Annual costs
add_textbox(slide, Inches(8.5), Inches(1.9), Inches(4.5), Inches(0.5),
            "Annual Recurring", font_size=20, color=ACCENT_BLUE, bold=True)
annual_items = [
    "AWS hosting/CDN/monitoring: $6,000",
    "Supabase Pro Plan: $3,000",
    "SSL & domain: $200",
    "Maintenance & support: $12,000",
    "Total annual: $21,200/year",
]
tf = add_textbox(slide, Inches(8.5), Inches(2.5), Inches(4.5), Inches(3),
                 "", font_size=14, color=DARK_GRAY)
add_bullet_list(tf, annual_items, font_size=14, spacing=Pt(8))

add_shape_bg(slide, Inches(8.5), Inches(5.0), Inches(4), Inches(1.2), LIGHT_BLUE)
add_textbox(slide, Inches(8.7), Inches(5.1), Inches(3.6), Inches(0.4),
            "Year 1 Total: $131,200", font_size=18, color=DARK_BLUE, bold=True)
add_textbox(slide, Inches(8.7), Inches(5.5), Inches(3.6), Inches(0.4),
            "Year 2+: $21,200/year", font_size=18, color=DARK_BLUE, bold=True)


# ─── SLIDE 14: Pricing — Option B ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, WHITE)
section_header_bar(slide, "Pricing — Option B: IoTeye-Hosted SaaS")

add_textbox(slide, Inches(0.8), Inches(1.3), Inches(11), Inches(0.5),
            "No upfront cost — IoTeye retains platform ownership & offers managed service",
            font_size=18, color=GREEN, bold=True)

# Option B details
add_shape_bg(slide, Inches(1.5), Inches(2.0), Inches(4.5), Inches(2.5), LIGHT_BLUE)
add_textbox(slide, Inches(1.7), Inches(2.1), Inches(4), Inches(0.5),
            "Pricing", font_size=22, color=DARK_BLUE, bold=True)
tf = add_textbox(slide, Inches(1.7), Inches(2.7), Inches(4), Inches(1.8),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "Implementation fee: $0",
    "Monthly subscription: $2,500/month",
    "Annual total: $30,000/year",
    "Minimum commitment: 3-year term",
], font_size=16, spacing=Pt(10))

add_shape_bg(slide, Inches(7), Inches(2.0), Inches(5), Inches(2.5), LIGHT_GRAY)
add_textbox(slide, Inches(7.2), Inches(2.1), Inches(4.5), Inches(0.5),
            "What's Included", font_size=22, color=DARK_BLUE, bold=True)
tf = add_textbox(slide, Inches(7.2), Inches(2.7), Inches(4.5), Inches(1.8),
                 "", font_size=16, color=DARK_GRAY)
add_bullet_list(tf, [
    "All 3 phases (same 26-week timeline)",
    "Hosting, maintenance, security updates",
    "Ongoing support & platform updates",
    "No per-user fees",
], font_size=16, spacing=Pt(10))

# Comparison table
add_textbox(slide, Inches(0.8), Inches(4.8), Inches(11), Inches(0.5),
            "Option A vs. Option B — Cost Comparison", font_size=20, color=DARK_BLUE, bold=True)

comp_headers = [("", Inches(2.5)), ("Option A (Own Code)", Inches(3.5)), ("Option B (SaaS)", Inches(3.5))]
comp_rows = [
    ("Upfront Cost", "$110,000", "$0"),
    ("Annual Cost", "$21,200/year", "$30,000/year"),
    ("3-Year Total", "$173,600", "$90,000"),
    ("5-Year Total", "$216,000", "$150,000"),
    ("Code Ownership", "Yes — you own it", "No — IoTeye retains"),
]

y = Inches(5.3)
x_base = Inches(1.8)
for j, (h, w) in enumerate(comp_headers):
    x = x_base + sum(hw[1] for hw in comp_headers[:j])
    add_shape_bg(slide, x, y, w, Inches(0.4), ACCENT_BLUE)
    add_textbox(slide, x + Inches(0.1), y + Inches(0.02), w - Inches(0.2), Inches(0.35),
                h, font_size=13, color=WHITE, bold=True)
y += Inches(0.4)

for i, (label, a, b) in enumerate(comp_rows):
    bg = LIGHT_GRAY if i % 2 == 0 else WHITE
    for j, (val, w) in enumerate(zip([label, a, b], [h[1] for h in comp_headers])):
        x = x_base + sum(hw[1] for hw in comp_headers[:j])
        add_shape_bg(slide, x, y, w, Inches(0.35), bg)
        add_textbox(slide, x + Inches(0.1), y + Inches(0.01), w - Inches(0.2), Inches(0.3),
                    val, font_size=12, color=DARK_GRAY, bold=(j == 0))
    y += Inches(0.35)


# ─── SLIDE 15: Why IoTeye & Next Steps ───
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, DARK_BLUE)

add_textbox(slide, Inches(0.8), Inches(0.5), Inches(11), Inches(0.7),
            "Why IoTeye — Next Steps", font_size=36, color=WHITE, bold=True)

add_textbox(slide, Inches(0.8), Inches(1.5), Inches(5.5), Inches(0.5),
            "Why We're the Right Partner", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(0.8), Inches(2.1), Inches(5.5), Inches(4),
                 "", font_size=16, color=WHITE)
add_bullet_list(tf, [
    "5+ years in special care software — we know your workforce",
    "Arc Mercer is already a SpringBoard customer",
    "Production platforms: SpringBoard, BrainBook, Guardian",
    "Same tech stack (React, Supabase, Python, AWS) — proven",
    "Mobile-first, accessible design as a core competency",
    "No per-user fees — scales with your organization",
    "Flexible pricing: own the code or pay-as-you-go SaaS",
], font_size=16, color=WHITE, spacing=Pt(10))

add_textbox(slide, Inches(7), Inches(1.5), Inches(5.5), Inches(0.5),
            "Next Steps", font_size=24, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, Inches(7), Inches(2.1), Inches(5.5), Inches(3),
                 "", font_size=16, color=WHITE)
add_bullet_list(tf, [
    "Select pricing option (A or B)",
    "Schedule kickoff & discovery workshop",
    "Initiate Paycom SFTP access setup",
    "Configure Google Workspace SSO",
    "Phase One live in 10 weeks",
], font_size=16, color=WHITE, spacing=Pt(12))

# Contact box
add_shape_bg(slide, Inches(7), Inches(4.8), Inches(5), Inches(2), ACCENT_BLUE)
add_textbox(slide, Inches(7.3), Inches(4.9), Inches(4.5), Inches(0.5),
            "Contact Us", font_size=22, color=WHITE, bold=True)
add_textbox(slide, Inches(7.3), Inches(5.4), Inches(4.5), Inches(1.2),
            "IoTeye Inc.\nBasking Ridge, New Jersey\nmingjye.sheng@ioteyeinc.com\nwww.ioteyeinc.com",
            font_size=16, color=WHITE)

# Thank you
add_textbox(slide, Inches(0.8), Inches(6.2), Inches(5), Inches(0.8),
            "Thank You", font_size=40, color=WHITE, bold=True)


# Save
output_path = r"c:\Users\mingj\Documents\GitHub\sb_rewards\RFP\IoTeye - Arc Mercer Pitch.pptx"
prs.save(output_path)
print(f"Saved: {output_path}")
