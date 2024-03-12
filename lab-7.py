import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from time import perf_counter
from mpl_toolkits.mplot3d import Axes3D

def t1():
    list1 = []
    for i in range(1000000):
        list1.append(random.random())
    list2 = []
    for i in range(1000000):
        list2.append(random.random())

    start_time = perf_counter()
    multiply1 = np.multiply(list1, list2)
    end_time = perf_counter()
    result1 = end_time - start_time

    start_time = perf_counter()
    multiply2 = []
    for i in range(len(list1)):
        multiply2.append(list1[i]*list2[i])
    end_time = perf_counter()
    result2 = end_time - start_time

    print('Переможение массивов Nampy:', result1, '\nПеремножение стандартных списков:', result2)

def t2():
    file = pd.read_csv('data1.csv', delimiter=';', encoding='cp1251')
    time = file.iloc[:, 0]
    position = file.iloc[:, 3]
    hour_fuel = file.iloc[:, 17]

    plt.plot(time, position, 'c', time, hour_fuel, 'm')
    plt.title('График с использованем Matplotlib')
    plt.xlabel('Время')
    plt.ylabel('Часовой расход топлива (л\час)\n Положение дроссельной заслонки (%)')
    plt.show()

    plt.title('График корреляции')
    plt.xlabel('Положение дроссельной заслонки (%)')
    plt.ylabel('Часовой расход топлива (л\час)')
    plt.plot(position, hour_fuel, 'o')
    plt.show()

def t3():
    np.random.seed(40)
    xs = np.linspace(-5*np.pi, 5*np.pi, 100)
    ys = np.cos(xs)
    zs = np.sin(xs)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='orange')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Трёхмерный график')
    plt.show()

t1()
t2()
t3()
