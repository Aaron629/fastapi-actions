from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Cloud Run is working!"}


