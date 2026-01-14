#!/usr/bin/python3.10

players = ["alice", "bob", "charlie", "diana"]

scores = {
    "alice": 2300,
    "bob": 1800,
    "charlie": 2150,
    "diana": 2050
}


achievements = {
    "alice": [
        "first_kill", "level_10", "boss_slayer", "collector", "speed_demon"
        ],
    "bob": ["first_kill", "level_10", "collector"],
    "charlie": ["level_10", "boss_slayer", "speed_demon", "perfectionist"],
    "diana": ["first_kill", "level_10"]
}


regions = ["north", "east", "north", "central", "east"]


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")
    high_scorers = [p for p, s in scores.items() if s > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    doubled_scores = [s * 2 for s in scores.values()]
    print(f"Scores doubled: {doubled_scores}")
    active_players = [p for p in players if p in scores]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p: s for p, s in scores.items()}
    print(f"Player scores: {player_scores}")
    score_categories = {
        "high": len([s for s in scores.values() if s > 2000]),
        "medium": len([s for s in scores.values() if 1500 <= s <= 2000]),
        "low": len([s for s in scores.values() if s < 1500])
    }
    print(f"Score categories {score_categories}")
    achievements_counts = {p: len(a) for p, a in achievements.items()}
    print(f"achievement counts: {achievements_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")
    unique_achievements = {a for lst in achievements.values() for a in lst}
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {r for r in regions}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analytics ===")
    total_players = len(unique_players)
    print(f"Total players: {total_players}")
    total_achievements = len(unique_achievements)
    print(f"Total unique achievements: {total_achievements}")
    avg_score = sum(scores.values()) / len(scores)
    print(f"Average score {avg_score}")
    top_player = max(scores, key=scores.get)
    print(
        f"Top performer: {top_player}"
        f"({scores[top_player]}) points, "
        f"{len(achievements[top_player])} achievements"
    )
