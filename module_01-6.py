my_dict = {'Роман': 1986, 'Сергей': 1991, 'Ольга': 2000, 'Николай': 2004, 'Олег': 2008}
print('Словарь:', my_dict)
print('Год рождения Сергей:', my_dict['Сергей'])
print('Год рождения Иван:', my_dict.get('Иван', 'нет такого ключа'))
my_dict.update({'Петр': 1995, 'Кирил': 2007})
removed_year = my_dict.pop('Кирил')
print('Значение удалённого элемента \'Кирил\':', removed_year)
print('Изменённый словарь:', my_dict)

my_set = {4, 5, 5, 4, 7, True, True, False, True, 'Яблоко'}
print('Множество:', my_set)
my_set.add('Груша')
my_set.add(9)
my_set.discard(5)
print('Изменённое множество:', my_set)