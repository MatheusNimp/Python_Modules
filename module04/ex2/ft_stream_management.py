import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    user_id = input("\nInput Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")

    print(f"\n{{[}}STANDARD{{]}} Archive status from {user_id}: {report}")

    print("{[}ALERT{]} System diagnostic: Communication channels verified",
          file=sys.stderr)

    print("{[}STANDARD{]} Data transmission complete")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()
