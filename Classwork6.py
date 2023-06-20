def fill_array():
    N = int(input('Введите количество элементов в массиве: '))
    user_array = [0] * N
    for i in range(N):
        user_array[i] = int(input('Введите значение элемента массива: '))
    return user_array

# либо не используя функцию в две строки
# n = int(input('Введите количество элементов: '))
# arr = [int(input(f'Введите { i + 1}-е число массива:')) for i in range(n)]
# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод:
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15
# Вывод:
# 3 3 2 12
# array1 = fill_array()
# array2 = fill_array()

# def find_not_repited_numbers(array1,array2,res_array=[]):
#     for i in range(len(array1)):
#         if array1[i] not in array2:
#             res_array+=[array1[i]]
#     if res_array == []:
#         return "В первом списке нет таких элементов"
#     return f"Элементты первого массива, которых нет во втором: {res_array}"

# res = find_not_repited_numbers(array1, array2)
# print(res)           

# Другое решение без использования функции
# print(*[num for num in array1 if num not in array2]) 

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:5
# 1 2 3 4 5
# Вывод:0
# Ввод:5
# 1 5 1 5 1
# Вывод:2

# def find_num_that_has_two_smaller_neighbours(array):
#     count = 0
#     for i in range(1, len(array) - 1):
#         if array[i-1] < array[i] and array[i+1] < array[i]:
#             count+=1
#     return count

# user_array = fill_array()
# res = find_num_that_has_two_smaller_neighbours(user_array)
# print(res)

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: 1 2 3 2 3
# Ввод: 1 2 3 2 3
# Вывод: 2

# def find_couples_numbers(array):
#     counter = 0
#     pos_for_comparing = 1
#     for i in range(len(array)):
#         for j in range (pos_for_comparing, len(array)):
#             if array[i] == array[j]:
#                 counter +=1
#         pos_for_comparing+=1            
#     return counter
    
# user_array = fill_array()
# res = find_couples_numbers(user_array)
# print(res)

# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод: 
# 300 

# Вывод:
# 220 284

def find_sum_of_divisors_for_friendly_numbers(num):
    # divisor = 1
    # sum_of_divisors = 0
    # for divisor in range(1, num//2 + 1):
    #     if num % divisor == 0:
    #         sum_of_divisors += divisor
    #     divisor +=1
    # return sum_of_divisors 
    # или (второй более эффективный)
    res = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res += i
            k = num // i
            if k != i:
                res += k
    return res +1
        
def find_friendly_numbers(limiter):
    for i in range(1, limiter):
        for j in range(i+1, k):
            if find_sum_of_divisors_for_friendly_numbers(i) == j and find_sum_of_divisors_for_friendly_numbers(j)==i:
                print(f"{i} {j}")

k = int(input('Введите число-ограничитель для поиска дружественных чисел: '))
find_friendly_numbers(k)
