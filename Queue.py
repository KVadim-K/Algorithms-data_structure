class Queue:
    def __init__(self):
        self.items = []  # Создаем список для хранения элементов стека

    def isEmpty(self):
        return self.items == []  # Проверка на то пустая ли очередь
    def enqueue(self, item):
        self.items.insert(0, item)  # Добавление элемента в начало очереди

    def dequeue(self):
        return self.items.pop()  # Удаление элемента из начала очереди

    def size(self):
        return len(self.items)  # Просмотр размера очереди

# [1]
# [2, 1]
# [3, 2, 1]
# [4, 3, 2, 1]
# [5, 4, 3, 2, 1]

queue = Queue()
print(queue.isEmpty())  # проверка на пустой стек
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.isEmpty())  # проверка на пустой стек
print(queue.size())  # размер очереди
print(queue.dequeue())  # удаление 1 элемента из начала очереди
print(queue.size())  # размер очереди

