# Proposal: Employee Engagement & Recognition Platform

**Prepared for:** The Arc Mercer  
**Prepared by:** IoTeye Inc.  
**Date:** March 22, 2026  
**In Response To:** Request for Proposal — Employee Engagement & Recognition Platform (February 2026)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Company Profile](#2-company-profile)
3. [Technical Approach](#3-technical-approach)
4. [Scope of Work & Solution Design](#4-scope-of-work--solution-design)
5. [Integration Strategy](#5-integration-strategy)
6. [Accessibility Statement](#6-accessibility-statement)
7. [Phased Implementation Plan & Timeline](#7-phased-implementation-plan--timeline)
8. [Cost Proposal](#8-cost-proposal)
9. [Evaluation Criteria Alignment](#9-evaluation-criteria-alignment)
10. [Appendices](#10-appendices)

---

## 1. Executive Summary

We are pleased to submit this proposal in response to The Arc Mercer's Request for Proposal for an Employee Engagement & Recognition Platform. We understand the critical importance of transitioning from manual recognition processes to a structured, scalable system that fosters a culture of appreciation across your residential and day programs.

Our proposed solution is a custom-built, cloud-hosted SaaS platform leveraging modern, battle-tested technologies — **React** and **TypeScript** for the front end, **Supabase** (PostgreSQL) for the backend and real-time data layer, **Python** for integrations and business logic services, and **AWS** for secure, scalable cloud deployment. This technology stack delivers a high-quality, maintainable, and cost-effective platform tailored precisely to The Arc Mercer's unique requirements.

**Key Differentiators:**

- **Custom-Built for Your Workforce:** Unlike off-the-shelf platforms, our solution is designed from the ground up for non-technical, frontline staff — large buttons, intuitive icons, minimal text, and mobile-first design.
- **Seamless Paycom Integration:** A dedicated Python integration service ensures reliable, automated user provisioning and program assignment syncing with your HRIS.
- **Phased Delivery with Early Value:** Phase One goes live within 10 weeks of kickoff, delivering nominations, Paycom sync, and manual point support immediately.
- **Transparent & Auditable:** Every point adjustment is logged with full audit trails, giving leadership complete visibility and control.
- **Scalable SaaS Architecture:** AWS-hosted infrastructure scales with your organization and ensures 99.9% uptime.

---

## 2. Company Profile

### About IoTeye Inc.

**IoTeye Inc.** is a remote software products company headquartered in **Basking Ridge, New Jersey**. For over **5 years**, IoTeye has been building and delivering high-quality software products and tools — with a particular focus on the **special care** sector. Over **1,000 consumers** trust IoTeye's platforms today.

**Website:** [www.ioteyeinc.com](https://www.ioteyeinc.com)  
**Contact:** sale@ioteyeinc.com

### Solutions & Services

IoTeye's portfolio spans multiple domains directly relevant to The Arc Mercer's mission:

| Area | Description |
|---|---|
| **Special Care** | Purpose-built tools for organizations serving individuals with specialized care needs — IoTeye's core domain and the foundation of our understanding of your workforce. |
| **ERP Services** | Enterprise resource planning solutions for operational management, demonstrating our capacity to build complex, data-driven business systems. |
| **Route Optimization** | Intelligent routing solutions — our flagship product — showcasing expertise in real-time data processing and optimization algorithms. |
| **Communication Studio** | Communication and engagement tools, directly transferable to employee recognition and notification systems. |
| **Class Attendance & Contact Tracing** | Attendance tracking and people-management systems, demonstrating experience with check-in workflows and activity logging similar to the TAC meeting and engagement tracking required in this RFP. |

### Products

- **SpringBoard** — IoTeye's SaaS platform serving care organizations, built with modern web technologies and deployed on cloud infrastructure.
- **BrainBook** — An integrated learning and collaboration platform, demonstrating IoTeye's experience building user-facing web applications at scale.

### Why IoTeye for This Project

IoTeye's **special care industry expertise** is a direct match for The Arc Mercer's needs. Unlike general-purpose software vendors, IoTeye understands:

- **The frontline workforce** — direct-care professionals who primarily use smartphones and need simple, intuitive interfaces.
- **Compliance and auditability** — regulated care environments require transparent, traceable systems with full audit trails.
- **Budget-conscious operations** — non-profit organizations need maximum ROI with sustainable long-term costs.
- **User diversity** — designing for staff with varying levels of technical literacy is a core competency, not an afterthought.

Having built and operated SaaS products like SpringBoard and BrainBook, IoTeye brings proven experience in the full lifecycle: design, development, cloud deployment, and ongoing support.

### Technology Stack Proficiency

| Technology | Role in This Project | IoTeye Experience |
|---|---|---|
| **React + TypeScript** | Front-end application | Production SaaS applications (SpringBoard, BrainBook) serving 1,000+ users; component-based architecture for maintainability |
| **Supabase (PostgreSQL)** | Database, authentication, real-time subscriptions | Production deployments leveraging Row Level Security, real-time listeners, and built-in auth |
| **Python** | Integration services, business logic, automation | Extensive experience building API integrations, ETL pipelines, and scheduled jobs across IoTeye's product suite |
| **AWS** | Cloud infrastructure & deployment | Production SaaS deployments using ECS/Fargate, RDS, S3, CloudFront, and Lambda — powering IoTeye's live products |

### Commitment to The Arc Mercer's Mission

As a company whose core business is **special care software**, IoTeye deeply understands The Arc Mercer's mission of supporting individuals with intellectual and developmental disabilities. An employee recognition platform directly supports staff retention and morale — critical factors in maintaining quality of care. IoTeye's approach prioritizes simplicity, accessibility, and sustainability to ensure this platform delivers lasting value for your organization and the people it serves.

---

## 3. Technical Approach

### 3.1 Architecture Overview: Custom SaaS Build

We recommend a **custom-built SaaS solution** rather than an off-the-shelf product. This approach ensures The Arc Mercer receives a platform precisely tailored to its workflows, terminology, and organizational structure — without paying for features you don't need or compromising on ones you do.

```
┌─────────────────────────────────────────────────────────┐
│                    Client Layer                         │
│   React + TypeScript Progressive Web App (PWA)          │
│   Mobile-First Responsive Design                        │
│   Offline Capability for Low-Connectivity Environments  │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTPS
┌──────────────────────▼──────────────────────────────────┐
│                  API / Backend Layer                     │
│   Supabase (PostgreSQL + PostgREST + Auth + Realtime)   │
│   Row Level Security (RLS) for Data Access Control      │
│   Edge Functions for Business Logic                     │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│              Integration Services Layer                  │
│   Python Microservice (FastAPI)                          │
│   • Paycom HRIS Sync (API / SFTP)                       │
│   • Gift Card Vendor API Integration                    │
│   • Scheduled Jobs (Birthdays, Anniversaries)           │
│   • Notification Service (Email / Push)                 │
└──────────────────────┬──────────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────────┐
│                 AWS Infrastructure                       │
│   ECS Fargate (Containers) │ CloudFront (CDN)           │
│   S3 (Static Assets)       │ RDS (if needed)            │
│   Secrets Manager          │ CloudWatch (Monitoring)    │
│   WAF (Security)           │ Route 53 (DNS)             │
└─────────────────────────────────────────────────────────┘
```

### 3.2 Technology Selection Rationale

| Component | Technology | Why |
|---|---|---|
| **Front End** | React + TypeScript | Type-safe, component-based UI. Massive ecosystem for accessibility components. Progressive Web App (PWA) support for native-like mobile experience without app store distribution. |
| **Backend & Database** | Supabase (PostgreSQL) | Instant API generation, built-in authentication (supports SSO), Row Level Security for data isolation, real-time subscriptions for live dashboards, and managed infrastructure reducing operational burden. |
| **Integration Layer** | Python (FastAPI) | Best-in-class library ecosystem for HRIS integrations (SFTP, REST APIs, CSV parsing). Easy to maintain and extend for future integrations. |
| **Cloud Platform** | AWS | HIPAA-eligible infrastructure, SOC 2 compliance, auto-scaling, and 99.99% availability SLA. |

### 3.3 Security & Compliance

- **Data Encryption:** AES-256 encryption at rest; TLS 1.3 in transit.
- **Authentication:** Supabase Auth with support for SSO (SAML 2.0 / OAuth 2.0) — enabling employees to log in with existing organizational credentials.
- **Authorization:** Row Level Security (RLS) policies ensure employees only access their own data; admins and leadership access scoped to their programs.
- **Audit Logging:** Every point transaction, nomination action, and admin operation is logged with timestamp, actor, and action detail — immutable and queryable.
- **Infrastructure Security:** AWS WAF for web application firewall protection, VPC isolation, and secrets management via AWS Secrets Manager.

---

## 4. Scope of Work & Solution Design

### A. Program-Based Competition Engine

**Hierarchical Grouping:**
- Flexible program hierarchy supporting multi-level groupings (e.g., Residential → Group Homes; Day Programs → Campus, Senior, OTC, Janitorial).
- Programs are synced from Paycom to ensure employee-program assignments are always current.
- Admin UI to create, edit, and archive programs as organizational structure evolves.

**Nomination Workflow:**
- Intuitive submission portal with large, clearly labeled buttons for each award type:
  - 🏆 **Employee of the Month**
  - ⭐ **Rising Star**
  - 👥 **Team Impact Award**
- Step-by-step guided form: select nominee → select award type → write nomination statement → submit.
- Auto-populated nominee list filtered by program, with search functionality.

**Submission Logic:**
- Enforced business rules at the database level:
  - Maximum **1 nomination per candidate per month** per user.
  - Maximum **5 total nominations per month** per user.
- Clear, friendly UI feedback when limits are reached (e.g., "You've already nominated this person this month — thank you for your enthusiasm!").
- Monthly counters reset automatically on the 1st of each month.

**QA Queue (Administrative Dashboard):**
- Dedicated admin view showing all pending nominations with:
  - Nominee name, nominator, award type, program, and nomination text.
  - One-click actions: **Approve**, **Return for Edits** (with comment field), or **Decline** (with reason).
- Batch operations for high-volume periods.
- Filter and sort by program, award type, date, and status.
- Points are only awarded upon admin approval — never automatically on submission.

### B. Point Allocation & Engagement Tracking

**Top-Down Bestowal:**
- Leadership and authorized managers can instantly award ad-hoc points from a dedicated "Bestow Points" interface.
- Requires selection of recipient, point amount, and reason/category.
- Bestowed points appear immediately on the employee's dashboard with a recognition notification.

**Multi-Stream Accrual:**
Points are earned through multiple configurable streams:

| Stream | Point Value | Trigger |
|---|---|---|
| Employee of the Month (Approved) | Configurable by admin | QA queue approval |
| Rising Star of the Month (Approved) | Configurable by admin | QA queue approval |
| Team Impact Award (Approved) | Configurable by admin | QA queue approval |
| TAC Meeting Attendance | Configurable by admin | Admin check-in or attendance import |
| Newsletter Trivia | Configurable by admin | Correct answer submission |
| Birthday Milestone | Configurable by admin | Automated (Paycom DOB sync) |
| Work Anniversary Milestone | Configurable by admin | Automated (Paycom hire date sync) |
| Leadership Bestowal | Variable | Manual award by leadership |

- All point values are administrator-configurable — no code changes needed to adjust values.
- Milestone points (birthdays, anniversaries) are triggered automatically via scheduled jobs synced with Paycom data.

**Audit Trails:**
- Complete, immutable transaction log for every point adjustment:
  - **Fields:** Timestamp, employee, action type (earned/redeemed/adjusted/voided), point amount, source/reason, performed by.
- Admin reporting dashboard with:
  - Filterable transaction history by employee, program, date range, and type.
  - Export to CSV for external review.
  - Anomaly highlighting (e.g., unusually large bestowals).

### C. The Rewards Marketplace

**Digital Storefront:**
- Clean, visual catalog displaying available rewards with images, point costs, and descriptions.
- Categories: **Branded Merchandise**, **Cafeteria Meals**, **Digital Gift Cards**.
- Real-time point balance displayed prominently during browsing.
- One-tap redemption with confirmation dialog to prevent accidental spending.
- Order history view for employees.

**Fulfillment Tools:**
- Admin inventory management dashboard:
  - Add/edit/remove items with images, descriptions, point costs, and stock quantities.
  - Low-stock alerts and out-of-stock auto-hiding.
- Order fulfillment queue:
  - New orders appear in real-time.
  - Status tracking: **Pending → Processing → Fulfilled / Shipped**.
  - Employee notification on status changes.
- Digital gift card integration:
  - API-based delivery for instant digital gift card fulfillment (e.g., via a vendor such as Tango Card or similar).
  - Automated delivery via email with tracking.

### D. User Experience (UX) & Accessibility

**Universal Design Principles:**
- **Large touch targets:** Minimum 48x48px tap areas (exceeding WCAG 2.1 AA requirements).
- **High-contrast interface:** WCAG AAA contrast ratios (7:1) for all text and interactive elements.
- **Icon-driven navigation:** Every action has an accompanying icon — users never rely solely on text labels.
- **Minimal text-heavy menus:** Bottom navigation bar with 4-5 core actions (Home, Nominate, Store, My Points, Profile).
- **Progressive disclosure:** Complex features are behind simple entry points, avoiding information overload.
- **Reading level:** All interface text written at a 6th-grade reading level or below.

**Mobile-First Design:**
- **Progressive Web App (PWA):** Installable on any smartphone home screen without app store download — no high-end hardware required.
- **Responsive layout:** Designed for 320px+ screens, scaling gracefully to tablets and desktops.
- **Touch-optimized:** Swipe gestures, pull-to-refresh, and haptic-style feedback.
- **Low-bandwidth friendly:** Lazy-loaded images, compressed assets, and optional offline mode for unreliable connectivity.

**Dashboards:**

*Employee Dashboard:*
- Points balance (large, centered display).
- Recent point activity feed.
- Nomination status tracker.
- "Quick Nominate" action button.
- Birthday/Anniversary recognition feed.

*Leadership Dashboard:*
- Participation metrics by program (nomination counts, engagement rates).
- Trend charts (weekly/monthly activity).
- QA queue status (pending nominations count).
- Top nominators and nominees leaderboard.
- Point economy overview (points issued vs. redeemed).

---

## 5. Integration Strategy

### 5.1 Paycom Integration (Critical)

We propose a **dual-channel integration approach** to ensure maximum reliability:

**Primary: Paycom API Integration (REST)**
- Real-time or near-real-time user provisioning via Paycom's REST API.
- **Automated User Provisioning:**
  - New hires synced within 24 hours of Paycom entry.
  - Terminated employees automatically deactivated (soft delete — data retained for audit).
  - Role/program changes reflected automatically.
- **Data Fields Synced:** Employee ID, name, email, program/department assignment, hire date, date of birth, employment status.
- **Sync Schedule:** Nightly full sync + event-driven incremental sync (if Paycom webhooks are available).

**Fallback: SFTP File Transfer**
- If API access is limited or during initial implementation, we support Paycom's standard SFTP export:
  - Nightly CSV/XML file drop to a secure AWS S3 bucket.
  - Python ETL service parses, validates, and upserts employee records.
  - Discrepancy reports generated for HR review.

**Integration Architecture:**
```
Paycom HRIS
    │
    ├── REST API ──────► Python Integration Service (FastAPI)
    │                         │
    └── SFTP Export ──► S3 ──►│
                              │
                              ▼
                    Supabase (PostgreSQL)
                     Employee Records Table
                              │
                              ▼
                    React Front End (Live Data)
```

**Error Handling & Monitoring:**
- Retry logic with exponential backoff for API failures.
- Admin notifications for sync errors or data discrepancies.
- Monthly sync health reports.

### 5.2 Single Sign-On (SSO)

- **Supabase Auth** natively supports SAML 2.0 and OAuth 2.0 / OIDC.
- We will configure SSO to work with The Arc Mercer's existing identity provider (e.g., Microsoft Entra ID / Azure AD, Google Workspace, or Okta).
- **Employee experience:** Click "Sign In" → redirect to familiar organizational login → automatically authenticated and returned to the platform.
- **Fallback:** Email/password login for users without SSO credentials (e.g., part-time or seasonal staff), with secure password policies enforced.

---

## 6. Accessibility Statement

Our commitment to accessibility is central to this project, given The Arc Mercer's diverse workforce:

### Design Philosophy
We design for the **least technically experienced user first**. Every interface decision is validated against the question: *"Could a person who only uses their phone for calls and texts successfully complete this action?"*

### Specific Accommodations

| Challenge | Our Solution |
|---|---|
| Low technical literacy | Icon-based navigation, step-by-step guided flows, no jargon |
| Small screen / older phones | Mobile-first PWA, works on any modern browser, no app download required |
| Low vision / contrast needs | WCAG AAA contrast ratios, large fonts (min 16px body text), resizable text |
| Motor difficulties | Large touch targets (48x48px minimum), generous spacing between actions |
| Cognitive load | Progressive disclosure, one primary action per screen, clear success/error messaging |
| Language diversity | Simple language (6th grade level), icon-first design reduces language dependency |

### Standards Compliance
- **WCAG 2.1 Level AA** compliance — with AAA targets for contrast and text sizing.
- **Keyboard navigable** — full functionality available without a mouse.
- **Screen reader compatible** — semantic HTML, ARIA labels, and tested with NVDA/VoiceOver.

### Ongoing Accessibility
- User testing with frontline staff during each phase.
- Accessibility audit before each phase launch.
- Feedback mechanism built into the app for reporting usability issues.

---

## 7. Phased Implementation Plan & Timeline

### Phase One: Foundation (Weeks 1–10)
> *Centralized nominations, Paycom sync, and manual point support*

| Week | Milestone |
|---|---|
| 1–2 | **Kickoff & Discovery** — Requirements workshops with stakeholders, Paycom API access setup, environment provisioning |
| 3–4 | **Core Infrastructure** — AWS deployment pipeline, Supabase schema design, authentication/SSO configuration, Paycom integration development |
| 5–7 | **Nomination Engine** — Submission portal, QA queue, program hierarchy, nomination business rules |
| 7–8 | **Point System (Manual)** — Admin point bestowal, point balance views, audit trail, leadership dashboard |
| 9 | **User Acceptance Testing (UAT)** — Testing with selected staff across programs, accessibility audit |
| 10 | **Phase One Launch** — Production deployment, staff onboarding, admin training |

**Phase One Deliverables:**
- Nomination submission portal (Employee of the Month, Rising Star, Team Impact)
- QA queue with approve/return/decline workflow
- Paycom user sync (automated provisioning)
- SSO login
- Manual point bestowal by leadership
- Basic point balance display
- Admin audit trail

### Phase Two: Engagement (Weeks 11–18)
> *Individual dashboards and automated activity tracking*

| Week | Milestone |
|---|---|
| 11–12 | **Employee Dashboards** — Personalized point history, nomination tracker, activity feed |
| 13–14 | **Leadership Dashboards** — Participation metrics, trend charts, program comparisons |
| 15–16 | **Automated Tracking** — TAC meeting attendance logging, newsletter trivia module, birthday/anniversary automation |
| 17 | **UAT & Refinement** — User testing, performance optimization |
| 18 | **Phase Two Launch** — Feature rollout, updated training materials |

**Phase Two Deliverables:**
- Full employee dashboards with point history and progress
- Leadership analytics dashboards with trends
- Automated birthday and anniversary point awards
- TAC meeting attendance tracking
- Newsletter trivia integration
- Push/email notifications

### Phase Three: Marketplace (Weeks 19–26)
> *Full Store activation and fulfillment workflows*

| Week | Milestone |
|---|---|
| 19–20 | **Storefront Development** — Product catalog, category browsing, point-based checkout |
| 21–22 | **Fulfillment System** — Order management, status tracking, admin inventory tools |
| 23–24 | **Gift Card Integration** — Vendor API integration, automated digital delivery |
| 25 | **UAT & Load Testing** — End-to-end testing, security audit |
| 26 | **Phase Three Launch & Full Platform Go-Live** |

**Phase Three Deliverables:**
- Digital rewards storefront
- Physical merchandise ordering and fulfillment tracking
- Digital gift card instant delivery
- Inventory management tools
- Complete platform with all features active

### Overall Timeline Summary

```
Month 1–2:  ████████████ Phase One (Foundation)
Month 3–4:  ░░░░░░░░████████████ Phase Two (Engagement)  
Month 5–6:  ░░░░░░░░░░░░░░░░████████████ Phase Three (Marketplace)
```

**Total Duration: ~26 weeks (6.5 months) from kickoff to full launch.**

---

## 8. Cost Proposal

We offer two pricing options to accommodate different budget and ownership preferences:

---

### Option A: Source-Code Ownership (Custom Build)

Under this option, The Arc Mercer **owns the source code and all intellectual property**. IoTeye delivers the platform, and The Arc Mercer retains full control to modify, extend, or migrate the system independently in the future.

#### 8.1 Implementation Fees (One-Time)

| Phase | Description | Est. Hours | Cost |
|---|---|---|---|
| Phase One | Nominations, Paycom Sync, Manual Points, SSO, Core Infrastructure | ~480 hrs | $45,000 |
| Phase Two | Dashboards, Automated Tracking, Notifications | ~310 hrs | $30,000 |
| Phase Three | Rewards Marketplace, Gift Card Integration, Fulfillment | ~280 hrs | $35,000 |
| **Total Implementation** | | **~1,070 hrs** | **$110,000** |

*Includes: discovery, design, development, testing, deployment, training, and documentation.*

**Detailed Effort Breakdown:**

**Phase One — $45,000 (~480 hours, Weeks 1–10)**

| Task | Hours |
|---|---|
| Discovery & requirements workshops | ~40 |
| AWS infrastructure setup (ECS, CloudFront, CI/CD pipeline) | ~40 |
| Supabase schema design, RLS policies, auth/SSO configuration | ~40 |
| Paycom integration service (API + SFTP fallback, error handling, monitoring) | ~80 |
| Nomination engine (submission portal, business rules, guided flows) | ~80 |
| QA queue (admin dashboard, approve/return/decline workflow) | ~60 |
| Manual point bestowal + audit trail | ~40 |
| UI/UX design (mobile-first, WCAG AAA, icon-driven, accessibility) | ~60 |
| UAT, accessibility audit, deployment, staff training | ~40 |

**Phase Two — $30,000 (~310 hours, Weeks 11–18)**

| Task | Hours |
|---|---|
| Employee dashboards (point history, nomination tracker, activity feed) | ~80 |
| Leadership dashboards (analytics, trend charts, program comparisons) | ~80 |
| Automated tracking (attendance, trivia, birthday/anniversary jobs) | ~80 |
| Notification system (push + email) | ~40 |
| UAT & refinement | ~30 |

**Phase Three — $35,000 (~280 hours, Weeks 19–26)**

| Task | Hours |
|---|---|
| Rewards storefront (catalog, browsing, point-based checkout) | ~80 |
| Fulfillment system (order queue, status tracking, inventory management) | ~80 |
| Gift card vendor API integration + automated delivery | ~60 |
| Load testing, security audit, final deployment | ~40 |
| Documentation & admin training | ~20 |

> **Blended rate: ~$103/hr** across ~1,070 hours — well below the $150–$250/hr industry standard for custom SaaS development.

#### 8.2 Annual Licensing & Hosting (Recurring)

| Item | Annual Cost |
|---|---|
| AWS Infrastructure (hosting, CDN, storage, monitoring) | $6,000 |
| Supabase Pro Plan (database, auth, real-time) | $3,000 |
| SSL Certificates & Domain Management | $200 |
| Maintenance & Support (bug fixes, security patches, minor updates) | $12,000 |
| **Total Annual Cost** | **$21,200/year** |

#### Option A Cost Summary

| Category | Year 1 | Year 2+ |
|---|---|---|
| Implementation | $110,000 | — |
| Annual Licensing & Hosting | $21,200 | $21,200 |
| **Total** | **$131,200** | **$21,200/year** |

**What you own:** Full source code, database schema, deployment infrastructure, and all IP. The Arc Mercer can self-host, bring in other developers, or modify the platform without restriction after delivery.

---

### Option B: IoTeye-Hosted SaaS (No Implementation Fee)

Under this option, **IoTeye Inc. retains ownership of the platform and source code** and operates it as a managed SaaS service. The Arc Mercer pays no upfront implementation fee — instead, IoTeye recoups development costs through a monthly subscription. IoTeye may offer the platform to other organizations in the future.

#### Pricing

| Item | Monthly Cost | Annual Cost |
|---|---|---|
| Platform Subscription (all features, all phases) | $2,500/month | $30,000/year |
| Hosting, maintenance, security updates, and support | Included | Included |
| **Total** | **$2,500/month** | **$30,000/year** |

- **No implementation fee.** IoTeye absorbs the full development cost.
- **Minimum commitment:** 3-year initial term, renewing annually thereafter.
- **Includes:** All three phases delivered on the same timeline (26 weeks), plus ongoing hosting, maintenance, support, and security updates.

#### Option B Cost Summary

| Category | Annual Cost |
|---|---|
| Implementation Fee | $0 |
| Platform Subscription (includes hosting, maintenance, support) | $30,000/year |
| **Total** | **$30,000/year** |

**What you get:** Fully managed platform with no upfront cost, ongoing updates, and support. IoTeye handles all infrastructure, security, and maintenance.

**What IoTeye retains:** Source code ownership and the right to offer the platform (excluding The Arc Mercer's data) to other organizations.

---

### Option A vs. Option B Comparison

| Factor | Option A (Source Ownership) | Option B (IoTeye SaaS) |
|---|---|---|
| Upfront Cost | \$110,000 | \$0 |
| Annual Cost | \$21,200/year | \$30,000/year |
| 3-Year Total Cost | \$173,600 | \$90,000 |
| 5-Year Total Cost | \$216,000 | \$150,000 |
| 10-Year Total Cost | \$322,000 | \$300,000 |
| Source Code Ownership | ✅ The Arc Mercer owns all code | ❌ IoTeye retains ownership |
| Vendor Independence | ✅ Can self-host or hire other devs | ❌ Dependent on IoTeye |
| Customization Freedom | ✅ Unlimited modifications | ⚠️ Customizations by request |
| Platform Updates | ⚠️ Paid separately | ✅ Included in subscription |
| Best For | Long-term control & independence | Lower upfront risk & managed service |

---

### 8.3 Gift Card Transaction Fees (Both Options)

| Method | Fee Structure |
|---|---|
| Digital Gift Cards (via vendor API) | Vendor markup of 3–5% on face value (passed through at cost, no additional markup) |
| Physical Merchandise | No transaction fee; inventory purchased at wholesale by The Arc Mercer |
| Cafeteria Meals | No transaction fee; internal redemption tracking only |

### 8.4 Optional Add-Ons (Both Options)

| Add-On | Cost |
|---|---|
| Additional Paycom integration fields or custom sync logic | $3,000–$5,000 |
| Custom reporting / BI dashboard integration | $5,000 |
| Additional training sessions (per session) | $500 |
| Annual feature enhancement package (8 hours/month) | $15,000/year |

---

## 9. Evaluation Criteria Alignment

### Ease of Use
- Mobile-first PWA — no app download, works on any smartphone.
- Icon-driven navigation with large touch targets.
- Step-by-step guided nomination flows.
- Designed and tested with non-technical frontline staff.
- One-tap actions for all common tasks.

### Integration Robustness
- Dual-channel Paycom integration (API + SFTP fallback).
- Automated user provisioning with discrepancy reporting.
- SSO via SAML 2.0 / OAuth 2.0 — employees use existing credentials.
- Nightly sync with real-time status monitoring.

### Administrative Control
- Full QA queue with approve/return/decline workflow.
- Configurable point values — no code changes needed.
- Comprehensive audit trails for every point transaction.
- Leader dashboards with participation trends and program-level analytics.
- Inventory and fulfillment management tools.

### Total Cost of Ownership
- **Option A (Source Ownership):** Year 1 all-in: $131,200; Year 2+: $21,200/year. The Arc Mercer owns the code — no vendor lock-in, no per-user fees.
- **Option B (IoTeye SaaS):** $0 upfront, $30,000/year fully managed. Lower initial commitment with all maintenance and updates included.
- Both options: no per-user licensing fees — scales with your organization at no additional user cost.

---

## 10. Appendices

### Appendix A: Technology Stack Detail

| Layer | Technology | Version/Service |
|---|---|---|
| Front End | React | 18+ |
| Language | TypeScript | 5+ |
| UI Framework | Tailwind CSS + Headless UI | Latest |
| Backend/Database | Supabase (PostgreSQL) | Managed Cloud |
| Integration Services | Python (FastAPI) | 3.11+ |
| Cloud Platform | AWS | ECS Fargate, CloudFront, S3, Secrets Manager, CloudWatch |
| CI/CD | GitHub Actions | Automated testing and deployment |
| Monitoring | AWS CloudWatch + Sentry | Error tracking and performance monitoring |

### Appendix B: Data Security Summary

- AES-256 encryption at rest
- TLS 1.3 encryption in transit
- Row Level Security (RLS) at the database level
- SOC 2 Type II eligible AWS infrastructure
- Regular security patching and dependency updates
- Principle of least privilege access controls
- Immutable audit logs

### Appendix C: Support & Maintenance

**Included in Annual Support:**
- Bug fixes and security patches (48-hour SLA for critical issues)
- Supabase and AWS infrastructure monitoring
- Quarterly system health reports
- Email and phone support during business hours (M–F, 9 AM – 5 PM ET)

**Response Time SLAs:**

| Severity | Description | Response Time | Resolution Target |
|---|---|---|---|
| Critical | Platform down / data loss | 2 hours | 8 hours |
| High | Major feature unavailable | 4 hours | 24 hours |
| Medium | Non-critical bug / UI issue | 1 business day | 5 business days |
| Low | Enhancement request / question | 2 business days | Next scheduled release |

---

*IoTeye Inc. appreciates the opportunity to submit this proposal and looks forward to partnering with The Arc Mercer to build a recognition platform that celebrates and retains your dedicated workforce. We are available for a follow-up presentation or demo at your convenience.*

**Contact:**  
**IoTeye Inc.**  
Basking Ridge, New Jersey, USA  
sale@ioteyeinc.com  
https://www.ioteyeinc.com
