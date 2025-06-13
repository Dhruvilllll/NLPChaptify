# deployment/streamlit_app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from deployment.inference import run_pipeline
from outputs.markdown import show_markdown
from dotenv import load_dotenv

load_dotenv()

# App Title
st.set_page_config(page_title="YouTube Video Chaptering", layout="centered")
st.title("📺 YouTube Video Chaptering App")
st.markdown("Automatically generate timestamped video chapters using NLP.")

# Input Field
video_id = st.text_input("🔗 Enter YouTube Video ID (e.g. `dQw4w9WgXcQ`)")

# On Button Click
if st.button("🚀 Generate Chapters") and video_id:
    with st.spinner("Processing... Please wait ⏳"):
        try:
            # Run the full pipeline
            chapters, titles = run_pipeline(video_id)

            st.success("✅ Chapters Generated!")

            # Show Chapters
            for i, ch in enumerate(chapters):
                st.markdown(f"""
### Chapter {i+1}: {titles[i]}
🕒 `{ch['start']}s - {ch['end']}s`  
**Summary:** {ch['summary']}
---
""")

            # Display markdown output if available
            markdown_path = f"outputs/markdown/{video_id}_chapters.md"
            if os.path.exists(markdown_path):
                st.markdown("### 📄 Full Markdown Output")
                st.markdown(show_markdown(markdown_path))
            else:
                st.info("No markdown file found to display.")

        except Exception as e:
            st.error(f"❌ An error occurred:\n\n`{e}`")

# Footer
st.markdown("---")
st.markdown("🔧 Built by **Dhruvil Malvania** — [LinkedIn](https://www.linkedin.com/in/dhruvil-malvania-6a1479276/)")
