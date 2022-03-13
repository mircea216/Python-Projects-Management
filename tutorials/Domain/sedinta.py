from Domain.entitate import Entitate


class Sedinta(Entitate):
    def __init__(self, id_sedinta, id_elev, profesor):
        '''
        construieste un obiect de tip Sedinta
        :param id_sedinta: ID-ul sedintei
        :param id_elev: ID-ul elevului
        :param profesor: profesorul sedintei
        '''
        super().__init__(id_sedinta)
        self.__id_elev = id_elev
        self.__profesor = profesor

    @property
    def id_elev(self):
        return self.__id_elev

    @id_elev.setter
    def id_elev(self, value):
        self.__id_elev = value

    @property
    def profesor(self):
        return self.__profesor

    @profesor.setter
    def profesor(self, value):
        self.__profesor = value

    def __str__(self):
        '''
        determina o reprezentare string a obiectului
        :return: un obiect cu formatul de mai jos
        '''
        return f"ID SEDINTA: {self.id_entitate}, ID ELEV: {self.id_elev}, PROFESOR: {self.profesor}"
