# Site improvements log

One focused improvement per week, shipped as a PR for Paresh to approve. Read this before changing anything so earlier work is not redone or undone.

## 2026-11-17 — Credibility line in the hero + hero CTA no longer hidden behind the name

- **What:** Added one proof line under the hero headline (desktop and mobile): "11+ years at WPP/VML, FCB Kinnect, Schbang and Cheil on Amazon, Bata, Ford and Honda" (facts already on the page). Moved the desktop hero text block up slightly (top 31% → 25%) and put it above the big "Paresh Jain" marquee (`z-index:2`) so the "Free 30-min call" orb is no longer partly covered on 1280×720 / 1366×768 laptop screens.
- **Why:** The first screen said *what* Paresh does but gave no reason to believe it; the agency/brand names only appeared after scrolling. Cold-email visitors (UK/US/UAE agencies, Indian D2C founders) decide in seconds. On common laptop screens the main hero CTA was also half-covered by the marquee text.
- **How to judge:** In GA4, compare `hero_orb_call` + `hero_m_call` clicks and scroll-past-hero rate for the 2 weeks after merge vs before; count "New enquiry from pareshjain.com" emails and Google Calendar bookings (0 of each in the 28 days before this change, though v4 only launched on 17 Nov).

## Open ideas (not done yet)

- International visitors see INR-only prices and INR-only budget options in the form; "quoted in USD" has no figure. Needs Paresh to supply USD starting prices before anything can change.
- No client testimonial or named case-study result on the page yet — needs Paresh to supply an approved quote.
