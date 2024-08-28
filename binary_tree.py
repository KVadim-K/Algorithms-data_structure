class Node:
    def __init__(self, data):  # конструктор дерева
        self.left = None  # левое поддерево
        self.right = None  # правое поддерево
        self.value = data  # значение элемента

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

root = Node(70)
root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)

def printTree(root):
    if root:
        printTree(root.left)
        print(root.value)
        printTree(root.right)

printTree(root)


