# 🧠 Brain Tumor MRI Classifier – Streamlit Web App

A user-friendly, AI-powered web application that analyzes **brain MRI scans** to detect the presence of tumors. Built with **Streamlit** and a **deep learning model**, this tool makes advanced medical image classification accessible to both healthcare professionals and the general public.



## 📌 Project Overview

### 🎯 Purpose

To support **early detection of brain tumors** through a simple, web-based interface powered by AI. The application enables users to upload grayscale MRI scans and receive real-time predictions — helping clinicians, patients, and researchers.



## 🧠 How It Works

* A pre-trained **Convolutional Neural Network (CNN)** processes uploaded MRI scans.
* It classifies each image into one of two categories:

  * ✅ **No Tumor Found**
  * ⚠️ **Brain Tumor Detected**
* The app interface is built using **Streamlit**, with inference powered by **TensorFlow**.


## 🛠️ Technologies Used

| Component          | Tools / Libraries                                                                                      
| **Language**       | Python                                                                                                 
| **Modeling**       | TensorFlow (CNN)                                                                                       
| **Web App**        | Streamlit                                                                                              
| **Image Handling** | NumPy, Pillow (PIL)                                                                                    
| **Dataset**        | [Kaggle: Brain MRI Images](https://www.kaggle.com/navoneel/brain-mri-images-for-brain-tumor-detection) 


## 🚀 Try It Live

💻 **Launch the App**
👉 [Hugging Face Spaces Deployment](https://Sri-Harish-brain-tumor-detector.hf.space)

No installation needed — just upload an MRI image and see instant results.


## 📁 Project Structure

```
brain-tumor-detector/
├── main.py                # Streamlit application logic
├── brain_tumor_model.h5   # Trained CNN model (TensorFlow)
├── requirements.txt       # Python package dependencies
├── LICENSE                # Open-source MIT License
└── README.md              # Project documentation (this file)
```
## Drive Link for Trained CNN Model: https://drive.google.com/file/d/13jq33NwIxSrmuef4G3uZZQwrG0wT9VuK/view?usp=sharing
File size is above 100mb, github only supports files lesser than 100 mb
## 👥 Who Is This For?

* **Healthcare professionals** exploring AI tools for diagnostics
* **Researchers** in medical imaging and deep learning
* **Non-technical stakeholders** (HR, founders) assessing project feasibility and impact
* **Developers** interested in AI + healthcare applications



## 🚀 Deployment Guide

### 🖥️ Local Setup (Run on Your Machine)

#### ✅ Prerequisites
- Python 3.7 or higher
- `pip` package manager
- Git (optional)

#### 📦 Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/brain-tumor-detector.git
cd brain-tumor-detector
📥 Step 2: Create Virtual Environment & Install Dependencies
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
▶️ Step 3: Run the Streamlit App
bash
Copy code
streamlit run main.py
The app will open in your browser at:
http://localhost:8501

☁️ Deployment on Hugging Face Spaces
1. Create a New Space
Go to 👉 https://huggingface.co/spaces
Click "Create New Space", then:

Name: brain-tumor-detector

SDK: Select Streamlit

Visibility: Choose Public or Private

2. Upload Project Files
Ensure the following files are in the root directory:

bash
Copy code
main.py
brain_tumor_model.h5
requirements.txt
assets/              # (Optional) images or screenshots
3. Example requirements.txt
txt
Copy code
streamlit
tensorflow
numpy
pillow

4. Deploy Automatically
Once all files are uploaded, the app will automatically deploy and be accessible at:

php-template
Copy code
https://<your-username>-<space-name>.hf.space
```
📝 License
This project is licensed under the MIT License — free to use, modify, and distribute.

📬 Contact / Contribute
For questions, collaboration, or contributions, feel free to open an issue or pull request.




