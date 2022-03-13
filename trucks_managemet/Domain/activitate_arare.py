from Domain.entitate import Entitate


class ActivitateArare(Entitate):
    def __init__(self, id_activitate_arara, id_tractor, timp, zi, finalizare):
        super().__init__(id_activitate_arara)
        self.__id_tractor = id_tractor
        self.__timp = timp
        self.__zi = zi
        self.__finalizare = finalizare

    @property
    def id_tractor(self):
        return self.__id_tractor

    @id_tractor.setter
    def id_tractor(self, value):
        self.__id_tractor = value

    @property
    def timp(self):
        return self.__timp

    @timp.setter
    def timp(self, value):
        self.__timp = value

    @property
    def zi(self):
        return self.__zi

    @zi.setter
    def zi(self, value):
        self.__zi = value

    @property
    def finalizare(self):
        return self.__finalizare

    @finalizare.setter
    def finalizare(self, value):
        self.__finalizare = value

    def __str__(self):
        return f"ID ACTIVITATE ARARE: {self.id_entitate}, ID TRACTOR: {self.id_tractor}, TIMP: {self.timp}, " \
               f"ZI: {self.zi}, FINALIZARE: {self.finalizare}"
