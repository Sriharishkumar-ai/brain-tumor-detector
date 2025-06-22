# 🧠 Brain Tumor MRI Classifier (Streamlit App)

This project is a **deep learning-powered web application** built with **Streamlit** that detects brain tumors from grayscale MRI images. Users can upload an MRI scan and get an instant prediction — “Brain Tumor Detected” or “No Tumor Found” — from a CNN model trained on medical image data.

## 📌 Project Overview

### 🔬 Objective
To assist healthcare professionals and patients with a simple, accessible tool that leverages AI to classify brain MRI scans.

### 🧠 How it works
- A pre-trained **Convolutional Neural Network (CNN)** takes a grayscale MRI scan.
- It classifies the image into two categories:
  - ✅ **No Tumor**
  - ⚠️ **Brain Tumor Detected**
- The app is built using **Streamlit** for interactivity and **TensorFlow** for inference.

### 🧰 Tech Stack
- `Python`, `TensorFlow`, `Streamlit`, `NumPy`, `PIL`
- Model trained using dataset from [Kaggle: Brain MRI Images](https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection)


## 🚀 Live Demo

👉 **Try the app on Hugging Face**  
👉 [Launch on Hugging Face Spaces](https://Sri-Harish-brain-tumor-detector.hf.space)


## 📁 File Structure
brain-tumor-detector/
├── main.py                # Streamlit app logic
├── brain_tumor_model.h5   # Trained CNN model
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT license
├── README.md              # This file
└── assets/                # (Optional) screenshots, test images

