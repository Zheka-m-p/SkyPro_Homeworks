# 1
def back_null_in_array(array_):
    count_null = array_.count(0)
    array_ = [x for x in array_ if x != 0]
    array_.extend([0] * count_null)
    return array_


a = [1, 0, 2, 3, 0, 4]
assert back_null_in_array(a) == [1, 2, 3, 4, 0, 0]


# 2
def sum_row_odd_number(n):
    main_elem = 0
    for i in range(1, n):
        main_elem += 2 * i
    res = main_elem * n + sum(range(1, 2 * n, 2))
    return res


assert sum_row_odd_number(4) == 64
assert sum_row_odd_number(5) == 125
