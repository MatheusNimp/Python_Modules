def main():
    print("=== Game Analytics Dashboard ===")

    players = [
        {"name": "alice", "score": 2300, "active": True,  "region": "north",
         "achievements": ["first_kill", "level_10", "boss_slayer",
                          "treasure_hunter", "speed_demon"]
         },
        {"name": "bob", "score": 1800, "active": True,  "region": "east",
         "achievements": ["first_kill", "level_10", "collector"]
         },
        {"name": "charlie", "score": 2150,
         "active": True,  "region": "central",
         "achievements": ["level_10", "boss_slayer", "treasure_hunter",
                          "speed_demon", "perfectionist",
                          "marathon", "no_damage"]
         },
        {"name": "diana", "score": 2050, "active": False, "region": "north",
         "achievements": ["first_kill", "level_10",
                          "story_complete", "boss_slayer"]
         },
    ]

    print("\n=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    doubled_scores = [p["score"] * 2 for p in players]
    print(f"Scores doubled: {doubled_scores}")

    active_players = [p["name"] for p in players if p["active"]]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in players}
    print(f"Player scores: {player_scores}")

    score_bucket = [
        ("high" if p["score"] >= 2100 else (
            "medium" if p["score"] >= 1800 else "low"))
        for p in players
    ]
    score_categories = {
        "high": sum([1 for b in score_bucket if b == "high"]),
        "medium": sum([1 for b in score_bucket if b == "medium"]),
        "low": sum([1 for b in score_bucket if b == "low"]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts_by_player = {p["name"]: len(
        p["achievements"]) for p in players}
    print(f"Achievement counts: {achievement_counts_by_player}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    all_achievements = {a for p in players for a in p["achievements"]}

    achievement_counts = {
        a: sum([1 for p in players if a in p["achievements"]])
        for a in all_achievements
    }

    unique_achievements = {a for a, c in achievement_counts.items() if c > 1}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p["region"] for p in players if p["active"]}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    total_players = len(unique_players)
    print(f"Total players: {total_players}")

    total_unique_achievements = len(all_achievements)
    print(f"Total unique achievements: {total_unique_achievements}")

    scores = [p["score"] for p in players]
    average_score = sum(scores) / len(scores)
    print(f"Average score: {average_score}")

    top_score = max(scores)
    top_player = [p for p in players if p["score"] == top_score][0]
    top_name = top_player["name"]
    top_achievements = len(top_player["achievements"])
    print(f"Top performer: {top_name} ({top_score}"
          f" points, {top_achievements} achievements)", end="")


if __name__ == "__main__":
    main()
