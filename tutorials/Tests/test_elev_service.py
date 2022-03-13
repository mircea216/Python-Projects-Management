from Domain.elev_validator import ElevValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.elev_service import ElevService
from Tests.tests_utils import clear_file


def test_create_a_student():
    clear_file("test_students.txt")
    student_validator = ElevValidator()
    student_repository = GenericFileRepository("test_students.txt")
    student_service = ElevService(student_repository, student_validator)
    student_service.create_a_student("1", "A", 12)
    assert len(student_service.get_all_students()) == 1
    assert student_repository.get_entity_by_id("1").nume == "A"
    assert student_repository.get_entity_by_id("1").varsta == 12
    student_service.create_a_student("2", "A", 10)
    student_service.create_a_student("3", "A", 13)
    assert len(student_service.get_all_students()) == 3

