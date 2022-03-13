from Domain.sedinta import Sedinta
from Domain.sedinta_validator import SedintaValidator
from Repository.generic_file_repository import GenericFileRepository
from random import *
from string import ascii_letters


class SedintaService():
    def __init__(self, tutorial_repository: GenericFileRepository, tutorial_validator: SedintaValidator,
                 student_repository: GenericFileRepository):
        '''
        construieste un obiect de tip SedintaService ce preia repository-ul generic si validatorul sedintelor
        :param tutorial_repository: repository de Sedintae
        :param tutorial_validator: validatorul sedintelor
        '''
        self.__tutorial_repository = tutorial_repository
        self.__tutorial_validator = tutorial_validator
        self.__student_repository = student_repository

    def create_a_tutorial(self, id_sedinta, id_elev, profesor):
        '''
        adauga in storage un obiect de tip Sedinta daca acesta nu exista deja
        :param id_sedinta: ID-ul sedintei
        :param id_elev: ID-ul elevului
        :param profesor: profesorul sedintei
        '''
        if self.__student_repository.get_entity_by_id(id_elev) is None:
            raise KeyError(f"Nu a fost inregistrat niciun elev cu ID-ul {id_elev}")
        tutorial = Sedinta(id_sedinta, id_elev, profesor)
        self.__tutorial_validator.validate(tutorial)
        self.__tutorial_repository.create_an_entity(tutorial)

    def get_all_tutorials(self):
        '''
        determina o lista cu toate sedintele
        :return:  - list, output
        '''
        list_of_tutorials = [[tutorial, self.__student_repository.get_entity_by_id(tutorial.id_elev).nume] for tutorial
                             in self.__tutorial_repository.get_all_entities()
                             if self.__student_repository.get_entity_by_id(tutorial.id_elev) is not None]
        return list_of_tutorials

    def print_students_with_a_number_of_tutorials_greater_than_a_given_number(self, given_number):
        '''
        determina elevii cu un numar de sedinte mai mare decat un numar dat
        :param given_number: numarul dat
        :return: elevii cu proprietatea ceruta
        '''
        dict_of_students = {}
        list_of_students_ids = [tutorial[0].id_elev for tutorial in self.get_all_tutorials()]
        for student in self.__student_repository.get_all_entities():
            dict_of_students[student.id_entitate] = list_of_students_ids.count(student.id_entitate)
        list_of_students = [self.__tutorial_repository.get_entity_by_id(key) for key in dict_of_students if
                            dict_of_students[key] >= given_number]
        return list_of_students

    def sort_teachers_in_descending_order_by_number_of_tutorial(self):
        '''
        sorteaza profesorii descrescator dupa numarul de sedinte
        :return: o lista cu profesorii sortati
        '''
        dict_of_teachers = {}
        list_of_teachers = [tutorial[0].profesor for tutorial in self.get_all_tutorials()]
        for tutorial in self.get_all_tutorials():
            dict_of_teachers[tutorial[0].profesor] = list_of_teachers.count(tutorial[0].profesor)
        return sorted(list(dict_of_teachers.items()), key=lambda x: x[1], reverse=True)

    def delete_student_and_tutorials(self, id_stergere):
        '''
        sterge un elev si toate sedintele lui daca acesta exsista
        :param id_stergere: ID-ul ce trebuie sters
        '''
        if self.__student_repository.get_entity_by_id(id_stergere) is None:
            raise KeyError(f"Nu exista niciun elev cu ID-ul {id_stergere}!")
        for tutorial in self.get_all_tutorials():
            if tutorial[0].id_elev == id_stergere:
                self.__tutorial_repository.delete_an_entity(tutorial[0].id_entitate)
        self.__student_repository.delete_an_entity(id_stergere)

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
                if key_function(given_list[j]) < key_function(given_list[j + 1]):
                    # swapping values
                    given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]
                    swapped = True
            if swapped is False:
                break
        if reverse == False:
            return given_list
        else:
            return given_list[::-1]

    def BUBBLE_SORT_with_python_interface(self):
        '''
        sorteaza elevii dupa numarul de profesori cu care fac sedintele de pregatire
        :return: o lista sortata a elevilor
        '''
        dict_of_students = {}
        for student in self.__student_repository.get_all_entities():
            dict_of_students[student.__str__()] = []
        for tutorial in self.get_all_tutorials():
            if tutorial[0].profesor not in dict_of_students[
                self.__student_repository.get_entity_by_id(tutorial[0].id_elev).__str__()]:
                dict_of_students[self.__student_repository.get_entity_by_id(tutorial[0].id_elev).__str__()].append(
                    tutorial[0].profesor)
        return self.bubble_sort(list(dict_of_students.items()), key_function=lambda x: len(x), reverse=False)

    def get_n_random_tutorials(self, n):
        '''
        adauga n entitati de tip Sedinta random
        :param n: numar dat de entitati
        '''
        list_of_students_id_s = [student.id_entitate for student in self.__student_repository.get_all_entities()]
        for index in range(n):
            id_sedinta = "".join(choice(ascii_letters) for i in range(5))
            id_elev = choice(list_of_students_id_s)
            profesor = ""
            for j in range(randint(2, 7)):
                profesor = profesor + "".join(choice(ascii_letters) for i in range(randint(4, 7))) + " "
            tutorial = Sedinta(id_sedinta, id_elev, profesor)
            self.__tutorial_validator.validate(tutorial)
            self.__tutorial_repository.create_an_entity(tutorial)
