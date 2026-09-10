import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from parser import extract_text
from analyzer import analyze_resume

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024
ALLOWED_EXTENSIONS = {"docx", "txt"}
os.makedirs(UPLOAD_DIR, exist_ok=True)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.errorhandler(413)
def too_large(_error):
    return render_template("index.html", result=None, error="File is too large. Maximum size is 10 MB.")

@app.route("/")
def home():
    return render_template("index.html", result=None, error=None)

@app.route("/analyze", methods=["POST"])
def analyze():
    filepath = None
    try:
        resume = request.files.get("resume")
        if not resume or not resume.filename:
            return render_template("index.html", result=None, error="Please select a PDF or DOCX resume.")
        if not allowed_file(resume.filename):
            return render_template("index.html", result=None, error="Only DOCX files are supported in the lightweight version.")
        filename = secure_filename(resume.filename)
        filepath = os.path.join(UPLOAD_DIR, filename)
        resume.save(filepath)
        text = extract_text(filepath)
        if len(text.strip()) < 80:
            return render_template("index.html", result=None, error="Not enough readable text was found.")
        result = analyze_resume(
            text=text,
            qualification=request.form.get("qualification", "").strip(),
            degree=request.form.get("degree", "").strip(),
            purpose=request.form.get("purpose", "").strip(),
            company=request.form.get("company", "").strip(),
            role=request.form.get("role", "").strip(),
            job_description=request.form.get("job_description", "").strip(),
        )
        return render_template("index.html", result=result, error=None)
    except Exception as exc:
        return render_template("index.html", result=None, error=f"Analysis failed: {exc}")
    finally:
        if filepath and os.path.exists(filepath):
            try: os.remove(filepath)
            except OSError: pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
