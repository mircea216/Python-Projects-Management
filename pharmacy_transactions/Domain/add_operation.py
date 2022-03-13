from Domain.undo_redo_operation import UndoRedoOperation
from Repository.generic_file_repository import GenericFileRepository


class AddOperation(UndoRedoOperation):
    def __init__(self, repository: GenericFileRepository, added_object):
        super().__init__(repository)
        self.__added_object = added_object

    def undo(self):
        self._repository.delete_an_entity(self.__added_object.id_entitate)

    def redo(self):
        self._repository.create_an_entity(self.__added_object)
k

class DeleteOperation(UndoRedoOperation):
    def __init__(self, repository: GenericFileRepository, deleted_object):
        super().__init__(repository)
        self.__deleted_object = deleted_object

    def undo(self):
        self._repository.create_an_entity(self.__deleted_object)

    def redo(self):
        self._repository.delete_an_entity(self.__deleted_object.id_entitate)


class UpdateOperation(UndoRedoOperation):
    def __init__(self, repository: GenericFileRepository, updated_object, to_update_object):
        super().__init__(repository)
        self.__updated_object = updated_object
        self.__to_update_object = to_update_object

    def undo(self):
        self._repository.delete_an_entity(self.__updated_object.id_entitate)  # the new one
        self._repository.create_an_entity(self.__to_update_object)  # the old one

    def redo(self):
        self._repository.delete_an_entity(self.__to_update_object.id_entitate)  # the old one
        self._repository.create_an_entity(self.__updated_object)  # the new one

class RaisePrice(UndoRedoOperation):
    def __init__(self, repository: GenericFileRepository, stack):
        super().__init__(repository)
        self.__stack = stack

    def undo(self):
        for med in self.__stack:
            self._repository.delete_an_entity(med[1].id_entitate)
            self._repository.create_an_entity(med[0])

    def redo(self):
        for med in self.__stack:
            self._repository.delete_an_entity(med[1].id_entitate)
            self._repository.create_an_entity(med[1])
