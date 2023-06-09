# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# def quick_sort(array):
#     if len(array) < 1:
#         return array
#     else:
#         pivot = array[0]
        
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# n = int(input('Введите количество элементов первого множества: '))
# m = int(input('Введите количество элементов второго множества: '))
# list1 = [0]*n
# list2 = [0]*m
# for i in range(n):
#     list1[i] = input('Введите значение элемента для первого множества:')
# for j in range(m):
#     list2[j] = input('Введите значение элемента для второго множества:')

# common_list = list1+list2
# quick_sort(common_list)
# final_common_list=set(common_list)
# print(final_common_list)
    

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

N = int(input("Введите количество кустов: "))
listOfBerries = [0] * N
for i in range(len(listOfBerries)):
    listOfBerries[i] = int(input(f"Введите количество ягод на {i+1} кусте: "))
    
if len(listOfBerries) <=3:
    maxBerries=sum(listOfBerries)
else:
    for i in range(len(listOfBerries)-3):
        first = listOfBerries[i]
        second = listOfBerries[i+1]
        third = listOfBerries[i+2]
        fourth = listOfBerries[i+3]
        maxBerries = first + second + third
        berriesToCompare = second + third + fourth
        if berriesToCompare > maxBerries:
            maxBerries = berriesToCompare
            
print(maxBerries)