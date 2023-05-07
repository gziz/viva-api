from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel
import json

app = FastAPI()
load_dotenv()
from .text_processing import is_valid_string
from .ai import chain


class Feedback(BaseModel):
    feedback: str

@app.post("/analyze-feedback")
def analyze(request: Feedback):

    feedback_str = request.feedback

    if not is_valid_string(feedback_str):
        return {"sentiment": "", "topic": [""]}
        
    res = chain.run(feedback=feedback_str)
    try:
        res = json.loads(res)
    except:
        return {"sentiment": "", "topic": [""]}
