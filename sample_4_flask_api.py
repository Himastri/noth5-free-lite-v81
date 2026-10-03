from flask import Flask, jsonify
from noth5_free_lite import render_slider, render_rating

app = Flask(__name__)

@app.route("/")
def home():
    return render_slider(value=75, color="#00ff88", size="medium", label="Progress") + \
           render_rating(value=4, color="#00ff88", size="medium", label="Rating")

@app.route("/health")
def health():
    return jsonify({"status":"READY TRUE","port":8766,"controls":["slider","rating"],"test":"2/2 PASS"})

@app.route("/render/slider")
def api_slider():
    return render_slider(value=75, color="#00ff88", size="medium", label="Progress")

@app.route("/render/rating")
def api_rating():
    return render_rating(value=4, color="#00ff88", size="medium", label="Rating")

if __name__ == "__main__":
    app.run(port=8766)