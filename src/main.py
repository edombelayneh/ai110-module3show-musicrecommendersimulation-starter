"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs from the dataset.")

    user_profiles = [
        {
            "label": "High-Energy Pop",
            "genre": "pop",
            "mood": "happy",
            "energy": 0.88,
            "tempo_bpm": 125,
            "valence": 0.82,
            "danceability": 0.85,
            "acousticness": 0.10,
        },
        {
            "label": "Chill Lofi",
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.40,
            "tempo_bpm": 76,
            "valence": 0.58,
            "danceability": 0.60,
            "acousticness": 0.78,
        },
        {
            "label": "Deep Intense Rock",
            "genre": "rock",
            "mood": "intense",
            "energy": 0.92,
            "tempo_bpm": 150,
            "valence": 0.45,
            "danceability": 0.65,
            "acousticness": 0.10,
        },
        # --- Adversarial profiles ---
        {
            # Edge case: mood and energy directly contradict each other.
            # "melancholic" is a low-energy mood in the catalog (Antchi Hoye: energy 0.40),
            # but this user wants high energy (0.91). The scorer must choose between
            # awarding +2.0 for a mood match on a slow song vs. rewarding a fast song
            # that never gets the mood bonus. Watch which trade-off wins.
            "label": "Conflicted Listener (high energy + melancholic)",
            "genre": "rock",
            "mood": "melancholic",
            "energy": 0.91,
            "tempo_bpm": 150,
            "valence": 0.45,
            "danceability": 0.65,
            "acousticness": 0.10,
        },
        {
            # Edge case: genre and mood don't exist anywhere in the catalog.
            # No song earns the +3.0 genre bonus or +2.0 mood bonus, so the
            # entire ranking falls through to numerical features only.
            # Reveals which songs are numerically closest to "average" — and
            # whether the top result actually makes any intuitive sense.
            "label": "Genre Ghost (unknown genre + mood)",
            "genre": "metal",
            "mood": "angry",
            "energy": 0.50,
            "tempo_bpm": 100,
            "valence": 0.50,
            "danceability": 0.50,
            "acousticness": 0.50,
        },
    ]

    for profile in user_profiles:
        label = profile["label"]
        user_prefs = {k: v for k, v in profile.items() if k != "label"}

        print(f"\n{'='*40}")
        print(f"Profile: {label}")
        print(f"{'='*40}")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        for song, score, explanation in recommendations:
            print(f"{song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"  Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
