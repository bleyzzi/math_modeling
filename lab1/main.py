import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')


class MclarenMars:
    def __init__(self, k, b, c, n):
        self.k, self.b, self.c, self.n = k, b, c, n
        self.bsv = [0 for _ in range(n)]
        self.v = [0 for _ in range(k)]

    def mclaren_mars_method(self):
        for i in range(self.k):
            self.v[i] = self.b[i]
        for i in range(self.n):
            s = int(self.c[i] * self.k)
            self.bsv[i] = self.v[s]
            if i + self.k < self.n:
                self.v[s] = self.b[i + self.k]
        return self.bsv


class MultiplicativeCongruentialMethod:
    def __init__(self, n, m, alpha, betta):
        self.n = n
        self.alpha = [0 for _ in range(n + 1)]
        self.alpha[0] = alpha
        self.betta = max(betta, m - betta)
        self.bsv = [0 for _ in range(n)]
        self.m = m

    def mcm(self):
        for i in range(1, self.n + 1):
            temp = (self.betta * self.alpha[i - 1])
            self.alpha[i] = temp % self.m
            self.bsv[i - 1] = self.alpha[i] / self.m
        return self.bsv


if __name__ == "__main__":
    bsv1 = MultiplicativeCongruentialMethod(1000, 2 ** 31, 18154591, 432144333).mcm()
    print(f'Тысячный элемент первой последовательности: {bsv1[999]}')
    print(f'Проверка сходимости/n Ожидаемый первый элемент: {0.251522}. Полученный первый элемент {bsv1[0]}')
    print(f'Ожидаемый пятнадцатый элемент: {0.994069}. Полученный пятнадцатый элемент {bsv1[14]}')
    print('\n')
    bsv2 = MultiplicativeCongruentialMethod(1000, 2 ** 31, 95831023, 122596613).mcm()
    plt.hist(bsv1, edgecolor='black', bins=10)
    plt.title("Histogram for 1000 elements")
    plt.xlabel("Values")
    plt.ylabel("Frequencies")
    plt.savefig('my_plot_bsv1.png')
    plt.clf()
    bsv3 = MclarenMars(96, bsv1, bsv2, 1000).mclaren_mars_method()
    print(f'Тысячный элемент последовательности МакЛарена-Марсальи: {bsv3[999]}')
    print(f'Проверка сходимости/n Ожидаемый первый элемент: {0.029776}. Полученный первый элемент {bsv3[0]}')
    print(f'Ожидаемый пятнадцатый элемент: {0.347685}. Полученный пятнадцатый элемент {bsv3[14]}')
    plt.hist(bsv3, edgecolor='black', bins=10)
    plt.title("Histogram for 1000 elements")
    plt.xlabel("Values")
    plt.ylabel("Frequencies")
    plt.savefig('my_plot_bsv2.png')
