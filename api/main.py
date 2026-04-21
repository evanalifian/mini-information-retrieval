import sys
import os

# Tambahkan root project ke path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from services.read_documents import documents as docs
from services.text_preprocessing import TextPreprocessing
from services.inverted_index import InvertedIndex
from services.bm25 import BM25
from fastapi import FastAPI


# create API
app = FastAPI()


# create route '/' API
@app.get("/search")
def read_root(q: str = ""):
    # >= step 1: text preprocessing
    tp = TextPreprocessing(q, docs)
    # tokenization
    tp.tokenization()
    # case folding
    tp.case_folding()
    # stopword removal
    tp.stopword_removal()
    # stemming
    tp.stemming()
    # get tokens
    tokens = tp.tokens

    # >= step 2: get documents length and create inverted index
    # sum all doc length
    total_doc_length = 0

    for k in tokens:
        total_doc_length += tp.get_doc_length(tokens[k])

    # calulate avgl
    avgl = total_doc_length / len(list(tokens.values())[1:])  # avgl value

    # >= step 3: corpus table
    corpus = InvertedIndex(tokens)
    # select all unique terms from each docs
    corpus.take_unique_term()
    # create corpus table
    corpus.create_corpus_table()
    # get corpus taable
    corpus_table = corpus.corpus_table

    # inisialisasi BM25
    bm25 = BM25(tokens, corpus_table, avgl)

    # hitung ranking
    ranking = bm25.rank()

    return {"q": q, "result": ranking}
