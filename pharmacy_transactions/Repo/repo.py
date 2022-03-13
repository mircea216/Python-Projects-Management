from Repository.generic_file_repository import GenericFileRepository


class NewRepoEx:
    def __init__(self, med_repo: GenericFileRepository):
        '''
        constructorul retine storage-ul de medicamente
        :param med_repo: storage de medicamente de tip GenericFileRepository
        '''
        self.__med_repo = med_repo

    def write_file(self):
        '''
        scrie intr-un fisier excel toate medicamentele
        '''
        import xlsxwriter
        l = []
        new_list = self.__med_repo.get_all_entities()
        for i in new_list:
            l.append([i.id_entitate, i.nume, i.producator, i.pret, i.reteta])

        with xlsxwriter.Workbook('test2.xlsx') as workbook:
            worksheet = workbook.add_worksheet()
            for row_num, data in enumerate(l):
                worksheet.write_row(row_num, 0, data)

