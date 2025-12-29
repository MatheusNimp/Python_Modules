def garden_operations():
    print("Testing ValueError...\n")
    try:
        int("abc")
    except ValueError as error:
        print(f"Caught ValueError: {error}\n")
    print("Testing ZeroDivisionError...\n")
    try:
        10 / 0
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}\n")
    print("Testing FileNotFoundError...\n")
    try:
        raise FileNotFoundError("missing.txt")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: No such file '{error}'\n")
    print("Testing KeyError...\n")
    try:
        data = {"name": "Oak", "height": 200, "age": 365}
        print(data["missing_plant"])
    except KeyError as error:
        print(f"Caught KeyError: {error}\n")
    print("Testing mutiple error together...\n")
    try:
        int("abc")
        data = {"name": "Oak", "height": 200, "age": 365}
        print(data["missing_plant"])
        10 / 0
        raise FileNotFoundError("missing.txt")
    except (ValueError, KeyError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
