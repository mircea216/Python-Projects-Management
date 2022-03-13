def clear_file(file_name):
    '''
    functie de golire a fisierelor din teste
    :param file_name: numele fisierului de test
    '''
    with open(file_name, 'w') as fp:
        pass
