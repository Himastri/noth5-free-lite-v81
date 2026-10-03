from noth5_free_lite import render_control

def chatbot_reply(user_msg):
    low = user_msg.lower()
    if "progress" in low or "slider" in low:
        return render_control("slider", value=75, color="#00ff88", size="medium", label="Progress")
    if "star" in low or "rating" in low:
        return render_control("rating", value=4, color="#ffaa00", size="large", label="Customer Rating")
    return "Type 'show progress' or 'show rating'"

# Simulate chatbot
for msg in ["show progress", "show rating"]:
    html = chatbot_reply(msg)
    print(f"User: {msg}\nBot HTML: {html[:200]}...\n")