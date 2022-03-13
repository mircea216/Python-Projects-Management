from Domain.entitate import Entitate
from Repository.generic_file_repository import GenericFileRepository
from Tests.utils import clear_file


def test_generic_file_repository():
    file_name = "test_repo.txt"
    clear_file(file_name)
    generic_file_repository = GenericFileRepository(file_name)
    # GET ALL ENTITIES
    assert generic_file_repository.get_all_entities() == []
    clear_file(file_name)
    entity = Entitate("1")
    # CREATE
    generic_file_repository.create_an_entity(entity)
    assert len(generic_file_repository.get_all_entities()) == 1
    try:
        entity2 = Entitate("1")
        generic_file_repository.create_an_entity(entity2)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
    # GET ENTITY BY ID
    assert generic_file_repository.get_entity_by_id("1") is not None
    assert generic_file_repository.get_entity_by_id("2") is None

    # DELETE
    assert len(generic_file_repository.get_all_entities()) == 1
    generic_file_repository.delete_an_entity("1")
    assert len(generic_file_repository.get_all_entities()) == 0
    try:
        generic_file_repository.delete_an_entity("1")
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
