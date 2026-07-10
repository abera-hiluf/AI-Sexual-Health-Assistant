import streamlit as st

def render_disclaimer():
    """
    Renders an styled medical disclaimer box at the bottom of the page
    or near sensitive elements.
    """
    st.markdown(
        """
        <div style="
            background-color: rgba(239, 68, 68, 0.05);
            border: 1px solid rgba(239, 68, 68, 0.2);
            border-left: 4px solid #ef4444;
            border-radius: 8px;
            padding: 1rem;
            margin-top: 2rem;
            margin-bottom: 2rem;
            font-size: 0.9rem;
            line-height: 1.5;
            color: #7f1d1d;
        ">
            <strong style="color: #ef4444; display: flex; align-items: center; gap: 6px;">
                ⚠️ Medical Disclaimer
            </strong>
            <div style="margin-top: 4px;">
                This AI Assistant is for informational and educational purposes only. 
                It is <strong>not a medical device or a clinical diagnostic tool</strong>, and should not 
                replace professional medical advice, diagnosis, treatment, or consultation with a qualified doctor or healthcare professional. 
                If you are experiencing a medical emergency, please contact your local emergency services immediately.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
