from Domain.sedinta_validator import SedintaValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.sedinta_service import SedintaService
from Tests.tests_utils import clear_file


def test_create_a_tutorial():
    clear_file("test_tutorials.txt")
    student_repository = GenericFileRepository("test_students.txt")
    tutorial_validator = SedintaValidator()
    tutorial_repository = GenericFileRepository("test_tutorials.txt")
    tutorial_service = SedintaService(tutorial_repository, tutorial_validator, student_repository)
    tutorial_service.create_a_tutorial("1", "1", "Mihnea")
    assert len(tutorial_service.get_all_tutorials()) == 1


def test_print_students_with_a_number_of_tutorials_greater_than_a_given_number():
    clear_file("test_tutorials.txt")
    student_repository = GenericFileRepository("test_students.txt")
    tutorial_validator = SedintaValidator()
    tutorial_repository = GenericFileRepository("test_tutorials.txt")
    tutorial_service = SedintaService(tutorial_repository, tutorial_validator, student_repository)
    tutorial_service.create_a_tutorial("1", "1", "Mihnea")
    tutorial_service.create_a_tutorial("2", "1", "Mihnea")
    tutorial_service.create_a_tutorial("3", "1", "Mihnea")
    assert len(tutorial_service.print_students_with_a_number_of_tutorials_greater_than_a_given_number(2)) == 1


def test_delete_student_and_tutorials():
    clear_file("test_tutorials.txt")
    student_repository = GenericFileRepository("test_students.txt")
    tutorial_validator = SedintaValidator()
    tutorial_repository = GenericFileRepository("test_tutorials.txt")
    tutorial_service = SedintaService(tutorial_repository, tutorial_validator, student_repository)
    tutorial_service.create_a_tutorial("1", "1", "Mihnea")
    tutorial_service.create_a_tutorial("2", "1", "Mihnea")
    tutorial_service.create_a_tutorial("3", "1", "Mihnea")
    tutorial_service.delete_student_and_tutorials("1")
    assert len(tutorial_repository.get_all_entities()) == 0
    assert len(student_repository.get_all_entities()) == 2