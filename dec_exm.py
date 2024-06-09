def is_year_leap(year):
    return True if int(year)%4 == 0 else False

print(is_year_leap(input("Веддите год: ")))