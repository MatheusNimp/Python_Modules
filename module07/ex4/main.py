from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()
    dragon = TournamentCard(
        "dragon_001", "Fire Dragon", 5, "Legendary", 8, 7, 1200)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Epic", 6, 6, 1150)

    platform.register_card(dragon)
    platform.register_card(wizard)

    for card in (dragon, wizard):
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("Creating tournament match...")
    print(f"Match result: {platform.create_match('dragon_001', 'wizard_001')}")

    print("Tournament Leaderboard:")
    for index, card in enumerate(platform.get_leaderboard(), start=1):
        print(f"{index}. {card.name} - Rating: "
              f"{card.rating} ({card.wins}-{card.losses})")

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
