from fastapi import FastAPI, Query
from recommender import get_recommendations
from utils import fetch_text_from_url, is_url
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/recommend")
def recommend(q: str = Query(..., description="Job description or URL")):
    query_text = fetch_text_from_url(q) if is_url(q) else q
    return {"results": get_recommendations(query_text)}

