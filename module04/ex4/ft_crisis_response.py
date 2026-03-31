FILES_TO_TEST = [
    "lost_archive.txt",
    "classified_data.txt",
    "standard_archive.txt",
    "corrupted_archive.txt"
]


def access_archive(filename: str) -> None:
    if filename == "classified_vault.txt":
        raise PermissionError("Security protocols deny access")

    with open(filename, "r") as file:
        content = file.read().strip()

    if "CORRUPTION" in content or "ERROR" in content:
        raise ValueError("Corrupted archive detected")

    print(f'SUCCESS: Archive recovered - "{content}"')
    print("STATUS: Normal operations resumed")


def handle_archive_access(filename: str) -> None:
    if filename == "standard_archive.txt":
        print(f"\nROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")

    try:
        access_archive(filename)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except ValueError:
        print("RESPONSE: Data corruption detected in archive")
        print("STATUS: Crisis handled, data integrity protocols activated")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, emergency protocols complete")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    for filename in FILES_TO_TEST:
        handle_archive_access(filename)
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
