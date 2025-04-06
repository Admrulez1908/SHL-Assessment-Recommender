from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
import pandas as pd
from difflib import get_close_matches

def load_recommender():
    return FAISS.load_local("data/faiss_index", OpenAIEmbeddings())

def get_recommendations(query, top_k=10):
    vectordb = load_recommender()
    results = vectordb.similarity_search(query, k=top_k)

    df = pd.read_csv("data/assessments.csv")
    recommendations = []
    for result in results:
        matched = df[df['description'].str.contains(result.page_content[:20], na=False)]
        if matched.empty:
            continue
        row = matched.iloc[0]
        recommendations.append({
            "title": row['title'],
            "url": row['url'],
            "remote": row['remote'],
            "adaptive": row['adaptive'],
            "duration": row['duration'],
            "type": row['type']
        })
    return recommendations

