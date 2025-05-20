import streamlit as st

st.write("Tema ativo", st.runtime.scriptrunner.get_script_run_ctx().theme)
