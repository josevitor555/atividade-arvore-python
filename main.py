#  Chamando os módulos
from index import BinaryTree

# Criando uma árvore binária
tree = BinaryTree("A")

# Inserindo nós à esquerda e à direita
tree.insert_left("B")
tree.insert_left("C")
tree.insert_left("D")

# Inserindo um nó à direita
tree.insert_right("E")
tree.insert_right("F")
tree.insert_right("G")
tree.insert_right("H")

# Acessando os nós filhos
left_child = tree.get_left_child()

# Acessando o nó filho esquerdo
right_child = tree.get_right_child()

# ------- Validando os métodos --------

# Visualizando a árvore
BinaryTree.print_tree(tree)

# Contanto as folhas
count_leaves = BinaryTree.count_sheets(tree)

print("-" * 30)
print("Total de folhas na árvore:", count_leaves)

# Método para contar os nós da árvore
count_nodes = BinaryTree.count_nodes(tree)
print("Total de nós na árvore:", count_nodes)

# Calcula a altura da subárvore direita
count_height = BinaryTree.height(tree)
print("Total de arestas (Altura da árvore):", count_height)

# Métodos para retornar o valor minimo e máximo
min_value = BinaryTree.min_value(tree)
print("Valor mínimo na árvore:", min_value)

# Método para retornar o valor máximo
max_value = BinaryTree.max_value(tree)
print("Valor máximo na árvore:", max_value)

# Método find
found_node = BinaryTree.find(tree, "A")
if found_node:
  print(f"Nó encontrado: {found_node.root}")
else:
  print("Nó não encontrado.")
