def format_chapters(summaries, timestamps=None):
    chapters = []
    for i, summary in enumerate(summaries):
        entry = {"index": i + 1, "summary": summary}
        if timestamps:
            entry["start"] = timestamps[i]["start"]
            entry["end"] = timestamps[i]["end"]
        chapters.append(entry)
    return chapters
