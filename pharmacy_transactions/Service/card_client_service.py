from Domain.add_operation import AddOperation, DeleteOperation, UpdateOperation
from Domain.card_client import CardClient
from Domain.card_client_validator import CardClientValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.undo_redo_service import UndoRedoService


class CardClientService:
    def __init__(self, client_card_validator: CardClientValidator, client_cards_repository: GenericFileRepository,
                 undo_redo_service: UndoRedoService, transactions_repository: GenericFileRepository):
        '''
        Construieste un dictionar avand drept chei ID-urile cardurilor si drept valori obiecte de tip CardClient
        '''
        self.__client_card_validator = client_card_validator
        self.__client_cards_repository = client_cards_repository
        self.__undo_redo_service = undo_redo_service
        self.__transactions_repository = transactions_repository

    def get_all_client_cards(self):
        '''
        determina o lista de obiecte de tip CardClient
        :return: self.client_cards_repository.get_all_client_cards(), list, output
        '''
        return self.__client_cards_repository.get_all_entities()

    def create_client_card(self, id_client, nume, prenume, CNP, data_nasterii, data_inregistrarii):
        '''
        adauga un card de client in lista
        :param id_client: id_ul clientului
        :param nume: numele clientului
        :param prenume: prenumele clientului
        :param CNP: CNP-ul clientului
        :param data_nasterii: date nasterii clientului
        :param data_inregistrarii: date inregistrarii clientului
        '''
        ok = 1
        list_of_client_cards = self.get_all_client_cards()
        for client_card in list_of_client_cards:
            if CNP in client_card.__str__() and CNP != "" and CNP != " ":
                ok = 0
        if ok == 0:
            raise ValueError("Clientul cu CNP-ul introdus exista deja! Reincercati!")
        card_client = CardClient(id_client, nume, prenume, CNP, data_nasterii, data_inregistrarii)
        self.__client_card_validator.validate(card_client)
        self.__client_cards_repository.create_an_entity(card_client)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__client_cards_repository, card_client))
        self.__undo_redo_service.clear_redo()

    def delete_client_card(self, id_de_stergere):
        '''
        sterge un card de client dupa ID
        :param id_de_stergere: string, input
        '''
        list_of_dependent_id_s = [transaction.id_client for transaction in
                                  self.__transactions_repository.get_all_entities()]
        if id_de_stergere in list_of_dependent_id_s:
            raise KeyError(
                f"Cardul de client cu ID-ul {id_de_stergere} nu poate fi sters deoarece depinde de tranzactie!")
        to_be_deleted = self.__client_cards_repository.get_entity_by_id(id_de_stergere)
        self.__client_cards_repository.delete_an_entity(id_de_stergere)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__client_cards_repository, to_be_deleted))
        self.__undo_redo_service.clear_redo()

    def update_client_card(self, id_client_de_modificare, nume_nou, prenume_nou, CNP_nou, data_nasterii_noua,
                           data_inregistrarii_noua):
        '''
        modifica atributele unui card de client
        :param id_client_de_modificare: id_ul clientului
        :param nume_nou: numele clientului
        :param prenume_nou: prenumele clientului
        :param CNP_nou: CNP-ul clientului
        :param data_nasterii_noua: date nasterii clientului
        :param data_inregistrarii_noua: date inregistrarii clientului
        '''
        ok = 1
        list_of_client_cards = self.get_all_client_cards()
        for client_card in list_of_client_cards:
            if CNP_nou in client_card.__str__() and CNP_nou != "":
                ok = 0
        if ok == 0:
            raise ValueError("Clientul cu CNP-ul nou introdus exista deja! Reincercati!")
        new_client_card = self.__client_cards_repository.get_entity_by_id(id_client_de_modificare)
        if new_client_card == None:
            raise KeyError(f"Cardul de client cu ID-ul {id_client_de_modificare} nu este inregistrat!")
        updated_object = self.__client_cards_repository.get_entity_by_id(id_client_de_modificare)
        if nume_nou != "":
            new_client_card.nume = nume_nou
        if prenume_nou != "":
            new_client_card.prenume = prenume_nou
        if CNP_nou != "":
            new_client_card.CNP = CNP_nou
        if data_nasterii_noua != "":
            new_client_card.data_nasterii = data_nasterii_noua
        if data_inregistrarii_noua != "":
            new_client_card.data_nasterii = data_nasterii_noua
        self.__client_card_validator.validate(new_client_card)
        self.__client_cards_repository.update_an_entity(new_client_card)
        self.__undo_redo_service.add_to_undo(
            UpdateOperation(self.__client_cards_repository, new_client_card, updated_object))
        self.__undo_redo_service.add_to_redo(
            UpdateOperation(self.__client_cards_repository, updated_object, new_client_card))
        self.__undo_redo_service.clear_redo()
