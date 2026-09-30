import streamlit as st
from src.helper import extract_text_from_pdf, ask_openai
from src.job_api import fetch_linkedin_jobs, fetch_naukari_jobs


st.set_page_config(page_title="Job Recommender", layout="wide")

st.title("📄 AI Job Recommender")

st.markdown(
    "Upload your resume and get job recommendations based on your skills and experience."
)

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Summarize your resume.."):
        sumamry = ask_openai(f"Summarize this resume highlighting the skills , education and experience : \n\n {resume_text}", max_tokens=1000)

    with st.spinner("Finding Skill Gaps"):
        gaps = ask_openai(f"Analyze this resume and highlight missing skills , certification and experience needed for better job opportunities: \n\n {resume_text}", max_tokens=400)

    with st.spinner("Creating future Roadmap"):
        roadmap = ask_openai(f"Based on this resume , please suggest future roadmpa to improve this person's carrear prospects(skills to learn, certification needed, industry exposure): \n\n {resume_text}", max_tokens=400)

    # Display nicely formatted results
    st.markdown("---")
    st.header("📄 Resume Summary")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{sumamry}</div>", unsafe_allow_html = True)

    st.markdown("---")
    st.header("🛠️ Skill Gaps & Missing Areas")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{gaps}</div>", unsafe_allow_html = True)

    st.markdown("---")
    st.header("🚀 Future Roadmap & Preparation Strategy")
    st.markdown(f"<div style='background-color: #000000; padding: 15px; border-radius: 10px; font-size:16px; color:white;'>{roadmap}</div>", unsafe_allow_html = True)

    st.success("✅ Analysis Completed Successfully!")    

    if st.button("🔎 Get Job Recommendations"):
        with st.spinner("Fetching job recommendations..."):
            keywords = ask_openai(
                f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. Give a comma seperated list only, No explaination \n\n Summary:, {sumamry}" ,
                max_tokens=100)
            
            cleaned_search_keywords = keywords.replace("\n","".strip())
        st.success(f"Extracted Search Keywords : {cleaned_search_keywords}")

        with st.spinner("Fetching jobs from LinkedIn and Naukari"):
            linkedin_jobs = fetch_linkedin_jobs(cleaned_search_keywords, rows = 30)
            naukari_jobs = fetch_naukari_jobs(cleaned_search_keywords, rows = 30)
       
        st.markdown("---")
        st.header("💼 Top LinkedIn Jobs")

        if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                st.markdown(f"- 📍 {job.get('location')}")
                st.markdown(f"- 🔗 [View Job]({job.get('link')})")
                st.markdown("---")
        else:
            st.warning("No LinkedIn jobs found.")

        st.markdown("---")
        st.header("💼 Top Naukri Jobs (India)")
            
        if naukari_jobs:
                for job in naukari_jobs:
                    st.markdown(f"**{job.get('title')}** at *{job.get('companyName')}*")
                    st.markdown(f"- 📍 {job.get('location')}")
                    st.markdown(f"- 🔗 [View Job]({job.get('url')})")
                    st.markdown("---")
        else:
                st.warning("No Naukri jobs found.") 