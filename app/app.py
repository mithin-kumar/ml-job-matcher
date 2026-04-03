from fastapi import FastAPI, UploadFile
import shutil
from app.parser import extract_text
from app.matcher import match

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Matcher Running"}

@app.post("/match")
async def match_resume(file: UploadFile):

    temp_file = f"temp_{file.filename}"

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(temp_file)
    result = match(text)

    return result.to_dict()
