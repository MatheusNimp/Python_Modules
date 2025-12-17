def ft_water_reminder():
    last_watering = input("Days since last watering: ")
    if int(last_watering) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")