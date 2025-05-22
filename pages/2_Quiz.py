import streamlit as st

if "xp" not in st.session_state:
    st.session_state["xp"] = 0
st.session_state["xp"] = st.session_state.xp

st.title("🤔 Quiz")
st.header("Let's test your knowledge!")

st.write("Practice your knowledge answering the question: ")
question = "**QUESTION:** Which programming language are we using to build this app?"
choices = ["A) Java", "B) Python", "C) CU"]
right_choice = "B) Python"

choice = st.radio(question, choices)



if st.button("confirm answer"):
   if choice == right_choice:
      st.session_state["xp"] += 10
      st.success(f"✅Congratulations, you are right! +10xp. (total XP = {st.session_state ['xp']})")
else:
   st.error("❌Oh, you are wrong 😔... Try again!")
