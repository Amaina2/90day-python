first_name = input("What is your first name? ")
last_name = input ("what is your last name? ")
age = int(input("What is your age? "))
height_meters = float(input("What is your height in meters? "))
major = input("What is your major? ")
year_of_study = int(input("What year are you of study are you in? "))
university = input("What is the name of your university? ")
fav_prog_lang = input("What is your favourite programming language? ")
dream_company = input("what is your dream company to work for? ")
dream_job = input("What is your dream job? ")
num_of_siblings = input("How many siblings do you have? ")
own_laptop = input("Do you own a laptop? (yes/no)")

if own_laptop == "yes":
    print(True)
elif own_laptop == "no":
    print(False)
else:
    print("invalid answer")

has_prog_xp = input("Do you have coding experience? (yes/no)")
if has_prog_xp == "yes":
    print(True)
elif has_prog_xp == "no":
    print(False)
else:
    print("invaid input")

# Step 2: Display Profile
print("========== STUDENT PROFILE ==========")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Height: {height_meters} m")
print(f"University: {university}")
print(f"Course: {major}")
print(f"Year: {year_of_study}")
print(f"Favorite Language: {fav_prog_lang}")
print(f"Dream Job: {dream_job}")
print(f"Dream Company: {dream_company}")
print(f"Number of Siblings: {num_of_siblings}")
print(f"Owns Laptop: {own_laptop}")
print(f"Programming Experience: {has_prog_xp}")

print(
    f"{first_name} {last_name} is {age} years old and stands at {height_meters} m tall. "
    f"They are in year {year_of_study} studying {major} at {university}. "
    f"Their favorite programming language is {fav_prog_lang}, and they dream of working as a "
    f"{dream_job} at {dream_company}. {first_name} has {num_of_siblings} sibling(s), "
    f"owns a laptop: {own_laptop}, and has programming experience: {has_prog_xp}.")

print("\n========== DATA TYPES ==========")
print(type(first_name))
print(type(last_name))
print(type(age))
print(type(height_meters))
print(type(major))
print(type(university))
print(type(year_of_study))
print(type(fav_prog_lang))
print(type(dream_company))
print(type(dream_job))
print(type(num_of_siblings))
print(type(own_laptop))
print(type(has_prog_xp))