from Domain.card_client_validator import CardClientValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.card_client_service import CardClientService
from Tests.test_utils import clear_file


def test_create_client_card():
    clear_file("test_client_cards.txt")
    client_card_repository = GenericFileRepository("test_client_cards.txt")
    client_card_validator = CardClientValidator()
    client_card_service = CardClientService(client_card_validator, client_card_repository)
    client_card_service.create_client_card("12", "Smith", "John", "1234567891123", "2001-03-19", "2009-10-20")
    assert len(client_card_service.get_all_client_cards()) == 1
    added = client_card_repository.get_entity_by_id("12")
    assert added.id_entitate == "12"
    assert added.nume == "Smith"
    assert added.prenume == "John"
    assert added.CNP == "1234567891123"
    assert added.data_nasterii == "2001-03-19"
    assert added.data_inregistrarii == "2009-10-20"
    try:
        client_card_service.create_client_card("12", "Smithish", "Johnny", "1234367891123", "2001-03-19", "2009-10-20")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_delete_client_card():
    clear_file("test_client_cards.txt")
    client_card_repository = GenericFileRepository("test_client_cards.txt")
    client_card_validator = CardClientValidator()
    client_card_service = CardClientService(client_card_validator, client_card_repository)
    client_card_service.create_client_card("12", "Smith", "John", "1234567891123", "2001-03-01", "2009-04-13")
    client_card_service.create_client_card("13", "Smithish", "Johnny", "1234367891123", "2001-03-01", "2009-04-13")

    client_card_service.delete_client_card("13")
    assert len(client_card_service.get_all_client_cards()) == 1
    try:
        client_card_service.delete_client_card("15")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_update_client_card():
    clear_file("test_client_cards.txt")
    client_card_repository = GenericFileRepository("test_client_cards.txt")
    client_card_validator = CardClientValidator()
    client_card_service = CardClientService(client_card_validator, client_card_repository)
    client_card_service.create_client_card("12", "Smith", "John", "1234567891123", "2001-03-01", "2009-04-13")
    client_card_service.create_client_card("13", "Smithish", "Johnny", "1234367891123", "2001-03-01", "2009-04-13")
    client_card_service.create_client_card("14", "Gregory", "Ann", "1234387991173", "2001-03-01", "2009-04-13")
    client_card_service.update_client_card("14", "A", "B", "1234387891173", "2001-03-01", "2009-04-13")
    updated_card = client_card_repository.get_entity_by_id("14")
    assert updated_card.id_entitate == "14"
    assert updated_card.nume == "A"
    assert updated_card.prenume == "B"
    assert updated_card.CNP == "1234387891173"
    assert updated_card.data_nasterii == "2001-03-01"
    assert updated_card.data_inregistrarii == "2009-04-13"
    try:
        client_card_service.update_client_card("17", "A", "B", "1238387891173", "2009-04-13", "2019-04-13")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
