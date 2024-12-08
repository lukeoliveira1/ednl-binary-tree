import tkinter as tk
from queue import Queue


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


# A


def insert_node(root: Node, node: Node):
    if node.data > root.data:
        if root.right is None:
            root.right = node
        else:
            insert_node(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert_node(root.left, node)

    return root


def create_tree(numbers):
    root = Node(numbers[0])
    for i in numbers[1:]:
        insert_node(root, Node(i))
    return root


# B


def search_tree(root: Node, number):
    if root is None:
        return False

    if root.data == number:
        return True 
    elif number < root.data:
        return search_tree(root.left, number)
    else:
        return search_tree(root.right, number)


# C


def print_tree(root: Node, level):
    if root == None:
        return "Árvore vazia"

    if root.left:
        print_tree(root.left, level+3)

    print("  " * level + str(root.data))

    if root.right:
        print("")
        print_tree(root.right, level+3)


# D


def count_nodes(root: Node):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)


# E


def count_leaf(root: Node):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return count_leaf(root.left) + count_leaf(root.right)


# F


def search_successor(current: Node):
    current = current.right
    while current and current.left:
        current = current.left
    return current


def delete_node(root: Node, to_remove):
    # base case
    if root is None:
        return root

    # chegar no node para deletar
    elif to_remove < root.data:
        root.left = delete_node(root.left, to_remove)
    # chegar no node para deletar
    elif to_remove > root.data:
        root.right = delete_node(root.right, to_remove)

    else:
        # chegou no node para ser deletado

        # 0 ou 1 filhos
        if root.left is None:
            return root.right # se não tem filho, vai retornar None
        if root.right is None:
            return root.left # se não tem filho, vai retornar None
        
        # pior caso, quando tem dois filhos
        succ: Node = search_successor(root)
        root.data = succ.data
        # deletar o valor repetido
        root.right = delete_node(root.right, succ.data)

    return root


# G


#     usar fila
#     coloca A na fila
#     adicionar filhos de A
#     remove A
#     adiciona filhos de B
#     remove B
#     adiciona filhos de C
#     remove C


def visit(root: Node):
    print(root.data)


def levels_path(root: Node):
    if not root:
        return

    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current = queue.get()
        visit(current)

        if current.left:
            queue.put(current.left)
        if current.right:
            queue.put(current.right)


# H


def pre_order(root: Node):
    visit(root)

    if root.left is not None:
        pre_order(root.left)

    if root.right is not None:
        pre_order(root.right)


def simetric(root: Node):
    if root.left is not None:
        simetric(root.left)

    visit(root)

    if root.right is not None:
        simetric(root.right)


def post_order(root: Node):
    if root.left is not None:
        post_order(root.left)

    if root.right is not None:
        post_order(root.right)

    visit(root)


# draw


def draw_tree(canvas, node, x, y, dx):
    if node is None:
        return

    # desenha o nó
    canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="lightblue")
    canvas.create_text(x, y, text=str(node.data), font=("Arial", 12))

    # desenha as linhas para os filhos
    if node.left:
        canvas.create_line(x, y, x - dx, y + 50, arrow=tk.LAST)
        draw_tree(canvas, node.left, x - dx, y + 50, dx // 2)
    if node.right:
        canvas.create_line(x, y, x + dx, y + 50, arrow=tk.LAST)
        draw_tree(canvas, node.right, x + dx, y + 50, dx // 2)


def display_tree(root):
    window = tk.Tk()
    window.title("Árvore Binária")

    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()

    draw_tree(canvas, root, 400, 50, 150)

    window.mainloop()
