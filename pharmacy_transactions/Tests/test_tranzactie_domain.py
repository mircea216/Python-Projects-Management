from Domain.tranzactie import Tranzactie


def test_tranzactie_domain():
    transaction = Tranzactie("1", "1", "1", 2, "12.03.2012", "15:03")
    assert transaction.id_entitate == "1"
    assert transaction.id_medicament == "1"
    assert transaction.id_client == "1"
    assert transaction.numar_bucati == 2
    assert transaction.data == "12.03.2012"
    assert transaction.ora == "15:03"

