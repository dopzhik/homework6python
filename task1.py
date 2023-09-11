# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

from random import randint
number_1, diff, count = randint(1, 10), randint(2, 4), randint(3, 6)
print(number_1, diff, count)
my_list = [(number_1 + (num-1)*diff) for num in range(1, count+1)]
print(*my_list)
