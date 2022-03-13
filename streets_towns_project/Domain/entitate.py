class Entitate:
    def __init__(self, id_entiate):
        self.__id_entitate = id_entiate

    @property
    def id_entitate(self):
        return self.__id_entitate

    def __eq__(self, other):
        return type(self) == type(other) and self.id_entitate == other.id_entitate

