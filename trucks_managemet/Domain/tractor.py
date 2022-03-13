from Domain.entitate import Entitate


class Tractor(Entitate):
    def __init__(self, id_tractor, model, inchiriere):
        '''

        :param id_tractor:
        :param model:
        :param inchiriere:
        '''
        super().__init__(id_tractor)
        self.__model = model
        self.__inchiriere = inchiriere

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def inchiriere(self):
        return self.__inchiriere

    @inchiriere.setter
    def inchiriere(self, value):
        self.__inchiriere = value

    def __str__(self):
        '''

        :return:
        '''
        return f"ID TRACTOR: {self.id_entitate}, MODEL: {self.model}, ESTE INCHIRIAT?: {self.inchiriere}"
