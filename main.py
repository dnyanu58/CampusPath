
print("================================")
print("       WELCOME TO CAMPUSPATH")
print("================================")

# Student Profile
name = input("Enter your name: ")
course = input("Enter your course: ")
passing_year = input("Enter your passing year: ")
target_role = input("Enter your target job role: ")
python_level = input("Enter your Python level: ")

# Display Student Details
print("\n========== STUDENT PROFILE ==========")

print("Name:", name)
print("Course:", course)
print("Passing Year:", passing_year)
print("Target Job:", target_role)
print("Python Level:", python_level)

print("\nYour placement journey starts here!")


# Skill Recommendations
print("\n========== SKILL RECOMMENDATIONS ==========")

level = python_level.lower().strip()

if level == "beginner":
    print("Your Python level is Beginner.")
    print("Recommended skills:")
    print("1. Python variables and data types")
    print("2. If-else conditions")
    print("3. Loops")
    print("4. Functions")

elif level == "intermediate":
    print("Your Python level is Intermediate.")
    print("Recommended skills:")
    print("1. Object-Oriented Programming")
    print("2. File Handling")
    print("3. Exception Handling")
    print("4. SQL and Database Connectivity")

elif level == "advanced":
    print("Your Python level is Advanced.")
    print("Recommended skills:")
    print("1. Data Structures and Algorithms")
    print("2. Flask or Django")
    print("3. API Development")
    print("4. Machine Learning Basics")

else:
    print("Please enter Beginner, Intermediate, or Advanced.")