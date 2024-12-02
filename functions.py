import tkinter as tk

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left : Node | None = None
        self.right : Node | None = None

# A

def insert_node(root : Node, node : Node):
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

def search_tree(root : Node, number):
    if root is None:
        print("Não possui esse valor na árvore")
        return
    
    if root.data == number:
        print(f"{root.data} foi encontrado")
        return
    elif number < root.data:
        search_tree(root.left, number)
    else:
        search_tree(root.right, number)

# C
def print_tree(root: Node):
    if root == None:
        return "Árvore vazia"
    
    print(root.data)
    print_tree(root.left)
    print_tree(root.right)

# D
def count_nodes(root:Node):
    if root is None:
        return 0
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)

# E
def count_leaf(root:Node):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return count_leaf(root.left) + count_leaf(root.right)
    
# Draw

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
