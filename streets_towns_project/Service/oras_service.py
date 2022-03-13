from Domain.oras import Oras
from Domain.oras_validator import OrasValidator
from Repository.generic_file_repository import GenericFileRepository


class OrasService:
    def __init__(self, generic_file_repository: GenericFileRepository, town_validator: OrasValidator):
        '''

        :param generic_file_repository:
        :param town_validator:
        '''
        self.__generic_file_repository = generic_file_repository
        self.__town_validator = town_validator

    def get_all_towns(self):
        '''

        :return:
        '''
        return self.__generic_file_repository.get_all_entities()

    def create_a_town(self, id_oras, nume, populatie):
        town = Oras(id_oras, nume, populatie)
        self.__town_validator.validate(town)
        self.__generic_file_repository.create_an_entity(town)


