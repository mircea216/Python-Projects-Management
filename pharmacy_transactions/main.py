from Domain.card_client_validator import CardClientValidator
from Domain.medicament_validator import MedicamentValidator
from Domain.tranzactie_validator import TranzactieValidator
from Repo.repo import NewRepoEx
from Repository.generic_file_repository import GenericFileRepository
from Service.card_client_service import CardClientService
from Service.medicament_service import MedicamentService
from Service.tranzactie_service import TranzactieService
from Service.undo_redo_service import UndoRedoService
from UserInterface.Console import Console


def main():
    # COMMON REPO
    transaction_repository = GenericFileRepository("transactions.txt")

    # MED

    med_validator = MedicamentValidator()
    med_repository = GenericFileRepository("meds.txt")
    undo_redo_service = UndoRedoService()
    med_service = MedicamentService(med_validator, med_repository, undo_redo_service, transaction_repository)

    # CLIENT CARD

    client_card_validator = CardClientValidator()
    client_card_repository = GenericFileRepository("client_cards.txt")
    client_card_service = CardClientService(client_card_validator, client_card_repository, undo_redo_service,
                                            transaction_repository)

    # TRANSACTION

    transaction_validator = TranzactieValidator()
    transaction_service = TranzactieService(transaction_validator, med_repository, client_card_repository,
                                            transaction_repository, undo_redo_service)
    excel_storage = NewRepoEx(med_repository)
    user_interface = Console(med_service, client_card_service, transaction_service, undo_redo_service, excel_storage)

    user_interface.run_console()


main()
