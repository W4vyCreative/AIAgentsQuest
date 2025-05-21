import streamlit as st

hf_token = st.secrets["HF_TOKEN"]

st.set_page_config(page_title="Gamified AI Agent", page_icon="🤖", layout="wide")
st.title("AI Agents Quest: Learning how to create your own AI agents in a gamified way!")
st.write("Welcome! This APP will guide you on building your own **AI agents** " "utilizing interactive challenges. Let's go!")
st.button("Press here")

st.sidebar.info("This is a sidebar")
