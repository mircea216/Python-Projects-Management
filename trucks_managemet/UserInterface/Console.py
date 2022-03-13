from Service.activitate_arare_service import ActivitateArareService
from Service.tractor_service import TractorService


class Console:
    def print_menu(self):
        print("1. ADD a truck")
        print("2. ADD an agricultural activity")
        print("3. PRINT the activities of an unrented truck")
        print("4. PRINT trucks sorted in ascending order by the time spent on activities")
        # print("5. PRINT the total number of stars for each type of product")
        print("6. GET a number of random trucks")
        print("a. SHOW ALL trucks")
        print("b. SHOW ALL agricultural activities")
        print("x. EXIT menu")

    def __init__(self, truck_service: TractorService, agricultural_activity: ActivitateArareService):
        self.__truck_service = truck_service
        self.__agricultural_activity = agricultural_activity

    def run_console(self):
        while True:
            self.print_menu()
            option = input("Select the option: ")
            if option == "1":
                self.UI_create_a_truck()
            elif option == "2":
                self.UI_create_an_agricultural_activity()
            elif option == "3":
                self.UI_print_the_activities_of_an_unrented_truck()
            elif option == "4":
                self.UI_sort_trucks_by_time_spent_on_activities()
            elif option == "5":
                self.UI_export_trucks_working_for_extra_time()
            elif option == "6":
                self.UI_get_random_trucks()
            elif option == "7":
                self.UI_delete_a_truck()
            elif option == "a":
                self.UI_get_all_trucks()
            elif option == "b":
                self.UI_get_all_agricultural_activities()
            elif option == "x":
                break
            else:
                print("Invalid option")

    def UI_create_a_truck(self):
        try:
            id_tractor = input("Dati ID-ul tractorului: ")
            model = input("Dati modelul  tractorului: ")
            inchiriere = input("Dati inchirierea tractorului: ")
            self.__truck_service.create_a_truck(id_tractor, model, inchiriere)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        except Exception as e:
            print("Eroare", e)

    def UI_create_an_agricultural_activity(self):
        try:
            id_activitate_arara = input("Dati ID-ul activitatii de arare: ")
            id_tractor = input("Dati ID-ul tractorului: ")
            timp = int(input("Dati timpul activitatii de arare: "))
            zi = int(input("Dati ziua activitatii de arare: "))
            finalizare = input("Dati finalizarea activitatii de arare: ")
            self.__agricultural_activity.create_an_agricultural_activity(id_activitate_arara, id_tractor, timp, zi,
                                                                         finalizare)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        except Exception as e:
            print("Eroare", e)

    def UI_get_all_trucks(self):
        list_of_trucks = self.__truck_service.get_all_trucks()
        for truck in list_of_trucks:
            print(truck)

    def UI_get_all_agricultural_activities(self):
        list_of_agricultural_activities = self.__agricultural_activity.get_all_agricultural_activities()
        for activity in list_of_agricultural_activities:
            print(activity)

    def UI_print_the_activities_of_an_unrented_truck(self):
        self.__agricultural_activity.print_the_activities_of_an_unrented_truck()

    def UI_sort_trucks_by_time_spent_on_activities(self):
        self.__agricultural_activity.sort_trucks_by_time_spent_on_activities()

    def UI_export_trucks_working_for_extra_time(self):
        file_name = input("Dati numele fisierului json: ")
        self.__agricultural_activity.export_trucks_working_for_extra_time(file_name)

    def UI_get_random_trucks(self):
        given_number_of_trucks = int(input("Dati un numar natural de entitati generate aleatoriu: "))
        self.__truck_service.get_random_trucks(given_number_of_trucks)

    def UI_delete_a_truck(self):
        try:
            id_stergere = input("Dati ID-ul de stergere: ")
            self.__truck_service.delete_a_truck(id_stergere)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        except Exception as e:
            print("Eroare", e)
