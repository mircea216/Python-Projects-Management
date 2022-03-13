from copy import deepcopy

from Domain.entitate import Entitate
import jsonpickle as jsonpickle


class GenericFileRepository:
    def __init__(self, file_name):
        '''
        construieste un un storage in care sa fie stocate entitatile si un fisier pentru citire si afisare
        :param file_name: nume de fisier
        '''
        self.__storage = {}
        self.__file_name = file_name

    def __read_file(self):
        try:
            with open(self.__file_name, "r") as fp:
                self.__storage = jsonpickle.decode(fp.read())
        except:
            self.__storage = {}

    def __write_file(self):
        with open(self.__file_name, "w") as fp:
            fp.write(jsonpickle.encode(self.__storage))

    def get_entity_by_id(self, id_entitate):
        '''
        returneaza o entitate dupa un ID dat
        :param id_entitate: string, ID dat, input
        :return: un obiect de tip entitate sau None
        '''
        self.__read_file()
        if id_entitate in self.__storage:
            return self.__storage[id_entitate]
        return None

    def get_all_entities(self):
        '''
        determina toate entitatile stocate
        :return:1 o list cu valorile din dictionar
        '''
        self.__read_file()
        return deepcopy(list(self.__storage.values()))

    def create_an_entity(self, entitate: Entitate):
        '''
        adauga o entitate in storage daca ID_ul acesteia exista
        :param entitate: obiect de tip Entitate
        '''
        if self.get_entity_by_id(entitate.id_entitate):
            raise KeyError(f"Exista deja entitatea cu ID-ul {entitate.id_entitate}!")
        self.__storage[entitate.id_entitate] = entitate
        self.__write_file()
