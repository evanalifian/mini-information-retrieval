# import pathlib
from pathlib import Path

# path to documents directory
path = Path("./documents")

# create dict to store documents
documents = {}

# read each file document an store to dict
for file in path.glob("*.txt"):
    with file.open("r") as f:
        content = f.read()
        documents[file.name] = content
