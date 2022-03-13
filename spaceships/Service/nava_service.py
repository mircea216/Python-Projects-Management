from Domain.nava_spatiala import Nava
from Domain.nava_spatiala_validator import NavaValidator
from Repository.generic_file_repository import GenericFileRepository


class NavaService():
    def __init__(self, spaceship_repository: GenericFileRepository, spaceship_validator: NavaValidator):
        '''
        construieste service-ul navelor preluand repository-ul si validatorul navelor
        :param spaceship_repository: repository de nave
        :param spaceship_validator: validator de nave
        '''
        self.__spaceship_repository = spaceship_repository
        self.__spaceship_validator = spaceship_validator

    def create_a_spaceship(self, id_nava, tip, max_hit_points):
        '''
        adauga in service un obiect de tip Nava daca nu exista deja
        :param id_nava: ID-ul navei
        :param tip: tipul navei
        :param max_hit_points: max_hit_points-urile navei
        '''
        spaceship = Nava(id_nava, tip, max_hit_points)
        self.__spaceship_validator.validate(spaceship)
        self.__spaceship_repository.create_an_entity(spaceship)

    def get_all_spaceship(self):
        return self.__spaceship_repository.get_all_entities()
