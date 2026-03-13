academy = {"Mathematics", "Science", "Literature", "History", "Art", "Physical Education"}

def addCourseForStudent(add_Course):
    courses = set();
    while add_Course.lower() == "yes":
        print("\nAdding a new course for the student.")
        print("Available courses: " )
        print("1. Mathematics")
        print("2. Science")
        print("3. Literature")
        print("4. History")        
        print("5. Art")
        print("6. Physical Education\n")

        new_course = input("Which course do you want to add?: ")

        if new_course in ["1", "2", "3", "4", "5", "6"]:
            course_mapping = {
                "1": "Mathematics",
                "2": "Science",
                "3": "Literature",
                "4": "History",
                "5": "Art",
                "6": "Physical Education"
            }
            if course_mapping[new_course] in courses:
                print("\nCourse already added.")
            else:
                courses.add(course_mapping[new_course])
        else:
            print("\nInvalid course.")
        
        add_Course = input("\nDo you want to add another course?: yes/no: ")
    
    return courses;

def addStudent(students):
    name = input("Enter student name: ").title()
    age = int(input("Enter student age: "))
    while age < 15 or age > 20:
        print("Invalid age. Please enter a number between 15 and 20.")
        age = int(input("Enter student age: "))
    add_Course = input("Do you want to add a new course?: yes/no: ")
    courses = addCourseForStudent(add_Course)
    
    student_info = {"name": name, "age": age, "courses": courses}
    students.append(student_info)

    print(f"Student {name} added successfully.")
    print("-" * 20)
    return students;

def viewStudents(students):
    if not students:
        choice = input("No students added yet. Do you wish to add a student now? yes/no: ")
        if choice.lower() == "yes":
            addStudent(students)
            print("\nStudent Information: ")
            for student in students:
                print(f"\nName: {student['name']}, Age: {student['age']}, Courses: {', '.join(student['courses'])}")
            print("-" * 20)
        else:
            choice = input("Press enter to return to the main menu.")
            if choice == "":
                return
        
    print("\nStudent Information: ")
    for student in students:
        print(f"\nName: {student['name']}, Age: {student['age']}, Courses: {', '.join(student['courses'])}")
    
    print("-" * 20)

def searchStudent(students):
    name = input("Enter student name to search: ")
    print(f"\nSearching results for {name}: ")
    for student in students:
        if student["name"] == name:
            print(f"\nName: {student['name']}, Age: {student['age']}, Courses: {', '.join(student['courses'])}")
            print("-" * 20)
            return
    print("Student not found.")
    print("-" * 20)

def showStatistics(students):
    print("\nStudent Statistics:")
    if not students:
        print("No students found.")
        print("-" * 20)
        return
    total_students = len(students)
    print(f"Total Students: {total_students}")
    
    average_age = sum(int(student['age']) for student in students) / total_students
    print(f"Average Age: {average_age:.2f}")
    
    students_in_course = {course: 0 for course in academy}
    for student in students:
        for course in student['courses']:
            if course in students_in_course:
                students_in_course[course] += 1
    
    for course, count in students_in_course.items():
        print(f"Students enrolled in {course}: {count}")
    
    course_with_most_students = max(students_in_course, key=students_in_course.get)
    print(f"Course with the most students: {course_with_most_students} ({students_in_course[course_with_most_students]} students)")

    course_with_least_students = min(students_in_course, key=students_in_course.get)
    print(f"Course with the least students: {course_with_least_students} ({students_in_course[course_with_least_students]} students)")
    
    courses_without_students = [course for course, count in students_in_course.items() if count == 0]
    if courses_without_students:
        print(f"Courses without students: {', '.join(courses_without_students)}")
    else:
        print("All courses have students enrolled.")
    
    print("-" * 20)

def main():
    students = []
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Show Statistics")
        print("5. Exit")
        print("\n" + "-" * 20)
        choice = input("Enter your choice: ")
        
        print("\n" + "-" * 20)
        if choice == '1':
            students = addStudent(students)
        elif choice == '2':
            viewStudents(students)
        elif choice == '3':
            searchStudent(students)
        elif choice == '4':
            showStatistics(students)
        elif choice == '5':
            choice = input("Are you sure you want to exit? yes/no: ")
            if choice.lower() == "yes":
                break
            else:
                print("\n" + "-" * 20)
                continue
        else:
            print("Invalid choice. Please try again.")
            print("\n" + "-" * 20)

if __name__ == "__main__":
    main()