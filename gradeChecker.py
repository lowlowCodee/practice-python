print("Grade Checker")

grade = float(input("Enter your grade: "))

if grade >= 99:
    print("You got 1.00")
elif grade >= 90:
    print("You got 1.50")
elif grade >= 85:
    print("You got 2.00")
elif grade >= 80:
    print("You got 2.50")
elif grade >= 75:
    print("You got 3.00")
else:
    print("you failed!!")