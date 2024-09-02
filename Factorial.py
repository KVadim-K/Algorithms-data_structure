# Факториальная сложность (O(n!)) встречается довольно редко и обычно связана с задачами,
# где необходимо перебрать все возможные перестановки элементов.

import math
from itertools import permutations

def generate_permutations(elements):
    all_permutations = list(permutations(elements))
    for perm in all_permutations:
        print(perm)

# Пример использования
elements = [1, 2, 3]
generate_permutations(elements)
print(f"Количество перестановок из {len(elements)} элементов ({len(elements)}!) равно {math.factorial(len(elements))}")
