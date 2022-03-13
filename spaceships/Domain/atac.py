from Domain.entitate import Entitate


class Atac(Entitate):
    def __init__(self, id_atac, id_nava_atacator, id_nava_atacata, pagube):
        '''
        construieste un obiect de tip Atac
        :param id_atac: ID-ul atacului
        :param id_nava_atacator: ID-ul navei atacator
        :param id_nava_atacata: ID-ul navei atacate
        :param pagube: pagubele produse de atac
        '''
        super().__init__(id_atac)
        self.__id_nava_atacator = id_nava_atacator
        self.__id_nava_atacata = id_nava_atacata
        self.__pagube = pagube

    @property
    def id_nava_atacator(self):
        return self.__id_nava_atacator

    @id_nava_atacator.setter
    def id_nava_atacator(self, value):
        self.__id_nava_atacator = value

    @property
    def id_nava_atacata(self):
        return self.__id_nava_atacata

    @id_nava_atacata.setter
    def id_nava_atacata(self, value):
        self.__id_nava_atacata = value

    @property
    def pagube(self):
        return self.__pagube

    @pagube.setter
    def pagube(self, value):
        self.__pagube = value

    def __str__(self):
        return f"ID ATAC: {self.id_entitate}, ID NAVA ATACTOR: {self.id_nava_atacator}, " \
               f"ID NAVA ATACATA: {self.id_nava_atacata}, PAGUBE: {self.pagube}"
