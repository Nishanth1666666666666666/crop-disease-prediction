from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Mock disease database
diseases = {
    "wheat": ["Rust", "Smut", "Powdery Mildew"],
    "rice": ["Blast", "Brown Spot", "Sheath Blight"],
    "maize": ["Leaf Blight", "Downy Mildew", "Ear Rot"]
}

# Prediction function
def predict_disease(crop, symptoms):
    crop = crop.lower()
    if crop in diseases:
        return random.choice(diseases[crop])
    else:
        return "Unknown disease (no data available)"

# API endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    crop = data.get("crop")
    symptoms = data.get("symptoms")
    prediction = predict_disease(crop, symptoms)
    return jsonify({"crop": crop, "prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)