# pyrefly: ignore [missing-import]
import streamlit as st
from src.pipeline import ask_ai
from components.styles import load_custom_css
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.disclaimer import render_disclaimer
from components.chat import render_chat
from components.footer import render_footer

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="AI Sexual Health Assistant",
    page_icon="🩺",
    layout="centered"
)

# Load premium custom CSS styles
load_custom_css()

# Render left UI sidebar and get user settings
app_mode, confidence_threshold, top_k = render_sidebar()

# Render main page hero header
render_hero()

# ---------------------------------------
# Main Layout Render
# ---------------------------------------
if app_mode == "Interactive Chatbot":
    # Multi-turn chat view
    st.subheader("💬 Interactive Assistant Chat")
    render_chat(confidence_threshold=confidence_threshold, top_k=top_k)
    
else:
    # Single Q&A view
    st.subheader("🔍 Quick Search Question & Answer")
    
    # Check if a question was clicked from the sidebar
    default_question = st.session_state.get("clicked_question", "")
    
    # Render main input text box
    question = st.text_input(
        "Enter your sexual health question:",
        value=default_question,
        placeholder="e.g., Can HIV be cured?",
        key="input_question"
    )
    
    # Read buttons and clear triggers
    ask_clicked = st.button("Ask AI", type="primary")
    auto_submit = st.session_state.pop("auto_submit", False)
    
    # Clear clicked question from state so typing works normally afterward
    if "clicked_question" in st.session_state:
        del st.session_state.clicked_question
        
    if ask_clicked or auto_submit:
        if question.strip():
            with st.spinner("Analyzing knowledge base..."):
                result = ask_ai(
                    question, 
                    confidence_threshold=confidence_threshold, 
                    top_k=top_k
                )
            
            # Beautiful Answer Card
            st.markdown(
                f"""
                <div class="custom-card">
                    <div class="answer-title">
                        <span>💬 AI Assistant Answer</span>
                    </div>
                    <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem; color: var(--text-color);">
                        {result["answer"]}
                    </p>
                    <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
                        <div class="metric-badge">
                            Similarity Match Score: {result["confidence"]}%
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            # Retrieved Sources
            if result["is_related"] and len(result["retrieved"]) > 0:
                with st.expander("📚 Retrieved Knowledge Base Context", expanded=True):
                    for idx, item in enumerate(result["retrieved"]):
                        st.markdown(
                            f"""
                            <div style="
                                background-color: rgba(25, 149, 173, 0.02);
                                border: 1px solid rgba(25, 149, 173, 0.08);
                                border-radius: 8px;
                                padding: 0.8rem 1rem;
                                margin-bottom: 0.8rem;
                            ">
                                <div style="font-weight: 600; color: #0d5c75; margin-bottom: 4px;">
                                    Reference #{idx+1} (Match: {round(item['score'] * 100, 1)}%)
                                </div>
                                <div style="font-style: italic; color: #557a84; margin-bottom: 6px; font-size: 0.9rem;">
                                    Q: "{item['question']}"
                                </div>
                                <div style="font-size: 0.95rem; line-height: 1.5; color: var(--text-color);">
                                    {item['answer']}
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
        else:
            st.warning("Please enter a question.")

# Render medical disclaimer and credit footer
render_disclaimer()
render_footer()