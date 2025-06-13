from utils.chunking import chunk_transcript

def test_chunking():
    dummy_transcript = [{"text": "This is a test sentence."} for _ in range(50)]
    chunks = chunk_transcript(dummy_transcript, max_tokens=200)
    assert isinstance(chunks, list)
    assert len(chunks) > 0
    assert isinstance(chunks[0], str)
