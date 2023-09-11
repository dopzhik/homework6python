# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: 6, 13
# [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
min_num = randint(3, 8)
max_num = randint(min_num+1, 15)
print(min_num, max_num)
list_1 = [randint(-10, 20) for _ in range(20)]
print(list_1)
cur_list = [i for i in range(20) if list_1[i] in range(min_num, max_num+1)]
print(cur_list)
print(range(min_num, max_num))
