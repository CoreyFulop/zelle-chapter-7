# class_standing.py

def main():
    print("This program calculates the class standing of a student based on the number of credits they have earned.\n")

    credits = eval(input("Enter the number of credits the student has: "))

    if credits >= 26:
        student = "Senior"
    elif credits >= 16:
        student = "Junior"
    elif credits >= 7:
        student = "Sophomore"
    else: # credits < 7
        student = "Freshman"

    print(f"\nWith {credits} credits, the student is a {student}.")

main()
