from Domain.sedinta import Sedinta


class SedintaValidator():
    def validate(self, tutorial: Sedinta):
        '''
        valideaza atributele unui obiect de tip Sedinta
        :param tutorial: obiect de tip Sedinta
        '''
        errors = []
        if tutorial.profesor == "":
            errors.append("Dati un nume de profesor nenul!")
        if tutorial.id_elev == "":
            errors.append("ID-UL elevului trebuie sa existe!")
        if len(errors):
            raise ValueError(errors)
