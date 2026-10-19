import streamlit as st
import PyPDF2
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")
st.write(
    "Analyze your resume, compare it with a job description, "
    "and identify relevant technical skills."
)

st.divider()


# ---------------- SKILL DATABASE ----------------

SKILLS = {
    "Python": ["python"],
    "Java": ["java"],
    "C++": ["c++"],
    "C Programming": ["c programming", " c language"],
    "SQL": ["sql", "structured query language"],
    "Machine Learning": ["machine learning"],
    "Deep Learning": ["deep learning"],
    "Artificial Intelligence": [
        "artificial intelligence",
        " ai "
    ],
    "Data Analysis": ["data analysis", "data analytics"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Scikit-learn": ["scikit-learn", "scikit learn"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Natural Language Processing": [
        "natural language processing",
        "nlp"
    ],
    "Computer Vision": ["computer vision"],
    "HTML": ["html"],
    "CSS": ["css"],
    "JavaScript": ["javascript"],
    "React": ["react", "react.js"],
    "Node.js": ["node.js", "nodejs"],
    "Flask": ["flask"],
    "Django": ["django"],
    "Streamlit": ["streamlit"],
    "Git": ["git", "github"],
    "Excel": ["excel", "microsoft excel"],
    "Power BI": ["power bi"],
    "Tableau": ["tableau"],
    "Data Structures": ["data structures"],
    "Problem Solving": ["problem solving"],
    "Communication": ["communication"],
    "Teamwork": ["teamwork", "team work"],
}


# ---------------- PDF TEXT EXTRACTION ----------------

def extract_resume_text(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)

        pages = []

        for page in reader.pages:
            pages.append(page.extract_text() or "")

        return "\n".join(pages)

    except Exception as error:
        st.error(f"Unable to read the PDF: {error}")
        return ""


# ---------------- SKILL DETECTION ----------------

def detect_skills(text):
    normalized_text = " " + text.lower() + " "
    found_skills = []

    for skill, keywords in SKILLS.items():
        for keyword in keywords:
            if keyword in normalized_text:
                found_skills.append(skill)
                break

    return sorted(found_skills)


# ---------------- RESUME UPLOAD ----------------

st.subheader("📄 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose a PDF resume",
    type=["pdf"]
)

st.subheader("💼 Job Description")

job_description = st.text_area(
    "Paste the job description",
    height=200,
    placeholder=(
        "Example: We need a Python Developer with "
        "knowledge of Python, SQL, Machine Learning and Git."
    )
)


# ---------------- ANALYSIS ----------------

if st.button("Analyze Resume", type="primary"):

    if uploaded_file is None:
        st.warning("Please upload a PDF resume.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        resume_text = extract_resume_text(uploaded_file)

        if not resume_text.strip():
            st.error(
                "No readable text found in the PDF. "
                "Try a text-based PDF resume."
            )

        else:
            resume_skills = detect_skills(resume_text)
            job_skills = detect_skills(job_description)

            matched_skills = sorted(
                set(resume_skills) & set(job_skills)
            )

            missing_skills = sorted(
                set(job_skills) - set(resume_skills)
            )

            # Calculate text similarity
            documents = [resume_text, job_description]

            try:
                vectorizer = TfidfVectorizer(
                    stop_words="english",
                    ngram_range=(1, 2)
                )

                matrix = vectorizer.fit_transform(documents)

                similarity = cosine_similarity(
                    matrix[0:1],
                    matrix[1:2]
                )[0][0]

                score = similarity * 100

            except ValueError:
                similarity = 0.0
                score = 0.0

            # ---------------- DISPLAY RESULTS ----------------

            st.divider()
            st.header("📊 Resume Analysis Results")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Text Similarity",
                f"{score:.1f}%"
            )

            col2.metric(
                "Matching Skills",
                len(matched_skills)
            )

            col3.metric(
                "Skills Not Found",
                len(missing_skills)
            )

            st.progress(float(similarity))

            st.info(
                "Text similarity is an estimate of textual overlap. "
                "It is not an official ATS score or a prediction "
                "of hiring success."
            )

            left, right = st.columns(2)

            with left:
                st.subheader("✅ Matching Skills")

                if matched_skills:
                    for skill in matched_skills:
                        st.write(f"✓ {skill}")
                else:
                    st.write("No matching skills detected.")

            with right:
                st.subheader("💡 Skills Not Found")

                if missing_skills:
                    for skill in missing_skills:
                        st.write(f"• {skill}")
                else:
                    st.write(
                        "All detected job-description skills "
                        "were found in the resume."
                    )

            st.subheader("🧠 Skills Detected in Resume")

            if resume_skills:
                st.write(", ".join(resume_skills))
            else:
                st.write("No skills from the current database detected.")

            with st.expander("View Extracted Resume Text"):
                st.text(resume_text)

            # ---------------- DOWNLOAD REPORT ----------------

            report = f"""
AI RESUME ANALYZER REPORT

Text Similarity: {score:.1f}%

SKILLS DETECTED IN RESUME:
{', '.join(resume_skills) or 'None detected'}

MATCHING SKILLS:
{', '.join(matched_skills) or 'None detected'}

JOB SKILLS NOT FOUND IN RESUME:
{', '.join(missing_skills) or 'None detected'}

Note:
Skill detection depends on the application's skill database.
A skill marked as not found may be expressed differently
in the resume. This report is not an official ATS evaluation.
"""

            st.download_button(
                label="📥 Download Analysis Report",
                data=report,
                file_name="resume_analysis.txt",
                mime="text/plain"
            )


st.divider()

st.caption(
    "AI Resume Analyzer | Python | Streamlit | Scikit-learn"
)