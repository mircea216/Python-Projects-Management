from Domain.medicament import Medicament


def test_medicament_domain():

    medicament = Medicament("12", "Paracetamol", "Farma", 120, "da")
    assert medicament.id_entitate == "12"
    assert medicament.nume == "Paracetamol"
    assert medicament.producator == "Farma"
    assert medicament.pret == 120
    assert medicament.reteta == "da"

