from Repository.generic_file_repository import GenericFileRepository


class UndoRedoOperation:

    def __init__(self, repository: GenericFileRepository):
        self._repository = repository

    def undo(self):
        raise NotImplemented('Should use a derived class!')

    def redo(self):
        raise NotImplemented('Should use a derived class!')
