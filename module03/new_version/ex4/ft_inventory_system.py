import sys


NEW_ITEM_NAME: str = "magic_item"
NEW_ITEM_QTY: int = 1


def main() -> None:
    """Parse inventory arguments and print inventory analysis."""
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    order: list[str] = []

    for arg in sys.argv[1:]:
        if arg.count(":") != 1:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item_name, quantity_str = arg.split(":")
        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue
        try:
            quantity: int = int(quantity_str)
        except ValueError as error:
            print(f"Quantity error for '{item_name}': {error}")
            continue
        inventory.update({item_name: quantity})
        order.append(item_name)

    print(f"Got inventory: {inventory}")
    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item_name in order:
        if total_quantity == 0:
            percentage: float = 0.0
        else:
            percentage = round(inventory[item_name] * 100 / total_quantity, 1)
        print(f"Item {item_name} represents {percentage:.1f}%")

    if inventory:
        most_abundant: str = order[0]
        least_abundant: str = order[0]
        for item_name in order[1:]:
            if inventory[item_name] > inventory[most_abundant]:
                most_abundant = item_name
            if inventory[item_name] < inventory[least_abundant]:
                least_abundant = item_name
        print(
            "Item most abundant: "
            f"{most_abundant} with quantity {inventory[most_abundant]}"
        )
        print(
            "Item least abundant: "
            f"{least_abundant} with quantity {inventory[least_abundant]}"
        )

    inventory.update({NEW_ITEM_NAME: NEW_ITEM_QTY})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
