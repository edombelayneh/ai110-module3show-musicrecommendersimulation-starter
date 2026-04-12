# 🎵 Music Recommender Simulation

## Project Summary

This project, called **Vibify 1.0**, is a rule-based music recommender simulation. It represents songs using attributes like genre, mood, energy, tempo, valence, danceability, and acousticness, and scores each song against a user taste profile. Songs earn points for matching genre and mood labels, and additional points for being numerically close to the user's target values. The scoring weights were deliberately tuned — genre bonus was lowered from 3.0 to 1.5, and mood bonus was raised to 2.5, because mood more reliably reflects what people actually want to hear. Several Ethiopian and East African songs were added to the catalog to better represent a broader range of musical culture.

---

## How The System Works

Each song has ten attributes. Three are for identification: id, title, and artist. Two are categorical: genre and mood. Five are numerical audio features on a 0.0 to 1.0 scale: energy, valence, danceability, acousticness, and tempo in beats per minute.

A user profile stores a preference for every one of those features. It has a favorite genre, a favorite mood, and a personal target value for each of the five numerical features.

To score a song the system awards points in two stages. First it checks the categorical features. A genre match earns 3.0 points. A mood match earns 2.0 points. No match earns 0.

For the numerical features the system rewards closeness, not just high or low values. The closer the song is to the user's target the more points it earns. A perfect match earns the full amount. As the gap grows the points drop sharply toward zero. The maximums are 1.5 for energy, 1.2 for valence, 1.0 for tempo, 0.8 for danceability, and 0.5 for acousticness.

The highest possible score is 10.0 points. Songs are ranked from highest to lowest. No more than two songs from the same artist appear in the top five. If two songs are within 0.02 points of each other the one with the genre match is ranked higher.

---

## Screenshot of Terminal Output

![alt text](<Screenshot 2026-04-12 at 12.28.20 PM.png>)

![alt text](<Screenshot 2026-04-12 at 12.38.02 PM.png>)

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Five user profiles were tested to evaluate how the system behaved across different scenarios:

- **High-Energy Pop** — The system correctly surfaced upbeat pop songs (e.g. Sunrise City) at the top. Results felt right.
- **Chill Lofi** — Got two strong matches right away (Midnight Coding and Library Rain), both genuinely slow and quiet lofi tracks.
- **Deep Intense Rock** — Storm Runner ranked first, the only song matching both genre and mood exactly. Clear separation from the rest.
- **Conflicted Listener** (high energy + melancholic mood) — Storm Runner still ranked first despite the user wanting a melancholic mood, because the genre match alone outweighed the melancholic song's mood bonus. This exposed a flaw and triggered a weight change: genre bonus was lowered from 3.0 to 1.5 and mood bonus was raised to 2.5. Valence was also boosted from 1.2 to 2.0.
- **Genre Ghost** (genre and mood not in catalog) — The system didn't crash, but all scores clustered between 5.1 and 5.4, making no result meaningfully better than another — it degraded gracefully but arbitrarily.

---

## Limitations and Risks

- The catalog has only 20 songs — users with specific or niche tastes will get poor results simply because options don't exist.
- Genre and mood matching is all-or-nothing: "ethio-jazz" earns zero points when a user asks for "jazz," even though they are related. There is no partial credit.
- The system has no diversity logic — a single genre can dominate results if its songs happen to score well numerically across many user types (e.g. Gym Hero appeared for multiple unrelated profiles).
- Lyrics, language, and cultural context are completely ignored. A user who specifically wants Amharic music has no way to express that beyond genre labels.
- All-or-nothing label matching means a wrong-mood song from the right genre can outrank a right-mood song from a different genre, which can produce results that feel off.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this made it clear how much a recommender depends on its catalog and its labels. The algorithm itself is simple, but the results are only as good as the data feeding it. A song can score well for the wrong reasons — Gym Hero kept appearing for "happy pop" users simply because its energy and danceability numbers were high, even though the song doesn't feel happy at all. The experiments also showed that every weight is a design decision: raising the mood bonus from 2.0 to 2.5 changed the rankings noticeably, deciding whether a slow Ethiopian ballad beat out a fast rock song for a user who wanted high energy. Those decisions are usually invisible to the person receiving the recommendations.

This project also showed where bias can quietly enter a system. The all-or-nothing label matching systematically under-serves users with culturally specific or niche tastes — there is no way to express that "ethio-jazz" is close to "jazz," so those users get treated as if they want something the catalog has never heard of. Real recommenders like Spotify likely use continuous similarity scores and hundreds of features to avoid exactly this kind of sharp cutoff, which gave a small but concrete glimpse into why that complexity exists.
