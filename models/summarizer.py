import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "facebook/bart-large-cnn")

# These will be initialized by load_model()
_tokenizer = None
_model = None

def load_model():
    global _tokenizer, _model
    try:
        print(f"🔄 Loading model: {DEFAULT_MODEL}")
        _tokenizer = AutoTokenizer.from_pretrained(DEFAULT_MODEL)
        _model = AutoModelForSeq2SeqLM.from_pretrained(DEFAULT_MODEL)
        print("✅ Model loaded successfully.")
    except Exception as e:
        print(f"[❌ Error] Failed to load model: {e}")
        print("⚠️ Using fallback summarizer (text truncation only)")
        _tokenizer = None
        _model = None

# Load model at import
load_model()

def summarize_with_transformers(text, max_length=128):
    if _tokenizer is None or _model is None:
        return text[:max_length] + "..."  # fallback summary
    inputs = _tokenizer([text], return_tensors="pt", truncation=True, padding=True)
    summary_ids = _model.generate(
        inputs["input_ids"],
        num_beams=4,
        max_length=max_length,
        early_stopping=True
    )
    return _tokenizer.decode(summary_ids[0], skip_special_tokens=True)

def summarize(text, max_length=128):
    return summarize_with_transformers(text, max_length)
