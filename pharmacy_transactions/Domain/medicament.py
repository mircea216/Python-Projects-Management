from Domain.entitate import Entitate


class Medicament(Entitate):
    def __init__(self, id_medicament, nume, producator, pret, reteta):
        '''
        creeaza un obiect de tipul medicament
        :param id_medicament: id_ul medicamentului
        :param nume: numele medicamentului
        :param producator: producatorul medicamentului
        :param pret: pretul medicamentului
        :param reteta: reteata
        '''
        super().__init__(id_medicament)
        self.__nume = nume
        self.__producator = producator
        self.__pret = pret
        self.__reteta = reteta

    def __str__(self):
        '''
        determina reprezintarea string a obiectului
        :return: un string al obiectului
        '''
        return f"ID medicament: {self.id_entitate}, NUME: {self.__nume}, PRODUCATOR: {self.__producator}, " \
               f"PRET: {self.__pret}, NECESITA RETETA?: {self.__reteta}"

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume_nou):
        self.__nume = nume_nou

    @property
    def producator(self):
        return self.__producator

    @producator.setter
    def producator(self, producator_nou):
        self.__producator = producator_nou

    @property
    def pret(self):
        return self.__pret

    @pret.setter
    def pret(self, pret_nou):
        self.__pret = pret_nou

    @property
    def reteta(self):
        return self.__reteta

    @reteta.setter
    def reteta(self, reteta_noua):
        self.__reteta = reteta_noua
