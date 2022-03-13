from Domain.tranzactie import Tranzactie


class TranzactieValidator:
    def validate(self, tranzactie: Tranzactie):
        errors = []
        if tranzactie.numar_bucati < 0:
            errors.append("Introduceti un numar de bucati valid!")
        value = True
        for character in str(tranzactie.data):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/"]:
                value = False
        if value == False:
            errors.append("Atentie la introducerea datei!")
        ok = True
        if len(str(tranzactie.data)) not in range(8, 11) or str(tranzactie.data).count("/") != 2:
            ok = False
        if ok == False:
            errors.append("Data tranzactiei trebuie sa aiba formatul DD/MM/YYYY!")
        else:
            data_str = str(tranzactie.data)
            day = int(data_str[:data_str.find("/")])
            month = int(data_str[data_str.find("/") + 1:data_str.rfind("/")])
            year = int(data_str[data_str.rfind("/ ") + 1:])
            if day not in range(1, 32) or month not in range(1, 13) or year not in range(2021):
                errors.append("Atentie la introducerea corecta a datelor!")
            if len(errors):
                raise ValueError(errors)
