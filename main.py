import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model once
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("brain_tumor_model.h5")

model = load_model()

# Custom styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #f0f5ff, #e6f0ff);
        font-family: 'Inter', sans-serif;
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        padding: 0.6em 2em;
        border-radius: 9999px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    .result-box {
        background-color: #dbeafe;
        border: 1px solid #93c5fd;
        padding: 1em;
        border-radius: 1em;
        text-align: center;
        color: #1e40af;
        font-weight: 600;
        margin-top: 1.5em;
    }
    .centered-img {
        display: flex;
        justify-content: center;
        margin-bottom: 1em;
    }
    /* Target the uploaded filename text */
    .uploadedFileName, .stFileUploader .uploaded-file-name {
        color: #2563eb !important;  /* 🔵 Blue */
        font-weight: 600;
        font-size: 0.95rem;
    }
    /* 👇 Hide default white file name info */
    .css-1uixxvy.e1b2p2ww15 {
        display: none !important;
    }

    label, footer {
        color: #1e3a8a !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header with centered brain icon
st.markdown("""
    <div class="centered-img">
        <img src="https://img.icons8.com/fluency/96/brain.png" width="72" alt="Brain">
    </div>
    <h1 style='text-align:center; color:#2563eb;'>Brain Tumor Detector</h1>
    <p style='text-align:center; font-size:16px; color:#7c3aed; font-weight:500;'>
    Upload a brain MRI image to detect tumor presence using AI
    </p>
""", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload MRI Scan (PNG, JPG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with st.spinner("Diagnosing..."):
        image = Image.open(uploaded_file).convert("L")
        resized = image.resize((256, 256))
        input_array = np.array(resized).reshape(1, 256, 256, 1) / 255.0

         # ✅ Custom violet-colored filename display
        st.markdown(f"""
            <div style='margin: 0.8em 0 0.3em; font-weight: 600; color: #7c3aed; font-size: 0.95rem;'>
                📄 Uploaded File: {uploaded_file.name}
            </div>
        """, unsafe_allow_html=True)

        # Show image preview
        st.image(image, caption="Uploaded MRI Image", use_container_width=True)

        # Predict
        prediction = model.predict(input_array)[0][0]

        # Show prediction result
        if prediction > 0.5:
            st.markdown(f"<div class='result-box'>🧠 <strong>Prediction:</strong> Brain Tumor Detected</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='result-box'>✅ <strong>Prediction:</strong> No Tumor Found</div>", unsafe_allow_html=True)

# Footer
st.markdown("<footer style='margin-top: 3em; text-align: center; color: gray;'>Powered by Streamlit & TensorFlow</footer>", unsafe_allow_html=True)
