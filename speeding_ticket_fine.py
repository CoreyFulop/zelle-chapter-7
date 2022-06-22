# speeding_ticket_fine.py

def main():
    print("This program determines the fine for speeding in Podunksville.\n")

    speed_limit = eval(input("Enter the speed limit in mph: "))

    speed = eval(input("Enter the clocked speed in mph: "))

    base_penalty = 50
    mph_over_penalty = 5
    over_90_penalty = 200

    if speed > 90:
        penalty = base_penalty + (speed - speed_limit) * mph_over_penalty + over_90_penalty
        print(f"\nThe penalty for travelling {speed} mph in a {speed_limit} zone is {penalty}.")
    elif speed > speed_limit:
        penalty = base_penalty + (speed - speed_limit) * mph_over_penalty
        print(f"\nThe penalty for travelling {speed} mph in a {speed_limit} zone is {penalty}.")
    else: # speed <= speed_limit
        print("\nThis speed is legal.")

if __name__ == "__main__":
    main()