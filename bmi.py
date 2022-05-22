# bmi.py

def main():
    print("This program calculates a person's BMI.\n")

    weight = eval(input("Please enter the person's weight in pounds: "))

    height = eval(input("Enter the person height in inches: "))

    bmi = (weight * 720) / height**2

    if bmi > 25:
        print(f"\nWith a BMI of {bmi}, you are above the healthy weight range for your height.")
    elif bmi >= 19:
        print(f"\nWith a BMI of {bmi}, you are in the healthy weight range for your height.")
    else: # bmi < 19
        print(f"\nWith a BMI of {bmi}, you are below the healthy weight range for your height.")
        
main()
