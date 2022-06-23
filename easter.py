# easter.py

def main():
    print("This program computes Easter for 1982-2048 (inclusive).\n")

    year = eval(input("Enter a year from 1982-2048 (inclusive): \n"))

    if year < 1982 or year > 2048:
        print(f"{year} is not in the correct range.")
    else:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19*a + 24) % 30
        e = (2*b + 4*c + 6*d + 5) % 7

        day = 22 + d + e

        if day > 31:
            day = day - 31
            month = "April"

            print(f"In {year}, Easter is on {month} {day}.")
        else:
            month = "March"

            print(f"In {year}, Easter is on {month} {day}.")

if __name__ == "__main__":
    main()