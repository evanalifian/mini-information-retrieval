import os
import json
import requests
from bs4 import BeautifulSoup
import time

FILE_NAME = "documents.json"

# ✅ 1. Cek apakah data sudah pernah di-scrape
if os.path.exists(FILE_NAME):
    print("Load data dari file (tanpa scraping)...")
    
    with open(FILE_NAME, "r") as f:
        documents = json.load(f)

else:
    print("Scraping data (hanya sekali)...")
    
    doc_id = 1
    documents = {}

    for i in range(1, 27):
        url = f"https://health.detik.com/berita-detikhealth/indeks?page={i}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        job_elements = soup.find_all("a", class_='media__link')

        for job in job_elements:
            if job.text.strip() != '':
                link_tag = job.get("href")
                documents[doc_id] = [job.text.strip(), link_tag]
                doc_id += 1 

        time.sleep(1)

    with open(FILE_NAME, "w") as f:
        json.dump(documents, f)

# ✅ 3. Pakai datanya
# for el in documents.values():
#     print(el)
