from noth5_free_lite import render_slider, render_rating

html_slider = render_slider(value=75, color="#00ff88", size="medium", label="Progress")
html_rating = render_rating(value=4, color="#00ff88", size="medium", label="Rating")

print("2 controls ready")
print(html_slider)
print(html_rating)