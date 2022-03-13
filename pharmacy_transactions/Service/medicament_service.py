import random
import string
from copy import copy

from Domain.add_operation import AddOperation, DeleteOperation, UpdateOperation, RaisePrice
from Domain.medicament import Medicament
from Domain.medicament_validator import MedicamentValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.undo_redo_service import UndoRedoService


class MedicamentService:
    def __init__(self, med_validator: MedicamentValidator, meds_repository: GenericFileRepository,
                 undo_redo_service: UndoRedoService, transactions_repository: GenericFileRepository):
        '''
        construieste un dictionar ce stocheaza medicamentele avand drept chei ID-urile si drept valori obiecte
        '''
        self.__meds_repository = meds_repository
        self.__med_validator = med_validator
        self.__undo_redo_service = undo_redo_service
        self.__transactions_repository = transactions_repository

    def get_all_meds(self):
        '''
        determina o lista de obiecte de tip Medicament
        :return: list, output
        '''
        return self.__meds_repository.get_all_entities()

    def create_med(self, id_medicament, nume, producator, pret, reteta):
        '''
        adauga un medicament in storage daca ID-ul acestuia nu exista deja
        :param id_medicament: ID_ul medicamentului
        :param nume: numele medicamentului
        :param producator: producaatorul medicamentului
        :param pret: pretul medicamentului
        :param reteta: necesitatea retetei
        '''
        medicament = Medicament(id_medicament, nume, producator, pret, reteta)
        self.__med_validator.validate(medicament)
        self.__meds_repository.create_an_entity(medicament)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__meds_repository, medicament))
        self.__undo_redo_service.clear_redo()

    def delete_med(self, id_stergere):
        '''
        sterge un medicament din storage dupa ID
        :param id_stergere: input, string
        '''
        list_of_dependent_id_s = [transaction.id_medicament for transaction in
                                  self.__transactions_repository.get_all_entities()]
        if id_stergere in list_of_dependent_id_s:
            raise KeyError(f"Medicamentul cu ID-ul {id_stergere} nu poate fi sters deoarece depinde de tranzactie!")
        to_be_deleted = self.__meds_repository.get_entity_by_id(id_stergere)
        self.__meds_repository.delete_an_entity(id_stergere)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__meds_repository, to_be_deleted))
        self.__undo_redo_service.clear_redo()

    def update_med(self, id_de_modificare, nume_nou, producator_nou, pret_nou, reteta_noua):
        '''
        modifica atributele unui obiect de tip Medicament daca acesta exista
        :param id_de_modificare: ID ul medicamentului dupa care se face modificarea
        :param nume_nou: numele nou al medicamentului
        :param producator_nou: producatorul nou al medicamentului
        :param pret_nou: pretul nou al medicamentului
        :param reteta_noua: necesitatea noua a retetei medicamentului
        '''
        medicament_nou = self.__meds_repository.get_entity_by_id(id_de_modificare)
        if medicament_nou == None:
            raise KeyError(f"Medicamentul cu ID-ul {id_de_modificare} nu exista!")
        updated_object = self.__meds_repository.get_entity_by_id(id_de_modificare)
        if nume_nou != "":
            medicament_nou.nume = nume_nou
        if producator_nou != "":
            medicament_nou.producator = producator_nou
        if pret_nou > 0:
            medicament_nou.pret = pret_nou
        if reteta_noua != "":
            medicament_nou.reteta = reteta_noua
        self.__med_validator.validate(medicament_nou)
        self.__meds_repository.update_an_entity(medicament_nou)
        self.__undo_redo_service.clear_redo()
        self.__undo_redo_service.add_to_undo(UpdateOperation(self.__meds_repository, medicament_nou, updated_object))
        self.__undo_redo_service.add_to_redo(UpdateOperation(self.__meds_repository, updated_object, medicament_nou))

    def get_random_meds(self, n):
        '''
        creeaza n random entitati de tip medicamnet
        :param n: numar de entitati dat
        '''
        for j in range(n):
            letters = string.ascii_letters
            id_med = ''.join(random.choice(letters) for i in range(5))
            nume = ''.join(random.choice(letters) for i in range(5))
            producatar = ''.join(random.choice(letters) for i in range(5))
            pret = random.choice(range(1, 200))
            reteta = ''.join(random.choice(["da", "nu"]))
            med = Medicament(id_med, nume, producatar, pret, reteta)
            if id_med not in self.get_all_meds():
                self.__meds_repository.create_an_entity(med)
                self.__undo_redo_service.add_to_undo(AddOperation(self.__meds_repository, med))

    def scumpire_cu_procent_dat(self, pret_comparare, procentaj_dat):
        '''
        scumpeste pretul fiecarui medicament cu pretul mai mic decat pretul de comparare cu un procent dat
        :param pret_comparare: pretul cu care se compara pretul medicamentului
        :param procentaj_dat:procentul cu care se scumpeste pretul fiecarui medicament
        '''
        errors = []
        if pret_comparare < 0:
            errors.append("Introduceti un pret de comparare valid!")
        if "%" not in procentaj_dat:
            errors.append("Introduceti un numar care sa contina simbolul % dupa el!")
            if len(errors) > 0:
                raise ValueError(errors)
        result_list = self.get_all_meds()
        newlist = []
        for medicament in result_list:
            if medicament.pret < pret_comparare:
                copy_med = copy(medicament)
                pretnou = medicament.pret + medicament.pret * (
                        float(procentaj_dat[:procentaj_dat.find("%")]) / 100)
                self.__meds_repository.update_an_entity(
                    Medicament(medicament.id_entitate, medicament.nume, medicament.producator, pretnou,
                               medicament.reteta))
                newlist.append([copy_med, self.__meds_repository.get_entity_by_id(medicament.id_entitate)])
        self.__undo_redo_service.clear_redo()
        self.__undo_redo_service.add_to_undo(RaisePrice(self.__meds_repository, newlist))


