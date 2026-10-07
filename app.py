from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)
CORS(app)

# Load Task 6 trained CNN model
model = tf.keras.models.load_model("task6_cnn_model.keras")

# CIFAR-10 class names
class_names = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]


@app.route("/")
def home():
    return "Flask API is running successfully!"


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Check if image is uploaded
        if "image" not in request.files:
            return jsonify({
                "error": "No image uploaded"
            }), 400

        file = request.files["image"]

        # Open image
        image = Image.open(file).convert("RGB")

        # Resize image to model input size
        image = image.resize((32, 32))

        # Convert image to NumPy array
        image_array = np.array(image)

        # Normalize pixel values
        image_array = image_array.astype("float32") / 255.0

        # Add batch dimension
        image_array = np.expand_dims(
            image_array,
            axis=0
        )

        # Make prediction
        prediction = model.predict(
            image_array,
            verbose=0
        )

        # Get predicted class index
        predicted_index = np.argmax(
            prediction[0]
        )

        # Get class name
        predicted_class = class_names[
            predicted_index
        ]

        # Calculate confidence
        confidence = float(
            prediction[0][predicted_index] * 100
        )

        # Return result to Streamlit
        return jsonify({
            "prediction": predicted_class,
            "confidence": confidence
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )