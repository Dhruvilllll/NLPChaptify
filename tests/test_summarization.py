from utils.summarization import summarize_chunks

def test_summarizer():
    chunks = ["Machine learning is a field of AI that enables systems to learn..."] * 3
    summaries = summarize_chunks(chunks)
    assert len(summaries) == len(chunks)
    assert isinstance(summaries[0], str)
