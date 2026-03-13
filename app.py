import streamlit as st

from utils.pdf_generator import create_resume_pdf
from parser.resume_parser import extract_resume_text

from pipeline.analyzer import analyze_resume
from pipeline.improver import improve_resume
from pipeline.jobs import suggest_jobs
from pipeline.cover_letter import generate_cover_letter
from pipeline.ats_score import calculate_ats_score


st.set_page_config(page_title="AI Resume Assistant", page_icon="🤖")

st.title("🤖 AI Resume Assistant")
st.write("Upload your resume and get AI-powered feedback, improvements, job suggestions, and more.")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

# Feature selection
st.subheader("Select Features")

analysis_option = st.checkbox("Resume Analysis")
improve_option = st.checkbox("Improve Resume")
ats_option = st.checkbox("ATS Resume Score")
job_option = st.checkbox("Job Suggestions")
cover_option = st.checkbox("Generate Cover Letter")

job_query = st.text_input("Job search role", "AI Engineer")
job_role = st.text_input("Target Job Role (for cover letter)", "AI Engineer")

# Extract resume text
resume_text = None

if uploaded_file:

    try:
        resume_text = extract_resume_text(uploaded_file)
        st.success("✅ Resume uploaded successfully!")

    except Exception as e:
        st.error(f"Error reading resume: {e}")


# Run pipeline
if st.button("Run AI Assistant"):

    if not uploaded_file:
        st.warning("Please upload a resume first.")
        st.stop()

    try:

        analysis = None
        improved = None

        # ATS SCORE
        if ats_option:

            st.subheader("📊 ATS Resume Score")

            ats_score = calculate_ats_score(resume_text)

            st.write(ats_score)

        # RESUME ANALYSIS
        if analysis_option:

            st.subheader("🔍 Resume Analysis")

            analysis = analyze_resume(resume_text)

            st.write(analysis)

        # RESUME IMPROVEMENT
        if improve_option:

            st.subheader("✨ Improved Resume")

            improved = improve_resume(resume_text, analysis)

            st.write(improved)

            st.success("Improved resume generated successfully!")

            # PDF DOWNLOAD
            try:

                pdf_file = create_resume_pdf(improved)

                st.download_button(
                    label="📄 Download Improved Resume PDF",
                    data=pdf_file,
                    file_name="improved_resume.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"PDF generation failed: {e}")

        # JOB SUGGESTIONS
        if job_option:

            st.subheader("💼 Job Suggestions")

            jobs = suggest_jobs(job_query)

            if isinstance(jobs, list):

                for job in jobs:

                    st.write(f"### {job['title']}")
                    st.write(f"🏢 Company: {job['company']}")
                    st.write(f"📍 Location: {job['location']}")

                    # Clickable apply button
                    st.link_button("🚀 Apply Now", job["link"])

                    st.divider()

            else:
                st.write(jobs)

        # COVER LETTER
        if cover_option:

            st.subheader("✉️ Cover Letter")

            cover = generate_cover_letter(improved or resume_text, job_role)

            st.write(cover)

    except Exception as e:

        st.error(f"Pipeline error: {e}")