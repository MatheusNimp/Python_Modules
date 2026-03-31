FILENAME = "ancient_fragment.txt"


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {FILENAME}")
    try:
        file = open(FILENAME, "r")
        print("Connection established...\n")
        content = file.read().strip()
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("RECOVERED DATA:")
    if content:
        for line in content.splitlines():
            print(line)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
