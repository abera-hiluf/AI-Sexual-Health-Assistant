# AI Sexual Health Information Assistant

## Overview

AI Sexual Health Information Assistant is a Retrieval-Augmented Question Answering (QA) system designed to provide accurate and accessible information related to sexual health topics, including HIV, sexually transmitted infections (STIs), hepatitis B, testing, prevention, treatment, and patient support.

The system combines semantic search with transformer-based language models to retrieve relevant health information and generate clear responses to user questions.

## Features

* Semantic search using transformer embeddings
* Retrieval of the most relevant health-related questions and answers
* Natural language answer generation using FLAN-T5
* English-language sexual health knowledge base
* Interactive chatbot interface (upcoming)
* Deployable as a web application

## Dataset

The project uses a curated dataset containing more than 18,000 sexual health question-answer pairs. The dataset covers topics such as:

* HIV/AIDS
* Sexually Transmitted Infections (STIs)
* Hepatitis B
* Prevention and testing
* Treatment and care
* Sexual health education

Duplicate questions were removed to improve retrieval quality.

## Technologies Used

* Python
* Sentence Transformers
* all-MiniLM-L6-v2
* FLAN-T5 Base
* Hugging Face Transformers
* Scikit-learn
* Pandas
* Kaggle Notebooks
* GitHub

## System Architecture

User Question
→ Semantic Embedding
→ Similarity Search
→ Top-K Retrieval
→ FLAN-T5 Response Generation
→ Final Answer

## Future Improvements

* Streamlit web application
* Conversation memory
* Improved retrieval models
* Response evaluation metrics
* Deployment on Hugging Face Spaces

## Author

Abera Hiluf

AI and Machine Learning Student at Anna University
