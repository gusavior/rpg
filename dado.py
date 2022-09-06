import random


def d20():
    r = []
    x = int(input('Quantas vezes deseja rolar os dados? '))
    for i in range(x):
        r.append(random.randint(1, 20))
    return r


def d12():
    r = []
    x = int(input('Quantas vezes deseja rolar os dados? '))
    for i in range(x):
        r.append(random.randint(1, 12))
    return r


def d10():
    r = []
    x = int(input('Quantas vezes deseja rolar os dados? '))
    for i in range(x):
        r.append(random.randint(0, 9))
    return r


def d8():
    r = []
    x = int(input('Quantas vezes deseja rolar os dados? '))
    for i in range(x):
        r.append(random.randint(1, 8))
    return r


def d6():
    r = []
    x = int(input('Quantas vezes deseja rolar os dados? '))
    for i in range(x):
        r.append(random.randint(1, 6))
    return r


def d4():
    r = []
    x = int(input('Quantas vezes deseja rolar os dados? '))
    for i in range(x):
        r.append(random.randint(1, 4))
    return r