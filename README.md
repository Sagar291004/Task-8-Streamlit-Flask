# Task 8: Integrating Streamlit Frontend with Flask API

## Objective

To establish communication between frontend and backend components for real-time inference.

## Project Description

This project integrates a Streamlit frontend with a Flask backend API for real-time image classification.

The user uploads an image through the Streamlit interface. The image is sent to the Flask API using an HTTP POST request. The Flask backend preprocesses the image and performs prediction using the trained CNN model. The prediction and confidence score are returned to the Streamlit frontend and displayed dynamically.

## Dataset

The project uses the CIFAR-10 image classification dataset.

The model classifies images into the following 10 categories:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

## Technologies Used

- Python
- Flask
- Flask-CORS
- Streamlit
- TensorFlow/Keras
- NumPy
- Pillow
- Requests
- CIFAR-10

## System Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
HTTP POST Request
  ↓
Flask API
  ↓
CNN Model
  ↓
Prediction
  ↓
JSON Response
  ↓
Streamlit Result Display
Project Files
app.py
Contains the Flask backend API. It receives the uploaded image, preprocesses it, performs model prediction and returns the prediction result as JSON.
streamlit_app.py
Contains the Streamlit frontend. It allows the user to upload an image, sends the image to the Flask API and displays the prediction and confidence score.
requirements.txt
Contains the Python libraries required to run the project.
API Endpoint
POST /predict

The API accepts an uploaded image and returns:
{
    "prediction": "Automobile",
    "confidence": 92.04
}

Testing Results
Test Case	Result	Status
Automobile Image	Automobile – 92.04%	Pass
Dog Image	Dog – 56.44%	Pass
No Image Uploaded	Validation message displayed	Pass
Flask API Running	Prediction received	Pass
Flask API Stopped	Connection error handled	Pass
Flask API Restarted	Prediction successful	Pass


Results
The Streamlit frontend successfully communicated with the Flask backend API. Real-time predictions were generated using the trained CNN model and displayed with confidence scores.
Conclusion
The Streamlit frontend was successfully integrated with the Flask backend API. The application demonstrated successful API communication, real-time prediction capability and reliable error handling.
