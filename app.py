from flask import Flask, request, jsonify
import joblib

# Create the Flask app
app = Flask(__name__)

# Load the saved model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Create a route (web address) that accepts messages
@app.route("/predict", methods=["POST"])
def predict():
    # Get the message from the request
    data = request.get_json()
    text = data["text"]
    
    # Convert the text and make a prediction
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    
    # Send back the result
    return jsonify({"prediction": prediction})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)