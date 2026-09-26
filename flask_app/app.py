from flask import Flask, render_template, request
import os
from detector import detect_vehicles

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        video = request.files["video"]
        path = os.path.join("uploads", video.filename)
        video.save(path)
        output = detect_vehicles(path)
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
