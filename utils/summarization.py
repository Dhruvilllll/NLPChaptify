import models
from models.summarizer import summarize

def summarize_chunks(chunks):
    summaries = []
    for idx, chunk in enumerate(chunks):
        print(f"Summarizing chunk {idx + 1}/{len(chunks)}")
        summary = summarize(chunk)
        summaries.append(summary)
    return summaries
