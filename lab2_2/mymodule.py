import random
from math import pi, ceil

"""Модуль для генерации случайных чисел для лабораторной работы"""

def generate_random_1():
    return random.randrange(-82, -51, 2)

def generate_random_2():
    return ceil(random.random() * random.randint(-93, -44))
