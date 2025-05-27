from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    return {"message": "Hello, world!"}