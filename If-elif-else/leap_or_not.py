def leap_year_check(year):
    if (not (year % 4 and year % 100 and year % 400)):
        print(year, "is leap Year")

    else:
        print(year, "is not leap Year")


leap_year_check(2025)
