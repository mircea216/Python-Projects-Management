from Domain.medicament import Medicament
from Repository.generic_file_repository import GenericFileRepository
from Tests.test_utils import clear_file


def test_repo_create_med():
    clear_file("test_meds.txt")
    med_repository = GenericFileRepository("test_meds.txt")
    med1 = Medicament("12", "Paracetamol", "Farma +", 100, "da")
    med_repository.create_an_entity(med1)
    assert len(med_repository.get_all_entities()) == 1
    added_med = med_repository.get_entity_by_id("12")
    assert added_med.id_entitate == "12"
    assert added_med.nume == "Paracetamol"
    assert added_med.producator == "Farma +"
    assert added_med.pret == 100
    assert added_med.reteta == "da"
    try:
        med2 = Medicament("12", "Furazolidon", "Farmec", 50, "da")
        med_repository.create_an_entity(med2)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_repo_delete_med():
    clear_file("test_meds.txt")
    med_repository = GenericFileRepository("test_meds.txt")
    med1 = Medicament("12", "Paracetamol", "Farma +", 100, "da")
    med2 = Medicament("14", "Furazolidon", "Farmec", 50, "nu")
    med_repository.create_an_entity(med1)
    med_repository.create_an_entity(med2)
    assert len(med_repository.get_all_entities()) == 2
    med_repository.delete_an_entity("14")
    assert len(med_repository.get_all_entities()) == 1
    try:
        med_repository.delete_an_entity("15")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False


def test_repo_update_med():
    clear_file("test_meds.txt")
    med_repository = GenericFileRepository("test_meds.txt")
    med1 = Medicament("12", "Paracetamol", "Farma +", 100, "da")
    med2 = Medicament("12", "Furazolidon", "Farmec", 50, "nu")
    med_repository.create_an_entity(med1)
    med_repository.update_an_entity(med2)
    updated_med = med_repository.get_entity_by_id("12")
    assert updated_med.id_entitate == "12"
    assert updated_med.nume == "Furazolidon"
    assert updated_med.producator == "Farmec"
    assert updated_med.pret == 50
    assert updated_med.reteta == "nu"
    try:
        med3 = Medicament("17", "Panadol", "Farma", 12, "da")
        med_repository.update_an_entity(med3)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
    assert len(med_repository.get_all_entities()) == 1
