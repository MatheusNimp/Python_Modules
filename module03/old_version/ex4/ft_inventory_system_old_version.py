def main():

    print("=== Player Inventory System ===")

    alice = {
        "sword":
        {
            "category": "weapon",
            "rarity": "rare",
            "quantity": 1,
            "value": 500
        },
        "potion":
        {
            "category": "consumable",
            "rarity": "common",
            "quantity": 5,
            "value": 50
        },
        "shield":
        {
            "category": "armor",
            "rarity": "uncommon",
            "quantity": 1,
            "value": 200
        }
            }
    bob = {
        "magic_ring":
        {
            "category": "accessory",
            "rarity": "rare",
            "quantity": 1,
            "value": 300
        },
        "potion":
        {
            "category": "consumable",
            "rarity": "common",
            "quantity": 0,
            "value": 50
        }
            }

    print("\n=== Alice's Inventory ===")

    inventories = {
            "Alice": alice,
            "Bob": bob
                  }
    alice_inv = inventories.get("Alice")

    total_value = 0
    total_items = 0
    categories = {}

    for item_name, item_data in alice_inv.items():
        category = item_data.get("category")
        rarity = item_data.get("rarity")
        quantity = item_data.get("quantity")
        unit_value = item_data.get("value")

        item_total = quantity * unit_value
        total_value = total_value + item_total
        total_items = total_items + quantity

        if category not in categories:
            categories[category] = quantity
        else:
            categories[category] = categories.get(category) + quantity

        print(
                f"{item_name} ({category}, {rarity}): "
                f"{quantity}x @ {unit_value} gold each = {item_total} gold"
            )

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")

    cat_str = ""
    for cat, count in categories.items():
        cat_str = cat_str + f"{cat}({count}), "
    print(f"Categories: {cat_str[:-2]}")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")

    bob_inv = inventories.get("Bob")
    alice_potion = alice_inv.get("potion")
    bob_potion = bob_inv.get("potion")

    give_quantity = 2
    if alice_potion is not None and bob_potion is not None:
        alice_quantity = alice_potion.get("quantity")
        bob_quantity = bob_potion.get("quantity")

        if alice_quantity >= give_quantity:
            alice_potion.update({"quantity": alice_quantity - give_quantity})
            bob_potion.update({"quantity": bob_quantity + give_quantity})
            print("Transaction successful!")
        else:
            print("Transaction failed!")
    else:
        print("Transaction failed!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice_inv.get('potion').get('quantity')}")
    print(f"Bob potions: {bob_inv.get('potion').get('quantity')}")

    print("\n=== Inventory Analytics ===")

    most_valuable_name = ""
    most_valuable_value = -1

    most_items_name = ""
    most_items_count = -1

    rare_items = {}

    for player_name, inv in inventories.items():
        player_value = 0
        player_items = 0

        for item_name, item_data in inv.items():
            quantity = item_data.get("quantity")
            val = item_data.get("value")
            rar = item_data.get("rarity")

            player_value = player_value + (quantity * val)
            player_items = player_items + quantity

            if rar == "rare" and quantity > 0:
                rare_items.update({item_name: True})

        if player_value > most_valuable_value:
            most_valuable_value = player_value
            most_valuable_name = player_name

        if player_items > most_items_count:
            most_items_count = player_items
            most_items_name = player_name

    print(f"Most valuable player: {most_valuable_name}"
          f" ({most_valuable_value} gold)")
    print(f"Most items: {most_items_name} ({most_items_count} items)")

    rare_str = ""
    for item_name in rare_items.keys():
        rare_str = rare_str + item_name + ", "
    print(f"Rarest items: {rare_str[:-2]}", end="")


if __name__ == "__main__":
    main()
