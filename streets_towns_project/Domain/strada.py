from Domain.entitate import Entitate


class Strada(Entitate):
    def __init__(self, id_strada, id_oras, nume, lungime):
        super().__init__(id_strada)
        self.__id_oras = id_oras
        self.__nume = nume
        self.__lungime = lungime

    @property
    def id_oras(self):
        return self.__id_oras

    @id_oras.setter
    def id_oras(self, value):
        self.__id_oras = value

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def lungime(self):
        return self.__lungime

    @lungime.setter
    def lungime(self, value):
        self.__lungime = value

    def __str__(self):
        return f"ID STRADA: {self.id_entitate}, ID ORAS: {self.id_oras}, NUME: {self.nume}, LUNGIME: {self.lungime}"

