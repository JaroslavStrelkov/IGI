import numpy as np

def run_task5():
    A = np.random.randint(-10, 10, size=(8, 8))
    print("Матрица A:")
    print(A)

    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nСоздание массива с помощью array:")
    print(arr1)

    arr2 = np.zeros((3, 3), dtype=int)
    arr3 = np.ones((6,7), dtype=int)
    print("Создание нулевого массива (3x3):")
    print(arr2)
    print("Создание массива из единиц (6x7):")
    print(arr3)

    print("Элемент A[6, 7]:", A[5, 6])
    print("Срез шестой строки A[0, :]:", A[5, :])
    print("Срез седьмого столбца A[:, 0]:", A[:, 6])

    A_squared = np.square(A)
    print("\nМатрица A в квадрате (поэлементно):")
    print(A_squared)
    
    print("\nМатематические и статистические характеристики:")
    print("Среднее значение всей матрицы:", np.mean(A))
    print("Медиана всей матрицы:", np.median(A))
    print("Коэффициент корреляции (пример для строк 0 и 1):", np.corrcoef(A[0, :], A[1, :]))
    print("Дисперсия всей матрицы:", np.var(A))
    print("Стандартное отклонение всей матрицы:", np.std(A))

    min_el = np.min(A)
    woIst = np.argwhere(A == min_el)[0]
    row_indx = woIst[0]
    newMatrix = np.insert(A, row_indx + 1, A[0], axis = 0)
    print(newMatrix)

    first_row = A[0, :]
    median_np = np.median(first_row)
    print(f"Медиана первой строки np-version: {median_np}")

    sorted_row = np.sort(first_row)
    l = len(sorted_row)
    if l % 2 == 0:
        my_median = (sorted_row[l//2 - 1] + sorted_row[l//2]) / 2
    else:
        my_median = sorted_row[l//2]
    print(f"Медиана первой строки my-version: {my_median}")

if __name__ == "__main__":
    run_task5()