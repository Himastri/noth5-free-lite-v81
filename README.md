# NOTH5 FREE LITE V81 - 2 Controls FREE - FREE of any license

![Banner](NOTH5_FREE_LITE_V81_BANNER.jpg)

Slider 0-100 + Rating 1-5 — Flask — 10 lines — Public Domain UNLICENSE

## Quick Start - 10 lines - No EXE needed

```python
from flask import Flask
app = Flask(__name__)

from noth5_free_lite import render_slider, render_rating

html_slider = render_slider()
html_rating = render_rating()
