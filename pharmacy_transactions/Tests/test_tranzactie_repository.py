from Domain.tranzactie import Tranzactie
from Repository.generic_file_repository import GenericFileRepository
from Tests.test_utils import clear_file


def test_repo_create_transaction():
    clear_file("test_transactions.txt")
    transaction_repository = GenericFileRepository("test_transactions.txt")
    transaction = Tranzactie("1", "1", "1", 2, "2020-01-02", "15:03")
    transaction_repository.create_an_entity(transaction)
    assert len(transaction_repository.get_all_entities()) == 1
    added = transaction_repository.get_entity_by_id("1")
    assert added.id_entitate == "1"
    assert added.id_medicament == "1"
    assert added.id_client == "1"
    assert added.numar_bucati == 2
    assert added.data == "2020-01-02"
    assert added.ora == "15:03"
    try:
        transaction1 = Tranzactie("1", "1", "1", 34, "2020-01-02", "15:53")
        transaction_repository.create_an_entity(transaction1)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_repo_delete_transaction():
    clear_file("test_transactions.txt")
    transaction_repository = GenericFileRepository("test_transactions.txt")
    transaction1 = Tranzactie("1", "1", "1", 2, "2020-01-02", "15:03")
    transaction2 = Tranzactie("2", "1", "1", 2, "2020-01-02", "15:03")
    transaction_repository.create_an_entity(transaction1)
    transaction_repository.create_an_entity(transaction2)
    assert len(transaction_repository.get_all_entities()) == 2
    transaction_repository.delete_an_entity("1")
    assert len(transaction_repository.get_all_entities()) == 1
    try:
        transaction_repository.delete_an_entity("5")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_repo_update_transaction():
    clear_file("test_transactions.txt")
    transaction_repository = GenericFileRepository("test_transactions.txt")
    transaction1 = Tranzactie("1", "1", "1", 2, "2020-01-02", "15:03")
    transaction2 = Tranzactie("1", "1", "1", 25, "2020-01-02", "15:03")
    transaction_repository.create_an_entity(transaction1)
    transaction_repository.update_an_entity(transaction2)
    updated = transaction_repository.get_entity_by_id("1")
    assert updated.id_entitate == "1"
    assert updated.id_medicament == "1"
    assert updated.id_client == "1"
    assert updated.numar_bucati == 25
    assert updated.data == "2020-01-02"
    assert updated.ora == "15:03"

    try:
        transaction3 = Tranzactie("111", "1", "1", 2, "2020-01-02", "15:03")
        transaction_repository.update_an_entity(transaction3)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
