# Створити алгоритм гри "Містечка". Тобто правила такі:
# Є словник із столицями країн. (10 столиць країн на твій вибір)
# Користувач "нескінченно" вводить назву міст і програма на основі словника видає відповідь так це столиця такої країни
# чи ні на жаль це не столиця якщо такої столиці у 10 країн зі словника немає. або введіть слово стоп,
# яке закінчить цикл.


"""ЛЗ 17"""
# Игра "Містечка".

# Создаем словарь с 10 столиц стран
popular_capitals = {'France': 'Paris',
                    'Spain': 'Madrid',
                    'Ukraine': 'Kyiv',
                    'America': 'Washington',
                    'Great Britain': 'London',
                    'Germany': 'Berlin',
                    'Japan': 'Tokio',
                    'China': 'Pekin',
                    'Italy': 'Rim',
                    'Brazil': 'Brasilia'
                    }


# Главная функция write_capital
def write_capital():
    # Делаем бесконечный цикл
    while True:

        capital = input('Write capital, if you want end a game, write "stop": ')
        if capital == 'stop':
            break

        is_capital = False
        for key, val in popular_capitals.items():
            if capital == val:
                print(f'Yes, {capital} is a capital of {key}')
                is_capital = True
                break

        if not is_capital:
            print(f'No, {capital} is not a capital!')


write_capital()


