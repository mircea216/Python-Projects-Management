from Domain.elev_validator import ElevValidator
from Domain.sedinta_validator import SedintaValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.elev_service import ElevService
from Service.sedinta_service import SedintaService
from Tests.run_all_tests import run_all_tests
from UserInterface.console import Console


def main():
    run_all_tests()

    student_validator = ElevValidator()
    student_repository = GenericFileRepository("students.txt")
    student_service = ElevService(student_repository, student_validator)

    tutorial_validator = SedintaValidator()
    tutorial_repository = GenericFileRepository("tutorials.txt")
    tutorial_service = SedintaService(tutorial_repository, tutorial_validator, student_repository)

    console = Console(student_service, tutorial_service)
    console.run_console()


main()
