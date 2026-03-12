import streamlit as st
from utils import read_resume
from resume_parser import parse_resume_llm
from crew import run_resume_assistant

st.set_page_config(page_title="AI Resume Assistant", layout="wide")

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

    with open(file_path,"wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = read_resume(file_path)

    st.info("Parsing resume...")

    parsed_resume = parse_resume_llm(resume_text)

    if st.button("Run AI Assistant"):

        with st.spinner("Running AI agents..."):

            result = run_resume_assistant(parsed_resume, options)

        st.success("Completed")

        st.write(result)