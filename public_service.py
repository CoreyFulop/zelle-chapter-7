# public_service.py

senator_age_requirement = 30
senator_citizen_years_requirement = 9 

rep_age_requirement = 25
rep_citizen_years_requirement = 7

def senator_eligability(senator_age_requirement, senator_citizen_years_requirement, input_age, input_citizen_years):
    if input_age >= senator_age_requirement and input_citizen_years >= senator_citizen_years_requirement:
        print("This person is eligable to be a US senator.")
    else:
        print("This person is not eligable to be a US senator.")

def rep_eligability(rep_age_requirement, rep_citizen_years_requirement, input_age, input_citizen_years):
    if input_age >= rep_age_requirement and input_citizen_years >= rep_citizen_years_requirement:
        print("This person is eligable to be a US representative.")
    else:
        print("This person is not eligable to be a US representative.")

def main():
    print("This program determines if a person is eligable to be a US senator or represenative.\n")

    age = eval(input("How old is the person: "))
    citizen_years = eval(input("How many years have they been a US citizen: "))

    print()

    senator_eligability(senator_age_requirement, senator_citizen_years_requirement, age, citizen_years)
    rep_eligability(rep_age_requirement, rep_citizen_years_requirement, age, citizen_years)

if __name__ == "__main__":
    main()