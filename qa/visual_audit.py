#!/usr/bin/env python3
"""Browser-level visual and interaction smoke tests for editorial portfolio."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "qa" / "screenshots"
OUT.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
    try:
        for name, width, height, device in [
            ("desktop", 1440, 900, False),
            ("mobile", 390, 844, True),
            ("tablet", 768, 1024, False),
        ]:
            context = browser.new_context(
                viewport={"width": width, "height": height},
                device_scale_factor=1,
                is_mobile=device,
                has_touch=device,
                reduced_motion="reduce",
            )
            page = context.new_page()
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto((ROOT / "index.html").as_uri(), wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(1800)
            assert page.locator("h1").count() == 1, f"{name}: heading count"
            assert page.locator("article.project").count() == 4, f"{name}: featured projects"
            assert page.locator("#heroTitle").is_visible(), f"{name}: hero hidden"
            assert page.locator(".hero-title .line").first.evaluate("(el) => el.scrollWidth <= el.clientWidth + 2"), f"{name}: clipped hero headline"
            assert page.locator(".contact .email-link").count() == 1, f"{name}: contact fallback"
            assert page.locator(".brief-form").evaluate("(form) => !form.checkValidity()"), f"{name}: required contact fields"
            overflow = page.evaluate("document.documentElement.scrollWidth - window.innerWidth")
            if overflow > 2:
                offenders = page.evaluate("""() => Array.from(document.querySelectorAll('body *')).map(el => {
                    let b=el.getBoundingClientRect();
                    return {tag:el.tagName, cls:String(el.className).slice(0,90), right:Math.round(b.right), left:Math.round(b.left), width:Math.round(b.width)};
                }).filter(x => x.right > innerWidth + 2 || x.left < -2).slice(0,20)""")
                print("OVERFLOW_DIAGNOSTIC", name, offenders, flush=True)
            assert overflow <= 2, f"{name}: horizontal overflow {overflow}px"
            assert not errors, f"{name}: JS errors {errors}"
            if name in ("desktop","mobile"):
                page.screenshot(path=str(OUT / (name + "-hero.jpg")), type="jpeg", quality=82)
                page.locator("#project-ford").scroll_into_view_if_needed()
                page.wait_for_timeout(300)
                page.screenshot(path=str(OUT / (name + "-work.jpg")), type="jpeg", quality=82)
            first = page.locator('button[data-open="ford-story"]')
            first.scroll_into_view_if_needed()
            first.click()
            assert page.locator("#ford-story").is_visible(), f"{name}: case failed to open"
            assert first.get_attribute("aria-expanded") == "true", f"{name}: case aria not expanded"
            first.click()
            assert not page.locator("#ford-story").is_visible(), f"{name}: case failed to close"
            if name == "mobile":
                menu = page.locator("#navToggle")
                menu.click()
                assert menu.get_attribute("aria-expanded") == "true", "Mobile menu state"
                assert page.locator("#navlinks").is_visible(), "Mobile nav invisible"
                page.locator('#navlinks a[href="#services"]').click()
                assert menu.get_attribute("aria-expanded") == "false", "Menu should close after navigation"
            print("PASS", name, width, height, "case toggle, contact fields, anchors, responsive overflow, JS")
            context.close()
    finally:
        browser.close()
