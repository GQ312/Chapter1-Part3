def year():
    num = int(input("Write your year: "))
    if num % 4 == 0:
        return "This year is leap year!"
    else:
        return "This year isn't leap year!"

print(year())