def ft_garden_intro():
    """
    Displays a simple introduction of a garden plant,
    including its name, height, and age.
    """
    plant = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===\n"
          f"Plant: {plant}\nHeight: {height}cm\n"
          f"Age: {age} days\n\n"
          "=== End of Program ===")


def main():
    """
    Main function that runs the garden introduction.
    """
    ft_garden_intro()


if __name__ == "__main__":
    """
    Entry point of the program.
    """
    main()
