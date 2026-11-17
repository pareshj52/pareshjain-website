"""Build the service pages in /services from the data below.

Run from the repo root:  python3 tools/build_services.py
Edit the SERVICES data, re-run, commit the generated HTML.
Facts used for proof come from the home page; do not add new claims here.
"""
import html, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "services"
SITE = "https://www.pareshjain.com"
BOOK = "https://calendar.google.com/calendar/u/0/appointments/schedules/AcZssZ1380Zcu-WXHLTQi5dZqrbtbLfTN_Pl_yzwDjDL7QWRDAgHdRhg_jQIUqrLBvdR7pw_g4_Txei-"
WA = "https://wa.me/919999896986?text=Hi%20Paresh%2C%20I%20saw%20your%20site%20and%20want%20to%20talk%20about%20our%20marketing."

PROOF = {
    "amazon": ("+14%", "Amazon Prime Day 2023", "More Prime members shopped than the year before, in what Amazon called its biggest Prime Day ever in India.", "FCB Kinnect · integrated plan"),
    "bata": ("Award", "Bata “Every Walk is a Ramp Walk”", "Named Most Admired Marketing Campaign of the Year at the Images Fashion Awards.", "FCB Kinnect · Account Director"),
    "himalayan": ("₹12 Cr", "Tata Himalayan × Khardungla Challenge", "In earned media coverage for a cause partnership.", "Schbang · led the digital campaign"),
    "honda": ("1,500", "Honda #HondaExcitesTheWorld", "Winners in a nationwide contest for India’s first MotoGP: 500 tickets and up to 1,000 merchandise prizes.", "FCB Kinnect · Account Director"),
    "mg": ("40%", "MG Motor India launch content", "Faster launch time-to-market, with more consistent content across channels.", "Cheil India · content standards, kits and SOPs"),
    "ford": ("APAC", "Ford 3D vehicle configurator", "Directed the build and APAC launch across product, engineering, creative and dealer teams.", "WPP / VML · 2024–2026"),
}

SERVICES = [
    {
        "slug": "campaign-launch-plan",
        "need": "plan",
        "nav": "Campaign & launch plan",
        "short": "One plan for a launch, festive push or new product. From ₹75,000.",
        "tier": "Project · 2–4 weeks",
        "title": "Campaign & launch plan",
        "seo_title": "Campaign & Launch Plan for Brands | Paresh Jain, New Delhi",
        "desc": "A complete campaign and launch plan in 2–4 weeks: proposition, big idea, channel and creator plan, budget split, KPIs and briefs your team can run with. Fixed fee from ₹75,000.",
        "lede": "One plan every team can work from, from the idea to the channel plan, so your launch ships on date and you know what success looks like.",
        "meta": [("From ₹75,000", "fixed fee"), ("2–4 weeks", "start to handover"), ("Written scope", "within 2 working days")],
        "for": ["You have a launch, a festive push or a new product coming up", "Your agency, creators and in-house team are each working from different ideas", "You need a budget split and KPIs you can defend to leadership", "You want a senior plan without hiring a full-time head of marketing"],
        "not": ["You only need posts made this week (an agency or freelancer is cheaper)", "You want media buying handled with no plan behind it", "Your budget for my fee is under ₹75,000: see the small business packages instead"],
        "get": [("Proposition & messaging", "Who it’s for, why they should care, and the few lines everyone repeats."), ("The big idea", "One campaign idea that works across channels, with routes if you want options."), ("Channel, creator & influencer plan", "What runs where, when, and who makes it."), ("Budget split & KPIs", "Where the money goes, what each channel must deliver, and how you’ll measure it."), ("Ready-to-run briefs", "Briefs your agency, creators or in-house team can start on the next day."), ("Handover session", "A walkthrough with your team so the plan doesn’t sit in a folder.")],
        "steps": [("Week 1", "Discovery", "Your goal, date, audience, past results and competitors. What’s in the way."), ("Week 2", "Strategy & idea", "Proposition, messaging and the big idea, reviewed with you."), ("Weeks 3–4", "Plan & briefs", "Channel and creator plan, budget split, KPIs and briefs."), ("Handover", "Walkthrough", "We go through it with your team and agree who does what next.")],
        "proof": ["amazon", "bata", "honda"],
        "price": ("From ₹75,000", "Fixed fee for the plan, agreed in writing before any work starts. Prices exclude GST and any media or production spend. Teams outside India are quoted in USD."),
        "faq": [("Can you also run the campaign?", "Yes. I can lead it to go-live as a fractional marketing lead, managing your agencies, creators and freelancers. Media and production costs are billed at actuals."), ("What if I don’t have an agency yet?", "The plan includes briefs any good agency or freelancer can pick up, and I can recommend partners."), ("How soon can you start?", "Usually within a week. Tell me your launch date and I’ll say straight away if it’s realistic."), ("What do you need from us?", "A kick-off call, access to past results and brand material, and one person who can make decisions.")],
    },
    {
        "slug": "fractional-marketing-lead",
        "need": "fractional",
        "nav": "Fractional marketing lead",
        "short": "A senior marketing lead about 2 days a week. From ₹1,50,000 a month.",
        "tier": "Monthly · about 2 days a week",
        "title": "Fractional marketing lead",
        "seo_title": "Fractional Marketing Lead / Part-time CMO | Paresh Jain",
        "desc": "A senior marketing lead on your team about two days a week: owns the plan and calendar, manages agencies and creators, reviews numbers weekly. From ₹1,50,000 a month, month-to-month after 3 months.",
        "lede": "A senior marketing lead on your team, without a full-time hire. I own the plan, run your agencies and creators, and review the numbers with you every week.",
        "meta": [("From ₹1,50,000", "a month"), ("About 2 days", "a week"), ("Month-to-month", "after the first 3 months")],
        "for": ["D2C brands and startups that need senior marketing judgement every week", "Founders spending too much of their own time managing agencies", "Teams between marketing heads, or not ready for a full-time hire", "Brands with a marketing budget but no single owner for it"],
        "not": ["You need someone in the office five days a week", "You only need a one-off plan: the campaign & launch plan fits better", "Your monthly budget for my fee is under ₹1,50,000: see the monthly marketing advisor package"],
        "get": [("The marketing plan & calendar", "A quarterly plan and a monthly calendar that I own and keep current."), ("Agency & creator management", "Briefing, reviewing and steering your agencies, creators and freelancers."), ("Weekly numbers review", "A weekly review with the founder or leadership: what worked, what changes."), ("Launches & campaigns", "Planning and leading campaigns to go-live, end to end."), ("Team set-up", "Processes, briefs and SOPs so the work keeps running between weeks."), ("Hiring help", "When you’re ready for a full-time lead, I help you hire and hand over.")],
        "steps": [("Weeks 1–2", "Audit & plan", "Where the marketing stands, what’s working, and a 90-day plan."), ("Every week", "Run & review", "Lead the work, manage partners, review numbers with you."), ("Every month", "Report & reset", "A short report and the next month’s calendar."), ("After 3 months", "Your call", "Continue month-to-month, scale up, or hand over to a hire.")],
        "proof": ["mg", "ford", "himalayan"],
        "price": ("From ₹1,50,000 a month", "For about two days a week. Month-to-month after the first 3 months. Prices exclude GST and any media or production spend. Teams outside India are quoted in USD."),
        "faq": [("Is this the same as a fractional CMO?", "Close. I lead marketing planning and delivery and manage your partners. I report to the founder or leadership and work alongside, not instead of, your team."), ("Do you work on-site?", "Mostly remote, with on-site days in Delhi NCR when they’re useful."), ("Can we start smaller?", "Yes. The monthly marketing advisor package is a lighter version for smaller businesses."), ("How do we stop if it isn’t working?", "After the first 3 months it’s month-to-month, so you can stop with a month’s notice.")],
    },
    {
        "slug": "agency-pitch-account-cover",
        "need": "agency",
        "nav": "Agency pitch & account cover",
        "short": "Senior help for a pitch or a difficult live account. From ₹15,000 a day.",
        "tier": "For agencies · by the day",
        "title": "Pitch & account cover for agencies",
        "seo_title": "Freelance Agency Pitch & Account Lead, White-label | Paresh Jain",
        "desc": "Senior agency help by the day: pitch strategy and decks, account and client leadership on live business, team set-up and SOPs. White-label available. From ₹15,000 a day.",
        "lede": "Senior help for a pitch, a difficult live account or a gap between leads, from someone who has spent 11+ years inside agencies. White-label if you prefer.",
        "meta": [("From ₹15,000", "a day"), ("White-label", "if you prefer"), ("11+ years", "inside 6 agencies")],
        "for": ["A pitch is due and you need senior strategy and a sharper story", "A key client needs senior attention this month", "Your account lead has left and the client is nervous", "You need SOPs, status reporting or a team set up properly"],
        "not": ["You need a full-time employee on your payroll", "You need design or production capacity rather than leadership"],
        "get": [("Pitch strategy & story", "The insight, the idea and the deck story, built with your team."), ("Presenting", "In the room with you, or behind the scenes if it’s white-label."), ("Account & client leadership", "Steadying live business, running status and stakeholder meetings."), ("Team set-up & SOPs", "Briefing flow, status reports and processes that hold up."), ("Gap cover", "Senior cover while you hire the next account lead.")],
        "steps": [("Day 1", "Brief", "What’s at stake, the client, the deadline, and your team."), ("Next days", "Work", "Strategy, story or account work, side by side with your team."), ("Before handover", "Hand back", "Notes and next steps so your team keeps going.")],
        "pkg_title": "Fixed-price options for agencies",
        "pkg_sub": "Book by the day, or take a fixed package for a pitch or a gap. White-label on all of them. Agencies outside India are quoted in USD.",
        "packages": [
            {"tier": "5 working days", "name": "Pitch sprint", "price": "₹70,000", "unit": "fixed fee", "about": "Senior strategy and story for one new-business pitch.", "items": ["Brief decode and client and category research", "The insight, strategy and big idea", "Deck story and slide-by-slide outline", "One rehearsal with your team", "Presenting with you, or behind the scenes"], "fit": "Good when a pitch is 1–3 weeks away and your strategist is stretched.", "cta": "Book a pitch sprint", "need": "agency_sprint", "pick": True},
            {"tier": "By the day", "name": "Senior cover day", "price": "₹15,000", "unit": "a day", "about": "Flexible senior help for a live account, a workshop or a review.", "items": ["Account and client leadership on live business", "Strategy workshops and planning sessions", "Brief writing and creative reviews", "Status reporting and stakeholder meetings"], "fit": "Good for short, specific needs.", "cta": "Check my availability", "need": "agency"},
            {"tier": "Monthly · 8 days", "name": "Interim account lead", "price": "₹1,20,000", "unit": "a month", "about": "Steady a key client while you hire the next account lead.", "items": ["Owns the client relationship and status rhythm", "Team briefing, SOPs and quality checks", "A handover plan for your new hire"], "fit": "Good when an account lead has left and the client is nervous.", "cta": "Talk about cover", "need": "agency_interim"},
        ],
        "proof": ["ford", "bata", "honda"],
        "price": ("From ₹15,000 a day", "Billed by the day, with a written scope first. Prices exclude GST. Agencies outside India are quoted in USD."),
        "faq": [("Will you work under our agency’s name?", "Yes. White-label is fine, and I keep client work confidential."), ("How much notice do you need?", "Tell me the deadline. For pitches, a few days’ notice is usually enough to start."), ("Which agencies have you worked in?", "WPP/VML, FCB Kinnect, Schbang and Cheil, among six agencies over 11+ years.")],
    },
    {
        "slug": "d2c-brand-growth",
        "need": "d2c_audit",
        "nav": "D2C & brand projects",
        "short": "Agency & ads audit, creator campaigns, quick-commerce plans. From ₹49,999.",
        "tier": "For D2C and consumer brands",
        "title": "Fixed-price projects for D2C and consumer brands",
        "seo_title": "D2C Ads Audit, Influencer & Quick-commerce Plans | Paresh Jain",
        "desc": "Fixed-price projects for D2C brands: an independent agency and ads audit (₹49,999), a creator and influencer campaign plan (₹49,999) and a quick-commerce and marketplace spend plan (₹59,999).",
        "lede": "Independent, senior answers to the questions D2C founders keep asking: is my agency working, should I spend on creators, and is quick commerce worth it?",
        "meta": [("From ₹49,999", "fixed fee"), ("2–3 weeks", "per project"), ("Independent", "no media sales or commission")],
        "for": ["You’re spending on Meta, Google or marketplace ads and returns have dropped", "You’ve changed agencies and still aren’t sure what’s working", "You’re planning a creator or influencer push and want it to pay back", "You’re deciding whether to go big on Blinkit, Zepto, Instamart or Amazon"],
        "not": ["You want someone to run the ads day to day (I can brief and steer whoever does)", "You need guaranteed ROAS: nobody honest can promise it"],
        "pkg_title": "Pick a project",
        "pkg_sub": "Each one ends with a written plan and a walkthrough with your team. Prices exclude GST and any media spend.",
        "packages": [
            {"tier": "2 weeks", "name": "Agency & ads audit", "price": "₹49,999", "unit": "fixed fee", "about": "An independent second opinion on your agency, your ads and your funnel.", "why": "The most common founder complaint: ‘we changed agencies and nothing changed.’", "items": ["Read-only review of Meta and Google ad accounts", "Funnel check: offer, landing pages, product pages, checkout", "Attribution check: what platforms claim vs. actual orders", "Agency scope, reporting and fees reviewed against results", "A clear verdict (keep, fix or replace) and a 30-60-90 day plan"], "fit": "Good if you spend ₹2 lakh+ a month on ads and aren’t sure it’s working.", "cta": "Get an audit", "need": "d2c_audit", "pick": True},
            {"tier": "2–3 weeks", "name": "Creator & influencer campaign plan", "price": "₹49,999", "unit": "fixed fee", "about": "A creator campaign built to sell, not just to get views.", "items": ["Campaign idea and creator mix: macro, micro and nano", "Selection criteria and a shortlist brief for your agency", "Creator briefs, dos and don’ts, approval flow", "Budget split, fee benchmarks and a usage-rights checklist", "Tracking plan: codes, links and what counts as success"], "fit": "Good before a launch, a sale or a big festive push.", "cta": "Plan a creator campaign", "need": "d2c_creator"},
            {"tier": "2–3 weeks", "name": "Quick-commerce & marketplace plan", "price": "₹59,999", "unit": "fixed fee", "about": "Decide where to sell and spend: Blinkit, Zepto, Instamart, Amazon or Flipkart.", "items": ["Which platforms, cities and SKUs to start with", "Spend plan against listing fees and minimum spends", "Listing, pricing and pack-size recommendations", "How to separate paid from organic sales", "A 90-day test plan with stop and scale rules"], "fit": "Good if quick commerce is eating budget and you can’t tell if it pays.", "cta": "Plan my marketplace spend", "need": "d2c_qcomm"},
        ],
        "steps": [("Week 1", "Access & discovery", "Read-only access, your numbers, and a call with you and your agency."), ("Week 2", "Analysis", "I review, benchmark and pressure-test what’s happening."), ("Weeks 2–3", "Plan", "A written plan with priorities, owners and numbers to watch."), ("Handover", "Walkthrough", "We go through it with your team and agency.")],
        "proof": ["amazon", "honda", "bata"],
        "price": ("From ₹49,999", "Fixed fee per project, agreed in writing before work starts. If you move to a fractional engagement within 30 days, the project fee is adjusted against the first month. Prices exclude GST and any media spend."),
        "faq": [("Will you tell my agency they’re doing badly?", "I’ll tell you what the numbers show, fairly. Often the fix is a clearer brief, offer or budget split, not a new agency."), ("Do you need logins?", "Read-only access to ad accounts and analytics is enough. I don’t change live campaigns during an audit."), ("Do you take commission from creators or platforms?", "No. I don’t sell media or take referral fees, so the advice stays independent."), ("Can you run the plan afterwards?", "Yes, as a fractional marketing lead managing your agencies and creators.")],
    },
    {
        "slug": "website-development",
        "need": "web_ai",
        "nav": "Websites: Shopify, WordPress & AI",
        "short": "Fast, simple websites and stores that are built to get enquiries. From ₹24,999.",
        "tier": "Websites & online stores",
        "title": "Websites that are built to sell, not just to look good",
        "seo_title": "Shopify, WordPress & AI Website Packages | Paresh Jain",
        "desc": "Fixed-price websites for small businesses and D2C brands: AI-built landing pages from ₹24,999, WordPress business sites ₹39,999, Shopify starter stores ₹59,999, Shopify refresh ₹34,999 and care plans from ₹7,999/month.",
        "lede": "Simple, fast websites and Shopify stores, planned by a marketer so every page has a job: get the enquiry, the WhatsApp message or the sale.",
        "meta": [("From ₹24,999", "fixed price"), ("1–3 weeks", "to launch"), ("Tracking set up", "GA4 and Meta Pixel included")],
        "for": ["You need a clean, fast website or store live in weeks, not months", "You’re launching a D2C brand on Shopify with a small catalogue", "Your current site looks dated or doesn’t bring enquiries", "You want analytics and ad tracking set up properly from day one"],
        "not": ["You need custom apps, complex integrations, marketplaces or member portals", "You have hundreds of products with complex variants and rules (I’ll refer you to a specialist agency)"],
        "pkg_title": "Pick a website package",
        "pkg_sub": "Fixed prices for theme-based, not-too-complex builds. Hosting, domain, paid themes, apps and plugins are billed at actuals. Prices exclude GST.",
        "packages": [
            {"tier": "5–7 working days", "name": "AI-built landing page or mini-site", "price": "₹24,999", "unit": "fixed fee", "about": "A fast 1–3 page site built with modern AI and no-code tools such as Framer.", "items": ["Up to 3 pages, mobile-first", "Page copy written for you", "Enquiry form and WhatsApp button", "GA4 and Meta Pixel set up", "Basic SEO: titles, descriptions, sitemap", "Domain connected, 2 rounds of changes"], "fit": "Good for a launch, an offer, a consultant or a new service.", "cta": "Get a landing page", "need": "web_ai"},
            {"tier": "2–3 weeks", "name": "WordPress business website", "price": "₹39,999", "unit": "fixed fee", "about": "A professional business site you can update yourself.", "items": ["Up to 8 pages on a quality theme", "Page structure and copy guidance", "Enquiry form, WhatsApp and Google Maps", "Speed and mobile basics", "GA4, Meta Pixel and Search Console", "Training video so your team can edit it"], "fit": "Good for service businesses, clinics, manufacturers and B2B firms.", "cta": "Build my website", "need": "web_wp", "pick": True},
            {"tier": "2–3 weeks", "name": "Shopify starter store", "price": "₹59,999", "unit": "fixed fee", "about": "A launch-ready Shopify store for a small D2C catalogue.", "items": ["Theme set-up and branding", "Up to 30 products uploaded", "Payments (e.g. Razorpay) and shipping (e.g. Shiprocket) set up", "Essential apps: reviews, WhatsApp, COD controls", "Policy pages, GA4 and Meta Pixel", "Handover session and checklist"], "fit": "Good for new D2C brands and businesses moving from Instagram selling.", "cta": "Launch my store", "need": "web_shopify"},
            {"tier": "1–2 weeks", "name": "Shopify store refresh", "price": "₹34,999", "unit": "fixed fee", "about": "Fix the pages that lose sales on an existing Shopify store.", "items": ["Quick conversion audit of home, product, cart and checkout", "Redesigned home and product page templates", "Trust: reviews, delivery and returns info, FAQs", "Speed clean-up: apps and images", "Tracking checked end to end"], "fit": "Good if traffic comes in but too few people buy.", "cta": "Refresh my store", "need": "web_refresh"},
            {"tier": "Monthly", "name": "Website care plan", "price": "₹7,999", "unit": "a month", "about": "Keep the site updated, backed up and improving.", "items": ["Updates, backups and uptime checks", "Up to 3 hours of small changes a month", "Monthly check of enquiries and traffic"], "fit": "Good after any of the builds above. Cancel any time.", "cta": "Add a care plan", "need": "web_care"},
        ],
        "steps": [("Days 1–2", "Brief & plan", "Goals, pages, products and what each page must do."), ("Week 1", "Design & build", "Theme, layout and copy in place on a private preview link."), ("Week 2", "Review & changes", "You review on your phone and laptop; we make the changes."), ("Launch", "Go live & handover", "Domain, tracking and a handover session with your team.")],
        "proof": ["ford", "mg"],
        "price": ("From ₹24,999", "Fixed fee per package, agreed in writing before work starts. Hosting, domain, paid themes, apps and plugins are billed at actuals. Prices exclude GST. " + "I lead every project and review every deliverable. Specialist designers, editors and developers I brief and manage do the production."),
        "faq": [("Who builds the website?", "I lead every project and review every deliverable. Specialist designers, editors and developers I brief and manage do the production."), ("What is an ‘AI website’?", "A site built with modern AI-assisted, no-code tools such as Framer. It’s fast to build and easy to change, which suits landing pages and small sites."), ("Will I own the website?", "Yes. The domain, hosting and store accounts are in your name, and you get all logins at handover."), ("What isn’t included?", "Custom apps, complex integrations, large catalogue migrations and paid themes or plugins. I’ll quote separately or refer you to a specialist."), ("Can you also bring traffic?", "Yes. Pair the site with a launch sprint, an ads audit or the monthly advisor package.")],
    },
    {
        "slug": "creative-services",
        "need": "cr_social",
        "nav": "Creative: brand, social & ads",
        "short": "Brand kits, monthly social creatives and ad creative packs. From ₹24,999.",
        "tier": "Creative services",
        "title": "Creative that’s briefed by a campaign lead",
        "seo_title": "Brand Kit, Social Media Creatives & Ad Creatives | Paresh Jain",
        "desc": "Fixed-price creative for small businesses and D2C brands: logo and brand starter kit ₹24,999, monthly social creatives ₹29,999/month and Meta and Google ad creative packs ₹39,999.",
        "lede": "Good-looking creative is easy to buy. Creative that has a clear idea, the right message and a reason to exist is harder. Every piece here starts with a proper brief.",
        "meta": [("From ₹24,999", "fixed price"), ("Briefed properly", "every piece has a job"), ("Ready to post", "sized for each platform")],
        "for": ["You need a simple, professional brand look to start with", "You want consistent social posts without hiring a designer full-time", "You run Meta or Google ads and need fresh creatives to test", "You’ve had pretty creative that didn’t sell"],
        "not": ["You need a full agency for TV, large shoots or big-budget film", "You want unlimited designs on demand"],
        "pkg_title": "Pick a creative package",
        "pkg_sub": "Fixed prices. Stock images, music licences, shoots and ad spend are billed at actuals. Prices exclude GST.",
        "packages": [
            {"tier": "2 weeks", "name": "Logo & brand starter kit", "price": "₹24,999", "unit": "fixed fee", "about": "A simple, professional identity you can use everywhere.", "items": ["2 logo directions, refined into 1 final logo", "Colour palette and font pairing", "1-page brand guide", "5 social media templates", "Business card and WhatsApp profile artwork"], "fit": "Good for new businesses and brands that have outgrown a DIY logo.", "cta": "Start my brand kit", "need": "cr_brand"},
            {"tier": "Monthly", "name": "Monthly social creatives", "price": "₹29,999", "unit": "a month", "about": "A month of on-brand posts, planned around what you’re selling.", "items": ["Monthly content plan tied to your offers and dates", "12 static posts or carousels", "4 reels edited from your footage", "Captions and hashtags", "Ready-to-post files for Instagram, Facebook and LinkedIn"], "fit": "Good if you post inconsistently or everything looks different.", "cta": "Plan my month", "need": "cr_social", "pick": True},
            {"tier": "1–2 weeks", "name": "Ad creative pack", "price": "₹39,999", "unit": "fixed fee", "about": "Fresh Meta and Google ads built around different hooks to test.", "items": ["3 angles and hooks based on your customer", "10 static ads in feed, story and display sizes", "3 short video ads edited from your footage or stock", "Headline and copy variations", "A simple test plan: what to run first and what to measure"], "fit": "Good when ads are fatiguing or you’re about to scale spend.", "cta": "Get an ad pack", "need": "cr_ads"},
        ],
        "steps": [("Days 1–2", "Brief", "Your customer, offer and what the creative must achieve."), ("Week 1", "Concepts", "Directions or first drafts for your feedback."), ("Week 2", "Final files", "Refined designs and edits, sized for every platform."), ("Every month", "Plan & review", "For monthly packages: next month’s plan and what performed.")],
        "proof": ["bata", "honda", "himalayan"],
        "price": ("From ₹24,999", "Fixed fee per package. Stock, music licences, shoots and ad spend are billed at actuals. Prices exclude GST. " + "I lead every project and review every deliverable. Specialist designers, editors and developers I brief and manage do the production."),
        "faq": [("Who makes the creative?", "I lead every project and review every deliverable. Specialist designers, editors and developers I brief and manage do the production."), ("How many changes do I get?", "Two rounds of changes on each deliverable are included."), ("Do I own the files?", "Yes. You get the final files and the right to use them for your business."), ("Can you shoot product photos or videos?", "I can plan the shoot and brief a photographer; shoot costs are quoted separately at actuals."), ("Can this run with ads?", "Yes. The ad creative pack pairs well with the agency & ads audit or your existing agency.")],
    },
    {
        "slug": "small-business-marketing",
        "need": "sme",
        "nav": "Small business packages",
        "short": "Affordable packages for SMEs and MSMEs. From ₹4,999.",
        "tier": "For small businesses & MSMEs",
        "title": "Senior marketing help, sized for small businesses",
        "seo_title": "Marketing Packages for Small Businesses & MSMEs | Paresh Jain",
        "desc": "Affordable marketing packages for small businesses and MSMEs: a ₹4,999 strategy session, ₹14,999 marketing health check, ₹19,999 local visibility plan (Google, reviews, WhatsApp), ₹34,999 launch & festive sprint and ₹39,999/month marketing advisor.",
        "lede": "The same planning I’ve done for big brands, in smaller, fixed-price packages for founders, shops, clinics, manufacturers and service businesses.",
        "meta": [("From ₹4,999", "fixed price"), ("1 hour to monthly", "pick what fits"), ("No lock-in", "on any package")],
        "packages": [
            {"tier": "One session · 90 minutes", "name": "Strategy session", "price": "₹4,999", "unit": "one-off", "about": "A focused call on your biggest marketing question.", "items": ["90-minute video call with me", "We look at your business, customers and current marketing", "Written summary of your top 5 actions within 2 working days"], "fit": "Good if you want a senior second opinion before you spend.", "cta": "Book a session", "need": "sme_session"},
            {"tier": "One week", "name": "Marketing health check", "price": "₹14,999", "unit": "fixed fee", "about": "A full review of how you’re showing up, and what to fix first.", "items": ["Review of your website, Google Business Profile, social and any ads", "A look at 3 competitors", "A 90-day action plan in priority order", "60-minute walkthrough call"], "fit": "Good if you’re doing a bit of everything and don’t know what’s working.", "cta": "Get a health check", "need": "sme_audit", "pick": True},
            {"tier": "One week", "name": "Local visibility plan", "price": "₹19,999", "unit": "fixed fee", "about": "Get found on Google Maps, Search and WhatsApp, even when people never click through to a website.", "why": "Many customers now decide from the Google listing, reviews and a WhatsApp chat.", "items": ["Google Business Profile review: categories, photos, posts, Q&A", "A simple system to ask for and reply to reviews", "Consistent listings on Justdial, IndiaMART or sector sites", "WhatsApp Business set-up plan: catalogue, quick replies, broadcast rules", "What to track: calls, direction requests, enquiries"], "fit": "Good for shops, clinics, restaurants, showrooms and local service firms.", "cta": "Get found locally", "need": "sme_local"},
            {"tier": "Two weeks", "name": "Launch & festive sprint", "price": "₹34,999", "unit": "fixed fee", "about": "One campaign plan for a launch, sale or festive season, sized for small budgets, including how to keep the new customers.", "items": ["The offer, the message and the idea", "Channel mix: WhatsApp, Instagram, Google, local and offline", "A 4-week content and posting calendar", "Budget split and what to measure", "An after-sale plan to bring festive buyers back"], "fit": "Good if you have a date coming up and want it to land, and last.", "cta": "Plan my campaign", "need": "sme_sprint"},
            {"tier": "Monthly", "name": "Monthly marketing advisor", "price": "₹39,999", "unit": "a month", "about": "A senior marketing advisor on call, without the retainer of an agency.", "items": ["2 strategy calls a month", "WhatsApp access on working days", "A monthly plan and numbers review", "Feedback on your agency’s or freelancer’s work"], "fit": "Good if you have someone doing the work and need someone steering it.", "cta": "Talk about advisory", "need": "sme_advisor"},
        ],
        "for": ["Founder-led businesses, shops, clinics, restaurants, manufacturers and service firms", "You’re spending on marketing but not sure what’s working", "You have a freelancer or small agency and need someone senior steering them", "You want a clear plan you can run with your own team"],
        "not": ["You want someone to post on your behalf every day (see creative services for monthly creatives)", "You need guaranteed sales numbers: nobody honest can promise those"],
        "steps": [("Step 1", "Free 30-minute call", "Tell me about the business and I’ll suggest the right package, or none."), ("Step 2", "Pay & schedule", "Fixed price, agreed in writing. We book the session or kick-off."), ("Step 3", "Plan & actions", "You get a clear, written plan you can act on."), ("Step 4", "Keep going if you like", "Move to monthly advice, or come back when you need me.")],
        "proof": ["amazon", "himalayan", "mg"],
        "price": ("From ₹4,999", "All small business packages are fixed price and exclude GST and any ad spend. The first 30-minute call is free."),
        "faq": [("Why would a big-brand marketer work with small businesses?", "Because the fundamentals are the same: a clear offer, the right customers and a plan. Small businesses usually get the most from senior advice, because every rupee counts."), ("Do you make posts, ads or the website?", "Yes, through the creative and website packages, which I lead with specialist designers and developers. The packages on this page are about planning and advice."), ("Do you work outside Delhi?", "Yes, everything works over video calls and WhatsApp. I’m in New Delhi if something needs to happen in person."), ("Can I upgrade later?", "Yes. If the health check turns into a bigger project, its fee is adjusted against a launch sprint or plan."), ("Do you provide a GST invoice?", "Prices exclude GST, and you get a proper invoice for every package.")],
    },
]

GA = """<script src="/assets/tracking.js"></script>
<script defer src="/assets/consent.js"></script>"""

TRACK = """<script>
(function(){
  function track(name, params){
    try{ if(window.gtag) gtag('event', name, params||{}); }catch(e){}
    try{ if(window.fbq && PJ.META_PIXEL){ if(name==='whatsapp_click'||name==='call_click') fbq('track','Contact',params||{}); else fbq('trackCustom', name, params||{}); } }catch(e){}
  }
  document.addEventListener('click', function(e){
    var a=e.target.closest('[data-track]'); if(!a) return;
    var t=a.dataset.track, name='cta_click';
    if(t.indexOf('whatsapp')>-1) name='whatsapp_click';
    else if(t.indexOf('call')>-1) name='call_click';
    track(name, {cta:t, page:location.pathname});
  });
})();
</script>"""


def e(s):
    return html.escape(s, quote=True)


PERSONA = {"campaign-launch-plan": "brands", "fractional-marketing-lead": "brands", "agency-pitch-account-cover": "agency", "d2c-brand-growth": "d2c", "website-development": "build", "creative-services": "build", "small-business-marketing": "sme"}


def page(s):
    hub = f"/?for={PERSONA[s['slug']]}#services"
    url = f"{SITE}/services/{s['slug']}.html"
    others = "".join(
        f'<a href="/services/{o["slug"]}.html"><b>{e(o["nav"])}</b><span>{e(o["short"])}</span></a>'
        for o in SERVICES if o is not s)
    meta = "".join(f"<li><b>{e(a)}</b><span>{e(b)}</span></li>" for a, b in s["meta"])
    fit = "".join(f"<li>{e(x)}</li>" for x in s["for"])
    nofit = "".join(f"<li>{e(x)}</li>" for x in s["not"])
    steps = "".join(f'<li><span class="when">{e(w)}</span><h3>{e(h)}</h3><p>{e(p)}</p></li>' for w, h, p in s["steps"])
    proof = "".join(
        f"<article><b>{e(PROOF[k][0])}</b><h3>{e(PROOF[k][1])}</h3><p>{e(PROOF[k][2])}</p><small>{e(PROOF[k][3])}</small></article>"
        for k in s["proof"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in s["faq"])
    enquire = f"/?need={s['need']}#contact"

    get_block = ""
    offers = []
    if "get" in s:
        dels = "".join(f'<div class="del"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in s["get"])
        get_block += f"""<section class="sec" id="what-you-get">
  <div class="wrap">
    <h2>What you get</h2>
    <div class="grid-3">{dels}</div>
  </div>
</section>
"""
        num = "".join(ch for ch in s["price"][0] if ch.isdigit())
        offers.append({"@type": "Offer", "name": s["title"], "price": num, "priceCurrency": "INR"})
    if "packages" in s:
        cards = []
        for p in s["packages"]:
            items = "".join(f"<li>{e(i)}</li>" for i in p["items"])
            cls = "pkg pick" if p.get("pick") else "pkg"
            btn = "btn-sun" if p.get("pick") else "btn-ink"
            why = f'<p class="why">{e(p["why"])}</p>' if p.get("why") else ""
            cards.append(
                f'<article class="{cls}" id="{p["need"]}"><p class="tier">{e(p["tier"])}</p><h3>{e(p["name"])}</h3>'
                f'<p class="price">{e(p["price"])} <small>{e(p["unit"])}</small></p><p>{e(p["about"])}</p>{why}'
                f'<ul>{items}</ul><p class="fit">{e(p["fit"])}</p>'
                f'<a class="btn {btn}" href="/?need={p["need"]}#contact" data-track="pkg_{p["need"]}">{e(p["cta"])}</a></article>')
        n = len(cards)
        gcls = "grid-3" if n in (3, 5, 6) else "grid-4"
        get_block += f"""<section class="sec{' white' if 'get' in s else ''}" id="packages">
  <div class="wrap">
    <h2>{e(s.get("pkg_title", "Pick a package"))}</h2>
    <p class="sub">{e(s.get("pkg_sub", "Fixed prices, no lock-in. Not sure which one? Book the free 30-minute call and I’ll tell you honestly, including if you don’t need me."))}</p>
    <div class="{gcls}">{''.join(cards)}</div>
  </div>
</section>
"""
        offers += [{"@type": "Offer", "name": p["name"], "price": "".join(ch for ch in p["price"] if ch.isdigit()), "priceCurrency": "INR"} for p in s["packages"]]

    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Service", "name": s["title"], "description": s["desc"], "url": url,
             "provider": {"@type": "Person", "@id": f"{SITE}/#paresh", "name": "Paresh Jain", "url": f"{SITE}/"},
             "areaServed": "Worldwide", "offers": offers},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "Services", "item": f"{SITE}/#services"},
                {"@type": "ListItem", "position": 3, "name": s["nav"], "item": url}]},
            {"@type": "FAQPage", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faq"]]},
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(s['seo_title'])}</title>
<meta name="description" content="{e(s['desc'])}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<meta name="theme-color" content="#1E2448">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Paresh Jain">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(s['seo_title'])}">
<meta property="og:description" content="{e(s['desc'])}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(s['seo_title'])}">
<meta name="twitter:description" content="{e(s['desc'])}">
<meta name="twitter:image" content="{SITE}/assets/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
{GA}
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="/">Paresh Jain</a>
    <nav class="nav" aria-label="Main">
      <a href="/#work">Work</a>
      <a class="mob-keep" href="{hub}"><span class="lg">Services &amp; prices</span><span class="sm">Services</span></a>
      <a href="/services/small-business-marketing.html">Small business</a>
      <a class="btn btn-sun" href="{BOOK}" target="_blank" rel="noopener" data-track="svcpage_nav_call">Book a free call</a>
    </nav>
  </div>
</header>

<main id="main">
<section class="s-hero">
  <div class="wrap">
    <p class="crumb"><a href="/">Home</a> / <a href="{hub}">Services</a> / {e(s['nav'])}</p>
    <p class="tier">{e(s['tier'])}</p>
    <h1>{e(s['title'])}</h1>
    <p class="lede">{e(s['lede'])}</p>
    <ul class="hero-meta">{meta}</ul>
    <div class="ctas">
      <a class="btn btn-sun" href="{BOOK}" target="_blank" rel="noopener" data-track="svcpage_hero_call">Book a free 30-min call</a>
      <a class="btn btn-line" href="{enquire}" data-track="svcpage_hero_enquire">Send an enquiry</a>
    </div>
    <p class="hero-note">You leave the call with three fixes, whether or not you hire me.</p>
  </div>
</section>

<section class="sec white" id="fit">
  <div class="wrap">
    <h2>Is this right for you?</h2>
    <div class="two">
      <div class="box"><h3>A good fit if</h3><ul class="ticks">{fit}</ul></div>
      <div class="box no"><h3>Probably not if</h3><ul>{nofit}</ul></div>
    </div>
  </div>
</section>

{get_block}

<section class="sec white" id="how">
  <div class="wrap">
    <h2>How it works</h2>
    <ol class="steps">{steps}</ol>
  </div>
</section>

<section class="sec" id="proof">
  <div class="wrap">
    <h2>Work I’ve led</h2>
    <p class="sub">Campaigns from 11+ years inside WPP/VML, FCB Kinnect, Schbang and Cheil.</p>
    <div class="proof">{proof}</div>
    <p class="more"><a href="/#work">See all launches and results →</a> · <a href="{hub}">Compare all packages →</a></p>
  </div>
</section>

<section class="sec white" id="price">
  <div class="wrap">
    <div class="pricebox">
      <div><p class="tier muted">Price</p><p class="price-big">{e(s['price'][0])}</p><p>{e(s['price'][1])}</p></div>
      <a class="btn btn-sun" href="{BOOK}" target="_blank" rel="noopener" data-track="svcpage_price_call">Book a free call</a>
    </div>
  </div>
</section>

<section class="sec" id="faq">
  <div class="wrap">
    <h2>Questions</h2>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="sec white" id="other-services">
  <div class="wrap">
    <h2>Other ways to work with me</h2>
    <div class="others">{others}</div>
  </div>
</section>

<section class="close">
  <div class="wrap">
    <p class="avail">Taking new projects now</p>
    <h2>Tell me the goal. I’ll tell you what I’d do.</h2>
    <p class="lede">Book a free 30-minute call, send a short enquiry, or message me on WhatsApp. I reply within one working day.</p>
    <div class="ctas">
      <a class="btn btn-sun" href="{BOOK}" target="_blank" rel="noopener" data-track="svcpage_close_call">Book a free call</a>
      <a class="btn btn-line" href="{enquire}" data-track="svcpage_close_enquire">Send an enquiry</a>
      <a class="btn btn-line" href="{WA}" target="_blank" rel="noopener" data-track="svcpage_close_whatsapp">WhatsApp</a>
    </div>
    <footer class="foot">
      <span>New Delhi, India · working with teams worldwide</span>
      <nav aria-label="Footer"><a href="/">Home</a><a href="/privacy.html">Privacy</a><a href="https://www.linkedin.com/in/paresh-jain-662b7589/" target="_blank" rel="noopener">LinkedIn</a><span>© 2026 Paresh Jain</span></nav>
    </footer>
  </div>
</section>
</main>

<div class="mbar">
  <a class="btn btn-sun" href="{BOOK}" target="_blank" rel="noopener" data-track="svcpage_mbar_call">Book a free call</a>
  <a class="btn btn-line" href="{WA}" target="_blank" rel="noopener" data-track="svcpage_mbar_whatsapp">WhatsApp</a>
</div>
{TRACK}
</body>
</html>
"""


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for s in SERVICES:
        (OUT / f"{s['slug']}.html").write_text(page(s), encoding="utf-8")
        print("wrote", s["slug"])
