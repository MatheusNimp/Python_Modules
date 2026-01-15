def main():
    file_name = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    print(f"\nAcessing Storage Vault: {file_name}")
    file_obj = None
    try:
        file_obj = open(file_name, "r")
        print("Connection established...")
        data = file_obj.read()

        print("RECOVERED DATA:\n")
        print(data, end="")

        if len(data) > 0 and data[-1] != "\n":
            print()

        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    finally:
        if file_obj is not None:
            file_obj.close()


if __name__ == "__main__":
    main()
