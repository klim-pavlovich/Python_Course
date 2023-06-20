# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам 

# vowel_letters = ['а','у','о','ы','и','э','я','ю','ё','е']
# res_for_good_rythm = 'Парам пам-пам'
# res_for_bad_rythm = 'Пам парам'

# def checking_the_rythm(user_poem: str):
#     counter_of_phrases = 1
#     # Находим количество фраз
#     for i in range(len(user_poem)):
#         if poem_from_user[i] == " ":
#             counter_of_phrases +=1
#     # Создаем массив, где количество счетчиков (нулей) = количеству фраз
#     array_with_quintities_of_vowel_in_phrases = []
#     # Создаем временный счетчик для подсчета гласных в каждой отдельной фразе
#     temp_counter = 0
#     # 
#     for i in range (len(user_poem)):
#         if poem_from_user[i] in vowel_letters:
#             temp_counter+=1
#             if i == len(user_poem) - 1:
#                 array_with_quintities_of_vowel_in_phrases.append(temp_counter)
#         elif poem_from_user[i] == " ":
#             array_with_quintities_of_vowel_in_phrases.append(temp_counter)
#             temp_counter = 0
#     if all(element == array_with_quintities_of_vowel_in_phrases[0] for element in array_with_quintities_of_vowel_in_phrases):
#         return res_for_good_rythm
#     return res_for_bad_rythm

# poem_from_user = input("Введите стих в стиле Винни-Пуха: ")
# poem_from_user = poem_from_user.replace('-','')
# print(checking_the_rythm(poem_from_user))


# Задача 36: Напишите функцию print_operation_table (operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table (operation, num_rows=6, num_columns=6):
    for i in range(1, num_columns+1):
        for j in range(1, num_rows+1):
            element = operation(i,j)
            print(element, end =" ")
        print()
    
print_operation_table(lambda x, y: x * y)