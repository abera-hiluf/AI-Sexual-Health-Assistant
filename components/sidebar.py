import streamlit as st

def render_sidebar():
    """
    Renders the Left UI Sidebar. Provides configuration sliders,
    sample quick questions, medical helpline references, and developer info.
    """
    with st.sidebar:
        # Title and header
        st.markdown(
            '<div class="sidebar-title">🩺 AI Health Panel</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="sidebar-subtitle">Configure search parameters, explore topics, and find national helplines.</div>',
            unsafe_allow_html=True
        )

        st.divider()

        # Section: Mode Selection
        st.markdown("### ⚙️ Assistant Mode")
        app_mode = st.radio(
            "Select mode:",
            ["Single Q&A Model", "Interactive Chatbot"],
            key="app_mode",
            index=0
        )

        st.divider()

        # Section: Parameters
        st.markdown("### 📊 Search Parameters")
        
        confidence_threshold = st.slider(
            "Confidence Match Threshold (%)",
            min_value=0,
            max_value=100,
            value=45,
            step=5,
            help="Minimum semantic search similarity score needed to accept retrieved content. Lower values retrieve more answers but increase risk of unrelated context."
        )
        
        top_k = st.slider(
            "Context Retrieval Size (Top-K)",
            min_value=1,
            max_value=5,
            value=3,
            step=1,
            help="Number of relevant knowledge base articles/questions retrieved to form the context for FLAN-T5."
        )

        st.divider()

        # Section: Sample Questions / Topics
        st.markdown("### 💡 Quick-Start Questions")
        
        # We categorize the questions to make it organized and highly interactive
        topic = st.selectbox(
            "Browse topics:",
            ["HIV/AIDS", "STIs & Hepatitis B", "Testing & Prevention", "Treatment & Care"]
        )

        sample_questions = {
            "HIV/AIDS": [
                "Can HIV be cured?",
                "What is the difference between HIV and AIDS?",
                "How is HIV transmitted?",
                "What is PEP and PrEP?"
            ],
            "STIs & Hepatitis B": [
                "What are common symptoms of Chlamydia?",
                "Is Hepatitis B vaccine safe and effective?",
                "What are the symptoms of Gonorrhea?",
                "How is Hepatitis B transmitted?"
            ],
            "Testing & Prevention": [
                "How often should I get tested for STIs?",
                "Do condoms protect against all STIs?",
                "Where can I get a confidential HIV test?",
                "How can I reduce my risk of getting STIs?"
            ],
            "Treatment & Care": [
                "What is antiretroviral therapy (ART)?",
                "How are bacterial STIs treated?",
                "Can herpes be cured?",
                "What should I do if my test result is positive?"
            ]
        }

        # Render question buttons
        st.caption("Click a question to ask the AI:")
        for idx, question in enumerate(sample_questions[topic]):
            if st.button(question, key=f"q_{topic.replace(' ', '_')}_{idx}"):
                st.session_state.clicked_question = question
                st.session_state.auto_submit = True
                # Trigger a rerun so the main input field updates instantly
                st.rerun()

        st.divider()

        # Section: Important Medical Support Resources
        st.markdown("### 📞 Support & Helpline Contacts")
        
        st.markdown(
            """
            <div class="resource-card">
                <strong>CDC-INFO (USA)</strong><br>
                1-800-CDC-INFO (1-800-232-4636)<br>
                <a href="https://www.cdc.gov/cdc-info/index.html" target="_blank">cdc.gov/cdc-info</a>
            </div>
            <div class="resource-card">
                <strong>National AIDS Hotline (USA)</strong><br>
                1-800-342-AIDS (1-800-342-2437)<br>
                Available 24/7
            </div>
            <div class="resource-card">
                <strong>Planned Parenthood Helpline</strong><br>
                1-800-230-PLAN (1-800-230-7526)<br>
                <a href="https://www.plannedparenthood.org" target="_blank">plannedparenthood.org</a>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        # Section: Developer Information
        st.markdown("### 🧑‍💻 System Metadata")
        st.markdown(
            """
            **Developer:** Abera Hiluf  
            *Anna University*  
            
            **AI Models:**  
            - Embedding: `all-MiniLM-L6-v2`  
            - Indexing: `FAISS CPU`  
            - Generator: `FLAN-T5 Base`  
            """
        )

    return app_mode, confidence_threshold / 100.0, top_k
