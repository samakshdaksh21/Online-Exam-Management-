import online_exam
import mlib

# online_exam.DatabaseCreate()
# online_exam.connection()
# online_exam.TablesCreate()

while True:
    print("\t\t\t Online Exam Management\n")
    print("=====================================================================")
    print("1. Student Management")
    print("2. Subject Management")
    print("3. Exam Management")
    print("4. Exit")
    choice = int(input("Enter Choice between 1 to 4 -------> : "))
    if choice == 1:
        mlib.MenuStudent()
    elif choice == 2:
        mlib.MenuSubject()
    elif choice == 3:
        mlib.MenuExam()
    elif choice == 4:
        break
    else:
        print("Wrong Choice.....Enter Your Choice again")