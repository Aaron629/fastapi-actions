from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# 類別編號對應花名
target_names = ["setosa", "versicolor", "virginica"]

class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: InputData):
    X = np.array(data.features).reshape(1, -1)
    prediction = model.predict(X)
    predicted_class = int(prediction[0])
    return {
        "prediction": predicted_class,
        "flower_name": target_names[predicted_class]
    }

@app.get("/")
def read_root():
    return {"message": "這是修改後的版本"}
