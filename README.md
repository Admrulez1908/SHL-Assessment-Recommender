# 🧠 SHL Assessment Recommendation System (AI Intern Assignment)

This project is a Generative AI-powered system that recommends SHL assessments based on a given job description (JD) or JD URL. It uses OpenAI's LLM and FAISS vector store to match job requirements with SHL’s assessment catalog.

---

## 🚀 Features

- 🔍 Input a **job description or JD URL**
- 🤖 LLM-based semantic matching (using OpenAI + FAISS)
- 🧠 Outputs **top SHL assessments** with:
  - Title
  - URL
  - Remote availability
  - Adaptive format
  - Duration
  - Assessment type

---

## 🛠️ Tech Stack

- 🧠 OpenAI GPT / Embeddings (via `langchain`)
- 🔎 FAISS for vector similarity search
- 🐍 Python + FastAPI backend
- 🧪 Jupyter notebooks for scraping + embedding
- 🧼 BeautifulSoup for text scraping
- 🌐 Supports both raw JD text and URLs

---

## 📁 Project Structure

