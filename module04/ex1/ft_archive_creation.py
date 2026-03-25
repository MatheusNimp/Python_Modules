FILENAME = "new_discovery.txt"
ENTRIES: list[str] = [
    "[ENTRY 001] New quantum algorithm discovered",
    "[ENTRY 002] Efficiency increased by 347%",
    "[ENTRY 003] Archived by Data Archivist trainee",
]


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {FILENAME}")
    file = open(FILENAME, "w", encoding="utf-8")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    file.write("\n".join(ENTRIES) + "\n")
    file.close()
    for entry in ENTRIES:
        print(entry)
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{FILENAME}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
