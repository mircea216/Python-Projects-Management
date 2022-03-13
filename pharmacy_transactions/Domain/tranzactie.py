from Domain.entitate import Entitate


class Tranzactie(Entitate):
    def __init__(self, id_tranzactie, id_medicament, id_client, numar_bucati, data, ora):
        '''
        Creeaza un obiect de tip Tranzactie
        :param id_tranzactie: ID-ul tranzactiei
        :param id_medicament: ID-ul medicamentului
        :param id_card_client: ID-ul cardului de client
        :param numar_bucati: numarul de bucati
        :param data: data tranzactiei
        :param ora: ora tranzactiei
        '''
        super().__init__(id_tranzactie)
        self.__id_medicament = id_medicament
        self.__id_client = id_client
        self.__numar_bucati = numar_bucati
        self.__data = data
        self.__ora = ora

    @property
    def id_medicament(self):
        return self.__id_medicament

    @property
    def id_client(self):
        return self.__id_client

    @property
    def numar_bucati(self):
        return self.__numar_bucati

    @numar_bucati.setter
    def numar_bucati(self, numar_bucati_nou):
        self.__numar_bucati = numar_bucati_nou

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data_noua):
        self.__data = data_noua

    @property
    def ora(self):
        return self.__ora

    @ora.setter
    def ora(self, ora_noua):
        self.__ora = ora_noua
