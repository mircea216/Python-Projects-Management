from Domain.elev import Elev


class ElevValidator():
    def validate(self, student: Elev):
        '''
        valideaza atributele unui obiect de tip Produs
        :param student: obiect de tip Produs
        '''
        errors = []
        if type(student.varsta) is not int:
            errors.append("Varsta este un numar intreg!")
        if student.nume == "":
            errors.append("Dati un nume nenul!")
        if len(errors):
            raise ValueError(errors)
