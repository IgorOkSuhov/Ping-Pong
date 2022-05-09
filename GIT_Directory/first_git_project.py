# это просто тренировка в пользовании Гитом на примере моей последней задачи
from itertools import takewhile
import itertools
from math import sqrt
def iterator():
    #Простое число - это число имеющее ровно два различных натуральных делителя
    n = int(input('Напишите последовательность итераций простого числа'))
    lst = []
    for i in range(2, n+1):
        if (i > 10):
            if (i%2==0) or (i%10==5):
                continue
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    print(lst)
a = iterator()


console_log = 'Test2'

