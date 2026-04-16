from read_documents import documents as docs
from text_preprocessing import TextPreprocessing

# stopwords list
stopwords = ["dengan", "dan", "untuk", "pada", "di", "dari", "yang", "karena", "akibat"]
# query
query = "Pencegahan demam tinggi"


# >= step 1: text preprocessing
tp = TextPreprocessing(stopwords, query, docs)
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
q = tp.get_doc_length(tokens["q"])
d4 = tp.get_doc_length(tokens["d4"])
d5 = tp.get_doc_length(tokens["d5"])
d6 = tp.get_doc_length(tokens["d6"])
d7 = tp.get_doc_length(tokens["d7"])
d8 = tp.get_doc_length(tokens["d8"])
total_docs = list(tokens.values())
avgl = (d4 + d5 + d6 + d7 + d8) / len(total_docs[1:]) #avgl value


# >= step 3: corpus
# only document (without query)
doc_tokens = {k: v for k, v in tokens.items() if k != "q"}

# take all unique terms
corpus = set()
for t in doc_tokens.values():
    corpus.update(t)

corpus = sorted(corpus)


# create corpus table
corpus_table = {}

for term in corpus:
    corpus_table[term] = {}
    df = 0

    for doc, words in doc_tokens.items():
        tf = words.count(term)
        corpus_table[term][doc] = tf

        if tf > 0:
            df += 1

    corpus_table[term]["dft"] = df

for k, v in corpus_table.items():
    print(k)
    print(v)
    print()