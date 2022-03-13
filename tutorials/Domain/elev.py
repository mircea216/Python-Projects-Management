from Domain.entitate import Entitate


class Elev(Entitate):
    def __init__(self,  id_elev, nume , varsta):
        '''
        construieste un obiect de tip Elev
        :param id_elev: ID-ul elevului
        :param nume: numele elevului
        :param varsta: varsta elevului
        '''
        super().__init__(id_elev)
        self.__nume = nume
        self.__varsta = varsta

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def varsta(self):
        return self.__varsta

    @varsta.setter
    def varsta(self, value):
        self.__varsta = value

    def __str__(self):
        '''
        determina o reprezentare string a obiectului
        :return: un obiect cu formatul de mai jos
        '''
        return f"ID ELEV: {self.id_entitate}, NUME: {self.nume}, VARSTA: {self.varsta}"

