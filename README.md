<p align="center">
  <img src="assets/logo/logo.png" width="130">
</p>

<h1 align="center">AI Sexual Health Assistant</h1>

<p align="center">
An interactive, Retrieval-Augmented Generation (RAG) web application designed to provide secure, confidential, and accurate sexual health education.
</p>

<p align="center">
Reduce response latency and improve answer relevance using semantic similarity search powered by Sentence Transformers and FAISS, combined with the FLAN-T5 model for answer generation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/FAISS-009688?style=for-the-badge">
  <img src="https://img.shields.io/badge/Sentence%20Transformers-5A67D8?style=for-the-badge">
  <img src="https://img.shields.io/badge/Transformers-FF9900?style=for-the-badge">
  <img src="https://img.shields.io/badge/FLAN--T5-4285F4?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

## Live Demo

**Frontend**

https://your-streamlit-app-link-here

---

## Problem

Users often need reliable sexual health information, but they may not know where to find clear, confidential, and educational answers quickly.

This project addresses that problem by combining semantic search with a language model to generate context-aware answers from a curated sexual health knowledge base.

---

## Why AI Sexual Health Assistant?

This assistant helps users ask sexual health questions in natural language and receive helpful answers based on a curated dataset of more than 18,000 question-answer pairs.

It uses a Retrieval-Augmented Generation pipeline:

- The user asks a question
- The system finds semantically similar questions from the knowledge base
- The best matching context is passed to the FLAN-T5 model
- The model generates a clear and educational answer

This approach improves relevance, reduces hallucination, and keeps responses grounded in the dataset.

---

## Features

| Feature | Description |
| ------- | ----------- |
| Semantic Search | Finds semantically similar questions using vector embeddings |
| Fast Retrieval | Uses FAISS for efficient nearest-neighbor search |
| Answer Generation | Uses FLAN-T5 to generate natural language responses |
| Knowledge Match Score | Displays retrieval similarity for the user question |
| Guardrails | Rejects unrelated questions gracefully |
| Educational Focus | Designed for sexual health education only |
| Modern UI | Clean Streamlit interface with custom styling |
| Medical Disclaimer | Includes a clear disclaimer for safety |

---

## Architecture

```text
User Question
     │
     ▼
SentenceTransformer
[Query Embedding]
     │
     ▼
FAISS Vector Index
[Top-K Retrieval]
     │
     ▼
Contextual Prompt
[Retrieved Knowledge + User Question]
     │
     ▼
FLAN-T5
[Generated Response]
     │
     ▼
Final Answer


Technologies Used
Python
Streamlit
Pandas
NumPy
PyTorch
Sentence Transformers
FAISS
Transformers
FLAN-T5
Retrieval-Augmented Generation (RAG)

# Clone the repository
git clone https://github.com/your-username/AI-Sexual-Health-Assistant.git

# Navigate to the project
cd AI-Sexual-Health-Assistant

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python -m streamlit run app.py

Author

Abera Hiluf Teshale

AI and Machine Learning Student (Anna University)
linkedn Profile:https://www.linkedin.com/in/abera-teshale-41a3a929b/
