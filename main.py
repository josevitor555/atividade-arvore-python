#  Chamando os módulos
from index import BinaryTree
from binarytree import Node, build

# Criando uma árvore binária

# tree = BinaryTree("A")

# # Inserindo nós à esquerda e à direita
# tree.insert_left("B")
# tree.insert_left("C")
# tree.insert_left("D")

# # Inserindo um nó à direita
# tree.insert_right("E")
# tree.insert_right("F")
# tree.insert_right("G")
# tree.insert_right("H")

# Function to convert your BinaryTree to binarytree.Node for visualization
def convert_to_binarytree_node(tree):
    if not tree:
        return None
    node = Node(tree.root)
    node.left = convert_to_binarytree_node(tree.get_left_child())
    node.right = convert_to_binarytree_node(tree.get_right_child())
    return node

#  Criando a 
tree = BinaryTree(4)

# Inserindo nós a arvore

# Valores menores que 4 (Root)
tree.insert(3)
tree.insert(2)
tree.insert(0)

# Valores maiores que 4 (Root)
tree.insert(8)
tree.insert(9)
tree.insert(7)
tree.insert(5)

# Caso 1: Nó sem filhos (Nó folhas)
# tree.delete(2) # Ok

# Caso 2: Nó com um filho
# tree.delete(5) # Ok

# Caso 3: Nó com dois filhos (substituir pelo sucessor)
# tree.delete(10) # Ok

# Convert to binarytree.Node for visualization
binarytree_root = convert_to_binarytree_node(tree)

# Print the tree in the console
print("Visualização da árvore binária: ")
print(binarytree_root)

from graphviz import Digraph

def save_tree_as_png(root, filename="binary_tree"):
  dot = Digraph()
  def add_nodes_edges(node, dot_graph):
    if not node:
      return
    
    dot.node(str(node.value))
    if node.left:
      dot.edge(str(node.value), str(node.left.value))
      add_nodes_edges(node.left, dot_graph)
      
      if node.right:
        dot.edge(str(node.value), str(node.right.value))
        add_nodes_edges(node.right, dot_graph)
        add_nodes_edges(root, dot)
        dot.render(filename, format="png", cleanup=True)
        print(f"Tree saved as {filename}.png")


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
found_node = BinaryTree.find(tree, 10)
if found_node:
  print(f"Nó encontrado: {found_node.root}")
else:
  print("Nó não encontrado.")
  
print("-" * 60)
  
# Método inorder
print("Arvore in-order - esquerda, raiz, direita: ")
BinaryTree.in_order(tree)

print("-" * 60)

# Método preorder
print("Arvore pre-order - raiz, esquerda, direita: ")
BinaryTree.pre_order(tree)

print("-" * 60)

# Método postOrder
print("Arvore post-order - esquerda, direita, raiz: ")
BinaryTree.post_order(tree)

# Salvando como png
save_tree_as_png(binarytree_root)