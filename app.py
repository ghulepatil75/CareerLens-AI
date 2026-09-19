import os, re, uuid
from pathlib import Path
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from analyzer import analyze_resume
from parser import extract_text

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this-in-production")
ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyzer")
def analyzer_page():
    return render_template("analyzer.html")

@app.route("/<page>")
def static_page(page):
    allowed = {"features", "how-it-works", "about", "contact", "faq", "privacy", "terms", "disclaimer", "guides"}
    if page in allowed:
        return render_template(f"{page}.html")
    return render_template("404.html"), 404

@app.post("/api/analyze")
def api_analyze():
    uploaded = request.files.get("resume")
    if not uploaded or not uploaded.filename:
        return jsonify({"error": "Please select a resume file."}), 400
    if not allowed_file(uploaded.filename):
        return jsonify({"error": "Only PDF, DOCX, and TXT files are supported."}), 400

    filename = secure_filename(uploaded.filename)
    suffix = Path(filename).suffix.lower()
    temp_path = UPLOAD_DIR / f"{uuid.uuid4().hex}{suffix}"
    try:
        uploaded.save(temp_path)
        text = extract_text(temp_path, suffix)
        if not text.strip():
            return jsonify({"error": "No readable text was found. If this is a scanned PDF, use a text-based PDF or DOCX."}), 400
        result = analyze_resume(
            text=text,
            role=request.form.get("role", "").strip(),
            company=request.form.get("company", "").strip(),
            job_description=request.form.get("job_description", "").strip()
        )
        return jsonify(result)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    except Exception:
        app.logger.exception("Resume analysis failed")
        return jsonify({"error": "The file could not be processed. Please try another file."}), 500
    finally:
        try:
            temp_path.unlink(missing_ok=True)
        except Exception:
            pass

@app.errorhandler(413)
def too_large(_):
    return jsonify({"error": "File is too large. Maximum size is 5 MB."}), 413

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
