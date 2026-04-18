from read_json_documents import load_documents_from_json
from text_preprocessing import TextPreprocessing
from inverted_index import InvertedIndex
from bm25 import BM25

# stopwords list
stopwords = ["dengan", "dan", "untuk", "pada", "di", "dari", "yang", "karena", "akibat"]
# query
query = "gejala demam tinggi pada tubuh"


# ambil dokumen dari JSON
docs = load_documents_from_json("./documents/PoPCites.json")

print("\n=== RAW DOCUMENTS ===")
for k, v in docs.items():
    print(k, ":", v[:100], "...")


# >= step 1: text preprocessing
tp = TextPreprocessing(stopwords, query, docs)

tp.tokenization()
tp.case_folding()
tp.stopword_removal()
tp.stemming()

tokens = tp.tokens


# >= step 2: get documents length and create inverted index
doc_lengths = {}
for key in tokens:
    if key != "q":
        doc_lengths[key] = tp.get_doc_length(tokens[key])

avgdl = sum(doc_lengths.values()) / len(doc_lengths)

print("\nAVGDL:", avgdl)


# >= step 3: corpus table
corpus = InvertedIndex(tokens)
corpus.take_unique_term()
corpus.create_corpus_table()

corpus_table = corpus.corpus_table



# inisialisasi BM25
bm25 = BM25(tokens, corpus_table, avgdl)

ranking = bm25.rank()

print("\n=== HASIL RANKING BM25 ===")
for doc, score in ranking:
    print(f"{doc}: {score:.4f}")