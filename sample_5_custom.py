from noth5_free_lite import render_slider, render_rating

# Exact replica of your EXE screenshot V81 FREE LITE 2/2 PASS
html_rating = render_rating(value=4, color="#00ff88", size="medium", label="Rating 4/5")
html_slider = render_slider(value=75, color="#00ff88", size="medium", label="Slider 75% = PENDING")

# Save to HTML file to open in browser like chatbot bubble
with open("sample_output.html","w",encoding="utf-8") as f:
    f.write(f"<html><body style='background:#0a0a0a;padding:20px'>{html_rating}<br>{html_slider}</body></html>")

print("Created sample_output.html - open in browser - looks like your EXE screenshot!")