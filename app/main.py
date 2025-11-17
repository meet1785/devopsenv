from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="DevOps-MLOps Playground API",
    description="Simple demo API to practice DevOps + MLOps concepts",
    version="0.1.0",
)


class PredictionInput(BaseModel):
    feature1: float
    feature2: float
    feature3: Optional[float] = 0.0


@app.get("/")
def read_root():
    return {
        "status": "ok",
        "message": "DevOps & MLOps journey started."
    }


@app.post("/predict")
def predict(input_data: PredictionInput):
    """
    Dummy 'ML' logic:
    You will later replace this with a real model.
    For now, it's just a weighted sum + threshold.
    """
    score = input_data.feature1 * 0.4 + input_data.feature2 * 0.4 + input_data.feature3 * 0.2
    label = "positive" if score >= 0.5 else "negative"

    return {
        "score": score,
        "label": label
    }
