import random
from string import ascii_letters

from Domain.tractor import Tractor
from Domain.tractor_validator import TractorValidator
from Repository.generic_file_repository import GenericFileRepository


class TractorService:
    def __init__(self, truck_repository: GenericFileRepository, truck_validator: TractorValidator,
                 agricultural_activity_repository: GenericFileRepository):
        '''
        
        :param truck_repository: 
        :param truck_validator: 
        '''
        self.__truck_repository = truck_repository
        self.__truck_validator = truck_validator
        self.__agricultural_activity_repository = agricultural_activity_repository

    def create_a_truck(self, id_tractor, model, inchiriere):
        '''
        
        :param id_tractor: 
        :param model: 
        :param inchiriere: 
        :return: 
        '''
        truck = Tractor(id_tractor, model, inchiriere)
        self.__truck_validator.validate(truck)
        self.__truck_repository.create_an_entity(truck)

    def delete_a_truck(self, id_stergere):
        '''

        :param id_stergere:
        :return:
        '''
        list_of_trucks_depending_on_activities = [activity.id_tractor for activity in
                                                  self.__agricultural_activity_repository.get_all_entities()]
        if id_stergere in list_of_trucks_depending_on_activities:
            raise KeyError(f"Nu se poate sterge tractorul cu ID-ul {id_stergere}!")
        self.__truck_repository.delete_an_entity(id_stergere)

    def get_all_trucks(self):
        '''
        :return: 
        '''
        return self.__truck_repository.get_all_entities()

    def get_random_trucks(self, given_number_of_trucks):
        '''
        genereaza o serie de n entitati random valide
        :param given_number_of_trucks: numar dat de entitati
        '''
        for index in range(given_number_of_trucks):
            id_tractor = "".join(random.choice(ascii_letters) for i in range(4))
            model = random.choice(range(1, 31))
            inchiriere = random.choice(["da", "nu"])
            random_truck = Tractor(id_tractor, model, inchiriere)
            self.__truck_validator.validate(random_truck)
            self.__truck_repository.create_an_entity(random_truck)
