from Domain.medicament_validator import MedicamentValidator
from Repository.generic_file_repository import GenericFileRepository
from Service.medicament_service import MedicamentService
from Tests.test_utils import clear_file


def test_create_med():
    med_validator = MedicamentValidator()
    clear_file("test_meds.txt")
    med_repository = GenericFileRepository("test_meds.txt")
    med_service = MedicamentService(med_validator, med_repository)
    med_service.create_med("12", "Paracetamol", "Farma +", 100, "da")
    assert len(med_service.get_all_meds()) == 1
    added_med = med_repository.get_entity_by_id("12")
    assert added_med.id_entitate == "12"
    assert added_med.nume == "Paracetamol"
    assert added_med.producator == "Farma +"
    assert added_med.pret == 100
    assert added_med.reteta == "da"
    try:
        med_service.create_med("12", "Furazolidon", "Farmec", 50, "da")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_delete_med():
    med_validator = MedicamentValidator()
    clear_file("test_meds.txt")
    med_repository = GenericFileRepository("test_meds.txt")
    med_service = MedicamentService(med_validator, med_repository)
    med_service.create_med("12", "Paracetamol", "Farma +", 100, "da")
    med_service.create_med("14", "Furazolidon", "Farmec", 50, "nu")
    med_service.delete_med("14")
    assert len(med_service.get_all_meds()) == 1
    try:
        med_service.delete_med("15")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_update_med():
    med_validator = MedicamentValidator()
    clear_file("test_meds.txt")
    med_repository = GenericFileRepository("test_meds.txt")
    med_service = MedicamentService(med_validator, med_repository)
    med_service.create_med("12", "Paracetamol", "Farma +", 100, "da")
    med_service.create_med("14", "Furazolidon", "Farmec", 50, "nu")
    med_service.update_med("14", "Panadol", "Plafar", 20, "da")
    updated_med = med_repository.get_entity_by_id("14")
    assert updated_med.id_entitate == "14"
    assert updated_med.nume == "Panadol"
    assert updated_med.producator == "Plafar"
    assert updated_med.pret == 20
    assert updated_med.reteta == "da"
    med_service.update_med("12", "", "", 0, "")
    unchanged_med = med_repository.get_entity_by_id("12")
    assert unchanged_med.id_entitate == "12"
    assert unchanged_med.nume == "Paracetamol"
    assert unchanged_med.producator == "Farma +"
    assert unchanged_med.pret == 100
    assert unchanged_med.reteta == "da"
    try:
        med_service.update_med("17", "", "", 0, "")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
    assert len(med_service.get_all_meds()) == 2
