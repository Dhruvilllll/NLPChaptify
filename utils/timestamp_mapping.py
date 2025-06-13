def map_summary_to_timestamp(transcript, chunks):
    timestamps = []
    words = [t['text'] for t in transcript]
    full_text = " ".join(words)

    start_time = 0
    for chunk in chunks:
        duration = len(chunk.split()) / len(full_text.split())
        timestamps.append({
            "start": round(start_time, 2),
            "end": round(start_time + (duration * transcript[-1]["start"]), 2)
        })
        start_time = timestamps[-1]["end"]
    return timestamps
