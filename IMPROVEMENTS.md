# Site improvements log

One focused improvement per week, shipped as a PR for Paresh to approve. Read this before changing anything so earlier work is not redone or undone.

## 2026-11-17 — Credibility line in the hero + hero CTA no longer hidden behind the name

- **What:** Added one proof line under the hero headline (desktop and mobile): "11+ years at WPP/VML, FCB Kinnect, Schbang and Cheil on Amazon, Bata, Ford and Honda" (facts already on the page). Moved the desktop hero text block up slightly (top 31% → 25%) and put it above the big "Paresh Jain" marquee (`z-index:2`) so the "Free 30-min call" orb is no longer partly covered on 1280×720 / 1366×768 laptop screens.
- **Why:** The first screen said *what* Paresh does but gave no reason to believe it; the agency/brand names only appeared after scrolling. Cold-email visitors (UK/US/UAE agencies, Indian D2C founders) decide in seconds. On common laptop screens the main hero CTA was also half-covered by the marquee text.
- **How to judge:** In GA4, compare `hero_orb_call` + `hero_m_call` clicks and scroll-past-hero rate for the 2 weeks after merge vs before; count "New enquiry from pareshjain.com" emails and Google Calendar bookings (0 of each in the 28 days before this change, though v4 only launched on 17 Nov).

## 2026-11-17 — Visual refresh + new hero portrait (asked for by Paresh, merged on his instruction)

- **What:** Wide Archivo display headings; smaller outlined hero name band behind the photo; brand names as a tile grid; white/grey section rhythm; prices as cards with the "Fractional" card raised; process steps as cards; contact badge "Taking new projects now" and headline "Tell me the launch date. I'll tell you if it's doable."; mobile: smaller intro, compact numbers row, first 4 projects + "See all 7 projects". New hero portrait (re-cut, graded, navy arch with thin orange outline) as `assets/paresh-jain-hero-700/1400.webp` with srcset.
- **Why:** Page was text-heavy and monotone, prices didn't stand out, mobile scroll was long, old cutout had haloed/smeared edges.
- **How to judge:** GA4 hero/price/contact CTA clicks, `see_all_work` events, and enquiry/booking emails over the next 2–4 weeks vs the first week of v4.

## 2026-11-17 — Service pages, SME/MSME packages, brand logos (preview, awaiting approval)

- **What:** 4 service pages in `/services/` built by `tools/build_services.py` (shared CSS `assets/site.css`): campaign & launch plan, fractional marketing lead, agency pitch & account cover, small business packages. New SME packages proposed: strategy session ₹4,999, marketing health check ₹14,999, launch & festive sprint ₹34,999, monthly marketing advisor ₹39,999/month (prices are proposals for Paresh to confirm). Home: "Small business" nav link, "Full details →" on each service card, SME package strip, logos (Simple Icons, monochrome) for Ford, Bata, Honda, MG, Tata, vivo, Uber; text for brands without a free logo file. Form: SME options + lower budget bands; `?need=` preselects the option. Sitemap updated.
- **Why:** Ads and SEO need a dedicated page per offer; smaller businesses had no entry point below ₹75,000.
- **How to judge:** Visits and CTA clicks on `/services/*`, enquiries selecting SME options.

## Open ideas (not done yet)

- International visitors see INR-only prices and INR-only budget options in the form; "quoted in USD" has no figure. Needs Paresh to supply USD starting prices before anything can change.
- Campaign images for "Launches & results" (needs approved images from Paresh).
- AI or new real portraits in other setups (blocked: sandbox can't reach canva.com).
- No client testimonial or named case-study result on the page yet — needs Paresh to supply an approved quote.
