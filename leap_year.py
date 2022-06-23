# leap_year.py

def divisibleByFour(number):
    remains = number % 4
    if remains == 0:
        return True
    else:
        return False

def divisibleByFourHundred(number):
    remains = number % 400
    if remains == 0:
        return True
    else:
        return False

def checkCentury(number):
    numbers = str(number)
    if numbers[-1] == "0" and numbers[-2] == "0":
        return True
    else:
        return False

def main():
    print("This program determines if a year is a leap year.\n")

    year = eval(input("Please enter a year: "))

    if divisibleByFour(year) == True:
        if checkCentury(year) == True:
            if divisibleByFourHundred(year) == False:
                print(f"{year} is not a leap year.")
            else: print(f"{year} is a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()