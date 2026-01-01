Placement Predictor – ML Web Application

This project is an end-to-end machine learning web application that predicts whether a student is likely to get placed based on CGPA and IQ. The project covers the complete journey from data analysis and model training to deployment as a live web application.

🚀 Features

Data analysis and visualization using pandas and matplotlib

Machine learning model built with scikit-learn

Clean separation of training and inference logic

Flask backend with both UI and API endpoints

Proper web flow using POST → Redirect → GET

Auto-clearing UI after prediction

Health check endpoint for deployment

Deployed online using Render

🧠 What I Learned

How to explore and understand datasets using pandas

Visualizing data to build intuition before training a model

Training and using ML models with scikit-learn

Converting Jupyter Notebook code into production-ready Python modules

Building a Flask web application for ML inference

Handling form submissions cleanly without duplicate requests

Managing Python virtual environments and dependencies

Deploying a Flask ML app on the cloud

🛠 Tech Stack

Python

pandas, numpy, matplotlib

scikit-learn

Flask

HTML/CSS

Render (deployment)

📂 Project Structure
ml100/
│── app.py
│── model_loader.py
│── model.pkl
│── requirements.txt
│── templates/
│ └── index.html
│── miniProject1D13.ipynb

▶️ Running the Project Locally

Clone the repository

git clone https://github.com/your-username/placement-predictor-ml.git
cd placement-predictor-ml

Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the application

python app.py

Open in browser

http://127.0.0.1:5000/

🌐 Live Demo

Deployed using Render:
👉 (Add your live URL here)

📌 API Endpoint (Optional)

POST /predict

{
"cgpa": 7.2,
"iq": 125
}

Response:

{
"prediction": 1
}

🎯 Future Improvements

Add confidence score to predictions

Improve UI styling

Use JavaScript fetch for seamless interaction

Add authentication and logging

Deploy frontend and backend separately

👤 Author

Siddhant Patel
Machine Learning & Software Development Enthusiast
