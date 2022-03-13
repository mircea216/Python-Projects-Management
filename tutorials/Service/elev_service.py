from Domain.elev import Elev
from Domain.elev_validator import ElevValidator
from Repository.generic_file_repository import GenericFileRepository


class ElevService():
    def __init__(self, student_repository: GenericFileRepository, student_validator: ElevValidator):
        '''
        construieste un obiect de tip ElevService ce preia repository-ul generic si validatorul elevilor
        :param student_repository: repository de elevi
        :param student_validator: validatorul elevilor
        '''
        self.__student_repository = student_repository
        self.__student_validator = student_validator

    def create_a_student(self, id_elev, nume, varsta):
        '''
        adauga in storage un obiect de tip Elev daca acesta nu exista deja
        :param id_elev: ID-ul elevului
        :param nume: numele elevului
        :param varsta: varsta elevului
        '''
        student = Elev(id_elev, nume, varsta)
        self.__student_validator.validate(student)
        self.__student_repository.create_an_entity(student)

    def get_all_students(self):
        '''
        determina o lista cu toate elevii
        :return: self.__student_repository.get_all_entities() - list, output
        '''
        return self.__student_repository.get_all_entities()
