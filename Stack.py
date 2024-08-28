class Stack:
    def __init__(self):
        self.items = []  # Создаем список для хранения элементов стека

    def isEmpty(self):
        return self.items == []  # Проверка на пустой стек

    def push(self, item):
        self.items.append(item)  # Добавление элемента в конец стека

    def pop(self):
        return self.items.pop()  # Удаление элемента из конца стека

    def peek(self):
        return self.items[len(self.items)-1]  # Просмотр последнего элемента стека

    def size(self):
        return len(self.items)  # Просмотр размера стека


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.isEmpty())  # проверка на пустой стек
print(stack.pop())  # удаление элемента из конца стека после его просмотра это 3
print(stack.peek())  # просмотр последнего элемента
print(stack.size())  # размер стека

while not stack.isEmpty():  # пока стек не пустой
    print(stack.pop())  # удаление элемента из конца стека
