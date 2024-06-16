import os

# Функция для импорта данных из файла
def import_data(filename):
    if not os.path.isfile(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip().split(';') for line in lines]

# Функция для экспорта данных в файл
def export_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in data:
            file.write(';'.join(entry) + '\n')

# Функция для добавления новой записи
def add_entry(data):
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    data.append([surname, name, patronymic, phone_number])

# Функция для поиска записи
def search_entry(data):
    search_query = input('Введите характеристику для поиска (фамилия, имя, отчество или номер телефона): ')
    for entry in data:
        if search_query in entry:
            print('Найдена запись:', ' '.join(entry))

# Функция для вывода всех данных
def print_data(data):
    for entry in data:
        print(' '.join(entry))
# Функция для изменения записи
def update_entry(data):
    search_query = input('Введите фамилию или имя для изменения записи: ')
    for i, entry in enumerate(data):
        if search_query in entry:
            print('Текущая запись:', ' '.join(entry))
            new_surname = input('Введите новую фамилию (оставьте пустым, чтобы не менять): ')
            new_name = input('Введите новое имя (оставьте пустым, чтобы не менять): ')
            new_patronymic = input('Введите новое отчество (оставьте пустым, чтобы не менять): ')
            new_phone_number = input('Введите новый номер телефона (оставьте пустым, чтобы не менять): ')
            data[i] = [
                new_surname if new_surname else entry[0],
                new_name if new_name else entry[1],
                new_patronymic if new_patronymic else entry[2],
                new_phone_number if new_phone_number else entry[3]
            ]
            print('Запись изменена.')
            return
    print('Запись не найдена.')

# Функция для удаления записи
def delete_entry(data):
    search_query = input('Введите фамилию или имя для удаления записи: ')
    for i, entry in enumerate(data):
        if search_query in entry:
            print('Удалена запись:', ' '.join(entry))
            del data[i]
            return
    print('Запись не найдена.')

# Основная программа
def main():
    data = import_data('phonebook.txt')
    while True:
        print('1. Вывести все данные')
        print('2. Добавить запись')
        print('3. Найти запись')
        print('4. Изменить запись')
        print('5. Удалить запись')
        print('6. Сохранить и выйти')
        choice = input('Выберите действие: ')
        if choice == '1':
            print_data(data)
        elif choice == '2':
            add_entry(data)
        elif choice == '3':
            search_entry(data)
        elif choice == '4':
            update_entry(data)
        elif choice == '5':
            delete_entry(data)
        elif choice == '6':
            export_data(data, 'phonebook.txt')
            break
        else:
            print('Неверный выбор. Пожалуйста, попробуйте снова.')

if __name__ == '__main__':
    main()

