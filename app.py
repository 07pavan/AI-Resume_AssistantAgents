import streamlit as st

from parser.resume_parser import extract_resume_text
from pipeline.analyzer import analyze_resume
from pipeline.improver import improve_resume
from pipeline.jobs import suggest_jobs
from pipeline.cover_letter import generate_cover_letter

st.title("🤖 AI Resume Assistant")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

analysis_option = st.checkbox("Resume Analysis")
improve_option = st.checkbox("Improve Resume")
job_option = st.checkbox("Job Suggestions")
cover_option = st.checkbox("Generate Cover Letter")

job_role = st.text_input("Target Job Role (for cover letter)")

if uploaded_file:

    try:
        resume_text = extract_resume_text(uploaded_file)

        st.success("Resume uploaded successfully!")

    except Exception as e:
        st.error(f"Error reading resume: {e}")

if st.button("Run AI Assistant"):

    if not uploaded_file:
        st.warning("Please upload a resume first.")
        st.stop()

    try:

        analysis = None
        improved = None

        if analysis_option:

            st.subheader("Resume Analysis")
            analysis = analyze_resume(resume_text)
            st.write(analysis)

        if improve_option:

            st.subheader("Improved Resume")
            improved = improve_resume(resume_text, analysis)
            st.write(improved)

        if job_option:

            st.subheader("Job Suggestions")
            jobs = suggest_jobs(resume_text)
            st.write(jobs)

        if cover_option:

            st.subheader("Cover Letter")
            cover = generate_cover_letter(improved or resume_text, job_role)
            st.write(cover)

    except Exception as e:

        st.error(f"Pipeline error: {e}")