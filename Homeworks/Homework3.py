# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# N = int(input("Введите количество элементов в массиве: "))
# massive = list(range(1, N+1))
# checkNum = int(input("Введите число для проверки: "))
# counter = 0
# for i in range(N):
#     if massive[i] == checkNum:
#         counter+=1
# print(counter)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# N = int(input("Введите количество элементов в массиве: "))
# massive = list(range(1,N+1))
# checkNum = int(input("Введите число для проверки: "))
# if checkNum > massive[-1]:
#     print(massive[-1])
# elif checkNum < massive[0]:
#     print(massive[0])
# else:
#     for i in range(N):
#         if checkNum == massive[i]:
#             print(massive[i])


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12

slovEng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVMY',
           5: 'K', 8:'JX', 10:'QZ'}
slovRus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
           4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}

num = int(input("Введите 1, если слово будет на английском, и 0, если на русском: "))
word = input("Введите слово: ").upper()

if num == 1:
    print("Вы получаете", sum([k for i in word for k,v in slovEng.items() if i in v]), "очков!")
elif num == 0:
    print("Вы получаете", sum([k for i in word for k,v in slovRus.items() if i in v]), "очков!")
else:
    print("Не хитри!")