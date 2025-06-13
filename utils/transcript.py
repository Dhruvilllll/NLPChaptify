import os
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv

load_dotenv()

def fetch_youtube_transcript(video_id: str, lang: str = "en"):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        return transcript
    except Exception as e:
        print(f"[ERROR] Failed to fetch transcript: {e}")
        return []

# Whisper fallback (if you want to use Whisper locally):
def fetch_whisper_transcript(audio_path: str):
    import whisper
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['segments']  # List of dicts: start, end, text
