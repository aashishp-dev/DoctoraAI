from flask import Flask, send_from_directory, request, jsonify

from agents import (
run_doctoraai,
parse_research,
parse_risk_level,
get_specialist
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

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
