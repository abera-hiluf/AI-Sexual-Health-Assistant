import streamlit as st

def render_footer():
    """
    Renders a centered footer bar containing credentials and technology stack info.
    """
    st.markdown(
        """
        <div style="
            text-align: center;
            padding: 1.5rem;
            margin-top: 3rem;
            border-top: 1px solid rgba(13, 92, 117, 0.05);
            font-size: 0.85rem;
            color: #8bb1b8;
        ">
            © 2026 AI Sexual Health Assistant. All Rights Reserved.<br>
            Developed by Abera Hiluf (Anna University) | Powered by RAG with FAISS, all-MiniLM-L6-v2, and FLAN-T5-Base.
        </div>
        """,
        unsafe_allow_html=True
    )
