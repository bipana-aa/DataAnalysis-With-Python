# name and favourite number
name = input("Enter your name: ")
fav = input("Enter your favourite number: ")
print("Name:", name)
print("Favourite number:", float(fav))

# total cost of apples
price = float(input("Enter the price of one apple: "))
qty = int(input("Enter the number of apples: "))
print(f"Total cost is ${price * qty:g}")

# format the name and make a username
first = input("Enter first name: ").strip().capitalize()
last = input("Enter last name: ").strip().upper()
username = first[:3] + last[-2:]    # first 3 letters + last 2 letters
print("Full name:", first, last)
print("Username:", username)
print("First letter:", first[0])

# gender from title
full = input("Enter name with title (Mr/Miss): ").strip()
title = full.split()[0].lower().rstrip(".")
if title == "mr":
    print("Male")
elif title in ("miss", "mrs", "ms"):
    print("Female")
else:
    print("Unknown")

# username checks
username = input("Enter a username: ").strip()
print("Vowel" if username[0].lower() in "aeiou" else "Not a vowel")
print("Last three characters:", username[-3:])
print("Strong username" if len(username) >= 8 else "Weak username")

# count even and odd numbers up to n
n = int(input("Enter n: "))
even = odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)

#numbers 1 to 100, then multiples of 3, then skip multiples of 9
for i in range(1, 101):
    print(i, end=" ")
print()
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=" ")
print()
for i in range(1, 101):
    if i % 3 == 0:
        if i % 9 == 0:
            continue    # skip these
        print(i, end=" ")
print()

#  divisible by both 4 and 6
for i in range(1, 201):
    if i % 4 == 0 and i % 6 == 0:
        print(i, end=" ")
print()

# sum of digits
num = input("Enter an integer: ")
total = 0
for ch in num:
    if ch.isdigit():
        total += int(ch)
print("Sum of digits:", total)

# list and dictionary
students = ["Ram Sharma", "Sita Karki", "Hari Thapa", "Gita Rai", "Nabin Shrestha"]
student_info = {
    "course": ["Python Programming", "JAVA", "C++", "JAVA"],
    "semester": "Second Semester",
    "instructor": "Mr. Anil Sharma",
    "institute": "ABC College",
    "Grade": {"1st_Sem": "A", "2nd_Sem": "A+"},
}

# list questions
print(students[2].split()[0])             # a. first name of 3rd student
print(students[0].upper())                # b. first student in uppercase
print(students[-1].split()[-1][-3:])      # c. last 3 letters of last surname
print(students[1].split()[-1].lower())    # d. 2nd student's last name
print(len(students))                      # e. total students

# dictionary questions
print(set(student_info["course"]))        # a. set removes the duplicate JAVA
print(student_info["instructor"].lower()) # b.
print(student_info["institute"][-7:])     # c.
title = student_info["instructor"].split()[0].lower().rstrip(".")
print("Male" if title == "mr" else "Female")   # d. from "Mr."
student_info["Grade"]["3rd_Sem"] = "B"    # e. add 3rd sem, update 2nd sem
student_info["Grade"]["2nd_Sem"] = "A"
print(student_info)

# username analyzer function
def analyze_username(username):
    username = username.strip().lower()
    total_characters = len(username.replace(" ", ""))
    vowels = sum(1 for ch in username if ch in "aeiou")

    if total_characters < 5:
        print("Username is too short.")
    elif username.isalpha():
        print("Username contains only alphabets.")
    else:
        print("Username contains mixed characters.")
    return (total_characters, vowels)

print(analyze_username("  BipanaKhadka  "))