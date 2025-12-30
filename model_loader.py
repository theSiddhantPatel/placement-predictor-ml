import pickle
import numpy as np

# load model once
with open("model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_placement(cgpa: float, iq: float) -> int:
    """
    Returns 1 if placed, 0 otherwise
    """
    input_data = np.array([[cgpa, iq]])
    prediction = model.predict(input_data)[0]
    return int(prediction)
