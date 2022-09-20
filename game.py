"""Игра угадай число"""

def binsearch(x: int,low=1,high=100) -> int:
    """Количество попыток для нахождения числа

    Args:
        x (int): Число для опредения.
        low (int, optional): Минимальное значение диапазона поиска. Defaults to 1.
        high (int, optional): Максимальное значение диапазона поиска. Defaults to 100.

    Returns:
        int: Количество попыток, требующихся, чтобы подобрать число, равное исходному.
    """
    mid = (low + high)//2
    count = 0 #исходное число попыток
    while x != mid:
        if x > mid:
            low = mid
        else:
            high = mid
        mid = (low + high)//2
        count += 1
    return count

import numpy as np
random_array = np.random.randint(1, 101, size=(100)) # загадываем список чисел

summa=0

for i in random_array:
    summa+=binsearch(i)
print(summa/100)

