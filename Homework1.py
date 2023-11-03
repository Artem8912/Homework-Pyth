def readfile():
    with open("Phone.txt","r") as file:
        return file.read()
def print_data():
    print(readfile())
def interface():
    with open("Phone.txt","a"):
        pass
    command = ""
    while command !="4":
        print(" Введите опцию\n"
        "1.Запись данных \n"
        "2.Вывод телефонной книги на экран\n"
        "3.Поиск данных\n"
        "4.Выход")
        command = input("Введите номер опции: ")
        while command not in ["1","2","3","4"]:
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
                print("Приложение закрыто")
interface()