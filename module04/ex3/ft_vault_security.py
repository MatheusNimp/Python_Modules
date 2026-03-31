READ_FILE = "classified_data.txt"
WRITE_FILE = "security_archive.txt"


def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    try:
        with open(READ_FILE, "r") as file:
            content = file.read()
        print(content, end="")
        if content and content[-1] != "\n":
            print()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")

    print("\nSECURE PRESERVATION:")
    with open(WRITE_FILE, "w") as file:
        file.write("[CLASSIFIED] New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
