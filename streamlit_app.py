import streamlit as st
import requests

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="CIFAR-10 AI Classifier",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🤖 CIFAR-10 Image Classification")

st.write(
    "Upload an image and get a real-time prediction "
    "using the Flask API backend."
)

st.divider()

# -------------------------------------------------
# Image Upload
# -------------------------------------------------

st.subheader("📤 Upload an Image")

uploaded_file = st.file_uploader(
    "Choose a JPG, JPEG or PNG image",
    type=["jpg", "jpeg", "png"]
)

# -------------------------------------------------
# Prediction
# -------------------------------------------------

if uploaded_file is not None:

    st.success("Image uploaded successfully!")

    # Display uploaded image
    st.image(
        uploaded_file,
        caption="Uploaded Image",
        width=350
    )

    st.divider()

    # Prediction button
    if st.button("🔍 Predict", type="primary"):

        with st.spinner("Sending image to Flask API..."):

            try:

                # Prepare image for API request
                files = {
                    "image": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type
                    )
                }

                # Send image to Flask API
                response = requests.post(
                    "http://127.0.0.1:5000/predict",
                    files=files
                )

                # Check API response
                if response.status_code == 200:

                    result = response.json()

                    prediction = result["prediction"]
                    confidence = result["confidence"]

                    # Display result
                    st.success(
                        f"Prediction: {prediction}"
                    )

                    st.metric(
                        "Predicted Class",
                        prediction
                    )

                    st.metric(
                        "Confidence",
                        f"{confidence:.2f}%"
                    )

                else:

                    result = response.json()

                    st.error(
                        result.get(
                            "error",
                            "Prediction failed"
                        )
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Unable to connect to Flask API. "
                    "Please make sure Flask is running."
                )

            except Exception as e:

                st.error(
                    f"An error occurred: {str(e)}"
                )

else:

    st.info(
        "👆 Please upload an image to get a prediction."
    )

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.divider()

st.caption(
    "Task 8 — Integrating Streamlit Frontend with Flask API"
) 