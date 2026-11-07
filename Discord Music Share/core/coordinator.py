import time
import random
from providers.spotify import SpotifyProvider
from providers.youtube import YouTubeProvider
from discord.client import DiscordClient
import config

class Coordinator:
    def __init__(self):
        self.spotify = SpotifyProvider()
        self.youtube = YouTubeProvider()
        self.discord = DiscordClient()
        self.last_track_id = None

    def run_cycle(self):
        print("Checking for music updates...")
        track = self.spotify.get_current_track()

        if not track:
            print("No music playing.")
            return

        # Simple state check to avoid redundant API calls
        current_track_id = f"{track.title}-{track.artist}"
        if current_track_id == self.last_track_id:
            print("Same track playing, skipping update.")
            return

        print(f"New track detected: {track.title} by {track.artist}")
        yt_url = self.youtube.search_track_url(track)
        self.discord.update_presence(track.title, track.artist, yt_url)

        self.last_track_id = current_track_id

    def start(self):
        while True:
            self.run_cycle()
            # Add jitter to polling interval to avoid bot detection
            sleep_time = config.POLLING_INTERVAL + random.uniform(-5, 5)
            print(f"Sleeping for {sleep_time:.2f}s...")
            time.sleep(max(10, sleep_time))
