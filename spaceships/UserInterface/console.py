from Service.atac_service import AtacService
from Service.nava_service import NavaService


class Console:
    def print_menu(self):
        print("1. ADD a spaceship")
        print("2. ADD an attack ")
        print("3. ")
        print("4. SORT_the_spaceship_in_descending_order_by_sum_of_damages")
        print("5. ")
        print("a. VIEW ALL spaceship")
        print("b. VIEW ALL attacks")
        print("x. EXIT menu")

    def __init__(self, spaceship_service: NavaService, attack_service: AtacService):
        self.__spaceship_service = spaceship_service
        self.__attack_service = attack_service

    def run_console(self):
        while True:
            self.print_menu()
            option = input("Select the option: ")
            if option == "1":
                self.UI_create_a_spaceship()
            elif option == "2":
                self.UI_create_an_attack()
            elif option == "3":
                self.UI_get_the_result_of_the_attack()
            elif option == "4":
                self.UI_sort_the_spaceship_in_descending_order_by_sum_of_damages()
            elif option == "5":
                self.UI_print_battles()
            elif option == "a":
                self.UI_view_all_spaceship()
            elif option == "b":
                self.UI_view_all_attacks()
            elif option == "x":
                break
            else:
                print("Invalid option!")

    def UI_create_a_spaceship(self):
        try:
            id_nava = input("Dati ID-ul navei: ")
            tip = input("Dati tipul navei: ")
            max_hit_points = int(input("Dati max_hit_points ale navei: "))
            self.__spaceship_service.create_a_spaceship(id_nava, tip, max_hit_points)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        except Exception as e:
            print("Eroare", e)

    def UI_create_an_attack(self):
        try:
            id_atac = input("Dati ID-ul atacului: ")
            id_nava_atacator = input("Dati ID-ul navei atacator: ")
            id_nava_atacata = input("Dati ID-ul navei atacate: ")
            pagube = int(input("Dati pagubele produse de atac: "))
            self.__attack_service.create_an_attack(id_atac, id_nava_atacator, id_nava_atacata, pagube)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid", ke)
        except Exception as e:
            print("Eroare", e)

    def UI_view_all_spaceship(self):
        list_of_spaceship = self.__spaceship_service.get_all_spaceship()
        for spaceship in list_of_spaceship:
            print(spaceship)

    def UI_view_all_attacks(self):
        list_of_attacks = self.__attack_service.get_all_attacks()
        for attack in list_of_attacks:
            print(f"ATACUL: **** {attack[0]} **** \n"
                  f"cu NAVA ATACATOR: **** {attack[1]} **** \n"
                  f"si cu NAVA ATACATA: **** {attack[2]} ****")

    def UI_get_the_result_of_the_attack(self):
        try:
            id_atac = input("Dati ID-ul atacului: ")
            attack_result = self.__attack_service.get_the_result_of_the_attack(id_atac)
            print(attack_result)
        except Exception as e:
            print(e)

    def UI_sort_the_spaceship_in_descending_order_by_sum_of_damages(self):
        sorted_list = self.__attack_service.sort_the_spaceship_in_descending_order_by_sum_of_damages()
        for spaceship in sorted_list:
            print(f"{spaceship[0]} -----> DAMAGES: {spaceship[1]}")

    def UI_print_battles(self):
        self.__attack_service.print_battles()
