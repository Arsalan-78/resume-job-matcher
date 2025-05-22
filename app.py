import streamlit as st
from resume_parser import extract_text_from_pdf
from job_matcher import load_jobs_data, match_jobs
from utils import get_resume_summary

st.set_page_config(page_title="AI Resume Critique & Job Matching Assistant", layout="centered")
st.title("📄 AI Resume Critique & Job Matching Assistant")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    st.subheader("✅ Extracted Resume Content")
    resume_text = extract_text_from_pdf(uploaded_file)
    st.text_area("Resume Text", resume_text, height=300)

    st.subheader("🔍 Resume Analysis")
    summary = get_resume_summary(resume_text)
    st.write(f"**Word Count:** {summary['word_count']}")
    st.write(f"**Named Entities:** {summary['entities_found']}")
    st.write(f"**Top Skills/Entities:** {', '.join(summary['top_skills'])}")

    st.subheader("💼 Matching Jobs for You")
    jobs_df = load_jobs_data()
    matches = match_jobs(resume_text, jobs_df)

    for title, score in matches:
        st.write(f"**{title}** - Match Score: {score:.2f}")