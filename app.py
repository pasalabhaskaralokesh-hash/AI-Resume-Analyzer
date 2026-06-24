import streamlit as st
import pdfplumber

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

skills_db = [
    "python", "java", "c", "c++",
    "machine learning", "deep learning",
    "artificial intelligence",
    "sql", "html", "css", "javascript",
    "qiskit", "data science"
]

if uploaded_file:
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    st.subheader("Resume Text")
    st.write(text[:1000])

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.success(skill)
    else:
        st.warning("No matching skills found")
