from noth5_free_lite import render_slider, render_rating

print("=== Slider variants ===")
for size in ["small","medium","large"]:
  for val, color in [(25,"#00ff88"), (75,"#ffaa00"), (100,"#ff4444")]:
    html = render_slider(value=val, color=color, size=size, label=f"Task {val}%")
    print(f"{size} {val}% {color} -> {len(html)} chars OK")

print("\n=== Rating variants ===")
for v in [1,2,3,4,5]:
  html = render_rating(value=v, color="#00ff88", size="medium", label=f"Review {v}")
  print(f"Rating {v}/5 -> {'★' * v} OK")