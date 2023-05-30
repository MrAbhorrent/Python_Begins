import random

def divider_line(n=50):
    print("=" * n)
    
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
n = int(input("Введите количество элементов в массиве: "))

def create_arrray(n):
    lower_border = 1
    high_border = 10
    new_array = []
    for i in range(n):
        new_array.append(random.randint(lower_border, high_border))
    return new_array

array = create_arrray(n)
print(array)
x = int(input("Input number X: "))

countX = sum(i==x for i in array)
print(f"{x} -> {countX}")
divider_line()

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

value_x = int(input("Input number X: "))
print(array)
search_number = array[0]
delta_begin = abs(value_x - array[0])
for i in array:
    delta = abs(value_x - i)
    if (delta < delta_begin):
        delta_begin = delta
        search_number = i
        
print(f"{value_x} -> nearest value {search_number}")
divider_line()

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
eng = {1: 'AEIOULNSTR', 
       2: 'DG', 
       3: 'BCMP', 
       4: 'FHVWY', 
       5: 'K', 
       8: 'JZ',
       10: 'QZ'}
rus = {1: 'АВЕИНОРСТ', 
       2: 'ДКЛМПУ', 
       3: 'БГЁЬЯ', 
       4: 'ЙЫ', 
       5: 'ЖЗХЦЧ',
       8: 'ШЭЮ',
       10: 'ФЩЪ'}
condition = False
answer = 0
while not condition:
    if condition:
        break
    answer = abs(int(input("Please choose your language 1 - Eng / 0 - Rus")))
    if answer not in [0,1]:
        print("Please input 1 or 0: ")
    else:
        condition = True

if answer == 1:
    user_text = input("Please input a word what you need count: ").upper()
    print(f"You have been earned "
          f"{sum([k for i in user_text for k, v in eng.items() if i in v])}"
          f" points")
else:
    user_text = input("Пожалуйста, ведите слово которе надо посчитать: ").upper()
    print(f"Вы заработали "
          f"{sum([k for i in user_text for k, v in rus.items() if i in v])}"
          f" очков")    