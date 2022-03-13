from Domain.card_client import CardClient
from Repository.generic_file_repository import GenericFileRepository
from Tests.test_utils import clear_file


def test_repo_create_client_card():
    clear_file("test_client_cards.txt")
    client_card_repository = GenericFileRepository("test_client_cards.txt")
    client_card = CardClient("12", "Smith", "John", "1234567891123", "12.03.2001", "13.04.2009")
    client_card_repository.create_an_entity(client_card)
    assert len(client_card_repository.get_all_entities()) == 1
    added = client_card_repository.get_entity_by_id("12")
    assert added.id_entitate == "12"
    assert added.nume == "Smith"
    assert added.prenume == "John"
    assert added.CNP == "1234567891123"
    assert added.data_nasterii == "12.03.2001"
    assert added.data_inregistrarii == "13.04.2009"
    try:
        client_card = CardClient("12", "Rose", "Daisy", "1234567891123", "12.03.2001", "13.04.2009")
        client_card_repository.create_an_entity(client_card)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_repo_delete_client_card():
    clear_file("test_client_cards.txt")
    client_card_repository = GenericFileRepository("test_client_cards.txt")
    client_card1 = CardClient("12", "Smith", "John", "1234567891123", "12.03.2001", "13.04.2009")
    client_card2 = CardClient("13", "Rose", "Daisy", "1234567801153", "22.03.2002", "14.05.2009")
    client_card_repository.create_an_entity(client_card1)
    client_card_repository.create_an_entity(client_card2)
    assert len(client_card_repository.get_all_entities()) == 2
    client_card_repository.delete_an_entity("12")
    assert len(client_card_repository.get_all_entities()) == 1
    try:
        client_card_repository.delete_an_entity("12")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_repo_update_client_card():
    clear_file("test_client_cards.txt")
    client_card_repository = GenericFileRepository("test_client_cards.txt")
    client_card1 = CardClient("12", "Smith", "John", "1234567891123", "12.03.2001", "13.04.2009")
    client_card2 = CardClient("12", "Rose", "Daisy", "1234567801153", "22.03.2002", "14.05.2009")
    client_card_repository.create_an_entity(client_card2)
    client_card_repository.update_an_entity(client_card1)
    updated = client_card_repository.get_entity_by_id("12")
    assert updated.id_entitate == "12"
    assert updated.nume == "Smith"
    assert updated.prenume == "John"
    assert updated.CNP == "1234567891123"
    assert updated.data_nasterii == "12.03.2001"
    assert updated.data_inregistrarii == "13.04.2009"

    try:
        client_card3 = CardClient("25", "Thomsan", "Ann", "1234567801183", "22.03.2002", "14.05.2009")
        client_card_repository.update_an_entity(client_card3)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
