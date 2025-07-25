# codex-test

This repository contains example code used for testing Codex features.

## RAG Proof of Concept

`rag_poc.py` is an interactive script demonstrating a simple Retrieval Augmented
Generation (RAG) workflow. It can:

1. Read a PDF file.
2. Split the text into overlapping chunks.
3. Convert those chunks into embeddings with Sentence Transformers.
4. Index the embeddings using FAISS.
5. Accept user questions and retrieve the most relevant chunks.
6. Use a Hugging Face question-answering model to generate an answer from the
   retrieved context.

### Usage

```bash
pip install PyPDF2 sentence-transformers faiss-cpu transformers
python rag_poc.py path/to/document.pdf
```

Then type your questions at the prompt. Enter `quit` to exit.
