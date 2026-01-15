def attempt_acess(file_name, routine):
    if routine:
        print(f"\nROUTINE ACCESS: Attempting access to '{file_name}'...")
    else:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")

    try:
        with open(file_name, "r") as f:
            data = f.read()
            print(f"SUCCESS: Archive recovered - '{data}'")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    attempt_acess("lost_archives.txt", False)
    attempt_acess("classified_vault.txt", False)
    attempt_acess("standard_archive.txt", True)

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
