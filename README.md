# AI Text Summarizer

A project that summarizes long texts using state-of-the-art AI models with a FastAPI backend and Streamlit frontend.

---

## Features

- Summarize any text quickly
- Adjustable summary length
- Easy-to-use web interface

---

## Project Structure

```text
ai_text_summarizer/
├─ app/               # Backend (FastAPI)
│  ├─ main.py         # FastAPI server
│  └─ summarizer.py   # Text summarization logic
├─ frontend/          # Frontend (Streamlit)
│  └─ app_frontend.py # Streamlit UI
├─ requirements.txt   # Project dependencies
└─ README.md          # Project documentation

Installation
# 1. Clone the repository
git clone https://github.com/NikoVlasov/ai-text-summarizer.git
cd ai-text-summarizer

# 2. Create and activate a virtual environment
python -m venv .venv

# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

Running the Project
FastAPI backend
uvicorn app.main:app --reload

Streamlit frontend
streamlit run frontend/app_frontend.py

Usage

Open the Streamlit interface in your browser

Paste the text you want to summarize

Adjust min_length and max_length if needed

Click "Summarize" to get a concise summary

License

This project is licensed under the MIT License.
