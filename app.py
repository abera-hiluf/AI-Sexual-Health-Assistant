# pyrefly: ignore [missing-import]
import streamlit as st
from src.pipeline import ask_ai

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Sexual Health Assistant",
    page_icon="🩺",
    layout="centered"
)

# ---------------------------------------
# Title
# ---------------------------------------

st.title("🩺 AI Sexual Health Assistant")

st.write(
    "Ask questions about sexual health using AI-powered semantic search and FLAN-T5 generation."
)

# ---------------------------------------
# User Input
# ---------------------------------------

question = st.text_input(
    "Enter your question:"
)

# ---------------------------------------
# Button
# ---------------------------------------

if st.button("Ask AI"):

    if question.strip():

        with st.spinner("Thinking..."):

            result = ask_ai(question)

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Confidence")

        st.success(f"{result['confidence']}%")

        st.subheader("Retrieved Questions")

        for item in result["retrieved"]:

            st.write(
                f"• {item['question']}"
            )

    else:

        st.warning("Please enter a question.")