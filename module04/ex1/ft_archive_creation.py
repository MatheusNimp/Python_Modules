def main():

    file_name = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    print(f"\nInitializing new storage unit: {file_name}")
    file_obj = None

    file_obj = open(file_name, "w")
    print("Storage unit created successfully...\n")

    content = (
        "{[}ENTRY 001{]} New quantum algorithm discovered\n"
        "{[}ENTRY 002{]} Efficiency increased by 347%\n"
        "{[}ENTRY 003{]} Archived by Data Archivist trainee\n")

    file_obj.write(content)

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")

    if file_obj is not None:
        file_obj.close()


if __name__ == "__main__":
    main()
