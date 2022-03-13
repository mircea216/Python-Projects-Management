from copy import deepcopy

from Domain.add_operation import AddOperation, DeleteOperation, UpdateOperation
from Domain.card_client import CardClient
from Domain.medicament import Medicament
from Domain.tranzactie import Tranzactie
from Domain.tranzactie_validator import TranzactieValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.undo_redo_service import UndoRedoService
from ViewModels.view_models import ViewModel


class TranzactieService:
    def __init__(self, transaction_validator: TranzactieValidator, med_repository: GenericFileRepository,
                 client_card_repository: GenericFileRepository, transaction_repository: GenericFileRepository,
                 undo_redo_service: UndoRedoService):
        '''
        construieste un obiect de tip TranzactieService
        :param transaction_validator: validator-ul
        :param transaction_repository: repository-ul
        '''
        self.__transaction_validator = transaction_validator
        self.__med_repository = med_repository
        self.__client_card_repository = client_card_repository
        self.__transaction_repository = transaction_repository
        self.__undo_redo_service = undo_redo_service

    def get_all_transactions(self):
        '''
        returneaza o lista cu toate tranzactiile
        :return: self.__transaction_repository.get_all_transactions()
        '''
        view_models = []
        for transaction in self.__transaction_repository.get_all_entities():
            medicament = self.__med_repository.get_entity_by_id(transaction.id_medicament)
            card_client = self.__client_card_repository.get_entity_by_id(transaction.id_client)
            transaction = ViewModel(transaction.id_entitate, medicament, card_client, transaction.numar_bucati,
                                    transaction.data, transaction.ora)
            view_models.append(transaction)

        return deepcopy(view_models)

    def create_transaction(self, id_tranzactie, id_medicament, id_client, numar_bucati, data, ora):
        '''
        Adauga o tranzactie in storage
        :param id_tranzactie: ID-ul tranzactiei
        :param id_medicament: ID-ul medicamentului
        :param id_card_client: ID-ul cardului de client
        :param numar_bucati: numarul de bucati
        :param data: data tranzactiei
        :param ora: ora tranzactiei
        '''
        errors = []
        if self.__med_repository.get_entity_by_id(id_medicament) is None:
            errors.append(
                f"Tranzactia nu se poate crea. Nu este inregistrat niciun medicament cu ID-ul {id_medicament}")
        if self.__client_card_repository.get_entity_by_id(id_client) is None and id_client != "0":
            errors.append(f"Tranzactia nu se poate crea. Nu este inregistrat niciun card cu ID-ul {id_client}")
        if len(errors) > 0:
            raise KeyError(errors)
        transaction = Tranzactie(id_tranzactie, id_medicament, id_client, numar_bucati, data, ora)
        self.__transaction_validator.validate(transaction)
        self.__transaction_repository.create_an_entity(transaction)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__transaction_repository, transaction))
        self.__undo_redo_service.clear_redo()
        med = self.__med_repository.get_entity_by_id(id_medicament)
        if id_client != "0":
            if med.reteta == "da":
                med.pret = int(med.pret - 15 / 100 * med.pret)
                print(f"Pretul platit pentru medicament este {med.pret}, iar reducerea acordata este de 15%")
                self.__med_repository.update_an_entity(med)
            else:
                med.pret = int(med.pret - 10 / 100 * med.pret)
                print(f"Pretul platit pentru medicament este {med.pret}, iar reducerea acordata este de 10%")
                self.__med_repository.update_an_entity(med)

    def delete_transaction(self, id_stergere):
        '''
        sterge o tranzactie din storage daca ID-ul acesteia exista in storage
        :param id_stergere: input, int
        '''
        to_be_deleted = self.__transaction_repository.get_entity_by_id(id_stergere)
        self.__transaction_repository.delete_an_entity(id_stergere)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__transaction_repository, to_be_deleted))
        self.__undo_redo_service.clear_redo()

    def update_transaction(self, id_de_modificare, id_medicament_nou, id_client_nou, numar_bucati_nou, data_noua,
                           ora_noua):
        '''
        modifica atributele unei tranzactii din storage prin inlocuire
        :param new_transaction: input, obiect de tip Tranzactie
        '''
        errors = []
        if self.__med_repository.get_entity_by_id(id_medicament_nou) is None:
            errors.append(
                f"Tranzactia nu se poate crea. Nu este inregistrat niciun medicament cu ID-ul {id_medicament_nou}")
        if self.__client_card_repository.get_entity_by_id(id_client_nou) is None and id_client_nou != "0":
            errors.append(f"Tranzactia nu se poate crea. Nu este inregistrat niciun card cu ID-ul {id_client_nou}")
        if len(errors) > 0:
            raise KeyError(errors)
        new_transaction = self.__transaction_repository.get_entity_by_id(id_de_modificare)
        if new_transaction == None:
            raise KeyError(f"Tranzactia cu ID-ul {id_de_modificare} nu exista!")
        updated_object = self.__transaction_repository.get_entity_by_id(id_de_modificare)
        if numar_bucati_nou != 0:
            new_transaction.numar_bucati = numar_bucati_nou
        if data_noua != "":
            new_transaction.data = data_noua
        if ora_noua != "":
            new_transaction.ora = ora_noua
        self.__transaction_validator.validate(new_transaction)
        self.__transaction_repository.update_an_entity(new_transaction)
        self.__undo_redo_service.add_to_undo(
            UpdateOperation(self.__transaction_repository, new_transaction, updated_object))
        self.__undo_redo_service.add_to_redo(
            UpdateOperation(self.__transaction_repository, updated_object, new_transaction))
        self.__undo_redo_service.clear_redo()

    def suitable_dates_for_printing(self, first_date, second_date, transaction: Tranzactie):
        '''
        determina daca o tranzactie se afla in intervalul de zile dat ca parametru
        :param first_date: prima data din interval
        :param second_date: a doua data din interval
        :param transaction: obiect de tip Tranzactie
        :return: obiectul de tip Tranzactie daca el respecta datele din interval sau None in caz contrar
        '''
        errors = []
        value = True
        for character in str(first_date):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                value = False
        if value == False:
            errors.append("Atentie la introducerea datei!")
        value = True
        for character in str(second_date):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                value = False
        if value == False:
            errors.append("Atentie la introducerea datei!")
        if len(errors):
            raise ValueError(errors)

        if transaction.data > first_date and transaction.data < second_date:
            return transaction

    # MAP FUNCTION + LAMBDA FUNCTION
    def print_transactions_from_a_given_range(self, first_date, second_date):
        '''

        :param first_date: prima data din interval
        :param second_date: a doua data din interval
        :return: o lista ce filtreaza tranzactiile care nu respecta proprietatea ceruta
        '''
        errors = []
        value = True
        for character in str(first_date):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                value = False
        if value == False:
            errors.append("Atentie la introducerea datei!")
        for character in str(second_date):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                value = False
        if value == False:
            errors.append("Atentie la introducerea datei!")
        if len(errors):
            raise ValueError(errors)

        list_of_transactions = self.get_all_transactions()
        mapped_list_of_transactions = map(
            lambda transaction: self.suitable_dates_for_printing(first_date, second_date, transaction),
            list_of_transactions)
        return list(mapped_list_of_transactions)

    # FILTER FUNCTION + LAMBDA FUNCTION

    def delete_transactions_from_a_given_range(self, first_date, second_date):
        '''
        sterge toate tranzactiile dintr-un interval dat
        :param first_date: prima data din interval
        :param second_date: a doua data din interval
        :return: o lista din care se sterg tranzactiile din intervalul date
        '''
        errors = []
        value = True
        for character in str(first_date):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                value = False
        if value == False:
            errors.append("Atentie la introducerea datei!")
        for character in str(second_date):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                value = False
        if value == False:
            errors.append("Atentie la introducerea datei!")
        if len(errors):
            raise ValueError(errors)

        list_of_transactions = self.get_all_transactions()
        filtered_list_of_transactions = filter(lambda
                                                   transaction: transaction.data < first_date or transaction.data > second_date,
                                               list_of_transactions)
        return list(filtered_list_of_transactions)

    def get_sale_number(self, medicament: Medicament):
        '''
        determina cheia de sortare - numarul de vanzari
        :param medicament: obiect de tip Medicament
        :return: sale_number, int, output
        '''
        sale_number = 0
        result_list = self.__transaction_repository.get_all_entities()
        for transaction in result_list:
            if medicament.id_entitate == transaction.id_medicament:
                sale_number += transaction.numar_bucati
        return sale_number

    # LAMBDA FUNCTION

    def descending_sort_of_meds_by_sale_number(self):
        '''
        returneaza medicamentele sortate descrescator dupa numar de vanzari
        :return: o lista a medicamentelor sortate descrescator dupa numarul de vanzari
        '''
        return self.QuickSort(self.__med_repository.get_all_entities(), key=lambda med: self.get_sale_number(med),
                      reverse=True)

    def get_discount_rate(self, card_client: CardClient):
        '''
        determina cheia de sortare - numarul de vanzari
        :param medicament: obiect de tip Medicament
        :return: sale_number, int, output
        '''
        discount_rate = 0
        result_list = self.__transaction_repository.get_all_entities()
        for transaction in result_list:
            if transaction.id_client == card_client.id_entitate:
                if transaction.id_client != "0":
                    med = self.__med_repository.get_entity_by_id(transaction.id_medicament)
                    if med.reteta == "da":
                        discount_rate = 15
                    else:
                        discount_rate = 10
                else:
                    discount_rate = 0
        return discount_rate

    # LAMBDA FUNCTION

    def descending_sort_of_client_cards_by_discount_rate(self):
        '''
        afiseaza cardurile de client sortate descrescator dupa reducerea facuta
        :return:
        '''
        sorted_list_of_client_cards = sorted(self.__client_card_repository.get_all_entities(),
                                             key=lambda client: self.get_discount_rate(client),
                                             reverse=True)
        return sorted_list_of_client_cards

    def refactorised_recursive_full_text_serach_in_meds_and_client_cards(self, list_of_meds_and_client_cards,
                                                                         given_string):
        '''
        realizeaza o cautare FULL TEXT in cadrul medicamentelor si cardurilor de clienti
        :param list_of_meds_and_client_cards: lista continand medicamentele si cardurile de clienti
        :param given_string: string-ul de cautare FULL TEXT
        :return: o lista cu toate obiectele care contin in scrierea lor given_string
        '''
        if len(list_of_meds_and_client_cards) > 0:
            if given_string in list_of_meds_and_client_cards[0]:
                return [list_of_meds_and_client_cards[
                            0]] + self.refactorised_recursive_full_text_serach_in_meds_and_client_cards(
                    list_of_meds_and_client_cards[1:],
                    given_string)
            else:
                return self.refactorised_recursive_full_text_serach_in_meds_and_client_cards(
                    list_of_meds_and_client_cards[1:], given_string)
        return []

    def bubble_sort(self, given_list, key_function=lambda x: x, reverse=False):
        '''
        BUBBLE SORT
        :param given_list: lista data, input, list
        :param key_function: functie ce se va defini ulterior
        :return: lista sortata crescator
        '''
        for i in range(len(given_list) - 1):
            swapped = False
            for j in range(len(given_list) - i - 1):
                if key_function(given_list[j]) > key_function(given_list[j + 1]):
                    # swapping values
                    given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
                    swapped = True
            if swapped is False:
                break
        if reverse == False:
            return given_list
        else:
            return given_list[::-1]

    def implement_a_sort_function_having_the_same_interface_as_Pyhton_SORTED_function(self):
        '''
        ordoneaza crescator medicamentele in functie de numar de vanzari
        :return: o lista a medicamentelor sortate crescator
        '''
        list_of_meds = [med for med in self.__med_repository.get_all_entities()]
        return self.bubble_sort(list_of_meds, key_function=lambda med: self.get_sale_number(med), reverse=True)

    def partition(self, array, key, start, end):
        pivot = array[start]
        low = start + 1
        high = end

        while True:
            while low <= high and key(array[high]) < key(pivot):
                high = high - 1

            while low <= high and not key(array[low]) < key(pivot):
                low = low + 1

            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break

        array[start], array[high] = array[high], array[start]

        return high

    def quick_sort(self, array, key, start, end):
        if start >= end:
            return

        p = self.partition(array, key, start, end)
        self.quick_sort(array, key, start, p - 1)
        self.quick_sort(array, key, p + 1, end)


    def QuickSort(self, array, key=lambda x: x, reverse=False):
        self.quick_sort(array, key, 0 , len(array)-1)
        if reverse is True:
            return array
        else:
            return array[::-1]
