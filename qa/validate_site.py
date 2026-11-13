#!/usr/bin/env python3
"""Dependency-free structure and conversion smoke tests for the portfolio."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.anchors = []
        self.images = []
        self.forms = []
        self.labels = []
        self.inputs = []
        self.scripts = []
        self.in_jsonld = False
        self.script_text = ""
        self.headings = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.anchors.append(attrs["href"][1:])
        if tag == "img":
            self.images.append(attrs)
        if tag == "form":
            self.forms.append(attrs)
        if tag == "label":
            self.labels.append(attrs)
        if tag in ("input", "select", "textarea"):
            self.inputs.append(attrs)
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_jsonld = True
            self.script_text = ""

    def handle_data(self, data):
        if self.in_jsonld:
            self.script_text += data

    def handle_endtag(self, tag):
        if tag == "script" and self.in_jsonld:
            self.scripts.append(json.loads(self.script_text))
            self.in_jsonld = False

def main():
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    parser = Audit()
    parser.feed(src)
    failures = []
    def assert_(ok, desc):
        if not ok: failures.append(desc)
    assert_(len(parser.ids) == len(set(parser.ids)), "Duplicate element IDs")
    assert_(not set(parser.anchors).difference(parser.ids), "Broken in-page anchor target")
    assert_(all(i.get("alt") for i in parser.images), "Image missing descriptive alt text")
    assert_(len(parser.forms) == 1, "Expected one contact form")
    assert_(len(parser.labels) >= 3, "Form labels missing")
    assert_(any(i.get("type") == "email" and "required" in i for i in parser.inputs), "Required email input missing")
    assert_(all(i.get("method", "").lower() == "post" for i in parser.forms), "Form must use POST")
    assert_(len(parser.scripts) == 1, "Missing Person structured data")
    assert_(any(x.get("@type") == "Person" for x in parser.scripts), "Unexpected structured data")
    assert_(len(re.findall(r'<article class="project"', src)) == 4, "Four flagship projects missing")
    assert_(len(re.findall(r'class="case-detail"', src)) == 4, "Four expandable case-study stories missing")
    assert_(len(re.findall(r'class="case-open"', src)) == 4, "Case-study controls missing")
    assert_(len(re.findall(r'class="project-stage', src)) == 4, "Editorial project visuals missing")
    assert_(len(re.findall(r'data-open="[^"]+"', src)) == 8, "Missing interactive case-study controls")
    assert_(len(re.findall(r'aria-controls="(ford|coin|amazon|himalayan)-story"', src)) == 4, "Case-study accessibility references missing")
    assert_(len(re.findall(r'<h1\b', src)) == 1, "Expected one primary hero headline")
    assert_('class="hero-graphic"' in src and 'class="marquee"' in src, "Kinetic editorial design modules missing")
    assert_('src="https://www.googletagmanager.com' not in src, "Analytics script must not load by default")
    assert_('prefers-reduced-motion' in src, "Reduced motion handling missing")
    assert_('id="contact"' in src and 'mailto:' in src, "Contact fallback missing")
    assert_('localStorage.getItem(key)' in src, "Analytics consent handling missing")
    assert_('G-XV39SFSW40' in src, "Analytics property not configured")
    assert_((ROOT / "robots.txt").exists(), "robots.txt missing")
    assert_((ROOT / "sitemap.xml").exists(), "sitemap.xml missing")
    if (ROOT / "sitemap.xml").exists():
        ET.parse(ROOT / "sitemap.xml")
    if failures:
        for issue in failures: print("FAIL", issue)
        raise SystemExit(1)
    print("PASS: structure, accessibility foundations, SEO, consent, contact fallbacks, cases.")

if __name__ == "__main__":
    main()
