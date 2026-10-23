import pandas as pd  # подключаем пандас чтобы работать с таблицей
# создаем пустую таблицу с нужными столбцами
kniga = pd.DataFrame(columns=["ФИО", "Адрес", "Телефон", "Дата рождения"])
while True:  # бесконечный цикл чтобы программа не закрывалась
    print("\n--- Адресная книга ---")
    print("1 - Просмотреть все записи")
    print("2 - Добавить запись")
    print("3 - Изменить запись")
    print("4 - Удалить запись")
    print("5 - Выйти")
    vibor = input("Выберите действие (1-5): ")  # ждем пока пользователь введет цифру
    if vibor == "1":
        if len(kniga) == 0:  # проверяем пустая ли таблица
            print("Адресная книга пуста")
        else:
            print(kniga)  # пандас сам красиво выведет таблицу
    elif vibor == "2":
        # спрашиваем все поля и добавляем новую строку
        fio = input("Введите ФИО: ")
        adres = input("Введите адрес: ")
        telefon = input("Введите телефон: ")
        data = input("Введите дату рождения: ")
        # создаем из одной строки маленькую таблицу и приклеиваем к основной
        novaya = pd.DataFrame([[fio, adres, telefon, data]], columns=kniga.columns)
        kniga = pd.concat([kniga, novaya], ignore_index=True)  # ignore_index чтобы номера шли подряд
        print("Запись добавлена")
    elif vibor == "3":
        if len(kniga) == 0:
            print("Адресная книга пуста")
        else:
            print(kniga)
            nomer = int(input("Введите номер записи для изменения: "))
            if nomer in kniga.index:  # проверяем есть ли такая строка
                print("Если поле менять не надо - оставьте его пустым")
                for stolbec in kniga.columns:  # идем по всем столбцам по очереди
                    novoe = input("Новое значение для поля " + stolbec + ": ")
                    if novoe != "":  # если пользователь что-то ввел - меняем
                        kniga.loc[nomer, stolbec] = novoe
                print("Запись изменена")
            else:
                print("Такой записи нет")
    elif vibor == "4":
        if len(kniga) == 0:
            print("Адресная книга пуста")
        else:
            print(kniga)
            nomer = int(input("Введите номер записи для удаления: "))
            if nomer in kniga.index:
                kniga = kniga.drop(nomer)  # удаляем строку по номеру
                kniga = kniga.reset_index(drop=True)  # перенумеровываем заново чтобы не было дырок
                print("Запись удалена")
            else:
                print("Такой записи нет")
    elif vibor == "5":
        print("Выходим")
        break  # выходим из цикла и программа закрывается
    else:
        print("Неверный выбор. Попробуйте снова.")