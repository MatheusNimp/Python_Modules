def ft_count_harvest_iterative():
    reamaning_days = int(input("Days until harvest: "))
    if reamaning_days != 0:
        for x in range(1, reamaning_days + 1, 1):
            print(f"Day: {x}")
    print("Harvest time!")
