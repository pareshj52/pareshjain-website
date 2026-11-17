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
        "proof": ["ford", "bata", "honda"],
        "price": ("From ₹15,000 a day", "Billed by the day, with a written scope first. Prices exclude GST. Agencies outside India are quoted in USD."),
        "faq": [("Will you work under our agency’s name?", "Yes. White-label is fine, and I keep client work confidential."), ("How much notice do you need?", "Tell me the deadline. For pitches, a few days’ notice is usually enough to start."), ("Which agencies have you worked in?", "WPP/VML, FCB Kinnect, Schbang and Cheil, among six agencies over 11+ years.")],
    },
    {
        "slug": "small-business-marketing",
        "need": "sme",
        "nav": "Small business packages",
        "short": "Affordable packages for SMEs and MSMEs. From ₹4,999.",
        "tier": "For small businesses & MSMEs",
        "title": "Senior marketing help, sized for small businesses",
        "seo_title": "Marketing Packages for Small Businesses & MSMEs | Paresh Jain",
        "desc": "Affordable marketing packages for small businesses and MSMEs: a ₹4,999 strategy session, a ₹14,999 marketing health check, a ₹34,999 launch sprint and a ₹39,999/month marketing advisor.",
        "lede": "The same planning I’ve done for big brands, in smaller, fixed-price packages for founders, shops, clinics, manufacturers and service businesses.",
        "meta": [("From ₹4,999", "fixed price"), ("1 hour to monthly", "pick what fits"), ("No lock-in", "on any package")],
        "packages": [
            {"tier": "One session · 90 minutes", "name": "Strategy session", "price": "₹4,999", "unit": "one-off", "about": "A focused call on your biggest marketing question.", "items": ["90-minute video call with me", "We look at your business, customers and current marketing", "Written summary of your top 5 actions within 2 working days"], "fit": "Good if you want a senior second opinion before you spend.", "cta": "Book a session", "need": "sme_session"},
            {"tier": "One week", "name": "Marketing health check", "price": "₹14,999", "unit": "fixed fee", "about": "A full review of how you’re showing up, and what to fix first.", "items": ["Review of your website, Google Business Profile, social and any ads", "A look at 3 competitors", "A 90-day action plan in priority order", "60-minute walkthrough call"], "fit": "Good if you’re doing a bit of everything and don’t know what’s working.", "cta": "Get a health check", "need": "sme_audit", "pick": True},
            {"tier": "Two weeks", "name": "Launch & festive sprint", "price": "₹34,999", "unit": "fixed fee", "about": "One campaign plan for a launch, sale or festive season, sized for small budgets.", "items": ["The offer, the message and the idea", "Channel mix: WhatsApp, Instagram, Google, local and offline", "A 4-week content and posting calendar", "Budget split and what to measure"], "fit": "Good if you have a date coming up and want it to land.", "cta": "Plan my campaign", "need": "sme_sprint"},
            {"tier": "Monthly", "name": "Monthly marketing advisor", "price": "₹39,999", "unit": "a month", "about": "A senior marketing advisor on call, without the retainer of an agency.", "items": ["2 strategy calls a month", "WhatsApp access on working days", "A monthly plan and numbers review", "Feedback on your agency’s or freelancer’s work"], "fit": "Good if you have someone doing the work and need someone steering it.", "cta": "Talk about advisory", "need": "sme_advisor"},
        ],
        "for": ["Founder-led businesses, shops, clinics, restaurants, manufacturers and service firms", "You’re spending on marketing but not sure what’s working", "You have a freelancer or small agency and need someone senior steering them", "You want a clear plan you can run with your own team"],
        "not": ["You want someone to make and post your content every day (I plan and steer, not produce)", "You need guaranteed sales numbers: nobody honest can promise those"],
        "steps": [("Step 1", "Free 30-minute call", "Tell me about the business and I’ll suggest the right package, or none."), ("Step 2", "Pay & schedule", "Fixed price, agreed in writing. We book the session or kick-off."), ("Step 3", "Plan & actions", "You get a clear, written plan you can act on."), ("Step 4", "Keep going if you like", "Move to monthly advice, or come back when you need me.")],
        "proof": ["amazon", "himalayan", "mg"],
        "price": ("From ₹4,999", "All small business packages are fixed price and exclude GST and any ad spend. The first 30-minute call is free."),
        "faq": [("Why would a big-brand marketer work with small businesses?", "Because the fundamentals are the same: a clear offer, the right customers and a plan. Small businesses usually get the most from senior advice, because every rupee counts."), ("Do you make posts, ads or the website?", "No. I plan, prioritise and steer. I can recommend freelancers and agencies, and review their work on the monthly package."), ("Do you work outside Delhi?", "Yes, everything works over video calls and WhatsApp. I’m in New Delhi if something needs to happen in person."), ("Can I upgrade later?", "Yes. If the health check turns into a bigger project, its fee is adjusted against a launch sprint or plan."), ("Do you provide a GST invoice?", "Prices exclude GST, and you get a proper invoice for every package.")],
    },
]

GA = """<script>window.PJ = { GA4: 'G-XV39SFSW40', META_PIXEL: '' };</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XV39SFSW40"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', PJ.GA4);
  if (PJ.META_PIXEL) {
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', PJ.META_PIXEL); fbq('track', 'PageView');
  }
</script>"""

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


def page(s):
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

    if "packages" in s:
        cards = []
        for p in s["packages"]:
            items = "".join(f"<li>{e(i)}</li>" for i in p["items"])
            cls = "pkg pick" if p.get("pick") else "pkg"
            btn = "btn-sun" if p.get("pick") else "btn-ink"
            cards.append(
                f'<article class="{cls}"><p class="tier">{e(p["tier"])}</p><h3>{e(p["name"])}</h3>'
                f'<p class="price">{e(p["price"])} <small>{e(p["unit"])}</small></p><p>{e(p["about"])}</p>'
                f'<ul>{items}</ul><p class="fit">{e(p["fit"])}</p>'
                f'<a class="btn {btn}" href="/?need={p["need"]}#contact" data-track="pkg_{p["need"]}">{e(p["cta"])}</a></article>')
        get_block = f"""<section class="sec" id="packages">
  <div class="wrap">
    <h2>Pick a package</h2>
    <p class="sub">Fixed prices, no lock-in. Not sure which one? Book the free 30-minute call and I’ll tell you honestly, including if you don’t need me.</p>
    <div class="grid-4">{''.join(cards)}</div>
  </div>
</section>"""
        offers = [{"@type": "Offer", "name": p["name"], "price": p["price"].replace("₹", "").replace(",", ""), "priceCurrency": "INR"} for p in s["packages"]]
    else:
        dels = "".join(f'<div class="del"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in s["get"])
        get_block = f"""<section class="sec" id="what-you-get">
  <div class="wrap">
    <h2>What you get</h2>
    <div class="grid-3">{dels}</div>
  </div>
</section>"""
        num = "".join(ch for ch in s["price"][0] if ch.isdigit())
        offers = [{"@type": "Offer", "price": num, "priceCurrency": "INR"}]

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
<meta name="twitter:card" content="summary_large_image">
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
      <a href="/#services">Services &amp; prices</a>
      <a href="/services/small-business-marketing.html">Small business</a>
      <a class="btn btn-sun" href="{BOOK}" target="_blank" rel="noopener" data-track="svcpage_nav_call">Book a free call</a>
    </nav>
  </div>
</header>

<main id="main">
<section class="s-hero">
  <div class="wrap">
    <p class="crumb"><a href="/">Home</a> / <a href="/#services">Services</a> / {e(s['nav'])}</p>
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
    <p class="more"><a href="/#work">See all launches and results →</a></p>
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
