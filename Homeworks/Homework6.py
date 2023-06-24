# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# start_element = int(input("Введите стартовое число: "))
# difference_element = int(input("Введите разность: "))
# quintity_of_nums = int(input("Введите количество чисел: "))
# array_of_user = [0]*quintity_of_nums
# array_of_user[0] = start_element
# array_of_user = [start_element + difference_element * i for i in range(quintity_of_nums)]
# print(array_of_user)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min = 1, max = 19
# Вывод: [1, 9, 13, 14, 19]
user_input = input("Введите числа через пробел: ")
min_num_of_user = input("Введите минимальное число: ")
max_num_of_user= input("Введите максимальное число: ")
user_array_of_nums = [int(num) for num in user_input.split()]

def find_indexes_of_nums_in_range(min_num: int, max_num: int, user_nums: int):
    final_array = []
    for i in range(len(user_nums)):
        if user_nums[i] >= min_num and user_nums[i] <= max_num:
            final_array.append(i)
    print(final_array)

# Выводим индексы тех чисел, чьи значения не превышают мин и макс
find_indexes_of_nums_in_range(int(min_num_of_user), int(max_num_of_user), user_array_of_nums)