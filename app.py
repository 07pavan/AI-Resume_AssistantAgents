import streamlit as st
from crew import run_resume_assistant
from utils import read_resume

st.title("AI Resume Assistant")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf","docx"])

analysis = st.checkbox("Resume Analysis")
improve = st.checkbox("Improve Resume")
jobs = st.checkbox("Job Suggestions")
cover_letter = st.checkbox("Generate Cover Letter")

options = []

if analysis:
    options.append("analysis")

if improve:
    options.append("improve")

if jobs:
    options.append("jobs")

if cover_letter:
    options.append("cover_letter")

if uploaded_file:

    file_path = uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = read_resume(file_path)

    if st.button("Run Selected AI Agents"):

        with st.spinner("Running AI agents..."):

            result = run_resume_assistant(resume_text, options)

        st.write(result)