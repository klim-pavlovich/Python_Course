# lambda - анонимная функция, чаще для нахождения мини макса и в сортировках

# square = lambda x: x **2
# print(square(2))
# summa = lambda x, y: x + y
# print(summa(2,3))

# map - функция, которая применяет функцию к каждому элементу итерируемое объекта (массив, строка, кортеж)
# аргументы: функция для каждого элемента, массив
# можно комбинировать lambda и map

# sp = ['1', '2','3','4','5']
# sp1 = map(int,sp)
# 
# sp2 = map(lambda x: x ** 2, sp1)
# for i in sp2:
#     print(i)


# filter - функция для фильтрации, работает аналогично map, но возвращает 
# True или False и если True - элемент возвращается, если False - нет (В консоль выводятся значения, а не True False!)
# также можно комбинировать с lambda
# аргументы: функция фильтрации, список

# sp = [1,2,3,4,5]
# sp1 = filter(lambda x: x % 2 == 0, sp)
# for i in sp1:
#     print(i)
# # к map и filter можно обратиться один раз, если нужно сохранить - обертываем
# sp2 = filter(lambda x: x % 2 == 0, sp)
# print(list(sp2))

# списочные выражения отрабатывают на больших даннных быстрее, чем map
# например
# sp = [x**2 for x in range(1,6)]
# print(sp)
# фильтрая без фильтра (if как filter)
# sp = [x for x in range(1, 6) if x % 2 == 0]

# ! удобный прием списка через пробелы одним вводом !

# sp = list(map(int, input("Введите набор чисел через пробел: ").split()))
# print(sp)

# zip - принимает два итерируемых объекта, возвращает объект кортежами, 
# можно распаковать с помощью "*"
# sp = ["a", "b", "c"]
# numbers = [1, 2, 3]
# print(*zip(sp, numbers))


# enumerate - позволяет нумеровать элементы спика
# принимает итеруемый объект, можно вторым аргументом назначить стартовое число, иначе с нуля

# week = ["понедельник", "вторник", "среда"]
# for n, day in enumerate(week, 1):
#     print(n, "-", day)


#  S = pi*a*b,

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# el_orbs = list(filter(lambda x: x[0] != x[1], orbits))
# find_max = max(el_orbs, key = lambda x: x[0]*x[1])
# print(find_max)

# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# values = [0, 2, 10, 6]

# def same_by(characteristic, objects):
#     if not objects:
#         return True
#     char_of_first = characteristic(objects[0])
#     for obj in objects[1:]:
#         if characteristic(obj) != char_of_first:
#             return False
#     return True

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print("different")
    
    
# values = [4, 5, 4]
# def same_by(characteristic, objects):
#     return len(set([characteristic(obj) for obj in objects])) <= 1  
# if same_by(lambda x: x % 3, values):
#     print('same')
# else:
#     print("different")

