from flask import Flask, send_from_directory, request, jsonify

from agents import (
    run_doctoraai,
    parse_research,
    parse_risk_level,
    get_specialist,
    ask_agent
)

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({
            "error": "No query provided"
        }), 400

    diagnosis, treatment, research, final = run_doctoraai(user_query)
    papers = parse_research(research)
    risk, clean_final = parse_risk_level(final)
    specialist = get_specialist(user_query)

    return jsonify({
        "final": clean_final,
        "risk": risk,
        "papers": papers,
        "specialist": specialist
    })

import fitz
import pytesseract
import os

if os.path.exists("/opt/homebrew/bin/tesseract"):
    pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
from PIL import Image

@app.route("/upload-lab", methods=["POST"])
def upload_lab():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    text = ""

    if file.filename.endswith(".pdf"):

        pdf = fitz.open(
            stream=file.read(),
            filetype="pdf"
        )

        for page in pdf:
            text += page.get_text()

    elif file.filename.lower().endswith(
        (".png", ".jpg", ".jpeg")
    ):

        image = Image.open(file)
        text = pytesseract.image_to_string(image)

    else:
        return jsonify({
            "error": "Unsupported file type"
        }), 400

    analysis = ask_agent(
        """
You are a medical lab report analyzer.

Analyze the report and provide:

1. Summary
2. Abnormal values
3. Possible concerns
4. Recommended specialist

Keep it short and clear.
        """,
        text
    )

    return jsonify({
        "analysis": analysis
    })



# ADD THIS HERE 👇

@app.route("/upload-prescription", methods=["POST"])
def upload_prescription():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    text = ""

    if file.filename.endswith(".pdf"):

        pdf = fitz.open(
            stream=file.read(),
            filetype="pdf"
        )

        for page in pdf:
            text += page.get_text()

    elif file.filename.lower().endswith(
        (".png", ".jpg", ".jpeg")
    ):

        image = Image.open(file)
        text = pytesseract.image_to_string(image)

    else:
        return jsonify({
            "error": "Unsupported file type"
        }), 400

    analysis = ask_agent(
"""
You are a prescription analyzer.

Return ONLY in this format:

MEDICINE: [name]
PURPOSE: [purpose]
DOSE: [dose]
TIMING: [timing]
DURATION: [duration]
WARNING: [important warning]

Example:

MEDICINE: Amoxicillin
PURPOSE: Antibiotic
DOSE: 500mg
TIMING: 1-1-1 after food
DURATION: 5 days
WARNING: Complete full course. Avoid skipping doses.

MEDICINE: Levocetirizine
PURPOSE: Allergy Relief
DOSE: 5mg
TIMING: At night
DURATION: 5 days
WARNING: May cause drowsiness.

Return only this format.
""",
text
)



    return jsonify({
        "analysis": analysis
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001
    )
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001
    )
    