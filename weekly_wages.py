# weekly_wages.py

def main():
    print("This program calculates a weekly wage.\n")

    hours = eval(input("Enter the number of hours worked: "))

    rate = eval(input("Enter the hourly rate: "))

    hours_cutoff = 40

    total = 0
    if hours <= hours_cutoff:
        total = hours * rate
        print(f"\nPay for {hours} hours is {total}.")
    else: # hours > hours_cutoff 
        overrated_hours = hours - hours_cutoff 
        total = (hours_cutoff  * rate) + (1.5 * rate * overrated_hours)
        print(f"\nPay for {hours_cutoff} normal hours and {overrated_hours} overtime hours is {total}.")

main()
