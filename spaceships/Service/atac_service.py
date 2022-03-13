from copy import copy

from Domain.atac import Atac
from Domain.atac_validator import AtacValidator
from Domain.nava_spatiala import Nava
from Repository.generic_file_repository import GenericFileRepository


class AtacService():
    def __init__(self, attack_repository: GenericFileRepository, attack_validator: AtacValidator,
                 spaceship_repository: GenericFileRepository):
        '''
        construieste service-ul atacurilor
        :param attack_repository: repository-ul de atacuri
        :param attack_validator: validatorul de atacuri
        :param spaceship_repository: repository-ul de nave
        '''
        self.__attack_repository = attack_repository
        self.__attack_validator = attack_validator
        self.__spaceship_repository = spaceship_repository

    def create_an_attack(self, id_atac, id_nava_atacator, id_nava_atacata, pagube):
        '''
        adauga in service un atac daca acesta nu exista deja in storage
        :param id_atac: ID-ul atacului
        :param id_nava_atacator: ID-ul navei atacator
        :param id_nava_atacata: ID-ul navei atacate
        :param pagube: pagubele produse de atac
        '''
        if self.__spaceship_repository.get_entity_by_id(id_nava_atacator) is None:
            raise ValueError(f"Nu a fost inregistrata nicio nava cu ID {id_nava_atacator}")
        if self.__spaceship_repository.get_entity_by_id(id_nava_atacata) is None:
            raise ValueError(f"Nu a fost inregistrata nicio nava cu ID {id_nava_atacata}")
        attack = Atac(id_atac, id_nava_atacator, id_nava_atacata, pagube)
        self.__attack_validator.validate(attack)
        self.__attack_repository.create_an_entity(attack)

    def get_all_attacks(self):
        '''
        determina o lista cu toate atacurile si navele corespunzatoare lor
        :return: o lista cu atacuri
        '''
        return [[attack, self.__spaceship_repository.get_entity_by_id(attack.id_nava_atacator),
                 self.__spaceship_repository.get_entity_by_id(attack.id_nava_atacata)] for attack in
                self.__attack_repository.get_all_entities()]

    def get_the_result_of_the_attack(self, id_atac):
        '''

        :param id_atac:
        :return:
        '''
        list_of_attacks = [attack[0].id_entitate for attack in self.get_all_attacks()]
        if id_atac not in list_of_attacks:
            raise ValueError("ID-ul atacului trebuie sa existe!")
        attack = self.__attack_repository.get_entity_by_id(id_atac)
        current_spaceship = self.__spaceship_repository.get_entity_by_id(attack.id_nava_atacata)
        new_spaceship = copy(current_spaceship)
        if current_spaceship.current_hit_points - attack.pagube >= 0:
            new_spaceship.current_hit_points = current_spaceship.current_hit_points - attack.pagube
        else:
            new_spaceship.current_hit_points = 0
        self.__spaceship_repository.update_an_entity(new_spaceship)
        return new_spaceship

    def sort_the_spaceship_in_descending_order_by_sum_of_damages(self):
        '''
        sorteaza descrescator navele spatiale dupa daunele provocate
        :return: o lista sortata descrecator a navelor
        '''
        dictionary_of_spaceship = {}
        for spaceship in self.__spaceship_repository.get_all_entities():
            dictionary_of_spaceship[spaceship.__str__()] = 0
        for spaceship in self.__spaceship_repository.get_all_entities():
            for attack in self.get_all_attacks():
                if spaceship.id_entitate == attack[0].id_nava_atacator or spaceship.id_entitate == attack[
                    0].id_nava_atacata:
                    dictionary_of_spaceship[spaceship.__str__()] += attack[0].pagube
        return sorted(list(dictionary_of_spaceship.items()), key=lambda x: x[1], reverse=True)

    def print_battles(self):
        '''
        afiseaza toate bataile
        :return:
        '''
        dict_of_battles = {}
        for attack in self.get_all_attacks():
            dict_of_battles[attack.__str__()] = attack

