
from roadmap import show_roadmap

print("================================")
print("       WELCOME TO CAMPUSPATH")
print("================================")

# 1. Student Profile
name = input("Enter your name: ")
course = input("Enter your course: ")
passing_year = input("Enter your passing year: ")
target_role = input("Enter your target job role: ")
python_level = input("Enter your Python level: ").lower().strip()

print("\n========== STUDENT PROFILE ==========")
print("Name:", name)
print("Course:", course)
print("Passing Year:", passing_year)
print("Target Job:", target_role)
print("Python Level:", python_level)

print("\nYour placement journey starts here!")

# 2. Skill Recommendations
print("\n========== SKILL RECOMMENDATIONS ==========")

if python_level == "beginner":
    print("1. Python variables and data types")
    print("2. If-else conditions")
    print("3. Loops")
    print("4. Functions")

elif python_level == "intermediate":
    print("1. Object-Oriented Programming")
    print("2. File Handling")
    print("3. Exception Handling")
    print("4. SQL Database Connectivity")

elif python_level == "advanced":
    print("1. Data Structures and Algorithms")
    print("2. Flask or Django")
    print("3. API Development")
    print("4. Machine Learning Basics")

else:
    print("Please enter Beginner, Intermediate, or Advanced.")

# 3. Score Validation
def get_score(subject, maximum):
    while True:
        try:
            score = int(input(
                f"Enter {subject} score (out of {maximum}): "
            ))

            if 0 <= score <= maximum:
                return score
            else:
                print(f"Enter marks between 0 and {maximum}.")

        except ValueError:
            print("Invalid input! Enter numbers only.")

# 4. Placement Readiness Test
print("\n========== PLACEMENT READINESS TEST ==========")

python_score = get_score("Python", 30)
sql_score = get_score("SQL", 25)
aptitude_score = get_score("Aptitude", 25)
communication_score = get_score("Communication", 20)

total_score = (
    python_score
    + sql_score
    + aptitude_score
    + communication_score
)

# 5. Placement Report
print("\n========== PLACEMENT REPORT ==========")
print("Student Name:", name)
print("Total Score:", total_score, "/ 100")

if total_score >= 80:
    print("Status: Excellent Preparation")

elif total_score >= 60:
    print("Status: Good Preparation")

elif total_score >= 40:
    print("Status: Average Preparation")

else:
    print("Status: Needs Improvement")

print("======================================")

# 6. Personalized Learning Roadmap
show_roadmap(target_role)

print("\nThank you for using CampusPath!")
print("Keep learning and keep improving!")
