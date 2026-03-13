all_students = []
courses = {"math", "english", "music", "politics"}

def menuSystem():
    user_input = int(input("""
        1. Add Student\n
        2. View All Students\n
        3. Search Student\n
        4. Show Statistics\n
        5. Exit\n
        Please enter a number of the action that should be carried out. \n 
        Number: """
    ))
    if 1 <= user_input <= 5:
        if user_input == 1:
            addStudent()
        elif user_input == 2:
            viewStudents()
        elif user_input == 3:
            searchStudent()
        elif user_input == 4:
            showStatistics()
        elif user_input == 5:
            input_5 = input("Are you sure you want to exit?")
            if input_5.lower() == "yes":
                return
            elif input_5.lower() == "no":
                print("Going back to the menu")
            else:
                print("Going back to the menu")
        else:
            print("Please input a correct number between 1 and 5")
            menuSystem()

def addStudent():
    student_name = input("Enter the full name of the student: ").title()
    while True:
        student_age = input("Enter the age of the student: ")
        if student_age.isdigit() and 15 <= int(student_age) <= 20:
            break
        else:
            print("Please enter an age between 15 and 20")
    while True:
        student_courses = input(f"Please input the courses to be added: {courses} ")
        student_courses = set(student_courses.strip().split(","))
        print(student_courses)
        if student_courses.issubset(courses):
            break
        else:
            print("Please enter 1 or more courses from the list")
    student = {"Name:" : student_name,"\nAge: " : student_age, "\nCourses: ": student_courses}
    all_students.append(student)


def viewStudents():
    if len(all_students) > 0:
        for student in all_students:
            print(student)
    else:
        choice = input("No students added yet. Do you wish to add one now? (y/n)")
        if choice == "y":
            addStudent()
        elif choice == "n":
            x = input("Press 'enter' to go back to menu")
            if x == "":
                menuSystem()
            else:
                print("You didn't press Enter")
                viewStudents
        else:
            print("Please give a valid input either y or no")
            viewStudents()

def searchStudent():
    name = input("Enter the full name of the student: ").title()
    for student in all_students:
        if name == student["Name:"]:
            print(student)
            return
        else:
            print("Not found")
    user_input = input("Press enter to go back to the menu: ")
    if user_input == "":
        menuSystem()
    else:
        searchStudent()

def showStatistics():
    print(f"The number of students are {len(all_students)}")
    print(f"The courses that available are: {courses}")
    counter_math = 0
    counter_english = 0
    counter_music = 0
    counter_politics = 0
    for student in all_students:
            counter_math += student["Courses: "].count("math")
            counter_english += student["Courses: "].count("english")
            counter_music += student["Courses: "].count("music")
            counter_politics += student["Courses: "].count("politics")
    all_counter = [(counter_math,"math"),(counter_english,"english"),(counter_music,"music"),(counter_politics,"politics")]
    all_counter.sort()
    print(f"lowest attended class is: {all_counter[0][1]}")
    all_counter.sort(reverse=True)
    print(f"highest attended class is: {all_counter[0][1]}")
    for course in all_counter:
        if course[0] == 0:
            print("The course that has no students is: ")
menuSystem()