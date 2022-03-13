from Domain.entitate import Entitate


class Nava(Entitate):
    def __init__(self, id_nava, tip, max_hit_points):
        '''
        construieste un obiect de tip Nava
        :param id_nava: ID-ul navei
        :param tip: tipul navei
        :param max_hit_points: max_hit_points-urile navei
        '''
        super().__init__(id_nava)
        self.__tip = tip
        self.__max_hit_points = max_hit_points
        self.__current_hit_points = max_hit_points

    @property
    def tip(self):
        return self.__tip

    @tip.setter
    def tip(self, value):
        self.__tip = value

    @property
    def max_hit_points(self):
        return self.__max_hit_points

    @max_hit_points.setter
    def max_hit_points(self, value):
        self.____max_hit_points = value

    @property
    def current_hit_points(self):
        return self.__current_hit_points

    @current_hit_points.setter
    def current_hit_points(self, value):
        self.__current_hit_points = value

    def __str__(self):
        return f"ID-UL NAVEI: {self.id_entitate}, TIP: {self.tip}, MAX HIT POINTS: {self.max_hit_points}," \
               f" CURRENT HIT POINTS: {self.current_hit_points}"
