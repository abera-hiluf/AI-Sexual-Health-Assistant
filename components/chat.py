import streamlit as st
from src.pipeline import ask_ai

def init_chat_history():
    """
    Initializes the session state variables for chat history.
    """
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "role": "assistant",
                "content": "Hello! I am your AI Sexual Health Assistant. Feel free to ask me questions regarding HIV, STIs, testing, prevention, or treatments. I am here to help answer your questions securely and confidentially.",
                "retrieved": [],
                "confidence": None
            }
        ]

def render_chat(confidence_threshold=0.45, top_k=3):
    """
    Renders the conversational chat interface and handles user inputs.
    """
    init_chat_history()

    # Check if a question was clicked from the sidebar quick-start
    if "clicked_question" in st.session_state:
        prompt = st.session_state.pop("clicked_question")
        st.session_state.pop("auto_submit", None)  # Clean up auto_submit flag
        
        st.session_state.chat_messages.append({
            "role": "user",
            "content": prompt,
            "retrieved": [],
            "confidence": None
        })
        
        result = ask_ai(prompt, confidence_threshold=confidence_threshold, top_k=top_k)
        
        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": result["answer"],
            "retrieved": result["retrieved"],
            "confidence": result["confidence"]
        })
        st.rerun()

    # Clear chat history button
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🗑️ Clear", help="Clear conversation history"):
            st.session_state.chat_messages = []
            init_chat_history()
            st.rerun()

    # Display past messages
    for msg in st.session_state.chat_messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
            # Show retrieval details for assistant responses if they are available
            if msg["role"] == "assistant" and msg["confidence"] is not None and len(msg["retrieved"]) > 0:
                with st.expander("🔍 Verified Retrieval Details"):
                    st.markdown(f"**Similarity Match:** `{msg['confidence']}%`")
                    st.markdown("**Retrieved Knowledge Reference Questions:**")
                    for item in msg["retrieved"]:
                        st.markdown(f"- *{item['question']}* (Match: `{round(item['score']*100, 1)}%`)")

    # Handle user new message input
    if prompt := st.chat_input("Ask a sexual health question..."):
        # Append user message to history
        st.session_state.chat_messages.append({
            "role": "user",
            "content": prompt,
            "retrieved": [],
            "confidence": None
        })
        
        # Display user message instantly
        with st.chat_message("user"):
            st.write(prompt)

        # Generate assistant response
        with st.chat_message("assistant"):
            with st.spinner("Analyzing knowledge base..."):
                result = ask_ai(prompt, confidence_threshold=confidence_threshold, top_k=top_k)
                
            st.write(result["answer"])
            
            # Show sources under expander
            if result["is_related"] and len(result["retrieved"]) > 0:
                with st.expander("🔍 Verified Retrieval Details"):
                    st.markdown(f"**Similarity Match:** `{result['confidence']}%`")
                    st.markdown("**Retrieved Knowledge Reference Questions:**")
                    for item in result["retrieved"]:
                        st.markdown(f"- *{item['question']}* (Match: `{round(item['score']*100, 1)}%`)")

            # Save assistant response to history
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": result["answer"],
                "retrieved": result["retrieved"],
                "confidence": result["confidence"]
            })
            
            st.rerun()
