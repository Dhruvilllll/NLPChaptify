import os
import json

def save_json(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_output(video_id, chapters, titles):
    save_json(chapters, f"outputs/chapters/{video_id}_chapters.json")
    save_json(titles, f"outputs/titles/{video_id}_titles.json")

    # Create Markdown
    md_lines = []
    for i, (ch, title) in enumerate(zip(chapters, titles)):
        start = seconds_to_hhmmss(ch.get("start", 0))
        end = seconds_to_hhmmss(ch.get("end", 0))
        md_lines.append(f"### Chapter {i+1}: {title}\n🕒 {start} - {end}\n{ch['summary']}\n\n---\n")
    md_text = "\n".join(md_lines)

    with open(f"outputs/markdown/{video_id}.md", "w", encoding="utf-8") as f:
        f.write(md_text)

def seconds_to_hhmmss(seconds):
    mins, secs = divmod(int(seconds), 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"
