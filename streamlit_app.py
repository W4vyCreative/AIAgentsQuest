import streamlit as st
hf_token = st.secrets.get("HF_TOKEN", None)

for key, default in {
    "xp": 0,
    "username": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

if "xp" not in st.session_state:
    st.session_state["xp"] = 0
if "username" not in st.session_state:
    st.session_state["username"] = ""

st.set_page_config(page_title="Gamified AI Agent", page_icon="🤖", layout="wide")
st.title("AI Agents Quest: Learning how to create your own AI agents in a gamified way!")
st.write("Welcome! This APP will guide you on building your own **AI agents** utilizing interactive tasks. Are you ready?")
st.write(f"Current XP = **{st.session_state. get('xp', 0)}**")

st.sidebar.success("👆 select a page above to navigate")

st.divider()

st.text_input("Insert your name here:", key="username")
username = st.session_state.username

if st.button("Press here"):
    st.success(f"Welcome, {username}! Get ready for your AI tasks!🎮")
    username = st.session_state.username

