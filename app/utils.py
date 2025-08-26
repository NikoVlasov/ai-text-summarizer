import requests
from io import BytesIO
from PyPDF2 import PdfReader
from collections import Counter
import re

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return ""

def extract_keywords(text, top_n=10):
    words = re.findall(r'\w+', text.lower())
    common = Counter(words).most_common(top_n)
    return [word for word, count in common]
