import student
import subject
import exam


def MenuStudent():
    while True:
        print("\t\t\t Student Record Management\n")
        print("==========================================================")
        print("1. Search Student Record")
        print("2. Delete Student Record")
        print("3. Update Update Record")
        print("4. Return to Main Menu")
        print("==========================================================")
        choice = int(input("Enter Choice between 1 to 5 -------> : "))
        if choice == 1:
            student.SearchStudentRec()
        elif choice == 2:
            student.DeleteStudent()
        elif choice == 3:
            student.UpdateStudent()
        elif choice == 4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")


def MenuSubject():
	while True:
		print("\t\t\t Subject Record Management\n")
		print("==========================================================")
		print("1. Search Subject Record")
		print("2. Delete Subject Record")
		print("3. Update Subject Record")
		print("4. Return to Main Menu")
		print("==========================================================")
		choice = int(input("Enter Choice between 1 to 5 ------> : "))
		if choice == 1:
			subject.SearchSubject()
		elif choice == 2:
			subject.DeleteSubject()
		elif choice == 3:
			subject.UpdateSubject()
		elif choice == 4:
			return
		else:
			print("Wrong Choice.....Enter Your Choice again")





def MenuExam():
	while True:
		print("\t\t\t Member Record Management\n")
		print("==========================================================")
		print("1. Delete Exam")
		print("2. View Exam")
		print("3. Return to Main Menu")
		print("==========================================================")
		choice = int(input("Enter Choice between 1 to 4 ------> : "))
		if choice == 1:
			exam.DeleteExam()
		elif choice == 2:
			exam.ViewExam()
		elif choice == 3:
			return
		else:
			print("Wrong Choice.....Enter Your Choice again")