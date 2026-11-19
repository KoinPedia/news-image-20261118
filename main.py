#!/usr/bin/env python3
"""Render the 18 November 2026 world news front page as a 1920x1080 PNG."""
import pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
HTML = ROOT / 'build' / 'src.html'
OUT = ROOT / 'build' / 'news-image-20261118.png'


with sync_playwright() as p:
    b = p.chromium.launch(args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1)
    pg.goto(HTML.resolve().as_uri())
    pg.wait_for_timeout(500)
    pg.screenshot(path=str(OUT))
    b.close()

Image.open(OUT).save(OUT)
print('saved', OUT, Image.open(OUT).size)
