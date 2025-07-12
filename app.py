from flask import Flask, render_template, request
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

# Auto-create 'resumes' folder if it doesn't exist
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'resumes')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Extract text from PDF
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''
        return text

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    missing_skills = []

    if request.method == 'POST':
        file = request.files['resume']
        if file.filename == '':
            return render_template('index.html', score="No file selected")

        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Extract resume text
        resume_text = extract_text_from_pdf(filepath)

        # Read job description
        with open("job_description.txt", "r", encoding="utf-8") as f:
            jd_text = f.read()

        # Match using TF-IDF and cosine similarity
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, jd_text])
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100
        score = round(score, 2)

        # Detect missing skills/keywords
        jd_keywords = set(jd_text.lower().split())
        resume_keywords = set(resume_text.lower().split())
        missing_skills = list(jd_keywords - resume_keywords)[:10]

    return render_template('index.html', score=score, missing_skills=missing_skills)

if __name__ == '__main__':
    app.run(debug=True)
