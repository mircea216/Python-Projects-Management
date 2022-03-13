from Domain.card_client import CardClient


def test_card_client_domain():

    client_card = CardClient("12", "Smith", "John", "1234567891123", "12.03.2001", "13.04.2009")
    assert client_card.id_entitate == "12"
    assert client_card.nume == "Smith"
    assert client_card.prenume == "John"
    assert client_card.CNP == "1234567891123"
    assert client_card.data_nasterii == "12.03.2001"
    assert client_card.data_inregistrarii == "13.04.2009"
