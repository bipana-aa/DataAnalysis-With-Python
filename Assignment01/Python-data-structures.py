students = ["Ram Sharma", "Sita Karki", "Hari Thapa", "Gita Rai", "Nabin Shrestha"]

student_info = {
    "course": ["Python Programming", "JAVA", "C++", "JAVA"],
    "semester": "Second Semester",
    "instructor": "Mr. Anil Sharma",
    "institute": "ABC College",
    "Grade": {"1st_Sem": "A", "2nd_Sem": "A+"},
}

# students list
print(students[2].split()[0])
print(students[0].upper())
print(students[-1].split()[-1][-3:])
print(students[1].split()[-1].lower())
print(len(students))

# student_info dictionary
print(set(student_info["course"]))
print(student_info["instructor"].lower())
print(student_info["institute"][-7:])
title = student_info["instructor"].split()[0].lower().rstrip(".")
print("Male" if title == "mr" else "Female")

student_info["Grade"]["3rd_Sem"] = "B"
student_info["Grade"]["2nd_Sem"] = "A"
print(student_info)