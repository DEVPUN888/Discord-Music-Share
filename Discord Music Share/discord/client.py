import requests
import config

class DiscordClient:
    def __init__(self):
        self.token = config.DISCORD_TOKEN
        self.base_url = "https://discord.com/api/v9/users/@me/settings"

    def update_presence(self, track_title: str, artist: str, yt_url: str):
        headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }

        # Payload for Rich Presence (Simplified for User Token)
        payload = {
            "activities": [{
                "name": "Spotify",
                "type": 2, # Listening
                "state": f"Listening to {track_title}",
                "details": f"by {artist}",
                "assets": {
                    "large_image": "spotify:logo"
                },
                "url": yt_url
            }]
        }

        try:
            response = requests.patch(self.base_url, headers=headers, json=payload)
            if response.status_code == 200:
                print(f"Updated presence to: {track_title}")
            else:
                print(f"Discord Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Discord Request Error: {e}")
