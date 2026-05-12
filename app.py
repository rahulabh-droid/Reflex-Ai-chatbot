import streamlit as st
from llm_backend import llm_response, google_llm_response

# ----------------------
# Page Config
# ----------------------
st.set_page_config(
    page_title="R.E.F.L.E.C.T Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>

/* ===== JARVIS BACKGROUND ===== */
.stApp {
    background: linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #020617
    );
    color: #e5e7eb;
}

/* ===== CENTER CONTENT ===== */
section.main > div {
    max-width: 880px;
    margin: auto;
}

/* ===== TITLE ===== */
h1 {
    text-align: center;
    color: #38bdf8;
    letter-spacing: 2px;
    font-weight: 600;
}

/* ===== CHAT BUBBLES ===== */
div[data-testid="stChatMessage"] {
    background: rgba(2, 6, 23, 0.85);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
    box-shadow: 0 0 12px rgba(56, 189, 248, 0.15);
}

/* ===== INPUT ===== */
div[data-testid="stChatInput"] input {
    background: rgba(2, 6, 23, 0.95);
    color: #e5e7eb;
    border-radius: 24px;
    padding: 14px;
    border: 1px solid #38bdf8;
}

/* ===== INPUT GLOW ===== */
div[data-testid="stChatInput"] input:focus {
    outline: none;
    box-shadow: 0 0 18px rgba(56, 189, 248, 0.8);
}

</style>
""", unsafe_allow_html=True)

# ----------------------
# Logo Center
# ----------------------
col1, col2, col3 = st.columns([1.6, 2, 0.7])

with col2:
    st.image("image2.jpg", width=160)

# ----------------------
# Sidebar
# ----------------------
with st.sidebar:
    st.markdown("""
    <h2 style="color:#38bdf8;">🧠 REFLECT PANEL</h2>
    <p style="color:#94a3b8;">Chat controls</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    model_choice = st.selectbox(
        "⚙️ AI Model",
        ["Gemini", "Local LLM"],
        key="model_choice"
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat cleared. How can I help you?"
            }
        ]
        st.rerun()

# ----------------------
# Header
# ----------------------
st.markdown("""
<h1>REFLECT</h1>
<p style="text-align:center; color:#7dd3fc; letter-spacing:1px;">
Just A Rather Very Intelligent System
</p>
""", unsafe_allow_html=True)

# ----------------------
# Session State
# ----------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Good evening, sir. REFLECT online. How may I assist you?"
        }
    ]

# ----------------------
# Display Chat History
# ----------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------
# User Input
# ----------------------
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):

            # Direct prompt (no mode logic)
            prompt = user_input

            # Choose model
            if st.session_state.model_choice == "Gemini":
                response = google_llm_response(prompt)
            else:
                try:
                    response = llm_response(prompt)

                except Exception:
                    response = (
                        "⚠️ Local LLM is not running.\n\n"
                        "Please start ollama using:\n"
                        "`ollama run phi3`"
                    )
        st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
