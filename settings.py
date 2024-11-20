import os

# API Keys
API_KEY = "your_openai_api_key"
SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
SPOTIFY_REDIRECT_URI = "http://localhost:8080/callback"
YOUTUBE_API_KEY = "your_youtube_api_key"

# ChromeDriver Path
CHROMEDRIVER_PATH = "C:/path/to/chromedriver.exe"

# Log File Settings
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "cassie.log")
os.makedirs(LOG_DIR, exist_ok=True)

# GUI Settings
WINDOW_TITLE = "C.A.S.S.I.E"
