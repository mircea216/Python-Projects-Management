from Domain.entitate import Entitate


class Oras(Entitate):
    def __init__(self, id_oras, nume, populatie):
        super().__init__(id_oras)
        self.__nume = nume
        self.__populatie = populatie

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def populatie(self):
        return self.__populatie

    @populatie.setter
    def populatie(self, value):
        self.__populatie = value

    def __str__(self):
        return f"ID ORAS:{self.id_entitate}   NUME: {self.nume}   POPULATIE: {self.populatie}"
