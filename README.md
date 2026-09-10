🚀 CareerLens AI

AI-Powered Resume Analysis & Career Intelligence

CareerLens AI is a local AI-powered resume analysis web application that helps students and job seekers understand why their resume may be failing ATS-style screening and what they can improve.

Upload your PDF or DOCX resume, provide your target role/company, and CareerLens analyzes your resume for ATS compatibility, skills, keywords, structure, and improvement opportunities.

«Built for students, freshers, and job seekers who want a better, more targeted resume.»

---

✨ Features

- 📄 PDF & DOCX resume parsing
- 🎯 ATS-style resume scoring
- 🔍 Resume structure analysis
- 🧠 Skill detection and categorization
- 🔑 Job-description keyword matching
- ⚠️ Missing keyword detection
- 💡 Personalized improvement suggestions
- 🏢 Target company analysis
- 💼 Target job-role context
- 📊 Resume strengths & weaknesses
- 🌐 Modern responsive web interface
- 💾 No database required
- 🔒 Resume processing can be performed locally

---

🖥️ How to Use CareerLens AI Locally

Anyone can run CareerLens AI on their own computer after downloading the project from GitHub.

1. Clone the Repository

git clone https://github.com/ghulepatil75/CareerLens-AI.git
cd CareerLens-AI

2. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux / macOS

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Start CareerLens AI

python app.py

You should see Flask start the local server.

5. Open the Application

Open your browser and visit:

http://127.0.0.1:5000

---

🎯 How a User Uses It

Step 1 — Upload Resume

Upload your existing:

- PDF resume
- DOCX resume

Step 2 — Enter Career Information

Provide information such as:

Degree:
B.Tech Electronics & Telecommunication

Target Role:
Embedded Systems Engineer

Target Company:
Optional

Step 3 — Analyze

Click the Analyze Resume button.

CareerLens AI evaluates your resume and identifies:

- ATS compatibility
- Skills
- Resume structure
- Keywords
- Missing keywords
- Strengths
- Weak areas
- Improvement opportunities

Step 4 — Understand Your Score

Example:

ATS Score: 72/100

Skills Match:       84%
Keyword Match:      68%
Structure:           76%
Experience:          61%
Overall Resume:      72%

Step 5 — Improve Your Resume

CareerLens AI provides actionable suggestions instead of simply giving you a score.

For example:

⚠ Missing Skill

Embedded C is not clearly mentioned.

Suggestion:
Add Embedded C under your technical skills
and demonstrate it in one relevant project.

Step 6 — Match Against a Job

You can use a job description to understand how closely your resume matches the target role.

Example:

Job Description:

Embedded Engineer
Required:
• C
• Embedded C
• ESP32
• Microcontrollers
• PCB Design

CareerLens can identify relevant keywords and highlight areas that may need improvement.

---

🏗️ Project Structure

CareerLens-AI/
│
├── app.py                 # Flask application
├── analyzer.py            # Resume analysis logic
├── parser.py              # PDF/DOCX parsing
├── requirements.txt       # Python dependencies
│
├── templates/
│   └── ...                # HTML templates
│
├── static/
│   └── ...                # CSS, JavaScript and assets
│
├── uploads/
│   └── ...                # Uploaded resume files
│
├── .gitignore
├── LICENSE
└── README.md

---

🛠️ Tech Stack

Technology| Purpose
Python| Core application
Flask| Web framework
HTML| Interface
CSS| Styling
JavaScript| Frontend interactions
PDF/DOCX parsers| Resume extraction
Git & GitHub| Version control

---

🔄 Application Workflow

                ┌─────────────────┐
                │  Upload Resume  │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Parse PDF/DOCX  │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Extract Resume  │
                │     Content     │
                └────────┬────────┘
                         ↓
             ┌────────────────────────┐
             │ Resume Analysis Engine │
             └────────────┬───────────┘
                          ↓
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
      ATS Score       Skills/Keywords   Structure
          │               │               │
          └───────────────┼───────────────┘
                          ↓
                ┌─────────────────┐
                │ Recommendations │
                └─────────────────┘

---

💻 Requirements

Before running the project, make sure you have:

- Python 3.x
- pip
- Git
- A modern web browser

Check Python:

python --version

Check pip:

pip --version

Check Git:

git --version

---

🐛 Troubleshooting

"python" command not found

Try:

python3 --version

and run:

python3 app.py

Dependencies are missing

Run:

pip install -r requirements.txt

Port 5000 is already in use

Stop the previous Flask process and run the application again.

---

🔐 Privacy

CareerLens AI is designed as a local application.

When running locally, your uploaded resume is processed by your local application rather than automatically being uploaded to a public CareerLens server.

«Always review the code and configuration before using the application with sensitive personal documents.»

---

⚠️ Disclaimer

CareerLens AI provides ATS-style resume analysis and educational career guidance.

The score is not an official ATS score and cannot predict whether a recruiter will shortlist a candidate.

Different companies use different recruitment systems and hiring criteria.

---

🚀 Future Improvements

Planned improvements may include:

- [ ] AI-powered resume rewriting
- [ ] Job description → resume matching
- [ ] Multiple resume versions
- [ ] Resume improvement suggestions
- [ ] Cover letter generation
- [ ] Resume comparison
- [ ] Export improved resume
- [ ] More ATS checks
- [ ] Better keyword intelligence
- [ ] Deployment as an online application

---

🤝 Contributing

Contributions, ideas and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

---

📄 License

This project is licensed under the MIT License.

---

⭐ Support the Project

If CareerLens AI is useful to you:

⭐ Star the repository

🍴 Fork the project

🐛 Report issues

💡 Suggest improvements

---

👨‍💻 Developer

Rohit Ghule

Electronics & Telecommunication Engineering
IoT • Embedded Systems • Python • AI

---

«Your resume gets one chance to make the first impression.
CareerLens AI helps you understand and improve it before you apply.»
