def validate_ingredients(ingredients: str) -> str:
    valid_elements = ["fire", "water", "earth", "air"]

    for element in valid_elements:
        if element in ingredients.lower():
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"
