import re
from transformers import AutoTokenizer

def chunk_transcript(transcript, chunk_size=500, overlap=50, model_name="facebook/bart-large-cnn"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    full_text = " ".join([t['text'] for t in transcript])
    ...


def chunk_transcript(transcript, chunk_size=500, overlap=50):
    full_text = " ".join([t['text'] for t in transcript])
    sentences = re.split(r'(?<=[.!?])\s+', full_text)

    chunks = []
    current_chunk = ""
    for sentence in sentences:
        current_chunk += sentence + " "
        if len(tokenizer.encode(current_chunk)) >= chunk_size:
            chunks.append(current_chunk.strip())
            current_chunk = " ".join(current_chunk.split()[-overlap:])  # Overlap
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks
