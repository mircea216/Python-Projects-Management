from Domain.nava_spatiala import Nava


class NavaValidator():
    def validate(self, spaceship: Nava):
        '''
        valideaza proprietatile unui obiect de tip Nava
        :param spaceship: obiect de tip Nava
        '''
        errors = []
        if spaceship.max_hit_points <= 0 or type(spaceship.max_hit_points) is not int:
            errors.append("Max Hit Points reprezinta un numar intreg pozitiv!")
        if spaceship.tip == "":
            errors.append("Tipul navei este un intreg nenul!")
        if len(errors):
            raise ValueError(errors)
