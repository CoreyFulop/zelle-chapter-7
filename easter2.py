# easter2.py

def terms(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    return a, b, c, d, e

def printDate(day, year):
    if day > 31:
        day = day - 31
        month = "April"

        print(f"In {year}, Easter is on {month} {day}.")
    else:
        month = "March"

        print(f"In {year}, Easter is on {month} {day}.")

def main():
    print("This program computes Easter for 1900-2099 (inclusive).\n")

    year = eval(input("Enter a year from 1900-2099 (inclusive): \n"))

    if year < 1900 or year > 2099:
        print(f"{year} is not in the correct range.")
    elif year == 1954 or year == 1981 or year == 2049 or year == 2076:
        a, b, c, d, e = terms(year)
        day = 22 + d + e - 7
        printDate(day, year)
    else:
        a, b, c, d, e = terms(year)
        day = 22 + d + e
        printDate(day, year)

if __name__ == "__main__":
    main()
