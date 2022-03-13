from Domain.oras import Oras
from Domain.strada import Strada
from Domain.strada_validator import StradaValidator
from Repository.generic_file_repository import GenericFileRepository
import json


class StradaService:
    def __init__(self, town_repo: GenericFileRepository, street_repo: GenericFileRepository,
                 street_validator: StradaValidator):
        '''

        :param town_repo:
        :param street_repo:
        '''
        self.__town_repo = town_repo
        self.__street_repo = street_repo
        self.__street_validator = street_validator

    def get_all_streets(self):
        '''

        :return:
        '''
        return self.__street_repo.get_all_entities()

    def create_a_street(self, id_strada, id_oras, nume, lungime):
        '''

        :param id_strada:
        :param id_oras:
        :param nume:
        :param lungime:
        :return:
        '''
        if self.__town_repo.get_entity_by_id(id_oras) is None:
            raise KeyError(f"Nu exista un oras cu ID-ul {id_oras}!")
        street = Strada(id_strada, id_oras, nume, lungime)
        self.__street_validator.validate(street)
        self.__street_repo.create_an_entity(street)

    def get_the_length_of_a_street(self, oras: Oras):
        '''

        :param oras:
        :return:
        '''
        street_length = 0
        list_of_streets = self.get_all_streets()
        for street in list_of_streets:
            if street.id_oras == oras.id_entitate:
                street_length += street.lungime
        return street_length

    def sort_towns_in_descending_order_by_street_length(self):
        '''

        :return:
        '''
        result_list = sorted(self.__town_repo.get_all_entities(), key=self.get_the_length_of_a_street, reverse=True)
        for town in result_list:
            print(town, "----->STREET LENGTH:", self.get_the_length_of_a_street(town))

    def number_of_towns(self, town: Oras):
        '''

        :param town:
        :return:
        '''
        list_of_streets = self.get_all_streets()
        number = 0
        for street in list_of_streets:
            if street.id_oras == town.id_entitate:
                number += 1
        return number

    def print_streets_belonging_to_more_than_2_towns(self):
        '''

        :return:
        '''

        list_of_streets = self.get_all_streets()
        for street in list_of_streets:
            if self.number_of_towns(self.__town_repo.get_entity_by_id(street.id_oras)) >= 2:
                print(street)

    def town_streets(self, oras: Oras):
        '''

        :return:
        '''
        all_streets = []
        streets = self.get_all_streets()
        for street in streets:
            if street.id_oras == oras.id_entitate:
                all_streets.append(street.__str__())
        return all_streets

    def export_json_file(self, file_name):
        towns = self.__town_repo.get_all_entities()
        towns_with_their_streets = [[town.__str__(), '---', self.town_streets(town)] for town in towns]
        with open(file_name, "w") as outfile:
            for a in towns_with_their_streets:
                json.dump(a, outfile)
