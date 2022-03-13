from Domain.atac_validator import AtacValidator
from Domain.nava_spatiala_validator import NavaValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.atac_service import AtacService
from Service.nava_service import NavaService
from Tests.run_all_tests import run_all_tests
from UserInterface.console import Console


def main():
    run_all_tests()
    spaceship_repository = GenericFileRepository("spaceship.txt")
    spaceship_validator = NavaValidator()
    spaceship_service = NavaService(spaceship_repository, spaceship_validator)

    attack_validator = AtacValidator()
    attack_repository = GenericFileRepository("attack.txt")
    attack_service = AtacService(attack_repository, attack_validator, spaceship_repository)
    user_interface = Console(spaceship_service, attack_service)
    user_interface.run_console()

main()
