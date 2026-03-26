# 📚 AI Study Assistant (RAG Agent)

An intelligent, context-aware AI tutor built with **Flask**, **Streamlit**, and **Google Gemini 2.5**. This agent allows you to upload personal study materials (PDFs, DOCX, TXT), ingest them into a local FAISS vector database, and ask follow-up questions bounded strictly to that material. It remembers conversational history and cites its sources.

---

## 🏗️ Architecture

- **Backend Context Engine**: Flask API exposing endpoints for document upload, vector querying, and holistic summarization.
- **RAG Datastore**: Fast, local FAISS vector similarity search tracking 3072-dimensional embeddings.
- **Frontend App**: Streamlit chat interface interacting with the backend for a seamless user experience.
- **LLM Backbone**: Google Gemini API (`models/gemini-embedding-001` and `models/gemini-2.5-flash`).

---

## 🚀 Quickstart: Docker Compose (Recommended)

The easiest way to run both the frontend and backend without worrying about local dependencies is through Docker. Both containers run natively on **Python 3.12**.

1. Ensure **Docker Desktop** is running.
2. Edit `.env` (or copy `.env.example` to `.env`) and add your actual Google Gemini API Key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   API_BASE=http://backend:5000
   ```
3. Boot the environment:
   ```bash
   docker-compose up --build
   ```
4. Access the UI by navigating to [http://localhost:8501](http://localhost:8501) in your browser.

---

## 💻 Manual Local Setup (Without Docker)

If you prefer to run the apps locally bare-metal:

### 1. Configure Environment
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_actual_api_key_here
API_BASE=http://localhost:5000
```

### 2. Install Dependencies
Set up your Python 3.12 virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

### 3. Start Backend API
Open a terminal and start the Flask core:
```powershell
flask run --port=5000
```

### 4. Start Frontend Web UI
Open a **second** terminal and launch Streamlit:
```powershell
streamlit run ui/app.py
```
Navigate to [http://localhost:8501](http://localhost:8501) to begin uploading documents!

---

## 🎯 Features

- **Document Ingestion Pipeline:** Splits and processes multi-page documents seamlessly via PyMuPDF.
- **Query Auto-Rewrite:** Pre-processes user queries alongside conversational memory for maximum contextual accuracy.
- **Direct Citations:** The LLM cites specific data chunks matching your documents.
- **Global Summarization:** Generates instant high-level outlines of all ingested materials.
