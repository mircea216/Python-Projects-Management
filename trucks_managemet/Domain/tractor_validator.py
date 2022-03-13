from Domain.tractor import Tractor


class TractorValidator:
    def validate(self, truck: Tractor):
        '''

        :param truck:
        :return:
        '''
        errors = []
        if truck.model == 0:
            errors.append("Modelul nu poate fi nul!")
        if truck.inchiriere not in ["da", "nu"]:
            errors.append("Inchirierea este din multime da/nu")
        if len(errors):
            raise ValueError(errors)
