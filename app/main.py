from fastapi import FastAPI
from pydantic import BaseModel
from app.summarizer import summarize_text

app = FastAPI(title="AI Text Summarizer API")

class TextRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30
    mode: str = "concise"

@app.post("/summarize/")
async def summarize(request: TextRequest):
    summary = summarize_text(
        text=request.text,
        max_length=request.max_length,
        min_length=request.min_length,
        mode=request.mode
    )
    return {"summary": summary}
