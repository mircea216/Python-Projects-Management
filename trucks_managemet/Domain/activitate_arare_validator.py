from Domain.activitate_arare import ActivitateArare


class ActivitateArareValidator:
    def validate(self, agricultural_activity: ActivitateArare):
        errors = []
        if agricultural_activity.zi not in range(1, 31) or type(agricultural_activity.zi) is not int:
            errors.append("Ziua activitatii trebuie sa fie din intervalul 1-30!")
        if agricultural_activity.finalizare not in ["da", "nu"]:
            errors.append("Finalizarea activitatii este fie da, fie nu!")
        if agricultural_activity.id_tractor == "":
            errors.append("ID-ul tractorului trebuie sa fie nenul!")
        if type(agricultural_activity.timp) is not int or agricultural_activity.timp == 0:
            errors.append("Timpul de lucru trebuie sa fie intreg nenul!")
        if len(errors):
            raise ValueError(errors)
