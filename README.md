# mini-information-retrieval (API)

We create our mini 'search engine'using python based on our midterm exam. We're using **bm25** for ranking documents.

## How to clone this project

first, you need to clone this repo and create **virtual environement**.

```bash
git clone https://github.com/evanalifian/mini-information-retrieval.git
cd mini-information-retrieval
python -m venv env
```

if you're using Windows, you need to run this script to install the libraries.

```bash
.\env\Scripts\activate
```

then, install the libraries from **requirements.txt**

```bash
pip install -r .\requirements.txt
```

## Work with API

If you have already clone this repo, you can run this repo by these commands:

```bash
uvicorn api.main:app --reload
```

After you run the API, now type `http://127.0.0.1:8000/search` on your browser or API tools like [Postman](https://www.postman.com/). Then you need to pass a **query** on the URL, and you see the result.

```bash
http://127.0.0.1:8000/search?q=Pencegahan%20demam%20berdarah
```
