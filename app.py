# app.py
import os
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

import argparse
from deployment.inference import run_pipeline
from utils.file_manager import save_json, save_markdown

def main():
    parser = argparse.ArgumentParser(description="🎬 YouTube Video Chapter Generator")
    parser.add_argument("--video_id", type=str, required=True, help="YouTube Video ID (e.g., dQw4w9WgXcQ)")
    args = parser.parse_args()

    video_id = args.video_id

    print(f"🚀 Running pipeline for Video ID: {video_id}...\n")

    # Run the full pipeline
    chapters, titles = run_pipeline(video_id)

    # Save as JSON
    output_json_path = f"outputs/chapters/{video_id}_chapters.json"
    save_json(chapters, output_json_path)

    # Save as Markdown
    output_md_path = f"outputs/markdown/{video_id}_chapters.md"
    save_markdown(chapters, titles, output_md_path)

    print("✅ Chapters generated and saved successfully!\n")
    print("📁 JSON:", output_json_path)
    print("📄 Markdown:", output_md_path)
    
    # Preview
    print("\n🧠 Final Chapters:\n")
    for i, chapter in enumerate(chapters):
        print(f"▶️ Chapter {i+1}: {titles[i]}")
        print(f"⏱ {chapter['start']} - {chapter['end']}")
        print(f"📄 Summary: {chapter['summary']}\n")

if __name__ == "__main__":
    main()
