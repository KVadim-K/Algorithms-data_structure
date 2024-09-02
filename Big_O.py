# O(1) - Константная сложность означает, что время выполнения алгоритма не зависит от размера входных данных.
def get_element(arr, index): # Доступ к элементу массива по индексу
    return arr[index]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_element(arr, 4))

# O(n) -Линейная сложность алгоритма означает, что время выполнения алгоритма пропорционально количеству входных данных.
def line_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(line_search(arr, 30))
print(line_search(arr, 60))

# O(log n) = Логарифмическая сложность означает, что время выполнения алгоритма увеличивается логарифмически с увеличением размера входных данных.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(arr, 70))
print(binary_search(arr, 25))



