# If statements
age = int(input("What is your age "))
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote ")

#Elif statements
grade = int(input("What is your score? "))

if grade >= 90:
    print("A")

elif grade >= 80:
    print("B")

elif grade >= 70:
    print("C")

else:
    print("FAIL")

#Logical operators and, not and or
is_available = bool(input("Are you available(True/False) "))

if age >= 18 and is_available == True:
    print("You can vote ")
else:
    print ("You cannot vote ")

#or
if age >= 18 or is_available == True:
    print("You can vote ")
else:
    print("You cannot vote")
