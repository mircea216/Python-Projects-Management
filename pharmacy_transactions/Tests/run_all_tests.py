from Tests.test_card_client_domain import test_card_client_domain
from Tests.test_card_client_repository import test_repo_update_client_card, test_repo_delete_client_card, \
    test_repo_create_client_card
from Tests.test_card_client_service import test_update_client_card, test_delete_client_card, test_create_client_card
from Tests.test_medicament_domain import test_medicament_domain
from Tests.test_medicament_repository import test_repo_create_med, test_repo_delete_med, test_repo_update_med
from Tests.test_medicament_service import test_create_med, test_delete_med, test_update_med
from Tests.test_tranzactie_domain import test_tranzactie_domain
from Tests.test_tranzactie_repository import test_repo_create_transaction, test_repo_delete_transaction, \
    test_repo_update_transaction
from Tests.test_tranzactie_service import test_create_transaction


def run_all_test():
    # MED

    # domain
    test_medicament_domain()

    # repository
    test_repo_create_med()
    test_repo_delete_med()
    test_repo_update_med()

    # service
    test_create_med()
    test_delete_med()
    test_update_med()

    # CLIENT_CARD

    # domain
    test_card_client_domain()

    # repository
    test_repo_create_client_card()
    test_repo_delete_client_card()
    test_repo_update_client_card()

    # service
    test_create_client_card()
    test_delete_client_card()
    test_update_client_card()

    # TRANSACTION

    # domain
    test_tranzactie_domain()

    # repository
    test_repo_create_transaction()
    test_repo_delete_transaction()
    test_repo_update_transaction()

