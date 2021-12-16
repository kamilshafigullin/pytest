
# функция нахождения минимума
def get_min(array):
    min = array[0]
    for i in range(len(array)):
        if (array[i] < min):
            min = array[i]
    return min

# функция нахождения максимума
def get_max(array):
    max = array[0]
    for i in range(len(array)):
        if (array[i] > max):
            max = array[i]
    return max

# функция нахождения суммы
def get_sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

# функция нахождения произведения
def get_mult(array):
    p = 1
    for i in range(len(array)):
        p *= array[i]
    return p

# функция нахождения затраченного времени
def get_time(start_time):
    return time.time() - start_time

# функция нахождения количества чётных чисел (для доп. теста)
def get_evens_count(array):
    evens = 0
    for i in range(len(array)):
        if (array[i] % 2 == 0):
            evens += 1
    return evens

# тесты
assert get_min([9, 2, 59]) == 2, "Должно быть 2"

assert get_max([1, 4, 27, 3]) == 27, "Должно быть 27"

assert get_sum([1, 7, 3]) == 11, "Должно быть 11"

assert get_mult([1, 2, 2, -1]) == -4, "Должно быть -4"

assert get_evens_count([7, 6, 3, 6, 2]) == 3, "Должно быть 3"

# назначаем ограничение выполнения программы размеров в 1 минуту
# assert get_time(maxmin.start_time) < 60, "Время выполнения программы вышло за границы допустимого"