import sys


def main():
    print("=== Command Quest ===")
    args = sys.argv
    argc = len(args)
    arguments_received = argc - 1
    program_name = args[0]
    if argc <= 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {arguments_received}")
        for i in range(1, argc):
            print(f"Argument {i}: {args[i]}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
