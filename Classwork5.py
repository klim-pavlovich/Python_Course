# def fact(x):
#     res = 1
#     for i in range(1, x + 1):
#         res *= i
#     return res

# print(fact(3))


# def fact_rec(x):
#     if x ==  0:
#         return 1
#     return x * fact_rec(x-1)
    
# print(fact_rec(4))
    
# Задача №31. Решение в группах
# Требуется найти N-е число Фибоначчи Рекурсией
# Input: 9
# Output: 21
#  0, 1, 1, 2, 3, 5, 8, 13, 21

# Декоратор для ускорения вычислений, путем кэширования
# from functools import lru_cache

# pos_of_num = int(input("Введите позицию числа Фибоначчи: "))

# @lru_cache()
# def fib_rec(pos_of_num):
#     if pos_of_num == 1:
#         return 0
#     if pos_of_num == 2 or pos_of_num == 3:
#         return 1
#     elif pos_of_num > 3:
#         return fib_rec(pos_of_num-1)+fib_rec(pos_of_num-2)
    
# print(fib_rec(pos_of_num))


# Задача №33. Общее обсуждение
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные. (усложнил себе: + минимальные на максимальные)
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def find_max_and_min(lst):
#     min = lst[0]
#     max = lst[1]
#     temp=0
#     if min>max:
#         min=temp
#         min=max
#         max=temp
#     for i in range(len(lst)):
#         if lst[i]>max:
#             max = lst[i]
#         if lst[i]<min:
#             min=lst[i]
#     return lst, max, min

# def change_max_and_min(lst,max,min):
#     for i in range(len(lst)):
#         if lst[i] == max:
#             lst[i] = min
#         elif lst[i] == min:
#             lst[i] = max
#     return lst

# quintityOfMarks = int(input("Введите количество оценок: "))
# marks = [0] * quintityOfMarks
# for i in range(len(marks)):
#     marks[i]=int(input("Введите оценку: "))
# marks, max, min = find_max_and_min(marks)
# print(change_max_and_min(marks, max, min))

        
# Другое решение (без усложнения)
# lst = [int(i) for i in '1 2 3 4 3'.split()]
# mx,mn = max(lst), min(lst)
# lst_str = [str(i) for i in lst]
# print(' '.join(lst_str).replace(str(mx),str(mn)))

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def isPrime(num):
#     if num >= 2 and num <= 3:
#         return 'Yes'
#     elif num <=1:
#         return 'No'
#     else:
#         for i in range(2, int(num ** 0.5) +1):
#             if num % i == 0:
#                 return 'No'
#         return 'Yes'
    
# num_of_user=int(input('Введите целое число: '))
# res = isPrime(num_of_user)
# print(res)


# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
# 3   1 2 3
# 3 2 1

# q_of_nums=int(input('Введите количество элементов: '))
# nums = input("Введите элементы через пробел: ").split()

# def reverse_elements(nums):
#     if nums == 0:
#         return ''
#     else:
        # return nums[-1] + reverse_elements(nums[:-1])
    
    
# q_of_els=int(input('Введите количество элементов: '))

# def reverse_elements(q_of_els):
#     if q_of_els == 0:
#         return []
#     element = input("Введите элемент: ")
#     reverse_elements(q_of_els - 1)
#     print(element, end=' ')
    
# def nums_mirror(n):
#     temp = input('Введите число: ')
#     if n == 1:
#         return temp
#     return nums_mirror(n-1) + temp
    
# reverse_elements(q_of_els)