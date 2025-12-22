def ft_count_harvest_recursive():
    remaining_days = int(input("Days until harvest: "))

    def pass_days(day):
        if day <= remaining_days:
            print(f"Day {day}")
            pass_days(day + 1)
        else:
            print("Harvest time!")
            return
    pass_days(1)


ft_count_harvest_recursive()
