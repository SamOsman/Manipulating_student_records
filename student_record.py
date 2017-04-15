
students = dict()
students = {"marcus": [71, 85], "tommy": [56, 75], "belle": [75, 81]}
counter = 0
repeat = True
ask = "return to main menu {press 1}, quit {press 2}"

while repeat:
    userChoice = input("\nMain menu: \n 1.add student \n 2.delete student \n 3.find student \n 4.view all students "
                       "\n 5.update student grade \n 6.exit")

    if userChoice == "1":  # add student
        newName = input("new students name:")
        newMidterm = input("midterm mark:")
        newFinal = input("Final mark:")
        # add a new student to the dict
        students[newName.lower()] = [newMidterm, newFinal]

        reply = input(ask)
        if reply == "1":
            repeat = True
        else:
            repeat = False

    elif userChoice == "2":  # delete student
        removeStudent = input("Enter name of student to remove:")
        students.pop(removeStudent.lower())
        print("student record has been deleted")

    elif userChoice == "3":  # find student
        findStudent = input("Search for a student:")
        if findStudent.lower() in students:
            print("student record exists")
        else:
            print("Student record does NOT exist")

    elif userChoice == "4":  # view all students
        for k, v in students.items():
            print("Student: {0}".format(k))
            print("mid-term:" + str(v[0]) + ", final: " + str(v[1]))

        reply = input(ask)
        if reply == "1":
            repeat = True
        else:
            repeat = False

    elif userChoice == "5":  # update student record
        student_name = input("Enter name of student to be updated:")


        while True:
            if student_name.lower() in students:

                mid_term = input("new mid term mark {leave empty if no updates}: ")
                final_term = input("new final term mark {leave empty if no updates}: ")

                if not mid_term == "":
                    students[student_name][0] = mid_term
                    print("Midterm upgraded for " + student_name)

                if not final_term == "":
                    students[student_name][1] = final_term
                    print("Final upgraded for " + student_name)

                break

            else:
                student_name = input("student record does not exist, please enter another student name:")
                continue


    else:
        print("goodbye")
        repeat = False
