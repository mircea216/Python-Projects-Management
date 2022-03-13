class MedicamentValidator:
    def validate(self, medicament):
        errors = []
        if medicament.pret <= 0:
            errors.append("Pretul medicamentului trebuie sa fie strict pozitiv")
        if medicament.reteta not in ["da", "nu"]:
            errors.append("Necesitatea retetei trebuie sa cuprinda un raspuns de tipul da/nu")
        if len(errors) > 0:
            raise ValueError(errors)
