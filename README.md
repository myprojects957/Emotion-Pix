# Emotionix - Movie Recommendation App Based on Emotion Detection

A Flask-based web application that detects user emotions through facial recognition and recommends movies based on detected emotions.

## Features

- **User Authentication**: Secure registration and login using Supabase
- **Emotion Detection**: Real-time facial emotion detection using FER (Facial Emotion Recognition)
- **Movie Recommendations**: Get movie suggestions based on detected emotions
- **Movie Search**: Search for movies with voice search capability
- **Camera Control**: Toggle camera on/off for privacy and security
- **Movie Caching**: Efficient caching system for API responses

## Technology Stack

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Supabase
- **APIs**: RapidAPI IMDB API for movie data
- **Video Processing**: OpenCV
- **Emotion Detection**: FER (Facial Emotion Recognition)

## Installation

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Local Setup

1. Clone the repository
```bash
git clone <your-repo-url>
cd Emotionix
```

2. Create a virtual environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Verify virtual environment is activated
```bash
# You should see (venv) at the beginning of your terminal prompt
# Example: (venv) C:\Users\YourName\Emotionix>
```

4. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

5. Create `.env` file with your credentials
```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_secret_key
RAPIDAPI_KEY=your_rapidapi_key
RAPIDAPI_HOST=imdb236.p.rapidapi.com
FLASK_SECRET_KEY=your_flask_secret_key
```

6. Run the application
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

### Deactivating Virtual Environment

When you're done working, deactivate the virtual environment:
```bash
deactivate
```

## Project Structure

```
Emotionix/
├── venv/                # Virtual environment (excluded from git)
├── app.py                # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
├── .env                 # Environment variables (not committed)
├── Procfile             # Deployment configuration
├── runtime.txt          # Python version specification
├── templates/           # HTML templates
│   ├── home.html        # Main app interface
│   ├── login.html       # Login page
│   └── register.html    # Registration page
├── static/              # Static assets (CSS, JS, images)
│   └── logo2.png        # App logo
└── movie_cache.db       # SQLite cache database
```

## API Keys Required

1. **Supabase** (Authentication)
   - Visit https://supabase.com
   - Create a new project
   - Copy URL and Anon Key

2. **RapidAPI** (Movie Data)
   - Visit https://rapidapi.com
   - Subscribe to "imdb236" API
   - Copy your API key

## Usage

1. **Register/Login**: Create an account or log in with existing credentials
2. **Enable Camera**: Toggle the camera switch in the navbar
3. **Capture Emotion**: Click "Capture Face" to detect emotion
4. **View Recommendations**: See movie suggestions based on detected emotion
5. **Search Movies**: Use the search bar to find specific movies
6. **Voice Search**: Click the microphone icon to search by voice

## Emotion-to-Genre Mapping

- 😊 Happy → Comedy
- 😢 Sadness → Drama
- 😠 Anger → Action
- 😮 Surprise → Adventure
- 😐 Neutral → Drama
- 😨 Fear → Horror

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions for Render.

## License

MIT License

## Support

For issues or questions, please contact the development team.
