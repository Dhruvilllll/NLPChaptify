
from IPython.display import Markdown, display

def show_markdown(filepath):
    """
    Display a markdown file inside a Jupyter notebook or Streamlit (if supported).
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            return content
    except Exception as e:
        print(f"[ERROR] Failed to load markdown: {e}")
        return ""
