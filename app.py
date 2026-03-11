import streamlit as st
from crew import run_resume_assistant
from utils import read_resume

st.title("AI Resume Assistant")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf","docx"])

if uploaded_file:

    file_path = uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = read_resume(file_path)

    if st.button("Analyze Resume"):

        with st.spinner("AI Agents are working..."):

            result = run_resume_assistant(resume_text)

        st.write(result)