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
- **Added after market research (same preview):** SME local visibility plan ₹19,999; after-sale plan inside the festive sprint; new D2C page (`/services/d2c-brand-growth.html`) with agency & ads audit ₹49,999, creator & influencer plan ₹49,999, quick-commerce & marketplace plan ₹59,999; agency pitch sprint ₹70,000 and interim account lead ₹1,20,000/month. Research notes in the project doc `claude/market-demand-packages-nov17.md`. Also added `/services/website-development.html` (AI-built landing page ₹24,999, WordPress site ₹39,999, Shopify starter ₹59,999, Shopify refresh ₹34,999, care plan ₹7,999/mo) and `/services/creative-services.html` (brand kit ₹24,999, social creatives ₹29,999/mo, ad creative pack ₹39,999), a home-page strip for both, and matching form options.
- **How to judge:** Visits and CTA clicks on `/services/*`, enquiries selecting SME/D2C/agency package options.

## 2026-11-17 — "Ways to work with me" organised by persona (preview)

- **What:** The services section is now a tab switcher: Brands & startups, D2C & consumer brands, Small businesses & MSMEs, Agencies, Websites & creative. Each tab has a one-line "you are…" description, 3–6 package cards (price, 2–3 deliverables, "Enquire" which preselects the form, "Details →" to the service page) and a link to the full service page. `?for=brands|d2c|sme|agency|build` opens a specific tab (use it in cold emails and ads). Keyboard arrows work, tab choice is tracked as `persona_select`, and without JS all personas show stacked. Fixed a bug where `?need=` options containing digits (d2c_*) weren't preselected.
- **Why:** 21 packages in one list was too much; visitors should see only what fits them.
- **How to judge:** `persona_select` events, package `Enquire` clicks per persona, enquiries by package.

## 2026-11-17 — Site wiring pass (preview)

- **What:** Branded `404.html` (links to home, services and every service page; GA4 `page_not_found` event). "Services" link now visible in the mobile header on every page. Service-page breadcrumbs and nav open the matching persona tab on the home page (`/?for=…#services`), plus a "Compare all packages" link. Checked every internal link, anchor, `?need=` and `?for=` value across all 11 pages: none broken.
- **Why:** Mobile visitors had no way to reach the services from the header; dead links showed Vercel's default 404.
- **How to judge:** `page_not_found` events stay near zero; service-page visits from mobile go up.

## 2026-11-17 — Go-live set-up: Google, Meta, AI search, consent (merged on Paresh's instruction)

- **What:** All tracking now lives in one file, `assets/tracking.js`. It holds the GA4 ID and empty slots for the Meta Pixel, Google Ads tag and Google Ads lead conversion; paste each ID there once and every page uses it. Google Consent Mode v2 asks first in the EEA, UK and Switzerland. A small cookie notice (`assets/consent.js`) shows to visitors on European time zones, and the Meta Pixel loads there only after "Accept". The thanks page fires the GA4 `generate_lead` event, plus Meta `Lead` and the Google Ads conversion once their IDs are set. `robots.txt` explicitly welcomes Google, Bing and the AI crawlers (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended, Meta). New `llms.txt` gives AI assistants a summary of services, prices and work. Service pages got full OG/Twitter tags; the home page description now covers all audiences; the privacy page is accurate for the current form fields, cookies and consent, with a "Change cookie choice" button; sitemap dates refreshed.
- **Why:** Ready for Google/Meta ads (incl. UK/EU) and for being cited by AI search.
- **How to judge:** GA4 Realtime shows page views and `generate_lead`; Meta Events Manager shows PageView/Lead once the Pixel ID is set.

## 2026-11-17 — Real logos and creatives from Paresh's portfolio

- **What:** Took assets from "Paresh_Jain_Portfolio.pdf" (from Gmail, the compressed copy of "Paresh's Portfolio '26"). The brand row is now a wall of 27 real brand logos plus 5 agency logos (`assets/logos/`), replacing Simple Icons and plain-text names. New "Creative from campaigns I've led" gallery on the home page and the creative services page, 9 pieces (`assets/work/`). Case rows for Bata, Himalayan, Honda, M3M and CoinDCX now show real visuals. CoinDCX case unhidden with agency/date corrected to Alchemist, May–Jul 2021 (per portfolio + resume). "17 brands" changed to "30+ brands". Dead CSS removed (.brand-list, .svc, .sme-*). llms.txt updated.
- **Why:** The site sold creative and campaigns with almost no visible work; the portfolio already had it.
- **How to judge:** Time on page, `case_open` events, enquiries mentioning creative.

## 2026-11-18 — Positioning: experienced, multi-category partner business owners can trust (preview)

- **What:** New positioning: "11 years inside India's top agencies. Now on your side of the table." The hero headline is now a visible H1, and the page title, description and OG tags have been updated to match. New sections:
  - **Why me:** a fair comparison of a typical agency set-up vs working with Paresh, 6 rows.
  - **Experience:** 11 categories, each with portfolio logos and a factual result where one exists; collapses to 5 on mobile with "See all".
  - **About:** a short story plus a career timeline from his resume.
  - **How I work:** four promises (you deal with me, straight answers, fixed scope and price, numbers you can check) above the 3-step process.

  Other changes:
  - Numbers band is now 11+ years, 30+ brands, 11 categories, 3 award-winning campaigns.
  - FAQ leads with owner objections (why not an agency, my category, my existing agency, burnt before).
  - Contact headline changed to "Tell me what's not working. I'll tell you what I'd do."
  - Nav now reads Why me / Work / About / Services.
  - llms.txt summary updated.
- **Why:** Paresh wants to be seen as a seasoned, multi-category professional that owners trust over the agencies that keep approaching them.
- **How to judge:** Scroll depth to #why/#experience, `persona_select`, enquiries and calls from business owners.

## Open ideas (not done yet)

- International visitors see INR-only prices and INR-only budget options in the form; "quoted in USD" has no figure. Needs Paresh to supply USD starting prices before anything can change.
- AI or new real portraits in other setups (blocked: sandbox can't reach canva.com).
- No client testimonial or named case-study result on the page yet — needs Paresh to supply an approved quote.
