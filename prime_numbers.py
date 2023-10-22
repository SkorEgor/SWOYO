from math import sqrt
import numpy as np


def prime_numbers(low, high):
    """Returns prime numbers in a range [low, high]

    :type low: int
    :type high: int

    :rtype: list[int]
    :return: prime numbers in a range

    If the range contains no prime numbers -> []
    """
    # (I) ПРОВЕРКИ ВВЕДЕНЫХ ПАРАМЕТРОВ
    # 1. Границы это целые числа - иначе возврат []
    if not (isinstance(low, int) and isinstance(high, int)):
        return []
    # 2. Не корректность границ
    # А. Нижняя и верхняя граница перепутаны - возврат [] | (альтернативное решение low, high = high,low)
    # Б. Верхняя граница < диапазона простых чисел
    if high < low or high < 2:
        return []
    # В. Приведение нижней границы к ближайшему простому числу, если она за диапазоном (для ускорения)
    if low < 0:
        low = 0

    # (II) Логический массив всех чисел от 0 до high
    # True - индекс элемента это простое число; False - не простое
    # вначале все значения True
    prime = np.ones(high + 1, dtype=bool)
    prime[0] = False
    prime[1] = False

    # (III) ОТСЕИВАНИЕ ЧИСЕЛ - АЛГОРИТМ: Решето Эратосфена.
    # Перебираем индексы
    # Из описания алгоритма: остановка при p^2 станет больше, чем n-> p>n^0.5
    for p in range(2, int(sqrt(high)) + 1):
        # Если число еще не зачеркнуто
        if prime[p]:
            # То зачеркиваем от этого числа с шагом этого числа
            # начинаем с p^2, потому что все меньшие числа, кратные p, уже зачеркнуты
            # и само число p нужно оставить
            prime[p * p::p] = False

    # (IV) Возврат чисел, в диапазоне с типом данных list
    return (np.arange(low, high + 1, dtype=int)[prime[low:]]).tolist()
