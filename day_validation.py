def day_valid(day, month):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 0 < day < days[month]:
        pass
    else:
        day = int(input("Please enter day in numerical expression: "))