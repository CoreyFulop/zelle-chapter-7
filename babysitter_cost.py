# babysitter_cost.py

def cost_calculate(starting_hour, ending_hour, starting_minute, ending_minute, rate):
    total_minutes = (ending_hour - starting_hour) * 60 + (ending_minute - starting_minute)
    duration_hours = total_minutes / 60
    babysitter_cost = duration_hours * rate
    return babysitter_cost

def main():
    print("This program calculates the total cost of a babysitter.\n")

    print("Input hours in the 24 hour clock format, e.g. 7 pm is 19.\n")

    start_h, start_m = eval(input("Enter the start time (hour, minute): "))

    end_h, end_m = eval(input("Enter the end time (hour, minute): "))

    base_rate = 2.50

    overtime_rate = 1.75

    if end_h < 21: # Period ends before overtime cutoff
        total_cost = cost_calculate(start_h, end_h, start_m, end_m, base_rate)
        print(f"The total cost for the babysitter is ${total_cost:.2f}.")
    elif start_h >= 21: # All minutes are overtime 
        total_cost = cost_calculate(start_h, end_h, start_m, end_m, overtime_rate)
        print(f"The total cost for the babysitter is ${total_cost:.2f}.")
    else: # Includes some base rated minutes and some overtime rated minutes
        base_rated_minutes = (21 - start_h) * 60 - start_m
        base_rated_hours = base_rated_minutes / 60
        base_cost = base_rated_hours * base_rate
        overtime_minutes = (end_h - 21) * 60 + end_m
        overtime_rated_hours = overtime_minutes / 60
        overtime_cost = overtime_rated_hours * overtime_rate
        total_cost = base_cost + overtime_cost
        print(f"The total cost for the babysitter is ${total_cost:.2f}.")

if __name__ == "__main__":
    main()
