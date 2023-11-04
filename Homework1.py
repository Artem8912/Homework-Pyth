def readfile1():
    with open("Phonebook1.txt","r",encoding="UTF-8") as file1:
        return file1.read()
def readfile2():
    with open("Phonebook2.txt","r",encoding="UTF-8") as file2:
        return file2.read()
def copy_to_newfile():
    count_str_f1=0
    count_str_f2=0
    with open("Phonebook1.txt","r",encoding="UTF-8") as file1:
        for el in file1:
            count_str_f1+=1
    with open("Phonebook2.txt","r",encoding="UTF-8") as file2:
        for el in file2:
            count_str_f2+=1
    print("В какой файл вы хотите скопировать данные: \n"
          "1.Phonebook1\n"
          "2.Phonebook2\n")
    option = input("Введите номер варианта: ")
    while option not in ["1","2"]:
        print("Введите корректное значение: ")
        option=input()
    match option:
        
        case "1":
            with open("Phonebook2.txt","r",encoding="UTF-8") as file2:
                str_num = int(input("Введите номер строки, которую нужно скопировать в файле Phonebook2.txt "))
                count=0
                for line in range(count_str_f2):
                    buff1=file2.readline()
                    count+=1
                    if count == str_num:
                        buff2 = buff1
            with open("Phonebook1.txt","a",encoding="UTF-8") as file1:
                readfile1()
                file1.write(buff2)
        case "2":
            with open("Phonebook1.txt","r",encoding="UTF-8") as file1:
                str_num = int(input("Введите номер строки, которую нужно скопировать в файле Phonebook1.txt "))
                count=0
                for line in range(count_str_f1):
                    buff1=file1.readline()
                    count+=1
                    if count == str_num:
                        buff2 = buff1
            with open("Phonebook2.txt","a",encoding="UTF-8") as file2:
                readfile2()
                file2.write(buff2)
        
def print_data():
    print(readfile1())
def search_contact():
    print(" Варианты для поиска\n"
        "1.Фамилия \n"
        "2.Имя\n"
        "3.Отчество\n"
        "4.Телефон\n"
        "5.Адрес\n ")
    command = input("Укажите номер варианта: ")
    while command not in ["1","2","3","4","5"]:
        print("Неккоректный ввод\n"
            "Повторите ввод")
        command = input("Введите номер опции: ")
    i_search_param = int(command)-1
    search = input("Укажите данные для поиска: ").title()
    contacts_list = readfile1().split("\n\n")
    contacts_list.pop()
    # print(contacts_list)
    for contact_str in contacts_list:
        # print(contact_str)
        contact_lst = contact_str.replace("\n"," ").split(" ")
        # print(contact_lst)
        if search in contact_lst[i_search_param]:
            print(*contact_lst)
    
     
def input_name():
    return input("Введите имя: ")
def input_surname():
    return input(" Введите фамилию: ")
def input_patronymic():
    return input(" Введите отчество: ")
def input_phone():
    return input("Введите телефон: ")
def input_adress():
    return input("Введите адрес: ")
def input_data():
    
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    str_contact = surname+" "+name+" "+patronymic+" "+phone+"\n"+adress+"\n\n"
    with open("Phonebook1.txt","a",encoding="UTF-8") as file1:
            file1.write(str_contact)
            
def interface():
    with open("Phonebook1.txt","a",encoding="UTF-8"):
        pass
    command = ""
    while command !="5":
        print(" Введите опцию\n"
        "1.Запись данных \n"
        "2.Вывод телефонной книги на экран\n"
        "3.Поиск данных\n"
        "4.Скопировать из одного файла в другой \n"
        "5.Выход")
        command = input("Введите номер опции: ")
        while command not in ["1","2","3","4","5"]:
            print("Неккоректный ввод\n"
                "Повторите ввод")
            command = input("Введите номер опции: ")
        match command:
            case "1":
                input_data()
            case "2":
                print_data()
            case "3":
                search_contact()
            case "4":
                copy_to_newfile()
            case "5":
                print("Приложение закрыто")
interface()
