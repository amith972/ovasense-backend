from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import os

# -----------------------------
# OPTIONAL: MongoDB
# -----------------------------
try:
    from pymongo import MongoClient
    MONGO_URI = os.getenv("MONGO_URI", "")
    client = MongoClient(MONGO_URI) if MONGO_URI else None
    db = client["ovasense"] if client else None
    collection = db["logs"] if db else None
except:
    collection = None

# -----------------------------
# FASTAPI INIT
# -----------------------------
app = FastAPI()

# ✅ CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for hackathon
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# REQUEST MODEL
# -----------------------------
class UserInput(BaseModel):
    user_id: str
    age: int
    height: float
    weight: float
    cycle: str
    exercise: int
    sleep: int
    stress: int
    diet: str

# -----------------------------
# RISK CALCULATION
# -----------------------------
def calculate_risk(data):
    risk = 0
    reasons = []

    # BMI
    bmi = data.weight / ((data.height / 100) ** 2)

    if bmi > 25:
        risk += 15
        reasons.append("High BMI")

    # Cycle
    if data.cycle.lower() == "irregular":
        risk += 20
        reasons.append("Irregular cycles")

    # Sleep
    if data.sleep < 6:
        risk += 10
        reasons.append("Poor sleep")

    # Exercise
    if data.exercise < 2:
        risk += 10
        reasons.append("Low activity")

    # Stress
    if data.stress > 3:
        risk += 10
        reasons.append("High stress")

    return min(risk, 100), reasons

# -----------------------------
# API ROUTE
# -----------------------------
@app.post("/chat-input")
def chat_input(user: UserInput):
    print("ROUTE HIT")

    risk, reasons = calculate_risk(user)

    response = {
        "pcos_risk": risk,
        "final_risk": risk,
        "reasons": reasons,
        "recommendations": [
            "Improve sleep schedule",
            "Exercise regularly",
            "Maintain balanced diet"
        ]
    }

    # -----------------------------
    # SAVE TO MONGODB (if available)
    # -----------------------------
    if collection:
        try:
            log = {
                "user_id": user.user_id,
                "input": user.dict(),
                "result": response,
                "timestamp": datetime.utcnow()
            }
            inserted = collection.insert_one(log)
            print("INSERTED:", inserted.inserted_id)
        except Exception as e:
            print("DB ERROR:", e)

    return response


# -----------------------------
# ROOT (optional)
# -----------------------------
@app.get("/")
def home():
    return {"status": "OvaSense backend running"}