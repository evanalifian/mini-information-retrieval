import json
import requests
from io import BytesIO
from PyPDF2 import PdfReader


def extract_text_from_pdf(url):
    try:
        response = requests.get(url, timeout=10)
        pdf_file = BytesIO(response.content)

        reader = PdfReader(pdf_file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        return text.strip()

    except Exception as e:
        print(f"Gagal baca PDF: {url}")
        return ""


def load_documents_from_json(json_path, max_docs=100):
    documents = {}

    with open(json_path, encoding="utf-8-sig") as f:
      data = json.load(f)

    count = 1

    for item in data:
        text = ""

        # ✅ PRIORITAS 1: ambil dari PDF
        pdf_url = item.get("fulltext_url")

        if pdf_url:
            print(f"[{count}] Ambil dari PDF...")
            text = extract_text_from_pdf(pdf_url)

        # ✅ PRIORITAS 2: fallback ke abstract + title
        if not text:
            print(f"[{count}] Pakai abstract...")
            title = item.get("title", "")
            abstract = item.get("abstract", "")
            text = title + " " + abstract

        if text.strip():
            documents[f"d{count}"] = text
            count += 1

        if count > max_docs:
            break

    return documents