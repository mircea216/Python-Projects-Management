from Domain.atac import Atac


class AtacValidator():
    def validate(self, attack: Atac):
        '''
        valideaza proprietatile unui atac
        :param attack: obiect de tip Atac
        '''
        errors = []
        if attack.pagube <= 0 or type(attack.pagube) is not int:
            errors.append("Pagubele produse de atac sunt un numar intreg, pozitiv!")
        if len(errors):
            raise ValueError(errors)
