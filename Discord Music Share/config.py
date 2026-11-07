# Discord Music Presence Configuration
import os
from dotenv import load_dotenv

load_dotenv()

# Spotify API Config
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

# YouTube API Config
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Discord Config
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# App Settings
POLLING_INTERVAL = int(os.getenv("POLLING_INTERVAL", 30))
