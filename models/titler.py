# models/titler.py

"""
Generate YouTube-style chapter titles based on chunk summaries.
"""

def generate_titles(summaries, max_words=8):
    """
    Generates a concise title for each summary.

    Args:
        summaries (list[str]): List of summary texts
        max_words (int): Maximum words allowed in the title

    Returns:
        list[str]: List of title strings
    """
    titles = []
    for summary in summaries:
        words = summary.strip().split()
        title = " ".join(words[:max_words])
        if len(words) > max_words:
            title += "..."
        titles.append(title)
    return titles
