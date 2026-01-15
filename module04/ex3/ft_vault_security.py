def main():
    src_file = "classified_vault.txt"
    dest_file = "security_archive.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")

    print("\nIntiating secure vault access...")
    try:
        with open(src_file, "r") as f:
            data = f.read()
        print("Vault connection established with failsafe protocols")

        print("\nSECURE EXTRACTION:")
        print(data, end="")
        if len(data) > 0 and data[-1] != "\n":
            print()

    except FileNotFoundError:
        print("{[}CLASSIFIED{]} ERROR: Classified vault not found")

    print("\nSECURE PRESARVATION:")
    with open(dest_file, "w") as f:
        f.write("{[}CLASSIFIED{]} New security protocols archived\n")

    print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
