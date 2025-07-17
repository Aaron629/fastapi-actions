# app/predict.py
from fastapi import APIRouter
from pydantic import BaseModel
import joblib

router = APIRouter()
model = joblib.load("app/model.pkl")

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@router.post("/predict")
def predict(data: IrisData):
    X = [[
        data.sepal_length, data.sepal_width,
        data.petal_length, data.petal_width
    ]]
    y = model.predict(X)
    return {"prediction": int(y[0])}
