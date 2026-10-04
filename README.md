# Chatbots can only show text. Now you can put a slider and star rating *inside* the chat message itself.

**Live Demo - No Install - See it inside bubble right now:**
**https://huggingface.co/spaces/Nagendra75/noth5-free-lite**

![Banner](NOTH5_FREE_LITE_V81_BANNER.jpg)

## The thing missing from every chatbot

Botpress, Voiceflow, Chatbase - they only show text inside the bubble. If you want a slider or rating, you have to build it outside as a separate webpage.

We built it so the control lives and works **inside the bubble itself**.

This gives you 2 controls to try inside your chatbot bubble:

- **Slider 0-100** - Users drag and pick a number inside the chat message. Smooth, live, no page reload.
- **Rating 1-5** - Users tap stars inside the chat message. Shows 4.5/5 instantly.

Both render **inside** the bubble, not outside.

## Try it live - No download, 10 seconds

**https://huggingface.co/spaces/Nagendra75/noth5-free-lite**

No install. No pip. See it working inside bubble before you download.

## Install - 10 lines - No EXE needed

pip install noth5-free-lite==81.2.0

from flask import Flask
app = Flask(__name__)

from noth5_free_lite import render_slider, render_rating

html_slider = render_slider()
html_rating = render_rating()

Put html_slider and html_rating inside your chatbot bubble HTML. It works inside.

## Quick Start

- sample_1_basic.py - Basic slider and rating inside bubble
- sample_3_chatbot_bubble.py - How to put it inside a real chatbot message
- sample_4_flask_api.py - Flask integration

## Is it safe to download?

- Code-signed - Windows shows verified publisher
- VirusTotal 0/70 - Scanned by 70 antivirus, 0 threats
- Portable - No admin, no install, runs in folder
- Works offline - No hidden network calls
- Open wrapper - Read demo_app.py to see how it renders inside bubble
- SHA256 published - Verify file

This does only one thing: render slider and rating inside chat bubble.

## Free for any project

Public Domain UNLICENSE - use for personal, commercial, anything.

From NOTH5 Factory Labs
Email: nagendra.prasadbk@gmail.com
GitHub: https://github.com/Himastri/noth5-free-lite-v81
Live Demo: https://huggingface.co/spaces/Nagendra75/noth5-free-lite
