from Domain.entitate import Entitate


class CardClient(Entitate):
    def __init__(self, id_client, nume, prenume, CNP, data_nasterii, data_inregistrarii):
        '''
        creeaza un obiect de tipul CardClient
        :param id_client: id_ul clientului
        :param nume: numele clientului
        :param prenume: prenumele clientului
        :param CNP: CNP-ul clientului
        :param data_nasterii: date nasterii clientului
        :param data_inregistrarii: date inregistrarii clientului
        '''
        super().__init__(id_client)
        self.__nume = nume
        self.__prenume = prenume
        self.__CNP = CNP
        self.__data_nasterii = data_nasterii
        self.__data_inregistrarii = data_inregistrarii

    def __str__(self):
        return f"ID client: {self.id_entitate}, NUME: {self.__nume}, PRENUME: {self.__prenume}, CNP: {self.__CNP}, " \
               f"DATA NASTERII: {self.__data_nasterii}, DATE INREGISTRARII: {self.__data_inregistrarii}"


    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume_nou):
        self.__nume = nume_nou

    @property
    def prenume(self):
        return self.__prenume

    @prenume.setter
    def prenume(self, prenume_nou):
        self.__prenume = prenume_nou

    @property
    def CNP(self):
        return self.__CNP

    @CNP.setter
    def CNP(self, CNP_nou):
        self.__CNP = CNP_nou

    @property
    def data_nasterii(self):
        return self.__data_nasterii

    @data_nasterii.setter
    def data_nasterii(self, data_nasterii_noua):
        self.__data_nasterii = data_nasterii_noua

    @property
    def data_inregistrarii(self):
        return self.__data_inregistrarii

    @data_inregistrarii.setter
    def data_inregistrarii(self, data_inregistrarii_noua):
        self.__data_inregistrarii = data_inregistrarii_noua
