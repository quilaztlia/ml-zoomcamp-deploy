import pickle
from typing import Any, Dict
#from fastapi import FastAPI
#import uvicorn
from pydantic import BaseModel, ConfigDict, Field
from typing import Literal

class Salarie(BaseModel):
    lead_source: Literal[
        "paid_ads", 
    ]
    number_of_courses_viewed: int = Field(..., ge=0)
    annual_income: float = Field(..., ge=0.0)

class PredictResponse(BaseModel):
    probability: float
    converted: bool

with open('pipeline_v1.bin', 'rb') as f_in:
        pipeline = pickle.load(f_in)


salarie = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}
result = pipeline.predict_proba(salarie)[0,1]

print(result)