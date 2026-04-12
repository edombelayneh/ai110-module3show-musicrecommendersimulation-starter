# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**Vibify 1.0**

---

## 2. Intended Use

Vibify 1.0 recommends songs based on a user's taste preferences — things like their favorite genre, mood, and how energetic they want the music to feel.

It is built for classroom exploration, not a real product. It assumes the user can describe what they want using a fixed set of attributes (genre, mood, energy, tempo, etc.). It does not learn from listening history or feedback — it only uses what the user tells it upfront.

---

## 3. How the Model Works

Each song in the catalog has a set of attributes: genre, mood, energy level, tempo, how positive it sounds (valence), how danceable it is, and how acoustic it is.

When a user describes their preferences, the system compares every song against those preferences and gives each song a score. Songs that match on genre get bonus points. Songs that match on mood get even more bonus points. Then, for each numerical feature (like energy or tempo), the closer the song is to what the user asked for, the more points it gets.

The song with the highest total score gets recommended first.

One deliberate change from the starter version: genre bonus was lowered from 3.0 to 1.5, and mood bonus was raised to 2.5. The reason is that mood is often what people actually care about when they listen to music — a happy song from an unfamiliar genre can still feel right, while a wrong-mood song from the right genre usually doesn't. Valence (how positive a song sounds) was also boosted from 1.2 to 2.0, because it tends to reflect mood better than other numbers do.

---

## 4. Data

The catalog has 20 songs. It covers a mix of genres: pop, lofi, rock, synthwave, ambient, jazz, indie pop, ethio-jazz, tizita, eskista, ethio-pop, gurage, and arabic. Moods include happy, chill, intense, focused, melancholic, moody, relaxed, nostalgic, energetic, uplifting, and peaceful.

Several Ethiopian and East African songs were added to the original starter dataset (Mahmoud Ahmed, Tilahun Gessesse, Aster Aweke, Hailu Mergia, Mulatu Astatke, Teddy Afro, Bezawork Asfaw, Gigi, Selamnesh Zemene, Al Moulouk). No songs were removed.

What is missing: the catalog is very small and leans heavily on a few genres. There is no hip-hop, R&B, classical, or country. Many moods have only one or two songs. A user who wants something very specific will likely get poor results simply because the catalog doesn't have enough options.

---

## 5. Strengths

The system works best when a user's preferences align clearly with what is in the catalog. For example:

- The Chill Lofi profile got two strong matches right at the top (Midnight Coding and Library Rain), both of which are genuinely slow, quiet lofi tracks.
- The Deep Intense Rock profile correctly surfaced Storm Runner as the top result — it is the only song that matches both the genre and mood exactly.
- When genre and mood both match, the scores are noticeably higher than everything else, which means the top recommendation is clearly separated from the rest. This makes the output feel confident rather than random.

---

## 6. Limitations and Bias

Genre and mood matching is all-or-nothing. A label either matches exactly or earns zero points — there is no partial credit. The system cannot tell that "ethio-jazz" and "jazz" are related, or that "intense" and "energetic" are similar feelings. This means users with niche or culturally specific tastes are systematically under-served.

The Conflicted Listener experiment made this visible: a user who wanted melancholic but high-energy music still got Storm Runner (a loud rock song) at the top, because the genre label matched while the mood did not. The only melancholic song in the catalog (Antchi Hoye) is slow and quiet — exactly the opposite of what the user's numbers described — but it still ranked #2 just because of the mood label.

The system also has no diversity logic. If one genre dominates the catalog numerically, it will keep appearing in results even when the user didn't ask for it. Gym Hero (pop/intense) shows up for multiple profiles because its energy and danceability numbers are extreme, which earns it partial points across many different user types.

Finally, lyrics, language, and cultural context are completely ignored. A user who wants Amharic music or Ethiopian instrumentals has no way to express that beyond genre labels — and those labels compete equally with "pop" and "rock."

---

## 7. Evaluation

Five profiles were tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, a Conflicted Listener (high energy but melancholic mood), and a Genre Ghost (a genre and mood that don't exist in the catalog).

For the standard profiles, results matched what was expected. The Chill Lofi user got quiet lofi tracks. The Rock user got Storm Runner. The Pop user got Sunrise City.

The most surprising result was the Conflicted Listener. Storm Runner ranked first even though the user wanted a melancholic mood — the genre match alone outweighed the only melancholic song's mood bonus. This triggered a weight change: genre was lowered and mood was raised to make the scoring better reflect what users actually feel.

The Genre Ghost confirmed that when no genre or mood matches exist, the system degrades gracefully — it doesn't crash, but the results feel arbitrary. All scores were clustered between 5.1 and 5.4, making it hard to say any result was meaningfully better than another.

---

## 8. Future Work

- Add partial credit for related genres and moods (for example, "ethio-jazz" should get some credit when a user asks for "jazz")
- Expand the catalog significantly — 20 songs is not enough to serve users with specific tastes
- Add a diversity rule so the same song or artist doesn't dominate multiple profiles
- Let users rate recommendations so the system can adjust weights over time
- Consider lyrics and language as a separate feature for users with cultural preferences
- Show users *why* a song ranked where it did in plain language, not just a list of feature scores

---

## 9. Personal Reflection

Building this made it clear how much a recommender system depends on its catalog and its labels. The algorithm itself is simple, but the results are only as good as the data feeding it. A song can score well for the wrong reasons — Gym Hero kept appearing for "happy pop" users simply because its numbers were high, even though the song doesn't feel happy at all.

The most interesting discovery was how powerful a single label can be. Raising the mood bonus from 2.0 to 2.5 changed the rankings noticeably. That small number decided whether a slow Ethiopian ballad beat out a fast rock song for a user who wanted high energy. It made me realize that every weight in a scoring system is a design decision with real consequences — and those decisions are usually invisible to the person receiving the recommendations.

Real music apps like Spotify or Apple Music probably use hundreds of features and continuous similarity scores instead of exact label matches. This project gave a small glimpse into why that complexity exists.
