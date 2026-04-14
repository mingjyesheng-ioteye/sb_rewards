# Competitive Feature Delta Analysis

**Project:** Employee Engagement & Recognition Platform — The Arc Mercer  
**Date:** April 14, 2026 (Revised)  
**Prepared by:** IoTeye Inc.  
**IoTeye Source:** `Proposal - Employee Engagement Platform.md` (full proposal, 751 lines)

---

## Proposals Compared

| Label | Vendor | Source File |
|---|---|---|
| **IoTeye** | IoTeye Inc. | `IoTeye - Arc Mercer Pitch.pptx` / `Proposal - Employee Engagement Platform.md` |
| **Proposal 1** | Anonymous Vendor | `competitive_proposals/Proposal_1.pdf` |
| **Proposal 2** | Abid Mahmood (Independent) | `competitive_proposals/Proposal_2.pdf` |

---

## 1. Features Competitors Have That IoTeye Does NOT

| Feature | Who Has It | IoTeye Gap | Risk |
|---|---|---|---|
| **Selection Committee Voting / Ranked-Choice** | P1, P2 | IoTeye QA queue only supports approve/return/decline. No committee voting, no drag-and-drop ranking, no ballot workflow. P2 explicitly states Arc Mercer uses ranked-choice drag-and-drop today. | **HIGH** |
| **Badge ID + PIN Login (frontline staff)** | P2 | IoTeye offers SSO (Google/Microsoft) with email/password fallback. P2 identifies that many frontline DSPs lack Arc Mercer email addresses and proposes Paycom badge ID + self-set PIN login. | **HIGH** |
| **Magic Link Login (frontline staff)** | P1 | P1 offers magic-link authentication for frontline staff without corporate email. IoTeye does not address this scenario. | **MEDIUM** |
| **TAC Meeting RSVP & Role Sign-Ups** | P1 | IoTeye includes TAC meeting attendance logging and automated point awards as a Phase 2 deliverable (admin check-in or attendance import). However, it does not include RSVP workflow, role sign-ups (setup, check-in, cleanup, leadership), or event reminders. P1 scopes a full TAC module with RSVP, role sign-ups, attendance, and approvals ($3,600). | **MEDIUM** |
| **Culture Group Sign-Ups & Participation Tracking** | P1 | Not mentioned anywhere in IoTeye proposal. P1 scoped as a dedicated module ($2,100). | **MEDIUM** |
| **Volunteer / Event Help Forms** | P1 | Not in IoTeye proposal. | **LOW-MEDIUM** |
| **Social Media Engagement Form (Screenshot Upload)** | P1 | Not in IoTeye proposal. P1 includes a form with screenshot upload and admin review workflow. | **LOW-MEDIUM** |
| **Nomination Revise-and-Resubmit Loop** | P1 | IoTeye includes "Return for Edits" with a comment field in the QA queue, which enables a resubmission path. However, P1 explicitly scopes a formal revise-and-resubmit loop as a dedicated workflow with status tracking through the cycle. IoTeye's mechanism is present but less formally defined. | **LOW-MEDIUM** |
| **Dark Mode** | P2 | P2 proposes light/dark mode for staff working night shifts at group homes. IoTeye does not mention it. | **LOW** |
| **In-Person Store QR Code Scanning** | P2 | P2 proposes QR code scanning for a physical in-person store. IoTeye only covers a digital storefront. Arc Mercer apparently plans to build a physical store. | **MEDIUM** |
| **Cafe Redemption Workflow (Cashier-Facing Screen)** | P1 | P1 includes a dedicated cashier-facing lookup screen for cafeteria meal redemption (search employee, confirm balance, deduct points). IoTeye lists "cafeteria meals" as a reward category with "internal redemption tracking only" but does not describe the operational point-of-sale mechanism for cafeteria staff. | **MEDIUM** |
| **Working Live Demo** | P2 | P2 built and shipped a live working demo at `arc-mercer-demo.vercel.app`. IoTeye has mockup screenshots only. | **HIGH** (competitive) |

---

## 2. Features IoTeye Has That Competitors Do NOT

| Feature | IoTeye Advantage | Impact |
|---|---|---|
| **BrainClaw AI Agent (already in production at Arc Mercer)** | NLP-based analytics, anomaly detection, ad-hoc reporting via natural language. Extends existing AI workspace with 94+ tools already running at Arc Mercer (SpringBoard 37 tools + Samsara 57 tools). Neither competitor offers anything comparable. | **VERY HIGH** |
| **Existing Relationship & Production Systems** | Arc Mercer already uses SpringBoard, Guardian, and BrainClaw. IoTeye has direct institutional knowledge of the organization. | **HIGH** |
| **WCAG AAA Accessibility Commitment (7:1 Contrast)** | IoTeye explicitly targets WCAG AAA contrast ratios (7:1) for all text and interactive elements, with 48x48px touch targets exceeding AA requirements. P2 mentions "high-contrast" generically. P1 does not specify a WCAG level. | **HIGH** |
| **Screen Reader & Keyboard Navigation** | IoTeye commits to semantic HTML, ARIA labels, NVDA/VoiceOver testing, and full keyboard navigability. Includes accessibility audits before each phase launch and a built-in feedback mechanism for usability issues. Neither competitor details screen reader or keyboard support. | **MEDIUM** |
| **Explicit SLA Tiers** | IoTeye provides severity-based SLAs: Critical (2hr response / 8hr resolution), High (4hr / 24hr), Medium (1 business day / 5 days), Low (2 business days / next release). P1 explicitly excludes post-launch support. P2 offers general monthly support with no SLA. | **HIGH** |
| **Dual Paycom Integration (SFTP + REST API)** | IoTeye proposes both SFTP (primary) and REST API (optional enhancement) with automated discrepancy reporting — data anomalies (missing fields, duplicates) are auto-flagged and sent to HR for review. P1 prices SFTP and API as separate cost paths. P2 acknowledges uncertainty about Paycom API access. | **MEDIUM** |
| **Multi-IDP SSO with Zero-Downtime Migration Path** | IoTeye explicitly plans for Google Workspace SSO now with a documented migration path to Microsoft Entra ID (Azure AD) — both providers run in parallel during transition with zero downtime. Neither competitor addresses the Google-to-Microsoft migration scenario. | **MEDIUM** |
| **AWS Infrastructure (HIPAA-Eligible, 99.9% Uptime)** | IoTeye deploys on AWS with WAF, VPC isolation, Secrets Manager, CloudWatch, and commits to 99.9% uptime. P1 uses Vercel. P2 uses Next.js/Supabase (likely Vercel). More enterprise-grade for a healthcare-adjacent organization. | **MEDIUM** |
| **Source Code Ownership Option** | Option A gives Arc Mercer full IP and source code ownership. Neither competitor explicitly offers this choice. | **MEDIUM** |
| **Batch QA Queue Operations** | IoTeye includes batch operations for the QA queue during high-volume nomination periods. Neither competitor mentions batch admin capabilities. | **LOW-MEDIUM** |
| **Offline Capability** | IoTeye mentions offline mode for low-connectivity environments with lazy-loaded images and compressed assets. Competitors do not address offline use. | **LOW-MEDIUM** |
| **Push Notifications (Mobile + Email)** | IoTeye includes push notifications leveraging Guardian experience (Twilio SMS, Expo push). P1 offers email + in-app only. P2 does not detail notification strategy. | **LOW-MEDIUM** |
| **Comprehensive Audit Trail & Anomaly Detection** | IoTeye includes anomaly highlighting for unusual point bestowals, immutable audit logging with full field detail (timestamp, actor, action type, amount, source), and CSV export. Competitors mention basic audit logs but not anomaly detection. | **MEDIUM** |

---

## 3. Pricing Comparison

| | IoTeye Option A (Own Code) | IoTeye Option B (SaaS) | Proposal 1 | Proposal 2 |
|---|---|---|---|---|
| **Upfront Cost** | $110,000 | $0 | $54,000 - $65,700 | $20,000 - $30,000 |
| **Annual / Ongoing** | $21,200/yr | $30,000/yr | ~$2,400 - $3,600/yr (hosting only) | $6,000 - $12,000/yr |
| **3-Year Total** | $173,600 | $90,000 | ~$61,200 - $76,500 | ~$38,000 - $66,000 |
| **5-Year Total** | $216,000 | $150,000 | ~$66,000 - $80,100 | ~$50,000 - $78,000 |
| **10-Year Total** | $322,000 | $300,000 | ~$78,000 - $101,700 | ~$80,000 - $150,000 |
| **Delivery Timeline** | 36 weeks (9 months) | 36 weeks | **16 weeks** | **11 - 15 weeks** |
| **Code Ownership** | Yes (Option A) | No | Implied (custom build) | Not addressed |
| **Ongoing Support Model** | Included in annual fee | Included in subscription | Not included (separate retainer) | $500 - $1,000/month |

### Key Pricing Observations

- IoTeye Option A is ~2x Proposal 1 and ~4x Proposal 2 on upfront cost.
- IoTeye Option B eliminates upfront cost but 3-year total ($90,000) still exceeds both competitors.
- At the 10-year horizon, IoTeye Option B ($300,000) approaches Option A ($322,000), while competitors remain significantly lower ($78k-$150k range).
- Both competitors deliver in roughly half the time or less (16 weeks and 11-15 weeks vs. 36 weeks).
- Proposal 1 explicitly excludes post-launch maintenance; would require a separate retainer not yet priced.
- Proposal 2 includes ongoing support at $500 - $1,000/month.
- Neither competitor includes enterprise-grade AWS infrastructure, HIPAA-eligible hosting, or SLA commitments in their pricing.

---

## 4. Scope / Depth Gaps to Address

| Area | Concern |
|---|---|
| **Selection Committee Voting** | Both competitors address this. It appears to be how Arc Mercer currently picks winners (ranked-choice by committee, not simple approval). IoTeye should add this module or clearly explain why QA-queue approval is sufficient. |
| **Frontline Authentication** | If frontline DSPs lack company email, SSO + email/password fallback breaks down. Badge ID + PIN (P2) or magic link (P1) solves this. IoTeye needs an answer here. |
| **Physical Store / QR Redemption** | Arc Mercer plans an in-person store component. IoTeye's storefront is digital-only. Add QR code scanning for physical redemption. |
| **Cafe Redemption Workflow** | No operational mechanism described for how a cafeteria worker processes a points-for-meal redemption. Add a cashier-facing lookup/deduction screen. |
| **Timeline Justification** | 36 weeks vs. 16 weeks (P1) and 11-15 weeks (P2) is a 2-3x gap that needs strong justification or scope compression. |

---

## 5. Top 5 Action Items

### 1. Add Selection Committee Voting Module
Both competitors include it. P2 specifically states Arc Mercer uses ranked-choice drag-and-drop today. The QA queue (approve/return/decline) alone does not replace committee-based ranked selection. **Add a voting/ranking workflow for the selection committee.**

### 2. Solve Frontline Auth Without Email
Badge ID + PIN (P2's approach) is the strongest answer for frontline DSPs without company email addresses. Magic link (P1) is an alternative. The current email/password fallback likely does not work for a significant portion of the workforce. **Add a non-email authentication path.**

### 3. Address Physical Store & Cafe Redemption
Add QR code scanning for in-person store redemption and a cashier-facing screen for cafeteria meal point deductions. Both competitors caught these operational details. **Expand the rewards marketplace to cover physical redemption workflows.**

### 4. Justify or Compress the 36-Week Timeline
Competitors deliver in 11-16 weeks. Even accounting for IoTeye's larger scope, the 2-3x timeline gap is difficult to defend without a compelling narrative. **Consider accelerating Phase 1 delivery or restructuring the phased approach.**

### 5. Lead with AI + Existing Relationship
BrainClaw is the killer differentiator. Neither competitor has anything close. Arc Mercer already runs 94 AI tools through IoTeye. **Frame BrainClaw as a core advantage, not an optional add-on.** The unified AI workspace spanning operations and employee engagement is a capability no other vendor can offer.

---

*This analysis is based on the text content of all three proposals and the original RFP. IoTeye features verified against the full `Proposal - Employee Engagement Platform.md` (751 lines, sections 1-10 including appendices). Competitor feature claims are taken at face value from their submitted documents.*
