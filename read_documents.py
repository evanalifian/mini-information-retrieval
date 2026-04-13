# create dict to store documents
documents = {}

# read each file document an store to dict
for i in range(4, 8 + 1):
    with open(f"./documents/document-{i}.txt") as f:
        documents[f"d{i}"] = f.read()