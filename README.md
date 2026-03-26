# OvaSense — AI PCOS/PCOD Risk Screening System

## Overview
OvaSense is an AI-powered web application that provides early risk screening for PCOS (Polycystic Ovary Syndrome) and PCOD (Polycystic Ovarian Disease).

The system uses clinical symptoms, lifestyle data, and conversational input to:
- Estimate PCOS and PCOD risk
- Provide explainable insights ("Why this score?")
- Recommend lifestyle improvements
- Simulate how risk changes based on behavior

## Features
- Voice-enabled chatbot input
- Real-time risk calculation
- PCOS vs PCOD risk comparison
- Explainability engine
- Personalized recommendations
- What-if simulation
- Risk tracking over time

## Tech Stack
- Backend: FastAPI (Python)
- Database: MongoDB
- AI/NLP: OpenAI API
- Frontend: React (planned)

## How to Run
### Backend
uvicorn server:app --host 0.0.0.0 --port 8000

### Frontend
Open index.html with Live Server

## Features
- AI-based PCOS risk prediction
- Lifestyle analysis
- Acne detection (OpenCV)
- Real-time scoring

```bash
pip install -r requirements.txt
uvicorn main:app --reload
