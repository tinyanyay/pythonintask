﻿# Задача 4. Вариант 30.
'''
Напишите программу, которая выводит имя, под которым скрывается
Вильгельм Аполлинарий Костровицкий. Дополнительно необходимо вывести
область интересов указанной личности, место рождения, годы рождения и
смерти (если человек умер), вычислить возраст на данный момент (или
момент смерти). Для хранения всех необходимых данных требуется использовать
переменные. После вывода информации программа должна дожидаться
пока пользователь нажмет Enter для выхода.
'''
# Shchukin F.O.
# 03.03.2016


real_name = 'Вильгельм Альберт Владимир \
Александр Аполлинарий Вонж-Костровицкий'
imaginary_name = 'Вильгельм Аполлинарий Костровицкий'
interests = ('Проза', 'Поэзия', 'Сюрреализм')
born_place = 'Рим, Лацио, Италия'
born_year = 1880
death_year = 1914
death_oldness = death_year - born_year

print(real_name + ' \nболее известный под псевдонимом '
              + imaginary_name + '.')

print('''
Нажмите чтобы вывести на экран:
1 - Место рождения,
2 - Год рождения,
3 - Возраст при смерти,
4 - Область интересов,
5 - Выход из программы\n\n''')

while True:
    try:
        choose = int(input('Ввод: '))
    except:
        print('Неправильный ввод')
        choose = 0

    if choose == 1:
        print('Место рождения: ' + str(born_place))
    elif choose == 2:
        print('Год рождения: ' + str(born_year))
    elif choose == 3:
        print('Возраст при смерти: ' + str(death_oldness))
    elif choose == 4:
        print('Область интересов: ' + ' '.join(interests))
    elif choose == 5:
        break

input('\nНажмите enter...')
