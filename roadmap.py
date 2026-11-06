
def show_roadmap(target_role):

    role = target_role.lower().strip()

    print("\n========== YOUR LEARNING ROADMAP ==========")

    if role == "python developer":
        topics = [
            "Python Basics",
            "Functions and OOP",
            "Data Structures",
            "SQL and Database",
            "Flask or Django",
            "Git and GitHub",
            "Python Projects"
        ]

    elif role == "data analyst":
        topics = [
            "Excel",
            "Python Basics",
            "SQL",
            "Statistics",
            "Pandas and NumPy",
            "Power BI",
            "Data Analysis Projects"
        ]

    elif role == "web developer":
        topics = [
            "HTML",
            "CSS",
            "JavaScript",
            "Python Basics",
            "Flask or Django",
            "SQL",
            "Web Development Projects"
        ]

    else:
        print("Roadmap not available for this role.")
        print("Try Python Developer, Data Analyst, or Web Developer.")
        return

    for day, topic in enumerate(topics, start=1):
        print(f"Step {day}: Learn {topic}")


# Test the roadmap
show_roadmap("Python Developer")
