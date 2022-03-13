from Domain.card_client import CardClient
from Domain.medicament import Medicament
from Domain.tranzactie_validator import TranzactieValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.tranzactie_service import TranzactieService
from Tests.test_utils import clear_file


def test_create_transaction():
    clear_file("test_transactions.txt")
    transaction_repository = GenericFileRepository("test_transactions.txt")

    clear_file("test_meds.txt")
    med_repository = GenericFileRepository("test_meds.txt")

    clear_file("test_client_cards.txt")
    client_card_repository = GenericFileRepository("test_client_cards.txt")

    transaction_validator = TranzactieValidator()
    transaction_service = TranzactieService(transaction_validator, transaction_repository, med_repository,
                                            client_card_repository)

    med1 = Medicament("4", "Paracetamol", "Farma +", 100, "da")
    client_card = CardClient("1", "Smith", "John", "1237567891123", "2001-03-12", "2009-10-12")

    med_repository.create_an_entity(med1)
    client_card_repository.create_an_entity(client_card)

    transaction_service.create_transaction("3", "4", "1", 2, "2012-01-03", "15:03")

    assert len(transaction_service.get_all_transactions()) == 1
    added = transaction_repository.get_entity_by_id("3")
    assert added.id_entitate == "3"
    assert added.id_medicament == "1"
    assert added.id_client == "1"
    assert added.numar_bucati == 2
    assert added.data == "2012-01-03"
    assert added.ora == "15:03"
    try:
        transaction_service.create_transaction("1", "1", "1", 34, "2012-03-12", "15:53")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

