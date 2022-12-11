def select_sorted(sort_columns=["high"], limit=10, group_by_name=False, order='desc', filename='dump.csv'):
    """Сортирует файл по заданым аргументам и выводит результат в файл 'dump.csv'"""
    dict_sort_columns = {'date': 0, 'open': 1, 'high': 2, 'low': 3, 'close': 4, 'volume': 5}
    index_sort_columns = dict_sort_columns[sort_columns[0]]  # получаем индекс столбца, по которому будем сортировать
    # print(index_sort_columns)
    with open('all_stocks_5yr.csv', 'r') as file_:
        first_string = '  '.join([i.ljust(13) for i in (file_.readline().strip().split(','))])

        # считываем из файла и создаем генераторное вырежение состоящее из списков, игнорируем строки с пустыми ячейками
        # в выбранном нами столбце, по которому будет вестись сортировка
        if group_by_name:
            ans = (i.strip().split(',') for i in file_ if
                   i.strip().split(',')[-1] == group_by_name)  # генераторное выражение,если нужна группировка по имемни
        else:
            ans = (i.strip().split(',') for i in file_ if i.strip().split(',')[index_sort_columns] != '')

        # выбираем лямба-функцию для ключа сортиривки в зависимости то того, по какому столбцу будем сортировать

        # lambda_for_keys = lambda x: float(x[index_sort_columns]) if index_sort_columns in [1, 2, 3, 4, 5] else lambda x: x[index_sort_columns]
        # lambda_for_keys = lambda x: x[index_sort_columns] if index_sort_columns == 0 else (lambda x: float(x[index_sort_columns]))
        if index_sort_columns == 0:
            lambda_for_keys = lambda x: x[index_sort_columns]
        else:
            lambda_for_keys = lambda x: float(x[index_sort_columns])

        # выбираем направление сортировки, desk -  по убыванию, иначе - по возрастанию
        if order == 'desc':
            res = sorted(ans, key=lambda_for_keys, reverse=True)
        else:
            res = sorted(ans, key=lambda_for_keys)  # работае такое вариант, но проблема с пустой строкой

    with open(filename, 'w') as write_object:
        print(first_string, file=write_object)
        for i in range(limit):
            print('  '.join([k.ljust(13) for k in res[i]]), file=write_object)

select_sorted(sort_columns=['high'], order='desc', limit=10, group_by_name=False, filename='dump.csv')
# select_sorted(sort_columns=['date'], order='asc', limit=10, group_by_name='ALL', filename='dump.csv')
# select_sorted(sort_columns=['low'], order='asc', limit=30, group_by_name='PCLN', filename='dump.csv')
