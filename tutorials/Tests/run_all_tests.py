from Tests.test_elev_service import test_create_a_student
from Tests.test_generic_file_repository import test_generic_file_repository
from Tests.test_sedinta_service import test_create_a_tutorial, \
    test_print_students_with_a_number_of_tutorials_greater_than_a_given_number, test_delete_student_and_tutorials


def run_all_tests():
    # Repository
    test_generic_file_repository()

    # Service
    test_create_a_student()
    test_create_a_tutorial()
    test_print_students_with_a_number_of_tutorials_greater_than_a_given_number()
    test_delete_student_and_tutorials()
