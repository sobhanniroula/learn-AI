from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

app = FastAPI()

class ReviewRequest(BaseModel):
    text: str

# What Gemini gives back, and what we send to the caller.
# We keep it small on purpose, so that fewer tokens are used.
class AnalysisResponse(BaseModel):
    label: str # postive, negative, or neutral
    score: int # 1 (very bad) to 5 (very good)
    theme: str # one word: what the review is mainly about (e.g., "service", "quality", "price", "delivery", etc.)

@app.post("/analyze-feedback")
def analyze_feedback(review: ReviewRequest):
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=(
            "Analyze this customer review. \n"
            "label must be one of: positive, negative, or neutral. \n"
            "score must be an integer between 1 (very bad) and 5 (very good). \n"
            "theme must be a single lowercase word describing the main topic of the review such as \"service\", \"quality\", \"price\", \"delivery\", etc. \n"
            f"Review: {review.text}\n"
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=AnalysisResponse,
        ),
    )
    return response.parsed