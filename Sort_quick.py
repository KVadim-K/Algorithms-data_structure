def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = list(filter(lambda i: i < element, s))  # используем список list с помощью лямбда-функции filter для отбора элементов меньше элемента
    center = [i for i in s if i==element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)  # сортируем левую часть, центральную часть и правую часть

print(quick_sort([5, 2, 9, 0, 1, 5, 3]))