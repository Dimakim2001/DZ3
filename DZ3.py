# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# from random import randint

# def get_list(n, first, last):
#     return [randint(first, last) for i in range(n)]

# def sum_odd_position(mylist):
#     return sum(mylist[1::2])

# n = 10
# first = 1
# last = 10

# mylist = get_list(n, first, last)
# print(mylist)
# print(sum_odd_position(mylist))


# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint
# import math

# def get_numbers(n, first, last):
#     return [randint(first, last) for i in range(n)]

# def mult_pairs(mylist):
#     return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

# n = 9
# first = 1
# last = 10

# mylist = get_numbers(n, first, last)
# print(mylist)
# print(mult_pairs(mylist))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input('Введите число: '))

# def conversion(n):
#     bin_num = ''
#     while n > 1:
#         bin_num += str(n % 2)
#         n = n // 2
#     return bin_num[::-1]

# print(conversion(n))


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# n = int(input('Введите число: '))

# def get_fibonacci(n):
#     fibo_nums = []
#     a, b = 1, 1
#     for i in range(n-1):
#         fibo_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range (n):
#         fibo_nums.insert(0, a)
#         a, b = b, a - b
#     return fibo_nums

# fibo_nums = get_fibonacci(n)
# print(get_fibonacci(n))
# print(fibo_nums.index(0))




