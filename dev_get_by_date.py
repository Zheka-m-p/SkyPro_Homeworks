def get_by_date(date="2017-08-08", dataset_name='all_stocks_5yr.csv', name="PCLN", filename='new_dump.csv'):
    """Функция добавляет данные в файл по указанной дате и тикеру компании, файл можно выбрать самим."""
    with open(dataset_name, 'r') as file_, open(filename, 'w') as writer_object:
        first_string = '  '.join([i.ljust(13) for i in (file_.readline().strip().split(','))])
        res = (i.strip().split(',') for i in file_ if
               i.strip().split(',')[-1] == name and i.strip().split(',')[0] == date)  # генераторное выражение
        for i in res:
            print(first_string, file=writer_object)
            print('  '.join([k.ljust(13) for k in i]), file=writer_object)


get_by_date(date="2017-08-08", name="PCLN", filename='new_dump.csv')
