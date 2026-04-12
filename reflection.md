# Reflection: Profile Comparisons

---

## Pair 1: High-Energy Pop vs. Chill Lofi

High-Energy Pop got Sunrise City at the top. Chill Lofi got Midnight Coding and Library Rain. These are completely different — and that's good. Each profile matched its genre and mood, which adds 4.0 bonus points before anything else is counted. The system pointed each user toward a completely different corner of the catalog, which is exactly what should happen.

---

## Pair 2: Deep Intense Rock vs. Conflicted Listener (high energy + melancholic)

Both profiles have high energy and fast tempo, but they want different moods. Storm Runner leads both lists, but it scored 9.70 for Deep Intense Rock (got genre + mood bonus) and only 7.21 for the Conflicted Listener (got genre bonus only, no mood match).

The interesting result is #2 for the Conflicted Listener: Antchi Hoye — a slow, quiet Ethiopian song. It has nothing to do with the user's energy or tempo request, but it is tagged "melancholic," which gave it a +2.5 mood bonus. That was enough to outrank faster songs. This shows that a single mood label can override what the numbers say, which isn't always what the user actually wants.

---

## Pair 3: Deep Intense Rock vs. Genre Ghost (unknown genre + mood)

Deep Intense Rock's top song scored 9.70. The Genre Ghost's top song only scored 5.44. The Genre Ghost asked for "metal/angry" — a genre and mood that don't exist in the catalog — so no song earned any categorical bonus. Without those bonuses, all scores are close together (5.44, 5.36, 5.31) and the results feel random. The system didn't crash, but it had nothing to work with beyond pure numbers.

---

## Why Does "Gym Hero" Keep Showing Up for the Wrong Profiles?

Gym Hero is tagged "pop/intense," but it shows up for both High-Energy Pop and Deep Intense Rock. The reason: its numbers are extreme. Energy = 0.93, danceability = 0.88. These values are close to what both profiles asked for numerically, so it earns high partial scores on every feature.

For a user who wants happy pop music, Gym Hero feels like a mismatch — it's a loud workout track, not a cheerful sing-along. But the system can't tell the difference because both descriptions translate to similar numbers. The mood label ("intense" vs. "happy") should have filtered it out, but the genre bonus for being "pop" kept it competitive. This is a real gap: the catalog uses broad labels, so the system treats a workout banger and a feel-good pop song as nearly the same thing.
