# 🏥 DoctoraAI

### AI-Powered Multi-Agent Healthcare Assistant

DoctoraAI is an intelligent healthcare platform that leverages multiple specialized AI agents to analyze symptoms, validate findings, assess risk levels, recommend specialists, and provide research-backed medical insights.

Built for the **INDIA.RUNS Redrob x H2S Hackathon**.

<p align="center">
  <a href="https://doctora-ai.vercel.app/"><strong> Link🔗</strong></a>•
  <a href="#how-it-works"><strong>How It Works</strong></a> •
  <a href="#tech-stack"><strong>Tech Stack</strong></a> •
  <a href="#-getting-started"><strong>Getting Started</strong></a>
</p>

---

## 🚀 Problem Statement

Millions of people rely on generic AI chatbots for medical guidance. Traditional systems provide a single response with limited validation, increasing the risk of misinformation.

DoctoraAI solves this by introducing a **multi-agent medical intelligence system** where multiple AI specialists independently analyze symptoms before a validator agent synthesizes the final response.

---

# 🧠 How DoctoraAI Works

```text
User Symptoms
      │
      ▼
┌─────────────────────┐
│ Diagnosis Agent     │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Treatment Agent     │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Research Agent      │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Validator Agent     │
└──────────┬──────────┘
           │
           ▼
Final Verified Response
```

---

# ✨ Features

### 🩺 Multi-Agent Medical Analysis

Multiple AI agents independently analyze the user's symptoms to improve reliability.

### 📊 Dynamic Risk Assessment

The Validator Agent assigns:

* Low Risk
* Moderate Risk
* High Risk

based on symptom severity and duration.

### 📚 Medical Research Integration

Provides relevant PubMed research references and summaries related to the user's symptoms.

### 🎤 Voice Symptom Input

Users can describe symptoms through speech using browser voice recognition.

### 👨‍⚕️ Recommended Specialist

Automatically recommends the most suitable medical specialist:

* Neurologist
* Cardiologist
* Dermatologist
* Pulmonologist
* Orthopedic
* Gastroenterologist
* Psychiatrist
* General Physician

### 📍 Nearby Doctor Finder

One-click Google Maps integration to locate nearby specialists instantly.

### ⚡ Modern Interactive UI

* Animated startup sequence
* Floating medical elements
* Symptom scanner animation
* Medical dashboard design
* Fully responsive interface

---

# 🛠 Tech Stack

## Frontend

* HTML5
* Tailwind CSS
* Vanilla JavaScript

## Backend

* Python
* Flask

## AI Layer

* Groq API
* Llama 3.3 70B Versatile

## Research Sources

* PubMed

## Deployment

* Vercel

---

# 📂 Project Structure

```text
DoctoraAI
│
├── app.py
├── agents.py
├── requirements.txt
├── vercel.json
│
└── templates
    └── index.html
```

---

# 🔄 Multi-Agent Architecture

| Agent           | Responsibility                                        |
| --------------- | ----------------------------------------------------- |
| Diagnosis Agent | Identifies possible conditions                        |
| Treatment Agent | Suggests treatment approaches                         |
| Research Agent  | Retrieves research-backed insights                    |
| Validator Agent | Cross-checks all outputs and generates final response |

---

# 🎯 Key Innovations

✅ Multi-Agent Reasoning

✅ Cross-Agent Validation

✅ Research-Based Insights

✅ Specialist Recommendation

✅ Google Maps Doctor Discovery

✅ Voice-Based Symptom Entry

✅ Risk Classification System

---

# ⚠ Disclaimer

DoctoraAI is designed for informational and educational purposes only.

It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a licensed healthcare professional regarding medical concerns.

---

# 👨‍💻 Team

### Event Horizon

GL Bajaj Institute of Technology and Management

Built with AI, Healthcare, and Accessibility in mind.


## 📄 License

This project was built for hackathon submission purposes.
