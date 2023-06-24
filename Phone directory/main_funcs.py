file_path = "Phone directory/contact_book.txt"

# Форматирование записи для вывода пользователю
def print_formatted_record(contact_data):
    formatted_data = f"{contact_data[0]}, {contact_data[1]} {contact_data[2]} {contact_data[3]}, {contact_data[4]}, {contact_data[5]}"
    print(formatted_data)

# Показ всех контактов
def show_all_records():
    print("\n")
    with open (file_path, "r", encoding="utf-8") as cf:
        for line in cf:
            contacts_data = line.strip().split(";")
            print_formatted_record(contacts_data)
    print("\n")
    
# Функция поиска контакта
def search_record():
    with open(file_path, "r", encoding="utf-8") as cf:
        contacts_data = cf.readlines()
        
    select_attribute_for_searching = input("\nЕсли хотите найти информацию о контакте по:\n"
                                           "\nПервичному ключу - введите 'пк',\n"
                                           "Фамилии - введите 'ф',\n"
                                           "По имени - введите 'и',\n"
                                           "По отчеству - введите 'о',\n"
                                           "Или - 'м', чтобы вернуться в главное меню: ")
    if select_attribute_for_searching == "пк":
        selected_primary_key = input("\nВведите первичный ключ контакта: ")
        contact_found = False
        for line in contacts_data:
            contacts_data = line.strip().split(";")
            if contacts_data[0] == selected_primary_key:
                print_formatted_record(contacts_data)
                print("\n")
                contact_found = True
                main()
        if not contact_found:
            print("\nТакого контакта нет в словаре, попробуйте еще раз.")
            search_record()
            
    if select_attribute_for_searching == "ф":
        selected_second_name = input("\nВведите фамилию контакта с заглавной буквы: ")
        contact_found = False
        for line in contacts_data:
            contacts_data = line.strip().split(";")
            if contacts_data[1] == selected_second_name:
                print_formatted_record(contacts_data)
                print("\n")
                contact_found = True
                main()
        if not contact_found:
            print("\nТакого контакта нет в словаре, попробуйте еще раз.")
            search_record()
            
    elif select_attribute_for_searching == "и":
        selected_first_name = input("\nВведите имя контакта с заглавной буквы: ")
        contact_found = False
        for line in contacts_data:
            contacts_data = line.strip().split(";")
            if contacts_data[2] == selected_first_name:
                print_formatted_record(contacts_data)
                print("\n")
                contact_found = True
                main()
        if not contact_found:
            print("\nТакого контакта нет в словаре, попробуйте еще раз.")
            search_record()
            
    elif select_attribute_for_searching == "о":
        selected_third_name = input("\nВведите отчество контакта с заглавной буквы: ")
        contact_found = False
        for line in contacts_data:
            contacts_data = line.strip().split(";")
            if contacts_data[3] == selected_third_name:
                print_formatted_record(contacts_data)
                print("\n")
                contact_found = True
                main()
        if not contact_found:
            print("\nТакого контакта нет в словаре, попробуйте еще раз.")
            search_record()
    
    elif select_attribute_for_searching == "м":
        main()
        
    else:
        print("\nВы ввели неверное значение, попробуйте еще раз.\n")
        search_record()

# Функция для добавления комментария
def add_comment_for_contact():
    isCommented = int(input("\nХотите добавить комменатрий?\n"
                            "Введите - '1', если хотите,\nВведите - '2', если комментарий не нужен: "))
    if isCommented == 1:
        comment = input("\nВведите комментарий: ")
        return comment
    elif isCommented == 2:
        comment = '-'
        return comment
    else:
        print("\nВы ввели неверное значение. Попробуйте еще раз.")
        add_comment_for_contact()

# Функция проверки корректности введенных данных и их сохранение при добавлении контакта
def checking_correctness_of_added_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment):        
        print("\nПроверьте верность веденных данных: ",
                name,
                second_name,
                third_name,
                phone_number,
                comment)
        isCorrected = int(input("Данные введены верно?\n"
                                "Введите - '1', если да,\nВведите - '2', если нет: "))
        
        # подготовливаем строчку для сохранения и добавляем ПК
        
        info_about_new_contact=primary_key+";"+name+";"+second_name+";"+third_name+";"+phone_number+";"+comment
        
        # Если пользователь ввел все верно - сохраняем
        if isCorrected == 1:
            with open (file_path, "a", encoding="utf-8") as cf:
                cf.write("\n")
                cf.write(info_about_new_contact)
            main()
        if isCorrected == 2:
            changed_attribute_while_adding = int(input("Введите - '1', чтобы изменить имя\n"
                                                    "Введите - '2', чтобы изменить фамилию\n"
                                                    "Введите - '3', чтобы изменить отчество\n"
                                                    "Введите - '4', чтобы изменить номер\n"
                                                    "Введите - '5', чтобы изменить комментарий\n"))
            if changed_attribute_while_adding == 1:
                name = input("\nВведите новое имя контакта: ")
                checking_correctness_of_added_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)
            elif changed_attribute_while_adding == 2:
                second_name = input("\nВведите новую фамилию контакта: ")
                checking_correctness_of_added_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)
            elif changed_attribute_while_adding == 3:
                third_name = input("\nВведите новую фамилию контакта: ")
                checking_correctness_of_added_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)
            elif changed_attribute_while_adding == 4:
                phone_number = input("Введите новый номер телефона контакта: ")
                checking_correctness_of_added_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)
            elif changed_attribute_while_adding == 5:
                comment = input("Введите новый комментарий для контакта: ")
                checking_correctness_of_added_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)

# Функция добавления контакта в книжку
def add_contact():
    print("\n")
    name_of_added_contact = input("Введите имя нового контакта: ")
    second_name_of_added_contact = input("Введите фамилию: ")
    third_name_of_added_contact = input("Введите отчество: ")
    phone_number_of_added_contact = input("Введите номер телефона: ")
    comment_of_added_contact = add_comment_for_contact()
    with open (file_path, "r", encoding="utf-8") as cf:
        lines = cf.readlines()
        last_line=lines[-1]
        primary_key_of_added_contact = int(last_line[0]) + 1
        primary_key_str = str(primary_key_of_added_contact)
        
    checking_correctness_of_added_contact_and_save(primary_key_str, name_of_added_contact, second_name_of_added_contact,third_name_of_added_contact,
                                            phone_number_of_added_contact,comment_of_added_contact)
    print("Контакт успешно сохранен!\n")
    main()

# Функция изменения информации о контакте
def change_record():
    pk_is_known = int(input("\nВы знаете первичный номер контакта, который хотите изменить?\n"
                            "Если да - нажмите 1,\n"
                            "Если нет - 2, \n"
                            "Для отмены - 3: "))

    if pk_is_known == 1:
        pk_for_changing_record = int(input("\nВведите ПК для изменения контакта: "))
        primary_key_str = str(pk_for_changing_record)

        with open(file_path, "r", encoding="utf-8") as cf:
            contacts_data = cf.readlines()
            

        contact_found = False
        for i, line in enumerate(contacts_data):
            contact_data = line.strip().split(";")
            if contact_data[0] == str(pk_for_changing_record):
                print_formatted_record(contact_data)
                print("\n")
                contact_found = True

                attribute_for_changing = int(input("Нажмите 1, чтобы изменить имя\n"
                                                  "Нажмите 2, чтобы изменить фамилию\n"
                                                  "Нажмите 3, чтобы изменить отчество\n"
                                                  "Нажмите 4, чтобы изменить номер\n"
                                                  "Нажмите 5, чтобы изменить комментарий\n"))

                if attribute_for_changing == 1:
                    contact_data[1] = input("\nВведите новое имя контакта: ")
                elif attribute_for_changing == 2:
                    contact_data[2] = input("\nВведите новую фамилию контакта: ")
                elif attribute_for_changing == 3:
                    contact_data[3] = input("\nВведите новое отчество контакта: ")
                elif attribute_for_changing == 4:
                    contact_data[4] = input("Введите новый номер телефона контакта: ")
                elif attribute_for_changing == 5:
                    contact_data[5] = input("Введите новый комментарий для контакта: ")

                contacts_data[i] = ";".join(contact_data) + "\n"
                break

        if not contact_found:
            print("\nТакого контакта нет в книге.")
            return

        with open(file_path, "w", encoding="utf-8") as cf:
            cf.writelines(contacts_data)

        checking_correctness_of_changed_contact_and_save(primary_key_str, contact_data[1], contact_data[2], contact_data[3], contact_data[4], contact_data[5])

    elif pk_is_known == 2:
        print("Тогда пересмотрите справочник.")
        show_all_records()
        change_record()
    elif pk_is_known == 3:
        print("\nИзменение контакта отменено.")
        print("\n")
        main()
    else:
        print("\nВы ввели некорректное значение. Попробуйте еще раз.")
        change_record()

# Функция проверки корректности введенных данных и их сохранение при изменени инфомации о контакте
def checking_correctness_of_changed_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment):        
        print("\nПроверьте верность веденных данных: ",
                name,
                second_name,
                third_name,
                phone_number,
                comment)
        isCorrected = int(input("Данные введены верно?\n"
                                "Введите - '1', если да,\nВведите - '2', если нет: "))
        
        # подготовливаем строчку для сохранения и добавляем ПК
        
        info_about_new_contact=primary_key+";"+name+";"+second_name+";"+third_name+";"+phone_number+";"+comment
        
        # Если пользователь ввел все верно - сохраняем
        if isCorrected == 1:
            rewrite_line(file_path,primary_key,info_about_new_contact)
            
        if isCorrected == 2:
            changed_attribute_while_adding = int(input("Введите - '1', чтобы изменить имя\n"
                                                    "Введите - '2', чтобы изменить фамилию\n"
                                                    "Введите - '3', чтобы изменить отчество\n"
                                                    "Введите - '4', чтобы изменить номер\n"
                                                    "Введите - '5', чтобы изменить комментарий\n"))
            if changed_attribute_while_adding == 1:
                name = input("\nВведите новое имя контакта: ")
                checking_correctness_of_changed_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)
            elif changed_attribute_while_adding == 2:
                second_name = input("\nВведите новую фамилию контакта: ")
                checking_correctness_of_changed_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)
            elif changed_attribute_while_adding == 3:
                third_name = input("\nВведите новую фамилию контакта: ")
                checking_correctness_of_changed_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)
            elif changed_attribute_while_adding == 4:
                phone_number = input("Введите новый номер телефона контакта: ")
                checking_correctness_of_changed_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)
            elif changed_attribute_while_adding == 5:
                comment = input("Введите новый комментарий для контакта: ")
                checking_correctness_of_changed_contact_and_save(primary_key,name,second_name,third_name,phone_number,comment)

def rewrite_line(file_path, primary_key, new_line):
    with open(file_path, "r", encoding="utf-8") as cf:
        lines = cf.readlines()

    for i, line in enumerate(lines):
        data = line.strip().split(";")
        if data[0] == str(primary_key):
            lines[i] = new_line + "\n"
            break

    with open(file_path, "w", encoding="utf-8") as cf:
        cf.writelines(lines)
        
    print("Изменения успешно сохранены!")
    main()
    
def main():
    print("Команды: 1 - показать справочник,\n"
          "2 - найти контакт,\n"
          "3 - добавить контакт,\n"
          "4 - изменить контакт")
    select = int(input("Выберите действие: "))
    if select == 1:
        show_all_records()
        main()
    elif select == 2:
        search_record()
    elif select == 3:
        add_contact()
    elif select == 4:
        change_record()
    

if __name__ == "__main__":
    main()