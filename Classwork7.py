# map - аргументы: функция для каждого элемента, массив
# filter - аргументы: функция фильтрации, список
# к map и filter можно обратиться один раз, если нужно сохранить - обертываем
# sp = [x ** 2 for x in range(1, 6)]
# фильтрая без фильтра
# sp = [x for x in range(1, 6) if x % 2 == 0]

# zip - возвращается объект кортежами, можно распокавать
# sp = ["a", "b", "c"]
# numbers = [1, 2, 3]
# print(*zip(sp, numbers))


# enumerate, можно вторым аргументом назначить первое число, иначе с нуля

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

