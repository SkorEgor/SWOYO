
1) Реализация с использованием sympy - готовой функцией списка простых чисел
```C
from sympy import sieve

def prime_numbers_sieve(low, high):
    # (I) ПРОВЕРКИ ВВЕДЕНЫХ ПАРАМЕТРОВ
    # 1. Границы это целые числа - иначе возврат []
    if not (isinstance(low, int) and isinstance(high, int)):
        return []
    # 2. Не корректность границ
    # А. Нижняя и верхняя граница перепутаны - возврат []
    # (альтернативное решение low, high = high,low)
    # Б. Верхняя граница < диапазона простых чисел
    if high < low or high < 2:
        return []

    # 3. Возврат - Список простых чисел. Конец включительно
    return list(sieve.primerange(low, high + 1))
```

---

2) Реализация без сторонних библиотек, из интернета, на срезах

```C
def prime_numbers_internet(low, high):
    # (I) ПРОВЕРКИ ВВЕДЕНЫХ ПАРАМЕТРОВ
    # 1. Границы это целые числа - иначе возврат []
    if not (isinstance(low, int) and isinstance(high, int)):
        return []
    # 2. Не корректность границ
    # А. Нижняя и верхняя граница перепутаны - возврат []
    # (альтернативное решение low, high = high,low)
    # Б. Верхняя граница < диапазона простых чисел
    if high < low or high < 2:
        return []
    # В. Приведение нижней границы к ближайшему простому числу,
    # если она за диапазоном (для ускорения)
    if low <= 2:
        low = 2

    n = high
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    prime = [True] * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if prime[i]:
            k = 3 * i + 1 | 1
            prime[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            prime[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * (
                    (n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(low, n // 3 - correction) if prime[i]]
```
---
После поиска наиболее оптимальных реализаций, я написал / обобщил программу на основе алгоритма *"Решето Эратосфена"*  
3) Моя реализация без сторонних библиотек
```C
# Функция получения простых чисел в диапазоне
# python без использования библиотек
def prime_numbers_clean(low, high):
    # (I) ПРОВЕРКИ ВВЕДЕНЫХ ПАРАМЕТРОВ
    # 1. Границы это целые числа - иначе возврат []
    if not (isinstance(low, int) and isinstance(high, int)):
        return []
    # 2. Не корректность границ
    # А. Нижняя и верхняя граница перепутаны - возврат []
    # (альтернативное решение low, high = high,low)
    # Б. Верхняя граница < диапазона простых чисел
    if high < low or high < 2:
        return []
    # В. Приведение нижней границы к ближайшему простому числу,
    # если она за диапазоном (для ускорения)
    if low <= 2:
        low = 2

    # (II) Логический массив всех чисел от 0 до high
    # True - индекс элемента это простое число; False - не простое
    # вначале все значения True
    prime = [True] * (high + 1)  # +1 - индексы с ноля, конец включительно
    # исключаем индексы 0,1 - они не простые
    prime[0] = False
    prime[1] = False

    # (III) ОТСЕИВАНИЕ ЧИСЕЛ - АЛГОРИТМ: Решето Эратосфена.
    # Перебираем индексы
    # Из описания алгоритма: остановка при p^2 станет больше, чем n-> p>n^0.5
    for p in range(2, int(high ** 0.5) + 1):
        # Если число еще не зачеркнуто
        if prime[p]:
            # То зачеркиваем от этого числа с шагом этого числа
            # начинаем с p^2, потому что все меньшие числа, кратные p, уже зачеркнуты
            # и само число p нужно оставить
            for i in range(p * p, high + 1, p):
                prime[i] = False

    # (IV) РЕЗУЛЬТА
    # Массив логический переводим в массив значений, отбрасывая индексы с false
    return [index for index in range(low, high + 1) if prime[index]]  
```
---
Для увелечения производительности переписал программу с использованием библиотек
4) Моя реализация с использованием numpy и math
```C
from math import sqrt
import numpy as np


def prime_numbers_numpy(low, high):
    # (I) ПРОВЕРКИ ВВЕДЕНЫХ ПАРАМЕТРОВ
    # 1. Границы это целые числа - иначе возврат []
    if not (isinstance(low, int) and isinstance(high, int)):
        return []
    # 2. Не корректность границ
    # А. Нижняя и верхняя граница перепутаны - возврат []
    # (альтернативное решение low, high = high,low)
    # Б. Верхняя граница < диапазона простых чисел
    if high < low or high < 2:
        return []
    # В. Приведение нижней границы к ближайшему простому числу,
    # если она за диапазоном (для ускорения)
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
    return (np.arange(low, high + 1, dtype=int)[prime[low:]]).tolist()
```
---
Для тестирования производительности написал следующий код. Постепенно увеличивая границы, перебираем функции и для каждой попытки делаем несколько вычислений. Результат с выбранным диапазоном заносим строчкой в DataFrame.

Результирующий DataFrame выводим графиком с помощью matplotlib в линейных и логарифмических осях

```C
import pandas as pd 


functions_for_test = [prime_numbers_sieve, prime_numbers_internet, prime_numbers_numpy, prime_numbers_clean]
function_names = list( map(lambda x: x.__name__.replace('prime_numbers_',''), functions_for_test))
test_data = pd.DataFrame(columns=function_names)

test_iterations = 500 # Кол-во итераций для одного диапазона значений

for limit_value in range (0, 5000,50):
    # Создаем строку теста. Ключи - названия функций; Значения - время
    test_string = pd.DataFrame(columns=function_names, index =[limit_value])
    # Перебор функций
    for functions in functions_for_test:
        start_time = time.perf_counter ()
    
        for i in range(test_iterations):
            functions(0,limit_value)
    
        end_time = time.perf_counter ()
        test_string[functions.__name__.replace('prime_numbers_','')]=end_time - start_time

    test_data = pd.concat([test_data, test_string], ignore_index=False)

test_data = test_data.rename(columns = {"numpy":"numpy_(my)", 'clean':'clean_(my)'})

import matplotlib.pyplot as plt
test_data.plot( y=test_data.columns.values.tolist())
plt.show()
test_data.plot( y=test_data.columns.values.tolist())
plt.yscale('log')
plt.xscale('log')
plt.show()

```
<div align="center">
<!--- Графики производительности - -->
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/SWOYO/range_from0_to5000_repetitions500_linear.png"  width=350>
<img src="https://raw.githubusercontent.com/SkorEgor/picturesgifs-for-readme/RobotControl/SWOYO/range_from0_to5000_repetitions500_logarithmic.png" width=350>
</div>

