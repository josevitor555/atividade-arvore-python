# Árvore binrária em Python

# Introdução
# Este módulo implementa uma árvore binária simples em Python.

class BinaryTree:
  def __init__(self, object) -> None:
    
    """Inicializa a árvore binária com um nó raiz."""
    self.root = object
    self.left_child = None
    self.right_child = None
    self.parent = None # Mudanças sucessor e predecessor
    
  # Método para inserir um novo nó na árvore
  
  # 1 - Método para inserir um nó à esquerda
  def insert_left(self, newBranch):
    
    """Insere um novo nó à esquerda do nó atual."""
    if self.left_child is None:
      self.left_child = BinaryTree(newBranch)
      self.left_child.parent = self
    else:
      tree = BinaryTree(newBranch)
      tree.left_child = self.left_child
      self.left_child.parent = tree
      self.left_child = tree
    
  # 2 - Método para inserir um nó à direita
  def insert_right(self, newBranch):
    
    """Insere um novo nó à direita do nó atual."""
    if self.right_child is None:
      self.right_child = BinaryTree(newBranch)
      self.right_child.parent = self
    else:
      tree = BinaryTree(newBranch)
      tree.right_child = self.right_child
      self.right_child.parent = tree
      self.right_child = tree
      
  # Método insert (chamando os métodos de inserção insert_left e insert_right)
  # def insert(self, newBranch):
    
  #   """Insere um novo nó na árvore."""
  #   if self.left_child is None:
  #     self.insert_left(newBranch)
  #   elif self.right_child is None:
  #     self.insert_right(newBranch)
  #   else:
  #     print("A árvore já está cheia.")
  
  # Pegar o nó filho esquerdo
  def get_left_child(self):
    
    """Retorna o nó filho esquerdo."""
    return self.left_child
  
  # Pegar o nó filho direito
  def get_right_child(self):
    
    """Retorna o nó filho direito."""
    return self.right_child
  
  # Pegar o nó pai
  def getRootVal(self):
    
    """Retorna o nó pai."""
    return self.root # Retorna o valor do nó raiz
  
  def setRootVal(self, value):
    
    """Define o valor do nó raiz."""
    self.root = value
    
  # Métodos de percurso da árvore
  
  
  # 1 - Percurso em ordem (In-order)
  def in_order(self):
    
    """Percurso ordem."""    
    if self.left_child:
      self.left_child.in_order()
    
    # Imprime o nó atual
    print(self.root)
    if self.right_child:
      self.right_child.in_order()
  
  # 2 - Percurso pré-ordem (pre-order)
  def pre_order(self):
    
    print(self.root)
    
    """Percurso pré-ordem."""    
    if self.left_child:
      self.left_child.pre_order()
    
    # Imprime o nó atual
    print(self.root)
    if self.right_child:
      self.right_child.pre_order()
  
  # 3 - Percurso pós-ordem (post-order)
  def post_order(self):
    
    """Percurso pós-ordem."""
    if self.left_child:
      self.left_child.post_order()
    
    if self.right_child:
      self.right_child.post_order()
    
    # Imprime o nó atual
    print(self.root)
  
  # Método para contar folhas (sheets)
  def count_sheets(self):
    
    # Se não houver filhos, é uma folha
    if not self.left_child and not self.right_child:
      return 1
    
    # Se houver filhos, conta as folhas nos filhos
    if self.left_child:
      left_sheets = self.left_child.count_sheets()
    else:
      left_sheets = 0
    
    # Se houver filhos, conta as folhas nos filhos
    if self.right_child:
      right_count = self.right_child.count_sheets()
    else:
      right_count = 0
    
    # Retorna a soma das folhas dos filhos
    return left_sheets + right_count    
  
  # Método para contar nós
  def count_nodes(self):
    
    """Conta o número de nós na árvore."""
    
    # Conta o número de nós 
    if self.left_child:
      print(f"Nó esquerdo: {self.left_child.root}")
      
      # Conta os nós do filho esquerdo
      
      count_left = self.left_child.count_nodes()
      # print(count_left)
    else:
      count_left = 0 # Se não houver filho esquerdo, conta como 0
      
    if self.right_child:
      print(f"Nó direito: {self.right_child.root}")
      
      # Conta os nós do filho direito
      count_right = self.right_child.count_nodes()
      # print(count_right)
    else:
      count_right = 0
    
    return 1 + count_left + count_right  # Conta o nó atual + nós dos filhos
  
  # Método para verificar a altura da árvore
  def height(self):
    
    # Calcula a altura da subárvore esquerda
    # if self.left_child:
    #   left_height = self.left_child.height() # Recursão para calcular a altura
    # else:
    #   left_height = 0
    
    # # Calcula a altura da subárvore direita
    # if self.right_child:
    #   right_height = self.right_child.height()
    # else:
    #   right_height = 0
    
    if not self.left_child and not self.right_child:
      return 0
      
    left_height = self.left_child.height() if self.left_child else 0
    right_height = self.right_child.height() if self.right_child else 0
    
    # Retorna a altura máxima entre as duas subárvores + 1 para o nó atual
    return 1 + max(left_height, right_height)
  
  # Método para buscar o valor minimo (min_value)
  def min_value(self):
    if self.left_child:
      return self.left_child.min_value()
    
    return self.root  # Se não houver filho esquerdo, o nó atual é o mínimo  
  
  # Método para buscar o valor máximo (max_value)
  def max_value(self):
    if self.right_child:
      return self.right_child.max_value()
    
    return self.root  # Se não houver filho direito, o nó atual é o máximo
  
  # Método para retornar o sucessor
  def successor(self):
    
    # Caso tenha filho a direita
    if self.right_child:
      node_successor = self.right_child.min_value() # O sucessor é o menor valor da subárvore direita
    else:
      
      # Vamos precisar add novo atributo: parent do nó
      node_current = self
      parent = self.parent
      
      # Repeticao deve verificar se tem parente e se está a esquerda
      while parent and node_current == parent.get_right_child():
        node_current = parent
        parent = parent.parent
      
      node_successor = parent # Se o nó atual for o último filho a direita, o sucessor é o pai
    
    # Se não tiver filho a direita, o sucessor é o pai
    return node_successor
  
  # Método de busca
  def find(self, value):
    
    # Verifica se o valor é igual ao nó atual
    if value == self.root:
      return self
    
    # # Se o valor for menor, busca na subárvore esquerda
    # if value > self.root and self.right_child:
    #   return self.right_child.find(value)
    
    # # Se o valor for maior, busca na subárvore direita
    # if value < self.root and self.left_child:
    #   return self.left_child.find(value)
    
    # Se o valor for maior, busca na subárvore direita
    if self.left_child:
      found = self.left_child.find(value)
      if found:
        return found # Se encontrar na subárvore esquerda, retorna o nó encontrado
    
    # Se o valor for menor, busca na subárvore direita
    if self.right_child:
      found = self.right_child.find(value)
      if found:
        return found # Se encontrar na subárvore direita, retorna o nó encontrado
    
    return False
  
  # Impressão da árvore
  def print_tree(self, level=0, prefix="Root: "):
    
    print(" " * (level * 4) + prefix + str(self.root))
    if self.left_child:
      self.left_child.print_tree(level + 1, "L--- ")
    if self.right_child:
      self.right_child.print_tree(level + 1, "R--- ")
  