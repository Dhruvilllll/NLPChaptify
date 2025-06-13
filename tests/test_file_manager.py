from utils.formatter import format_chapters

def test_format_chapters():
    summaries = ["Intro to ML", "Supervised vs Unsupervised"]
    chapters = format_chapters(summaries, chunk_duration=90)
    assert isinstance(chapters, list)
    assert len(chapters) == len(summaries)
    assert "start" in chapters[0] and "end" in chapters[0]
