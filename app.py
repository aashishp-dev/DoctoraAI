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

    print("🚀 Prescription route started")

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    print("📄 File received:", file.filename)

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
        print("📋 OCR Text:")
        print(text)

    else:
        return jsonify({
            "error": "Unsupported file type"
        }), 400

    try:
        print("🤖 Calling Groq...")
        analysis = ask_agent(
"""
You are a prescription analyzer.

Extract all medicines from the prescription.

Return ONLY in this format:

MEDICINE:
PURPOSE:
DOSE:
TIMING:
DURATION:
WARNING:
""",
            text
        )
        print("✅ AI Response:")
        print(analysis)
        return jsonify({
            "analysis": analysis
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

    except Exception as e:

     return jsonify({
        "error": str(e)
    }), 500

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001
    )

    