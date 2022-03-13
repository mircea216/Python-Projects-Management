from Domain.strada import Strada


class StradaValidator:
    def validate(self, strada: Strada):
        '''

        :param strada:
        :return:
        '''
        errors = []
        if strada.nume == "" or type(strada.nume) is not str:
            errors.append("Numele strazii trebuie sa fie un string nenul!")
        if strada.lungime <= 0 or type(strada.lungime) is not int:
            errors.append("Lungimea este reprezentata de un numar intreg strict pozitiv!")
        if len(errors) > 0:
            raise ValueError(errors)
