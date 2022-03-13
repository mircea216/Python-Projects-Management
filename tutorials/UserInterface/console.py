from Service.elev_service import ElevService
from Service.sedinta_service import SedintaService


class Console:
    def print_menu(self):
        print("1. ADD a student")
        print("2. ADD a tutorial")
        print("3. PRINT students with a number of tutorials greater than a given number")
        print("4. SORT teachers in descending order by number of tutorial")
        print("5. DELETE a student and their tutorials by a given ID")
        print("a. VIEW ALL students")
        print("b. VIEW ALL tutorials")
        print("x. EXIT menu")

    def __init__(self, student_service: ElevService, tutorial_service: SedintaService):
        self.__student_service = student_service
        self.__tutorial_service = tutorial_service

    def run_console(self):
        while True:
            self.print_menu()
            option = input("Select the option: ")
            if option == "1":
                self.UI_create_a_student()
            elif option == "2":
                self.UI_create_a_tutorial()
            elif option == "3":
                self.UI_print_students_with_a_number_of_tutorials_greater_than_a_given_number()
            elif option == "4":
                self.UI_SORT_teachers_in_descending_order_by_number_of_tutorial()
            elif option == "5":
                self.UI_delete_student_and_tutorials()
            elif option == "6":
                self.UI_BUBBLE_SORT_with_python_interface()
            elif option == "7":
                self.UI_get_n_random_tutorials()
            elif option == "a":
                self.UI_view_all_students()
            elif option == "b":
                self.UI_view_all_tutorials()
            elif option == "x":
                break
            else:
                print("Invalid option!")

    def UI_create_a_student(self):
        try:
            id_elev = input("Dati ID-ul elevului: ")
            nume = input("Dati numele elevului: ")
            varsta = int(input("Dati varsta elevului: "))
            self.__student_service.create_a_student(id_elev, nume, varsta)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        except Exception as e:
            print("Eroare", e)

    def UI_create_a_tutorial(self):
        try:
            id_sedinta = input("Dati ID-ul sedintei : ")
            id_elev = input("Dati ID-ul elevului : ")
            profesor = input("Dati profesorul sedintei: ")
            self.__tutorial_service.create_a_tutorial(id_sedinta, id_elev, profesor)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        except Exception as e:
            print("Eroare", e)

    def UI_view_all_students(self):
        list_of_students = self.__student_service.get_all_students()
        for student in list_of_students:
            print(student)

    def UI_view_all_tutorials(self):
        list_of_tutorials = self.__tutorial_service.get_all_tutorials()
        for tutorial in list_of_tutorials:
            print(f"SEDINTA DE PREGATIRE *** {tutorial[0]}  \n"
                  f"*********** NUME ELEV: {tutorial[1]}")

    def UI_print_students_with_a_number_of_tutorials_greater_than_a_given_number(self):
        try:
            given_number = int(input("Dati numarul: "))
            list_of_students = self.__tutorial_service.print_students_with_a_number_of_tutorials_greater_than_a_given_number(
                given_number)
            for student in list_of_students:
                print(student)
        except Exception as e:
            print("Eroare", e)

    def UI_SORT_teachers_in_descending_order_by_number_of_tutorial(self):
        sorted_list_of_teachers = self.__tutorial_service.sort_teachers_in_descending_order_by_number_of_tutorial()
        for teach in sorted_list_of_teachers:
            print(f"PROFESORUL: {teach[0]} --- numar de sedinte: {teach[1]}")

    def UI_delete_student_and_tutorials(self):
        try:
            id_stergere = input("Dati ID-ul ce trebuie sters: ")
            self.__tutorial_service.delete_student_and_tutorials(id_stergere)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)

    def UI_BUBBLE_SORT_with_python_interface(self):
        sorted_list = self.__tutorial_service.BUBBLE_SORT_with_python_interface()
        for item in sorted_list:
            print(f"STUDENT: {item[0]} ---> NUMBER OF TEACHES: {len(item[1])}")

    def UI_get_n_random_tutorials(self):
        try:
            n = int(input("Dati numarul de entitati: "))
            self.__tutorial_service.get_n_random_tutorials(n)
        except Exception as e:
            print("Eroare!", e)
