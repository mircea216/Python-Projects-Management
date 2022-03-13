class Entitate:
    def __init__(self, id_entitate):
        '''
        construieste un obiect de tip Entitate
        :param id_entitate: ID-ul entitatii
        '''
        self.__id_entitate = id_entitate

    @property
    def id_entitate(self):
        '''
        returneaza ID-ul unei entitati
        :return: string, output - self.__id_entitate
        '''
        return self.__id_entitate

    def __eq__(self, other):
        '''
        verifica egalitatea a doua entitati
        :param other: o entitate de un anumit tip
        :return: boolean - True sau False - output
        '''
        return type(self) == type(other) and self.id_entitate == other.id_entitate
