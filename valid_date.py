# valid_date.py

def testDays(maxdays, day, month, year):
    if 0 < int(day) <= maxdays:
        print(f"{month}/{day}/{year} is a valid date.")
    else:
        print(f"{month}/{day}/{year} is an invalid date.")

def main():
    print("This program determines if a (common year) given date is valid.\n")

    date = input("Please enter the date in month/day/year format: ")

    date_list = date.split("/")

    day = date_list[1]
    month = date_list[0].title()
    year = date_list[2]

    if month == "January":
        testDays(31, day, month, year)
    elif month == "February":
        testDays(28, day, month, year)
    elif month == "March":
        testDays(31, day, month, year)
    elif month == "April":
        testDays(30, day, month, year)
    elif month == "May":
        testDays(31, day, month, year)
    elif month == "June":
        testDays(30, day, month, year)
    elif month == "July":
        testDays(31, day, month, year)
    elif month == "August":
        testDays(31, day, month, year)
    elif month == "September":
        testDays(30, day, month, year)
    elif month == "October":
        testDays(31, day, month, year)
    elif month == "November":
        testDays(30, day, month, year)
    else: # month == "December"
        testDays(31, day, month, year)

if __name__ == "__main__":
    main()