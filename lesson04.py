import random
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов первого множества: "))
set_a = set(random.sample(range(1, 11), n))
m = int(input("Введите кол-во элементов второго множества: "))
set_b = set(random.sample(range(1, 11), m))

print(set_a)
print(set_b)
set_result = set_a.intersection(set_b)
print(set_result)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
n = int(input("Введите кол-во кустов на грядке: "))
array_blueberry = random.sample(range(1, 10), n)
print(array_blueberry)
max_blueberry = 0
stored_i = -1
for i in range(0, len(array_blueberry)):
    count_blueberry = 0
    if i + 2 < len(array_blueberry):
        count_blueberry = array_blueberry[i] + array_blueberry[i + 1] + array_blueberry[i + 2]
    elif i + 1 < len(array_blueberry):
        count_blueberry = array_blueberry[i] + array_blueberry[i + 1] + array_blueberry[0]
    else:
        count_blueberry = array_blueberry[i] + array_blueberry[1] + array_blueberry[0]
    if count_blueberry > max_blueberry:
        stored_i = i + 2    
    max_blueberry = max(max_blueberry, count_blueberry)
    print(f"{i} = {max_blueberry}")
    
print(f"Максимальное количестово ягод {max_blueberry} за один заход можно собрать подойдя к кусту {stored_i}")