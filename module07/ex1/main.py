from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2,
                               "Rare", 4, "+1 mana per turn"))

    print(f"Deck stats: {deck.get_deck_stats()}")
    print("Drawing and playing cards:")

    ordered_names = ["Lightning Bolt", "Mana Crystal", "Fire Dragon"]
    deck.cards.sort(key=lambda card: ordered_names.index(card.name))

    game_state: dict[str, object] = {}
    while deck.cards:
        card = deck.draw_card()
        print(f"Drew: {card.name} ({card.card_type})")
        print(f"Play result: {card.play(game_state)}")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
