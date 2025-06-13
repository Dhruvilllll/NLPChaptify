from utils.transcript import fetch_youtube_transcript

def test_transcript_fetching():
    video_id = "dQw4w9WgXcQ"  # Use any public video
    transcript = fetch_youtube_transcript(video_id)
    assert isinstance(transcript, list)
    assert len(transcript) > 0
    assert "text" in transcript[0]
