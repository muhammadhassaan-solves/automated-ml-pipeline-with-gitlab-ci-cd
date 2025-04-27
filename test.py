import os
import pickle

def test_model_loading():
    # 1. Make sure the file is there
    assert os.path.exists('model/model.pkl'), "model.pkl file does not exist"

    # 2. Try loading it
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)

    # 3. Sanity check
    assert model is not None, "Loaded model is None"
    print("✅ Model loaded successfully.")

if __name__ == "__main__":
    test_model_loading()
