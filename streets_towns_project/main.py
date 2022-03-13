from Domain.oras_validator import OrasValidator
from Domain.strada_validator import StradaValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.oras_service import OrasService
from Service.strada_service import StradaService
from UserInterface.Console import Console


def main():
    town_validator = OrasValidator()
    orase_repository = GenericFileRepository("orase.txt")
    orase_service = OrasService(orase_repository, town_validator)
    street_validator = StradaValidator()
    strazi_repository = GenericFileRepository("strazi.txt")
    strazi_service = StradaService(orase_repository, strazi_repository, street_validator)
    console = Console(orase_service, strazi_service)
    console.run_menu()


main()
