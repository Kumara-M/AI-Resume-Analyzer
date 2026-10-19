# AI Resume Analyzer 🤖

An AI-based Resume Analyzer built using Python and Streamlit. 
This application analyzes PDF resumes against job descriptions, 
identifies matching and missing skills, and calculates a text similarity score.

## 📌 Project Overview

The AI Resume Analyzer helps job seekers understand how well their resumes 
match a particular job description. It extracts resume text from PDF files 
and compares it with the required job skills.

## 🎯 Objectives

- Upload and analyze PDF resumes.
- Extract text from resumes automatically.
- Compare resumes with job descriptions.
- Calculate a text similarity score.
- Identify matching skills.
- Highlight potentially missing skills.
- Download an analysis report.

## 🛠️ Technologies Used

- Python
- Streamlit
- PyPDF2
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## ⚙️ Features

- Simple and user-friendly interface.
- PDF resume upload.
- Automatic text extraction.
- Job description analysis.
- Resume and job description similarity score.
- Matching skills identification.
- Missing skills identification.
- Extracted resume text preview.
- Downloadable analysis report.

## 📂 Project Structure

```text
AI-Resume-Analyzer/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
## 🚀 How to Use

Follow these steps to analyze a resume:

1. Open the AI Resume Analyzer application.
2. Upload your resume in PDF format.
3. Enter the job description in the text box.
4. Click the Analyze Resume button.
5. View the resume similarity score.
6. Check the matching skills identified in your resume.
7. Review the potentially missing skills.
8. View the extracted resume text if needed.
9. Download the analysis report if the download feature is available.

## 🧠 How It Works

The AI Resume Analyzer works through the following steps:

1. **Resume Upload:** The user uploads a resume in PDF format.
2. **Text Extraction:** PyPDF2 extracts text from the uploaded PDF.
3. **Job Description Input:** The user enters the job description they want to compare with the resume.
4. **Text Processing:** The application processes the resume text and job description.
5. **Similarity Calculation:** TF-IDF vectorization and cosine similarity estimate how similar the resume text is to the job description.
6. **Skill Matching:** The application checks the resume and job description against a predefined list of skills.
7. **Results Display:** The application displays the similarity score, matching skills, and potentially missing skills.
8. **Report Download:** The user can download the analysis report if the feature is implemented.

## 📊 Results

The application provides:

- Resume and job description similarity score.
- Matching skills.
- Potentially missing skills.
- Extracted resume text.
- Downloadable analysis report, if supported.

**Note:** The similarity score is an estimate of textual similarity, not an official ATS score or a guarantee of employment.
