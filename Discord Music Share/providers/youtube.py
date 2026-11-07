import requests
from providers.base import MusicTrack
import config

class YouTubeProvider:
    def __init__(self):
        self.api_key = config.YOUTUBE_API_KEY
        self.cache = {}

    def search_track_url(self, track: MusicTrack) -> str:
        query = f"{track.title} {track.artist}"
        if query in self.cache:
            return self.cache[query]

        try:
            url = "https://www.googleapis.com/youtube/v3/search"
            params = {
                "part": "snippet",
                "q": query,
                "type": "video",
                "maxResults": 1,
                "key": self.api_key
            }
            response = requests.get(url, params=params).json()
            video_id = response['items'][0]['id']['videoId']
            yt_url = f"https://www.youtube.com/watch?v={video_id}"
            self.cache[query] = yt_url
            return yt_url
        except Exception as e:
            print(f"YouTube Error: {e}")
            return ""
