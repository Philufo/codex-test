import sys
import PyPDF2
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
import numpy as np


def read_pdf(path):
    """Load a PDF file and return its text content."""
    reader = PyPDF2.PdfReader(path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def chunk_text(text, chunk_size=200, overlap=50):
    """Split text into overlapping chunks."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def build_index(chunks, model):
    """Create FAISS index from text chunks."""
    embeddings = model.encode(chunks, convert_to_numpy=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index, embeddings


def retrieve(query, model, index, chunks, top_k=3):
    """Retrieve top_k relevant chunks for the query."""
    q_embed = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(q_embed, top_k)
    return [chunks[i] for i in indices[0]]


def main(pdf_path):
    text = read_pdf(pdf_path)
    if not text:
        print("No text extracted from PDF.")
        return
    chunks = chunk_text(text)
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    index, _ = build_index(chunks, embedder)
    qa = pipeline('question-answering', model='distilbert-base-cased-distilled-squad')

    print("Loaded PDF. Ask questions (type 'quit' to exit).")
    while True:
        question = input('Question: ').strip()
        if question.lower() in {'quit', 'exit'}:
            break
        context = "\n".join(retrieve(question, embedder, index, chunks))
        result = qa(question=question, context=context)
        print(f"Answer: {result['answer']}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python rag_poc.py path/to/file.pdf')
    else:
        main(sys.argv[1])
