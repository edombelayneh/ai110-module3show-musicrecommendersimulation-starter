from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    target_valence: float
    target_tempo_bpm: float
    target_danceability: float
    target_acousticness: float

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(dict(row))
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """
    Scores a single song against user preferences and explains the reasoning.
    Returns (score, explanation) where score is at most 10.0.
    """
    score = 0.0
    reasons = []

    # Categorical scoring
    if song.get("genre") == user_prefs.get("genre"):
        score += 3.0
        reasons.append(f"genre match (+3.0)")
    if song.get("mood") == user_prefs.get("mood"):
        score += 2.0
        reasons.append(f"mood match (+2.0)")

    # Numerical scoring: max_points * max(0, 1 - gap / max_gap)
    # max_gap for 0-1 scale features is 1.0; tempo uses 100 BPM as the range
    numerical_features = [
        ("energy",       1.5, 1.0),
        ("valence",      1.2, 1.0),
        ("tempo_bpm",    1.0, 100.0),
        ("danceability", 0.8, 1.0),
        ("acousticness", 0.5, 1.0),
    ]

    for key, max_pts, max_gap in numerical_features:
        if key in user_prefs:
            gap = abs(song[key] - user_prefs[key])
            pts = max_pts * max(0.0, 1.0 - gap / max_gap)
            score += pts
            reasons.append(f"{key} (+{pts:.2f})")

    explanation = ", ".join(reasons) if reasons else "no matching features"
    return score, explanation


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Scores all songs against user preferences and returns the top k.
    Each result is (song_dict, score, explanation).
    """
    scored = [(song, *score_song(user_prefs, song)) for song in songs]
    ranked = sorted(scored, key=lambda x: x[1], reverse=True)
    return ranked[:k]
