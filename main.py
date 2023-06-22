# 1) Лениво заполнить матрицу от 1 до 9 и вывести квадратом разделяя значения пробелом
# 1 2 3
# 4 5 6
# 7 8 9
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for i in matrix:
#     print(i)
#
# 2) С клавы заполнить матрицу 5 х 5 и вывести
#
# arr = []
# for i in range(5):
#     a=[]
#     for j in range(5):
#         b = input("ввести значение ")
#         a.append(b)
#     arr.append(a)
# for i in arr:
#     print(i)

# 3)  С клавы заполнить матрицу пользовательского размера и вывести
# arr = []
# num = abs(int(input("ввести размер матрицы ")))
# for i in range(num):
#     a=[]
#     for j in range(num):
#         b = input("ввести значение ")
#         a.append(b)
#     arr.append(a)
# for i in arr:
#     print(i)

# 4) Принять у пользователя матрицу произвольного размера и посчитать сумму всех значений
# arr = []
# sum_values = 0
# num = abs(int(input("ввести размер матрицы ")))
# for i in range(num):
#     a=[]
#     for j in range(num):
#         b = int(input("ввести значение "))
#         sum_values = sum_values + b
#         a.append(b)
#     arr.append(a)
#
# for i in arr:
#     print(i)
# print("ваш результат", sum_values)

# 5) Принять у пользователя матрицу произвольного размера и посчитать сумму по каждому столбцу
# arr = []
# num = abs(int(input("ввести размер матрицы ")))
# for i in range(num):
#     a = []
#     for j in range(num):
#         b = int(input("ввести значение "))
#         a.append(b)
#     arr.append(a)
#
# for i in arr:
#     print(i)
#
# for row in range(len(arr)):
#     sum_row_col = 0
#     for col in range(len(arr)):
#         print(arr[col][row])
#         sum_row_col = sum_row_col + arr[col][row]
#     print()
#     print("ваш результат", sum_row_col)

# 6) Принять у пользователя матрицу произвольного размера и посчитать сумму по каждой строке
# arr = []
# num = abs(int(input("ввести размер матрицы ")))
# for i in range(num):
#     a = []
#     for j in range(num):
#         b = int(input("ввести значение "))
#         a.append(b)
#     arr.append(a)
#
# for i in arr:
#     print(i)
#
# for row in range(len(arr)):
#     sum_col_row = 0
#     for col in range(len(arr)):
#         print(arr[row][col])
#         sum_col_row = sum_col_row + arr[row][col]
#     print()
#     print("ваш результат", sum_col_row)

# 7) Принять у пользователя матрицу произвольного размера и посчитать сумму по каждой из диагоналей
# arr = []
# num = abs(int(input("ввести размер матрицы ")))
# for i in range(num):
#     a = []
#     for j in range(num):
#         b = int(input("ввести значение "))
#         a.append(b)
#     arr.append(a)
# for i in arr:
#     print(i)
#
# sum_first_diag = sum(arr[i][i] for i in range(num))
# sum_sec_diag = sum(arr[i][num - 1 - i] for i in range(num))
#
# print("Сумма по 1 диагонали: ", sum_first_diag)
# print("Сумма по 2 диагонали: ", sum_sec_diag)

# 8) Вывести матрицу 10 на 10 заполненую символом * по границам
# arr = []
# for i in range(10):
#     a=[]
#     for j in range(10):
#         b = input("ввести значение ")
#         a.append(b)
#     arr.append(a)
#
# arr = [['*' if i == 0 or i == 9 or j == 0 or j == 9 else ' ' for j in range(10)] for i in range(10)]
#
# for row in arr:
#     print(row)
# 9-12 ) Написать игру
# Суть в том, что появляется игровое поле 10 на 10 символов заполненное внутри пробелом, а внешне - *
# Появляется игрок в виде символа @
# Появляется враги в виде символа + (с каждым уровнем +1 )
# Суть игры в том, чтобы за минимальное количество шагов сьесть всех врагов
# Изначально есть 5 ходов
# За каждого врага +5 ходов
# Враги появляются по случайным координатам
#

