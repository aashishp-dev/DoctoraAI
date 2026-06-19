# 🏥 DoctoraAI

**A multi-agent medical AI system that orchestrates specialist AI agents to deliver validated, cross-checked health insights.**

Built for the **INDIA.RUNS Redrob x H2S** — Track 2: Ideathon Challenge.

<p align="center">
  <a href="https://doctora-ai.vercel.app/"><strong> Link🔗</strong></a>•
  <a href="#how-it-works"><strong>How It Works</strong></a> •
  <a href="#tech-stack"><strong>Tech Stack</strong></a> •
  <a href="#-getting-started"><strong>Getting Started</strong></a>
</p>

---

##  What is DoctoraAI?

DoctoraAI isn't just another AI chatbot wrapper. It's an **"Echo Chamber" multi-agent system** — instead of a single AI guessing at a diagnosis, three independent specialist agents analyze the same query from different angles, and a fourth **Validator Agent** cross-checks their outputs before producing a final, synthesized response.

This mirrors how real clinical decision-making benefits from second opinions — except it happens in seconds.

> ⚠️ **Disclaimer:** DoctoraAI is an informational prototype only. It is not a substitute for professional medical advice, diagnosis, or treatment.

---

## How It Works

```
                         ┌─────────────────────┐
                         │     User Query      │
                         │ "headache + fever   │
                         │  for 2 days"        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────┐
                │         Orchestration Layer       │
                └───────────────────────────────────┘
                    │             │              │
                    ▼             ▼              ▼
            ┌──────────┐  ┌──────────────┐  ┌────────────┐
            │ Agent A  │  │   Agent B    │  │  Agent C   │
            │Diagnosis │  │  Treatment   │  │  Research  │
            └────┬─────┘  └──────┬───────┘  └─────┬──────┘
                 │               │                │
                 └───────────────┼────────────────┘
                                 ▼
                      ┌───────────────────── ┐
                      │   Validator Agent    │
                      │  Cross-checks all 3, │
                      │flags contradictions, │
                      │ outputs risk level & │
                      │recommended specialist│
                      └──────────┬───────────┘
                                 ▼
                      ┌─────────────────────┐
                      │  Final Response     │
                      │ + Risk Level Badge  │
                      │ + Research Citations│
                      │ + Nearby Specialist │
                      └─────────────────────┘
```

### The Four Agents

| Agent | Role |
|---|---|
|  **Diagnosis Agent** | Analyzes symptoms, lists possible conditions by likelihood |
|  **Treatment Agent** | Suggests general treatment approaches, flags dangerous combinations |
|  **Research Agent** | Surfaces relevant medical literature with real source links |
|  **Validator Agent** | Synthesizes all three, resolves contradictions, assigns risk level |

---

## Features

-  **Multi-agent orchestration** — not a single LLM call, but coordinated specialist reasoning
-  **Voice input** — speak your symptoms instead of typing
-  **Dynamic risk assessment** — AI-determined Low/Moderate/High risk, not keyword guessing
-  **Linked research cards** — real, clickable references to medical literature
-  **Nearby specialist finder** — geolocation-based suggestion of the right doctor type to see
-  **Clean, dark-themed UI** — built with Tailwind, designed in Google Stitch

---

## Tech Stack

| Layer | Technology |
|---|---|
| **AI Inference** | [Groq API](https://groq.com/) — Llama 3.3 70B Versatile |
| **Backend** | Python, Flask |
| **Frontend** | HTML, Tailwind CSS, Vanilla JS |
| **Voice Input** | Web Speech API |
| **Deployment** | Vercel |
| **Design** | Google Stitch |

---

## 📁 Project Structure

```
DoctoraAI/
├── agents.py           # Multi-agent orchestration logic
├── app.py               # Flask backend & API routes
├── templates/
│   └── index.html       # Frontend UI
├── requirements.txt      # Python dependencies
├── vercel.json           # Deployment config
└── .env                  # API keys (not committed)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A free [Groq API key](https://console.groq.com/keys)

### Installation

```bash
# Clone the repo
git clone https://github.com/Mayank007-ahjin/DoctoraAI.git
cd DoctoraAI

# Install dependencies
pip install -r requirements.txt

# Add your API key
echo "GROQ_API_KEY=your_key_here" > .env

# Run locally
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## TO do Roadmap

- [ ] Lab report (PDF) upload — agents read and analyze actual medical documents
- [ ] Embedded map view for nearby specialists

---

## 👤 Author

**Mayank Karnatak**
B.Tech Student, GL Bajaj Institute

---

## 🤝 Contributors
Thanks to amazing contributors!

[![DoctoraAI Contributors](https://contrib.rocks/image?repo=Mayank007-ahjin/DoctoraAI)](https://github.com/Mayank007-ahjin/DoctoraAI/graphs/contributors)

---

## 📄 License

This project was built for hackathon submission purposes.
