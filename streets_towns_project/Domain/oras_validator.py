from Domain.oras import Oras


class OrasValidator:
    def validate(self, town: Oras):
        '''

        :param town:
        :return:
        '''
        errors = []
        if town.nume == "" or type(town.nume) is not str:
            errors.append("Numele orasului trebuie sa fie un string nenul!")
        if town.populatie <= 0 or type(town.populatie) is not int:
            errors.append("Populatia este reprezentata de un numar intreg strict pozitiv!")
        if len(errors) > 0:
            raise ValueError(errors)

