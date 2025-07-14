#  AI-Powered Resume Screening & Ranking System

An intelligent web application that automates the resume shortlisting process using Natural Language Processing (NLP) and Machine Learning techniques. This tool compares candidate resumes with job descriptions and generates a **match score** based on content similarity and missing skills.

> 👨 Developed by [Bakki Mahesh](https://github.com/mahesh123-pro)

---

##  Features

- 📄 Upload and analyze PDF resumes
- 📊 Generate a matching score between resume and job description
- 🔍 Detect and highlight missing skills/keywords
- 🧠 Built using AIML techniques (TF-IDF + Cosine Similarity)
- 🌐 Simple and clean UI (HTML/CSS/JS + Flask backend)
- ✅ Completely local processing (no external resume storage)

---

## 🤖 AI/ML Tools & Concepts Used

| Tool / Concept        | Description |
|-----------------------|-------------|
| `TF-IDF (Term Frequency-Inverse Document Frequency)` | Converts resume and JD into numerical vectors by evaluating term importance |
| `Cosine Similarity`   | Measures similarity between the vectorized resume and job description |
| `scikit-learn`        | Used for TF-IDF transformation and computing cosine similarity |
| `Natural Language Processing (NLP)` | Applied for keyword extraction and text preprocessing |
| `PyPDF2`              | Extracts text from uploaded PDF resumes |
| `Set operations in Python` | Used to identify missing keywords from job description |

---

## 🛠️ Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| Frontend    | HTML, CSS, JavaScript |
| Backend     | Python + Flask     |
| PDF Parsing | PyPDF2             |
| AI/ML       | scikit-learn (TF-IDF, Cosine Similarity) |
| Hosting     | Can be deployed on Render, Railway, or locally |




## 🧪 How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/mahesh123-pro/resume-screening-ai.git
cd resume-screening-ai

