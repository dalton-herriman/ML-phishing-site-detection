from fastapi import FastAPI, Query
from src.capture import capture_page
from src.predict import predict_url

app = FastAPI()

@app.get("/detect")
def detect(url: str = Query(...)):
    capture_page(url, out_path="output")
    result = predict_url("output")
    return result
