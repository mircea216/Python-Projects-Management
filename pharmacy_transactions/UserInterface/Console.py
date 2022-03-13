from datetime import date

from Repo.repo import NewRepoEx
from Service.card_client_service import CardClientService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService


class Console:
    def __init__(self, med_service: MedicamentService, client_card_service: CardClientService,
                 transaction_service: TranzactieService, undo_redo_service: UndoRedoService, excel_storage: NewRepoEx):
        self.__med_service = med_service
        self.__client_card_service = client_card_service
        self.__transaction_service = transaction_service
        self.__undo_redo_service = undo_redo_service
        self.__excel_storage = excel_storage

    def run_console(self):
        while True:
            print("1.CRUD meds")
            print("2.CRUD client cards")
            print("3.CRUD transactions")
            print("4.REFACTORISED RECURSIVE FULL TEXT SEARCH in meds and client cards")
            print("5.PRINT the transactions from a given range of days --- MAP FUNCTION")
            print("6.IMPLEMENT a QuickSort function having the same interface as Pyhton SORTED function")
            print("7.PRINT client cards sorted in descending order by discount rate --- LAMBDA FUNCTION")
            print("8.DELETE transactions from a given range of days --- FILTER FUNCTION")
            print("9.RAISE the price of the meds cheaper than a given price")
            print("10.EXPORT all meds in an excel file")
            print("11.IMPLEMENT a sort function having the same interface as Pyhton SORTED function")
            print("a.SHOW ALL meds")
            print("b.SHOW ALL client cards")
            print("c.SHOW ALL transactions")
            print("u.UNDO")
            print("r.REDO")
            print("x.EXIT menu")
            option = input("Introduce the option: ")
            if option == "1":
                self.handle_CRUD_meds()
            elif option == "2":
                self.handle_CRUD_client_card()
            elif option == "3":
                self.handle_CRUD_transactions()
            elif option == "4":
                self.UI_refactorised_recursive_full_text_serach_in_meds_and_client_cards()
            elif option == "5":
                self.UI_print_transactions_from_a_given_range()
            elif option == "6":
                self.UI_descending_sort_of_meds_by_sale_number()
            elif option == "7":
                self.UI_descending_sort_of_client_cards_by_discount_rate()
            elif option == "8":
                self.UI_delete_transactions_from_a_given_range()
            elif option == "9":
                self.UI_raise_the_price_of_meds()
            elif option == "10":
                self.__excel_storage.write_file()
            elif option == "11":
                self.UI_implement_a_sort_function_having_the_same_interface_as_Pyhton_SORTED_function()
            elif option == "a":
                self.UI_show_all_meds()
            elif option == "b":
                self.UI_show_all_client_cards()
            elif option == "c":
                self.UI_show_all_transactions()
            elif option == "u":
                self.__undo_redo_service.do_undo()
            elif option == "r":
                self.__undo_redo_service.do_redo()
            elif option == 'x':
                break
            else:
                print("Retry! Invalid option!")

    def handle_CRUD_meds(self):
        while True:
            print("1.ADD a med")
            print("2.DELETE a med")
            print("3.UPDATE a med")
            print("4.ADD random meds")
            print("a.SHOW ALL meds")
            print("x.BACK to menu")
            option = input("Select the option: ")
            if option == '1':
                self.UI_create_med()
            elif option == '2':
                self.UI_delete_med()
            elif option == '3':
                self.UI_update_med()
            elif option == '4':
                self.UI_get_random_meds()
            elif option == 'a':
                self.UI_show_all_meds()
            elif option == 'x':
                break
            else:
                print("Invalid option!")

    def UI_create_med(self):
        try:
            id_medicament = input("Dati ID-ul medicamentului: ")
            nume = input("Dati numele medicamentului: ")
            producator = input("Dati producatorul medicamentului: ")
            pret = int(input("Dati pretul medicamentului: "))
            reteta = input("Necesita medicamentul reteta? [da/nu]: ")
            self.__med_service.create_med(id_medicament, nume, producator, pret, reteta)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)
        except Exception as e:
            print("Eroare!", e)

    def UI_delete_med(self):
        try:
            id_stergere = input("Dati ID ul medicamentului pe care doriti sa il stergeti: ")
            self.__med_service.delete_med(id_stergere)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)
        except Exception as e:
            print("Eroare!", e)

    def UI_update_med(self):
        try:
            id_modificare = input("Dati ID-ul medicamentului pe care doriti sa il modificati: ")
            nume_nou = input("Dati numele medicamentului sau ENTER daca nu doriti sa il modificati: ")
            producator_nou = input("Dati producatorul medicamentului sau ENTER daca nu doriti sa il modificati: ")
            pret_nou = int(input("Dati pretul medicamentului sau 0 daca nu doriti sa il modificati: "))
            reteta_noua = input("Necesita medicamentul reteta [da/nu] sau ENTER daca nu doriti schimbare: ")
            self.__med_service.update_med(id_modificare, nume_nou, producator_nou, pret_nou, reteta_noua)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)
        except Exception as e:
            print("Eroare!", e)

    def UI_get_random_meds(self):
        n = int(input("Dati numarul entitati: "))
        self.__med_service.get_random_meds(n)

    def UI_show_all_meds(self):
        meds_storage = self.__med_service.get_all_meds()
        for med in meds_storage:
            print(med)

    def handle_CRUD_client_card(self):
        while True:
            print("1.ADD a client card")
            print("2.DELETE a client card")
            print("3.UPDATE a client card")
            print("a.SHOW ALL client cards")
            print("x.BACK to menu")
            option = input("Select the option: ")
            if option == "1":
                self.UI_create_client_card()
            elif option == "2":
                self.UI_delete_client_card()
            elif option == "3":
                self.UI_update_client_card()
            elif option == "a":
                self.UI_show_all_client_cards()
            elif option == "x":
                break
            else:
                print("Invalid option! ")

    def UI_create_client_card(self):
        try:
            id_card_client = input("Dati ID-ul cardului de client: ")
            nume = input("Dati numele clientului: ")
            prenume = input("Dati prenumele clientului: ")
            CNP = input("Dati CNP-ul clientului - cod unic - 13 cifre: ")
            data_nasterii_string = input("Dati data nasterii de forma ['yyyy-mm-dd']: ")
            data_inregistrarii_string = input("Dati data inregistrarii de forma ['yyyy-mm-dd']: ")
            data_nasterii = date(int(data_nasterii_string[:data_nasterii_string.find("-")]),
                                 int(data_nasterii_string[data_nasterii_string.find("-") + 1:data_nasterii_string.rfind(
                                     "-")]), int(data_nasterii_string[data_nasterii_string.rfind("-") + 1:]))
            data_inregistrarii = date(int(data_inregistrarii_string[:data_inregistrarii_string.find("-")]),
                                      int(data_inregistrarii_string[
                                          data_inregistrarii_string.find("-") + 1:data_inregistrarii_string.rfind(
                                              "-")]),
                                      int(data_inregistrarii_string[data_inregistrarii_string.rfind("-") + 1:]))
            self.__client_card_service.create_client_card(id_card_client, nume, prenume, CNP, data_nasterii,
                                                          data_inregistrarii)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)
        except Exception as e:
            print("Eroare!", e)

    def UI_delete_client_card(self):
        try:
            id_de_stergere = input("Dati ID-ul cardului de client care trebuie sters: ")
            self.__client_card_service.delete_client_card(id_de_stergere)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)
        except Exception as e:
            print("Eroare!", e)

    def UI_update_client_card(self):
        try:
            id_card_client_de_modificare = input("Dati ID-ul cardului de client care trebuie modificat: ")
            nume_nou = input("Dati numele clientului sau ENTER daca nu doriti sa il modificati: ")
            prenume_nou = input("Dati prenumele clientului sau ENTER daca nu doriti sa il modificati: ")
            CNP_nou = input("Dati CNP-ul clientului - cod unic - 13 cifre sau ENTER daca nu doriti sa il modificati: ")
            data_nasterii_string = input("Dati data nasterii de forma ['yyyy-mm-dd']: ")
            data_inregistrarii_string = input("Dati data inregistrarii de forma ['yyyy-mm-dd']: ")
            data_nasterii = date(int(data_nasterii_string[:data_nasterii_string.find("-")]),
                                 int(data_nasterii_string[data_nasterii_string.find("-") + 1:data_nasterii_string.rfind(
                                     "-")]), int(data_nasterii_string[data_nasterii_string.rfind("-") + 1:]))
            data_inregistrarii = date(int(data_inregistrarii_string[:data_inregistrarii_string.find("-")]),
                                      int(data_inregistrarii_string[
                                          data_inregistrarii_string.find("-") + 1:data_inregistrarii_string.rfind(
                                              "-")]),
                                      int(data_inregistrarii_string[data_inregistrarii_string.rfind("-") + 1:]))
            self.__client_card_service.update_client_card(id_card_client_de_modificare, nume_nou, prenume_nou, CNP_nou,
                                                          data_nasterii, data_inregistrarii)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)

    def UI_show_all_client_cards(self):
        client_cards_storage = self.__client_card_service.get_all_client_cards()
        for client_card in client_cards_storage:
            print(client_card)

    def handle_CRUD_transactions(self):
        while True:
            print("1.ADD a transaction")
            print("2.DELETE a transaction")
            print("3.UPDATE a transaction")
            print("a.SHOW ALL transactions")
            print("x.BACK to menu")
            option = input("Select the option: ")
            if option == "1":
                self.UI_create_transaction()
            elif option == "2":
                self.UI_delete_transaction()
            elif option == "3":
                self.UI_update_transaction()
            elif option == 'a':
                self.UI_show_all_transactions()
            elif option == "u":
                self.__undo_redo_service.do_undo()
            elif option == "r":
                self.__undo_redo_service.do_redo()
            elif option == 'x':
                break
            else:
                print("Invalid option!")

    def UI_create_transaction(self):
        try:
            id_tranzactie = input("Dati ID-ul tranzactiei: ")
            id_medicament = input("Dati ID-ul medicamentului: ")
            id_client = input("Dati ID-ul cardului de client: ")
            numar_bucati = int(input("Dati numarul de bucati: "))
            day, month, year = [int(x) for x in input("Dati data tranzactiei cu formatul DD/MM/YYYY: ").split('/')]
            data = date(year, month, day)
            ora = input("Dati ora tranzactiei cu formatul HH:MM: ")
            self.__transaction_service.create_transaction(id_tranzactie, id_medicament, id_client, numar_bucati, data,
                                                          ora)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)
        except Exception as e:
            print("Eroare!", e)

    def UI_delete_transaction(self):
        try:
            id_stergere = input("Dati ID ul tranzactiei pe care doriti sa o stergeti: ")
            self.__transaction_service.delete_transaction(id_stergere)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)
        except Exception as e:
            print("Eroare!", e)

    def UI_update_transaction(self):
        try:
            id_modificare = input("Dati ID-ul tranzactiei pe care doriti sa o modificati: ")
            id_medicament_nou = input("Dati ID-ul medicamentului sau 0 daca nu doriti sa il modificati: ")
            id_client_nou = input("Dati ID-ul cardului de client sau 0 daca nu doriti sa il modificati: ")
            numar_bucati_nou = int(input("Dati numarul de bucati nou sau 0 daca nu doriti sa il modificati: "))
            day, month, year = [int(x) for x in input("Dati data tranzactiei cu formatul DD/MM/YYYY: ").split('/')]
            data_noua = date(year, month, day)
            ora_noua = input("Dati ora noua sau ENTER daca nu doriti sa o modificati: ")

            self.__transaction_service.update_transaction(id_modificare, id_medicament_nou, id_client_nou,
                                                          numar_bucati_nou, data_noua, ora_noua)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except KeyError as ke:
            print("Introduceti un ID valid!", ke)
        except Exception as e:
            print("Eroare!", e)

    def UI_show_all_transactions(self):
        transactions_storage = self.__transaction_service.get_all_transactions()
        for transaction in transactions_storage:
            print(transaction)

    def UI_print_transactions_from_a_given_range(self):
        try:
            day1, month1, year1 = [int(x) for x in input("Dati prima data de format DD/MM/YYYY: ").split('/')]
            day2, month2, year2 = [int(x) for x in input("Dati a doua data de format DD/MM/YYYY: ").split('/')]
            first_date = date(year1, month1, day1)
            second_date = date(year2, month2, day2)
            mapped_list_of_transactions = self.__transaction_service.print_transactions_from_a_given_range(first_date,
                                                                                                           second_date)
            for transaction in mapped_list_of_transactions:
                if transaction != None:
                    print(transaction)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except Exception as e:
            print("Eroare!", e)

    def UI_delete_transactions_from_a_given_range(self):
        try:
            day1, month1, year1 = [int(x) for x in input("Dati prima data de format DD/MM/YYYY: ").split('/')]
            first_date = date(year1, month1, day1)
            day2, month2, year2 = [int(x) for x in input("Dati a doua data de format DD/MM/YYYY: ").split('/')]
            second_date = date(year2, month2, day2)
            filtered_list_of_transactions = self.__transaction_service.delete_transactions_from_a_given_range(
                first_date, second_date)
            for transaction in filtered_list_of_transactions:
                print(transaction)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except Exception as e:
            print("Eroare!", e)

    def UI_descending_sort_of_meds_by_sale_number(self):
        list_of_meds = self.__transaction_service.descending_sort_of_meds_by_sale_number()
        for med in list_of_meds:
            print(med, '----->SALE NUMBER', self.__transaction_service.get_sale_number(med))

    def UI_descending_sort_of_client_cards_by_discount_rate(self):
        sorted_list_of_client_cards = self.__transaction_service.descending_sort_of_client_cards_by_discount_rate()
        for client_card in sorted_list_of_client_cards:
            print(client_card, '----->DISCOUNT:', str(self.__transaction_service.get_discount_rate(client_card)) + '%')

    def UI_raise_the_price_of_meds(self):
        try:
            valoare_comparare = int(input("Dati valoare cu care se compara pretul: "))
            procent_scumpire = input("Dati procentul de ieftinire de forma 'a%': ")
            self.__med_service.scumpire_cu_procent_dat(valoare_comparare, procent_scumpire)
        except ValueError as ve:
            print("Introduceti date valide!", ve)
        except Exception as e:
            print("Eroare!", e)

    def UI_refactorised_recursive_full_text_serach_in_meds_and_client_cards(self):
        list_of_meds_and_client_cards = [med.__str__() for med in self.__med_service.get_all_meds()] + [
            client_card.__str__() for client_card in self.__client_card_service.get_all_client_cards()]
        given_string = input("Dati textul de cautare: ")
        result_list = self.__transaction_service.refactorised_recursive_full_text_serach_in_meds_and_client_cards(
            list_of_meds_and_client_cards, given_string)
        if not (len(result_list)):
            print("NO RESULT!")
        else:
            for item in result_list:
                print(item)

    def UI_implement_a_sort_function_having_the_same_interface_as_Pyhton_SORTED_function(self):
        sorted_list_of_meds = self.__transaction_service.implement_a_sort_function_having_the_same_interface_as_Pyhton_SORTED_function()
        for med in sorted_list_of_meds:
            print(med, "-----> SALE NUMBER:", self.__transaction_service.get_sale_number(med))

