import pickle
from typing import Any, Dict
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, ConfigDict, Field
from typing import Literal

class Salarie(BaseModel):
    lead_source: Literal[
        "paid_ads", 
        "organic_search"
    ]
    number_of_courses_viewed: int = Field(..., ge=0)
    annual_income: float = Field(..., ge=0.0)

class PredictResponse(BaseModel):
    probability: float
    converted: bool

app = FastAPI(title="convert")

with open('pipeline_v2.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

@app.get("/ping")
def convert():
    return "waaf!"

@app.post("/predict")
def predict(salarie: Salarie)-> PredictResponse:
    proba = pipeline.predict_proba(salarie.model_dump())[0,1]
    return PredictResponse(
        probability = proba,
        converted = bool(proba>= 0.5)      
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9697)