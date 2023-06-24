# # Первый способ работы с файлами
# f = open("file_example.txt","r",encoding="utf-8")
# data = f.read()
# print(data)
# # Обязательно закрываем, чтобы не висел в памяти
# f.close()

# в open("...") можно указывать абсолютный путь (D://...)

# Второй способ с использованием контекстного менеджера with
# Плюс в том, что файл закроется сам
# with open("file_example.txt","r",encoding="utf-8") as f2:
#     data = f2.read()
#     print(data)
    
# Как открывать файлы из других папок
# на примере file_example2 из папки выше
# with open("../file_example2.txt","r",encoding="utf-8") as f3:
#     data = f3.read()
#     print(data)
    
# Плюс можно открыть папку, в которой лежит файл
# через: cd НазваниеПапки и прогнать script: python Названиефайла.py

# Для чтения строк используется readlines(),
# она их считывает и превращает в список, со знаком переноса
# with open("../file_example2.txt","r",encoding="utf-8") as f3:
#     data = f3.readlines()
#     print(data)

# Если мы знаем, что будут знаки переноса,
# можно их убрать в полученном массиве через strip:

# with open("../file_example2.txt","r",encoding="utf-8") as f3:
#     data = f3.readlines()
#     data = list(map(str.strip, data))
#     print(data)


# Другие режимы работы
# Режим append - добавление в конец
# Также, можно добавлять список, но через writelines
# sp = ["\nCheck append", "\nAnd writting sp"]
# with open("../file_example2.txt","a",encoding="utf-8") as f3:
#     f3.writelines(sp)
    
# Режим перезаписи 'w'
# sp = ["Тестовая", "\nперезапись" "\nфайла"]
# with open("../file_example2.txt","w",encoding="utf-8") as f3:
#     f3.writelines(sp)
