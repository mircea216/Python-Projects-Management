from Service.oras_service import OrasService
from Service.strada_service import StradaService


class Console:
    def __init__(self, town_service: OrasService, strada_service: StradaService):
        self.__oras_service = town_service
        self.__strada_service = strada_service

    def run_menu(self):
        while True:
            print("1. ADD a town")
            print("2. ADD a street")
            print("3. PRINT towns sorted in descending order by street length")
            print("4. PRINT all streets belonging to more than two towns")
            print("5. EXPORT json - print towns with their streets ")
            print("a. SHOW ALL towns")
            print("b. SHOW ALL streets")
            print("x. EXIT menu")
            option = input("Introduce the option: ")
            if option == "1":
                self.UI_create_a_town()
            elif option == "2":
                self.UI_create_a_street()
            elif option == "3":
                self.UI_sort_towns_in_descending_order_by_street_length()
            elif option == "4":
                self.UI_print_streets_belonging_to_more_than_2_towns()
            elif option == "5":
                self.UI_export_json_file()
            elif option == "a":
                self.UI_show_all_towns()
            elif option == "b":
                self.UI_show_all_streets()
            elif option == "x":
                break
            else:
                print("Invalid option!")

    def UI_create_a_town(self):
        try:
            id_oras = input("Dati ID-ul orasului: ")
            nume = input("Dati numele orasului: ")
            populatie = int(input("Dati populatia orasului: "))
            self.__oras_service.create_a_town(id_oras, nume, populatie)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        except Exception as e:
            print("Eroare", e)

    def UI_show_all_towns(self):
        towns_list = self.__oras_service.get_all_towns()
        for town in towns_list:
            print(town)

    def UI_create_a_street(self):
        try:
            id_strada = input("Dati ID-ul strazii: ")
            id_oras = input("Dati ID-ul orasului: ")
            nume = input("Dati nuemele strazii: ")
            lungime = int(input("Dati lungimea strazii: "))
            self.__strada_service.create_a_street(id_strada, id_oras, nume, lungime)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        # except Exception as e:
        #    print("Eroare", e)

    def UI_show_all_streets(self):
        streets_list = self.__strada_service.get_all_streets()
        for street in streets_list:
            print(street)

    def UI_sort_towns_in_descending_order_by_street_length(self):
        self.__strada_service.sort_towns_in_descending_order_by_street_length()

    def UI_print_streets_belonging_to_more_than_2_towns(self):
        self.__strada_service.print_streets_belonging_to_more_than_2_towns()

    def UI_export_json_file(self):
        file_name = input("Dati numele fisierului pentru printare: ")
        self.__strada_service.export_json_file(file_name)
