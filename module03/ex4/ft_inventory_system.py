import sys
from typing import Dict, Tuple

# Teste command
# (python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1)


def parse_args(argv: list[str]) -> Dict[str, int]:
    """
    Parse command-line arguments in the format item:quantity.

    Example:
        sword:1 potion:5 shield:2

    Returns:
        A dictionary mapping item names to their total quantities.
    """
    inventory: Dict[str, int] = dict()

    i: int = 1
    while i < len(argv):
        arg: str = argv[i]
        parts: list[str] = arg.split(":")

        if len(parts) != 2:
            i += 1
            continue

        name: str = parts[0].strip()
        qty_str: str = parts[1].strip()

        if name == "":
            i += 1
            continue

        try:
            qty: int = int(qty_str)
        except ValueError:
            i += 1
            continue

        if qty < 0:
            i += 1
            continue

        current: int | None = inventory.get(name)
        if current is None:
            inventory.update({name: qty})
        else:
            inventory.update({name: current + qty})

        i += 1

    return inventory


def total_items(inventory: Dict[str, int]) -> int:
    """
    Calculate the total number of items in the inventory.

    Args:
        inventory: Dictionary of items and quantities.

    Returns:
        Sum of all quantities.
    """
    total: int = 0
    for _, qty in inventory.items():
        total += qty
    return total


def find_most_and_least(
    inventory: Dict[str, int]
) -> Tuple[str, int, str, int]:
    """
    Find the most and least abundant items.

    Args:
        inventory: Dictionary of items and quantities.

    Returns:
        A tuple containing:
        (most_item_name, most_quantity, least_item_name, least_quantity)
    """
    most_name: str = ""
    most_qty: int = -1
    least_name: str = ""
    least_qty: int = -1

    first: bool = True
    for name, qty in inventory.items():
        if first:
            most_name = name
            most_qty = qty
            least_name = name
            least_qty = qty
            first = False
        else:
            if qty > most_qty:
                most_name = name
                most_qty = qty
            if qty < least_qty:
                least_name = name
                least_qty = qty

    return most_name, most_qty, least_name, least_qty


def format_percent(part: int, whole: int) -> str:
    """
    Format a percentage with one decimal place.

    Args:
        part: Portion value.
        whole: Total value.

    Returns:
        Percentage as a formatted string.
    """
    if whole == 0:
        return "0.0"
    pct: float = (part * 100.0) / whole
    return f"{pct:.1f}"


def print_inventory_sorted_by_qty_desc(
    inventory: Dict[str, int],
    total: int
) -> None:
    """
    Print inventory items sorted by quantity (descending).

    Sorting is done manually without using sorted().
    """
    printed: Dict[str, bool] = dict()
    printed_count: int = 0
    n: int = len(inventory)

    while printed_count < n:
        max_name: str = ""
        max_qty: int = -1

        for name, qty in inventory.items():
            if printed.get(name) is not None:
                continue
            if qty > max_qty:
                max_qty = qty
                max_name = name

        if max_name == "":
            break

        percent: str = format_percent(max_qty, total)
        print(f"{max_name}: {max_qty} units ({percent}%)")

        printed.update({max_name: True})
        printed_count += 1


def abundance_categories(
    inventory: Dict[str, int]
) -> Dict[str, Dict[str, int]]:
    """
    Categorize items by abundance.

    Rules:
        - Moderate: quantity >= 4
        - Scarce: quantity <= 3

    Returns:
        A dictionary with category names
        as keys and item dictionaries as values.
    """
    moderate: Dict[str, int] = dict()
    scarce: Dict[str, int] = dict()

    for name, qty in inventory.items():
        if qty >= 4:
            moderate.update({name: qty})
        else:
            scarce.update({name: qty})

    return {"Moderate": moderate, "Scarce": scarce}


def restock_suggestions(inventory: Dict[str, int]) -> str:
    """
    Generate restock suggestions.

    Rule:
        Items with quantity <= 1 need restocking.

    Returns:
        A string representation of a list of item names.
    """
    result: str = "["
    first: bool = True

    for name, qty in inventory.items():
        if qty <= 1:
            if not first:
                result += ", "
            result += f"'{name}'"
            first = False

    result += "]"
    return result


def format_keys_as_list_string(inventory: Dict[str, int]) -> str:
    """
    Format dictionary keys as a list-like string.
    """
    s: str = "["
    first: bool = True

    for key in inventory.keys():
        if not first:
            s += ", "
        s += f"'{key}'"
        first = False

    s += "]"
    return s


def format_values_as_list_string(inventory: Dict[str, int]) -> str:
    """
    Format dictionary values as a list-like string.
    """
    s: str = "["
    first: bool = True

    for value in inventory.values():
        if not first:
            s += ", "
        s += f"{value}"
        first = False

    s += "]"
    return s


def main() -> None:
    """
    Entry point of the Inventory Master system.
    """
    inventory: Dict[str, int] = parse_args(sys.argv)

    print("=== Inventory System Analysis ===")

    total: int = total_items(inventory)
    unique: int = len(inventory)

    print(f"\nTotal items in inventory: {total}")
    print(f"Unique item types: {unique}")

    print("\n=== Current Inventory ===")
    print_inventory_sorted_by_qty_desc(inventory, total)

    print("\n=== Inventory Statistics ===")
    if unique == 0:
        print("Most abundant:  (0 units)")
        print("Least abundant:  (0 units)")
    else:
        (most_name, most_qty,
         least_name, least_qty) = find_most_and_least(inventory)
        print(f"Most abundant: {most_name} ({most_qty} units)")
        print(f"Least abundant: {least_name} ({least_qty} units)")

    print("\n=== Item Categories ===")
    categories: Dict[str, Dict[str, int]] = abundance_categories(inventory)
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_suggestions(inventory)}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {format_keys_as_list_string(inventory)}")
    print(f"Dictionary values: {format_values_as_list_string(inventory)}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()
