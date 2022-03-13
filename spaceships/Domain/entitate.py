class Entitate:
    def __init__(self, id_entitate):
        '''
        construieste un obiect de tip Entitate al carui ID va fi mostenit
        :param id_entitate: ID-ul entitatii
        '''
        self.__id_entitate = id_entitate

    def __eq__(self, other):
        '''
        verifica egalitatea a doua entitati
        :param other: un obiect de un anume tip
        :return: True sau False - boolean - output
        '''
        return type(self) == type(other) and self.__id_entitate == other.__id_entitate

    @property
    def id_entitate(self):
        '''
        getter pentru ID-ul entitatii
        :return: self.__id_entitate
        '''
        return self.__id_entitate
