from Domain.activitate_arare import ActivitateArare
from Domain.activitate_arare_validator import ActivitateArareValidator
from Domain.tractor import Tractor
from Repository.generic_file_repository import GenericFileRepository
import random
import json


class ActivitateArareService:
    def __init__(self, agricultural_activity_repository: GenericFileRepository,
                 agricultural_activity_validator: ActivitateArareValidator,
                 truck_repository: GenericFileRepository):
        self.__agricultural_activity_repository = agricultural_activity_repository
        self.__agricultural_activity_validator = agricultural_activity_validator
        self.__truck_repository = truck_repository

    def create_an_agricultural_activity(self, id_activitate_arara, id_tractor, timp, zi, finalizare):
        '''

        :param id_tractor:
        :param model:
        :param inchiriere:
        :return:
        '''
        if self.__truck_repository.get_entity_by_id(id_tractor) is None:
            raise KeyError(f"Nu a fost inregistrat niciun tractor cu ID-ul {id_tractor}!")
        agricultural_activity = ActivitateArare(id_activitate_arara, id_tractor, timp, zi, finalizare)
        self.__agricultural_activity_validator.validate(agricultural_activity)
        self.__agricultural_activity_repository.create_an_entity(agricultural_activity)

    def get_all_agricultural_activities(self):
        '''

        :return:
        '''
        return self.__agricultural_activity_repository.get_all_entities()

    def print_the_activities_of_an_unrented_truck(self):
        '''
        print the activities of an unrented truck chosen randomly
        '''
        unrented_trcuks = [truck for truck in self.__truck_repository.get_all_entities() if truck.inchiriere == "nu"]
        if len(unrented_trcuks) == 0:
            print("Nu exista tractoare neinchiriaete")
        else:
            random_truck = random.choice(unrented_trcuks)
            for agricultural_activity in self.get_all_agricultural_activities():
                if agricultural_activity.id_tractor == random_truck.id_entitate:
                    print(agricultural_activity)

    def sort_key(self, truck: Tractor):
        '''
        determina timpul petrecut de un tractor pentru toate activitatile sale agrare
        :param truck: obiect de tip Tractor
        :return: spent_time, int, output
        '''
        spent_time = 0
        for activity in self.get_all_agricultural_activities():
            if activity.id_tractor == truck.id_entitate:
                spent_time += activity.timp
        return spent_time

    def sort_trucks_by_time_spent_on_activities(self):
        '''
        afiseaza tractoarele ordonate crescator dupa numarul de ore pentru activitati
        '''
        sorted_list_of_trucks = sorted(self.__truck_repository.get_all_entities(), key=self.sort_key)
        for truck in sorted_list_of_trucks:
            print(truck, f"---> TIMP PENTRU ACTIVITATI: {self.sort_key(truck)}")

    def export_trucks_working_for_extra_time(self, file_name):
        dict = {1: 2, 2: [2, 3]}
        with open(file_name, "w") as fp:
            for keys, values in dict.items():
                el = keys, values
                el = list(el)
                fp.write(json.dump(el, fp))



