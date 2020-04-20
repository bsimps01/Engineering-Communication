import random

def leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("In the year", year,"it's a leap year")
        return True
    else:
        print("It's not a leap year in the year", year)
        return False

year = random.choice(range(1700, 2020))

leap_year(year)