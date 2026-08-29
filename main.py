print("========================================")
print("             DEVTRACK                    ")
print("  Developer Learning & Project Manager    ")
print("========================================")

##GLOBAL DATA STRUCTURES
lot = []


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
        print("Opening Dashboard...\n")
    elif choice == 2:
        # print("Opening Learning Topics...\n")
        print("========== LEARNING TOPICS =========")
        print("1. Add Topic")
        print("2. View Topics")
        print("3. Back")
        ch = int(input("Enter your choice: \n"))
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
                    print(lot)
                    c = input("Do you want to enter another topic? \n")
                    if c.lower() == "n":
                        break
        elif ch == 2:  # View Topics
            if len(lot) == 0:
                print("No learning topics added yet.\n")
            else:
                print("========== LEARNING TOPICS ==========")
                for i in range(0, len(lot)):
                    print(f"{i+1} {lot[i][0]} {lot[i][1]}  {lot[i][2]}\n")
                continue
        else:
            continue
    elif choice == 3:
        print("Opening Projects...\n")
    elif choice == 4:
        print("Opening Tasks...\n")
    elif choice == 5:
        print("Opening Study Sessions...\n")
    elif choice == 6:
        print("Opening Reports...\n")
    elif choice == 7:
        print("Goodbye!")
        break
    elif choice > 7:
        print("Invalid choice. Please try again.\n")
