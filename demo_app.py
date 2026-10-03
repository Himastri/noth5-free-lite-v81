import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) or '.')
# Now import will work even if sys.path missing current dir
from noth5_free_lite import render_slider, render_rating

html1 = render_slider(value=75, color="#00ff88", size="medium", min_val=0, max_val=100, label="Progress")
html2 = render_slider(value=100, color="#ff4444", size="large", label="Completion")
html3 = render_rating(value=4, color="#00ff88", size="medium", label="Rating")
html4 = render_rating(value=5, color="#ffaa00", size="large", label="Stars")

print("2 controls ready")
print("Slider OK:", "Slider" in html1)
print("Rating OK:", "Rating" in html3)
print(html1[:150])
print(html3[:150])