# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# 2 ** 4
# 2 ** 2 ** 2
# def exponentiation(num, exp):
#     if exp == 0:
#         return 1
#     return exponentiation((num),(exp-1)) * num
    
# num_of_user = int(input('Введите целое число, которое хотите возвести в степень: '))
# exp_of_user = int(input('Введите степень целым числом, в которую хотите возвести число: '))
# res_of_user = exponentiation(num_of_user,exp_of_user)
# print(res_of_user)



# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4


def sum(a,b):
    if b == 0:
        return a
    return sum(a+1,b-1)
        
# a = int(input('Введите первое целое неотрицательное число для нахождения суммы: '))
# b = int(input('Введите второе целое неотрицательное число для нахождения суммы: '))
# res = sum(a,b)
# print(res)