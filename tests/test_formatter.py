from utils.file_manager import save_json, load_json
import os

def test_file_save_and_load():
    dummy_data = {"test": 123}
    filepath = "outputs/test.json"
    save_json(dummy_data, filepath)

    assert os.path.exists(filepath)
    
    loaded = load_json(filepath)
    assert loaded["test"] == 123

    os.remove(filepath)
