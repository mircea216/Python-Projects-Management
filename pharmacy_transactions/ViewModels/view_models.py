from Domain.card_client import CardClient
from Domain.medicament import Medicament


class ViewModel:
    def __init__(self, id_tranzactie, medicament: Medicament, card_client: CardClient, numar_bucati, data, ora):
        self.id_tranzactie = id_tranzactie
        self.medicament = medicament
        self.card_client = card_client
        self.numar_bucati = numar_bucati
        self.data = data
        self.ora = ora

    def __str__(self):
        return f'ID_tranzactie:{self.id_tranzactie} \n-------cu medicamentul {self.medicament} \n-------si cardul de client' \
               f' {self.card_client},\n-------NUMAR BUCATI: {self.numar_bucati}, ' \
               f'DATA: {self.data}, ORA: {self.ora}'
