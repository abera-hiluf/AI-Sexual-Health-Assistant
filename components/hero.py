import streamlit as st

def render_hero():
    """
    Renders a premium hero banner with professional headings,
    subtitles, and description of the AI Search pipeline.
    """
    st.markdown(
        """
        <div class="main-title">🩺 AI Sexual Health Assistant</div>
        <div class="metric-badge" style="margin-bottom: 1.5rem;">
            🔐 Secure & Confidential QA System
        </div>
        <p style="font-size: 1.1rem; color: #4a6068; line-height: 1.6; margin-bottom: 1.5rem;">
            Ask questions about sexual health, prevention, testing, HIV, STIs, and treatments. 
            The system retrieves clinically-relevant information from our verified knowledge base of 
            <strong>18,000+ QA pairs</strong>, then generates supportive, easy-to-understand educational explanations.
        </p>
        """,
        unsafe_allow_html=True
    )
