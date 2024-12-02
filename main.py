from functions import *

numbers = [100, 50, 200, 70, 140, 30, 350, 117, 400, 42, 80, 65]

root = create_tree(numbers)
search_tree(root, 117)
# print_tree(root)
print(f"Possui {count_nodes(root)} nós")
print(f"Possui {count_leaf(root)} folhas")
# display_tree(root)