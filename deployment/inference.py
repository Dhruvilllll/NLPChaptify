import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.transcript import fetch_youtube_transcript
from utils.chunking import chunk_transcript
from utils.summarization import summarize_chunks
from utils.formatter import format_chapters
from utils.file_manager import save_output
from models.titler import generate_titles

def run_pipeline(video_id: str):
    transcript = fetch_youtube_transcript(video_id)
    chunks = chunk_transcript(transcript)
    summaries = summarize_chunks(chunks)
    titles = generate_titles(summaries)
    chapters = format_chapters(summaries)
    save_output(video_id, chapters, titles)
    return chapters, titles
