🎭 Emotionix – Emotion-Based Movie Recommendation System

Emotionix is an AI-powered web application developed by us that detects human facial emotions from images and recommends movies tailored to the user’s emotional state.
The project demonstrates the practical implementation of computer vision, machine learning, and full-stack web development to deliver a personalized entertainment experience.

🚀 Project Overview

Emotionix bridges the gap between human emotions and digital entertainment.
We designed and built this application to capture facial images via a camera, detect emotions using a deep learning–based facial emotion recognition model, and recommend movies by mapping detected emotions to relevant genres using external movie APIs.

This project was developed as a hands-on team exploration of deploying AI models in real-world, production-ready web applications.

✨ Key Features

🔐 Secure User Authentication using Supabase

😊 Facial Emotion Detection with FER (Facial Emotion Recognition)

🎬 Emotion-Based Movie Recommendation Engine

🔍 Movie Search Functionality using IMDb API (via RapidAPI)

🎙️ Voice-Based Movie Search for enhanced user experience

📷 Camera On/Off Toggle to ensure user privacy

🗄️ SQLite-Based Caching System to reduce API calls and improve performance

🛠️ Technology Stack
Programming Language

Python

Backend

Flask

Frontend

HTML

CSS

JavaScript

Computer Vision & AI

OpenCV

FER (Facial Emotion Recognition)

APIs & Services

Supabase (Authentication)

RapidAPI – IMDb236 (Movie Data)

Database

SQLite (API Response Caching)

⚙️ Installation & Local Setup
Prerequisites

Python 3.11 or higher

pip

Clone the Repository
git clone <your-repo-url>
cd Emotionix

Create & Activate Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate


macOS / Linux

python3 -m venv venv
source venv/bin/activate

Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

Environment Configuration

Create a .env file in the project root directory:

SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
FLASK_SECRET_KEY=your_flask_secret_key
RAPIDAPI_KEY=your_rapidapi_key
RAPIDAPI_HOST=imdb236.p.rapidapi.com


⚠️ Note: Never commit the .env file to version control.

Run the Application
python app.py


Access the application at:

http://localhost:5000

📁 Project Structure
Emotionix/
├── app.py                # Main Flask application
├── config.py             # Environment configuration handling
├── requirements.txt      # Project dependencies
├── templates/            # HTML templates
│   ├── home.html
│   ├── login.html
│   └── register.html
├── static/               # CSS, JavaScript, images
├── movie_cache.db        # SQLite cache database
└── .env                  # Environment variables (ignored)

🎯 Emotion-to-Genre Mapping Logic
Emotion	Recommended Genre
Happy	Comedy
Sad	Drama
Angry	Action
Surprise	Adventure
Neutral	Drama
Fear	Horror
📈 Learning Outcomes

Through this project, we gained hands-on experience in:

Building full-stack web applications using Flask

Integrating machine learning models into production-ready systems

Implementing facial emotion recognition using computer vision

Secure authentication and environment variable management

API integration, caching strategies, and performance optimization

🚀 Deployment

Emotionix is structured to be deployment-ready on cloud platforms such as Render.
Environment variables are securely managed, and optional services degrade gracefully if unavailable.

📜 License

This project is licensed under the MIT License.

👥 Authors

Developed by:

Ganesh Mane

Nagesh Fulari

Yashvardhan Mahamuni

Suhana Sheikh

⭐ If you like this project, consider giving it a star!