print("========================================")
print("             DEVTRACK                    ")
print("  Developer Learning & Project Manager    ")
print("========================================")


##GLOBAL VARIABLES
lot = []
lop = []


##FUNCTIONS


def open_dashboard():
    while True:
        print("1. Dashboard")
        print("2. Learning Topics")
        print("3. Projects")
        print("4. Tasks")
        print("5. Study Sessions")
        print("6. Reports")
        print("7. Exit\n")

        choice = int(input("Enter your choice: \n"))
        if choice == 1:
            continue
        elif choice == 2:
            learning_topics()
        elif choice == 3:
            projects()
        elif choice == 7:
            print("Goodbye!")
            break

        elif choice > 7:
            print("Invalid choice. Please try again.\n")


def learning_topics():
    print("========== LEARNING TOPICS =========")
    print("1. Add Topic")
    print("2. View Topics")
    print("3. Back\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:  # Add Topic
        while True:
            a = input("Enter topic name: ")
            b = input("Enter difficulty: ")
            c = input("Enter status: ")
            if c not in ("Not Started", "In Progress", "Completed"):
                print("Enter valid status")
            else:
                lot.append([a, b, c])
                print("Topic added")
                # print(lot)
                c = input("Do you want to enter another topic? \n")
                if c.lower() == "n":
                    return
    elif ch == 2:  # View Topics
        if len(lot) == 0:
            print("No learning topics added yet.\n")
            return
        else:
            print("========== LEARNING TOPICS ==========")
            for i in range(0, len(lot)):
                print(f"{i+1} {lot[i][0]} {lot[i][1]}  {lot[i][2]}\n")
            return
    elif ch == 3:  # Back
        return


def projects():
    print("========== PROJECTS ==========")
    print("1. Add Project")
    print("2. View Projects")
    print("3. Back")
    ch = int(input("Enter your choice"))
    if ch == 1:
        while True:
            name = input("Enter the Project Name:")
            desc = input("Enter the Project Description:")
            tech = input("Enter the Project Technology:")
            status = input("Enter the Project Status:")
            if status not in ("Not Started", "In Progress", "Completed", "On Hold"):
                print("Enter valid status")
            else:
                progress = int(input("Enter your Project Progress"))
                if progress >= 0 and progress <= 100:
                    print("Progress Validated!")
                    lop.append([name, desc, tech, status, progress])
                    print("Project Added!")
                    n = input("Do you want to enter another Project")
                    if n.lower() == "n":
                        return
                else:
                    print("Enter valid Progress number in the range 0-100")
    elif ch == 2:
        if len(lop) == 0:
            print("No projects added yet.\n")
            return
        else:
            print("========== PROJECTS ==========")
            for i in range(0, len(lop)):
                print(f"{i + 1}. ", end="")
                for j in range(0, len(lop[i])):
                    print(f" {lop[i][j]}")
            return
    elif ch == 3:
        return


open_dashboard()
