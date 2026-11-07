from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class MusicTrack:
    title: str
    artist: str
    duration_ms: int
    album_art_url: Optional[str] = None
    provider_url: Optional[str] = None

class MusicProvider(ABC):
    @abstractmethod
    def get_current_track(self) -> Optional[MusicTrack]:
        pass
