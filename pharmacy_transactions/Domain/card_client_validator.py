class CardClientValidator:
    def validate(self, card_client):
        errors = []
        ok = 1
        for character in str(card_client.data_nasterii):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                ok = 0
        if ok == 0:
            raise ValueError("Atentie la introducerea datei!")
        if str(card_client.data_nasterii).count("-") != 2 or len(str(card_client.data_nasterii)) != 10:
            errors.append("Data tranzactiei trebuie sa fie de forma [yyyy-mm-dd]!")
        if int(str(card_client.data_nasterii)[8]) not in range(4) or int(
                str(card_client.data_nasterii)[9]) not in range(10):
            errors.append("Atentie la ziua, luna si anul introduse!")
        if int(str(card_client.data_nasterii)[:str(card_client.data_nasterii).find("-")]) not in range(1900, 2021):
            errors.append("Atentie la ziua, luna si anul introduse!")
        if str(card_client.data_nasterii)[
           str(card_client.data_nasterii).find("-") + 1:str(card_client.data_nasterii).rfind("-")] not in ["00", "01",
                                                                                                           "02",
                                                                                                           "03",
                                                                                                           "04", "05",
                                                                                                           "06",
                                                                                                           "07",
                                                                                                           "08", "09",
                                                                                                           "10",
                                                                                                           "11",
                                                                                                           "12"]:
            errors.append("Atentie la ziua, luna si anul introduse!")
        if str(card_client.data_nasterii)[8] == '0' and str(card_client.data_nasterii)[9] == '0':
            errors.append("Atentie la ziua, luna si anul introduse!")
        if str(card_client.data_nasterii)[8] == '3' and int(str(card_client.data_nasterii)[9]) > 1:
            errors.append("Atentie la ziua, luna si anul introduse!")

        ok = 1
        for character in str(card_client.data_inregistrarii):
            if character not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]:
                ok = 0
        if ok == 0:
            raise ValueError("Atentie la introducerea datei!")
        if str(card_client.data_inregistrarii).count("-") != 2 or len(str(card_client.data_inregistrarii)) != 10:
            errors.append("Data tranzactiei trebuie sa fie de forma [yyyy-mm-dd]!")
        if int(str(card_client.data_inregistrarii)[8]) not in range(4) or int(
                str(card_client.data_inregistrarii)[9]) not in range(10):
            errors.append("Atentie la ziua, luna si anul introduse!")
        if int(str(card_client.data_inregistrarii)[:str(card_client.data_inregistrarii).find("-")]) not in range(1900,
                                                                                                                 2021):
            errors.append("Atentie la ziua, luna si anul introduse!")
        if str(card_client.data_inregistrarii)[
           str(card_client.data_inregistrarii).find("-") + 1:str(card_client.data_inregistrarii).rfind("-")] not in [
            "00", "01",
            "02",
            "03",
            "04", "05",
            "06",
            "07",
            "08", "09",
            "10",
            "11",
            "12"]:
            errors.append("Atentie la ziua, luna si anul introduse!")
        if str(card_client.data_inregistrarii)[8] == '0' and str(card_client.data_inregistrarii)[9] == '0':
            errors.append("Atentie la ziua, luna si anul introduse!")
        if str(card_client.data_inregistrarii)[8] == '3' and int(str(card_client.data_inregistrarii)[9]) > 1:
            errors.append("Atentie la ziua, luna si anul introduse!")

        if len(card_client.CNP) != 13:
            errors.append("CNP_ul are 13 cifre! Rescrieti-l!")
        for i in card_client.CNP:
            if int(i) not in range(10):
                errors.append("Introduceti un CNP valid!")

        if len(errors) > 0:
            raise ValueError(errors)
