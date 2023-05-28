# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# def findSumOfDigitsOfThreeDigitInteger(num):
#     if num < 100 or num > 999:
#         print("Вы ввели не трехзначное число, попробуйте еще раз")
#         num = int(input("Введите трехзначное число:"))
#         findSumOfDigitsOfThreeDigitInteger(num)
#     else:
#         first = num//100
#         second = num // 10 % 10
#         third = num - first * 100 - second * 10
#         sum = first + second + third
#         print(f"Сумма цифр числа {num} = {sum}")

# num = int(input("Введите трехзначное число:"))
# findSumOfDigitsOfThreeDigitInteger(num)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов 
# сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10


# numOfPaperCranes = int(input("Сколько журавликов сделали ребята вместе? Введите число: "))

# firstNum = numOfPaperCranes // 6
# secondNum = numOfPaperCranes // 6 * 4

# print(f"Петя и Сережа сделали по {firstNum} журавлика/ов, а Катя аж целых {secondNum} журавлика/ов!")


# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# numberOfTicket = int(input("Введите номер вашего билета (шестизначное число): "))
# firstDigit = numberOfTicket // 100000
# secondDigit =  numberOfTicket // 10000 % 10
# thirdDigit = numberOfTicket // 1000 % 10
# fourthDigit = numberOfTicket // 100 % 10
# fivesDigit = numberOfTicket // 10 % 10
# sixesDigit = numberOfTicket % 10
# if (firstDigit + secondDigit + thirdDigit) == (fourthDigit + fivesDigit + sixesDigit):
#     print("Вам попался счастливый билетик!")
# else:
#     print("Билет несчастливый, но Вам точно еще повезёт!")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# widthOfChocolate = int(input("Введите ширину шоколадки: "))
# lengthOfChocolate = int(input("Введите длину шоколодки: "))
# quintityOfBytes = int(input("Введите количество кусочков, которое хотите отломить: "))

# if quintityOfBytes <= 0 or quintityOfBytes > widthOfChocolate * lengthOfChocolate:
#     print("no")
# if quintityOfBytes % widthOfChocolate == 0 or quintityOfBytes % lengthOfChocolate == 0:
#     print("yes")
# else:
#     print("no")
