# CareerLens AI

CareerLens AI is a lightweight resume analyzer supporting PDF, DOCX, and TXT files.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Termux setup

```bash
pkg update
pkg install python
cd ~/CareerLens-AI
pip install -r requirements.txt
python app.py
```

If PyMuPDF fails to install on your phone, test DOCX/TXT first and deploy using a hosting provider that supports the dependency.

## Important

- The analyzer provides an educational ATS-style estimate.
- Do not upload highly sensitive documents.
- Review and customize the legal pages before publishing.
- Set a strong `SECRET_KEY` in production.
- Never commit secrets or API keys.
