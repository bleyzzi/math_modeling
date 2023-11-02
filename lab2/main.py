import numpy as np
"""
9)Бернулли –Bi(1,p), p = 0.3;Обратное биномиальное –Bi (r,m), r = 6, p = 0.25.
10)Геометрическое – G(p), p = 0.2;Биномиальное – Bi(m,p), m = 5, p = 0.6.
"""


# Распределение Бернулли
def bernulli_distribution(p, n=1000):
    dsv = np.random.rand(n)
    return np.where(dsv < p, 1, 0)


# Обратное биномиальное распределение
def inverse_binomial_distribution(r, p, n=1000):
    lst = []
    for _ in range(n):
        cnt, success = 0, 0
        while success < r:
            if bernulli_distribution(p, 1)[0] == 1:
                success += 1
            cnt += 1
            lst.append(cnt)
    return np.array(lst)


# Геометрическое распределение
def geometric_distribution(p, n=1000):
    lst = []
    for _ in range(n):
        cnt = 0
        while bernulli_distribution(p, 1)[0] == 0:
            cnt += 1
        lst.append(cnt)
    return np.array(lst)


# Биномиальное распределение
def binomial_distribution(m, p, n=1000):
    return np.array([sum(bernulli_distribution(p, m)) for _ in range(n)])


# Матожидание
def math_expectation(array):
    return np.sum(array)/len(array)


# Дисперсия
def dispersion(array):
    return math_expectation(array ** 2) - math_expectation(array) ** 2


if __name__ == '__main__':
    p = 0.3
    bsv = bernulli_distribution(p)
    print('\nРаспределение Бернулли')
    print('Истинное матожидание ', p)
    print('Матожидание ', math_expectation(bsv))
    print('Истинная дисперсия ', p * (1 - p))
    print('Дисперсия ', dispersion(bsv))

    r = 6
    p = 0.25
    bsv = inverse_binomial_distribution(r, p)
    print('\nОбратное биномиальное')
    print('Истинное матожидание ', r / p)
    print('Матожидание ', math_expectation(bsv))
    print('Истинная дисперсия ', (r * (1 - p)) / p ** 2)
    print('Дисперсия ', dispersion(bsv))

    p = 0.2
    bsv = geometric_distribution(p)
    print('\nГеометрическое распределение')
    print('Истинное матожидание ', 1 / p)
    print('Матожидание ', math_expectation(bsv))
    print('Истинная дисперсия ', (1 - p) / p ** 2)
    print('Дисперсия ', dispersion(bsv))

    p = 0.6
    m = 5
    bsv = binomial_distribution(m, p)
    print('\nБиномиальное распределение')
    print('Истинное матожидание ', m * p)
    print('Матожидание ', math_expectation(bsv))
    print('Истинная дисперсия ', m * p * (1 - p))
    print('Дисперсия ', dispersion(bsv))
