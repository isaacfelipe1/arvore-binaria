"""Construindo uma arvore binária"""
class Node:#Construindo um nó da raiz, esquerda e direita
    def __init__(self,data):
        self.data=data
        self.esquerda=None
        self.direita=None
    def __str__(self):#transformando em string
        return str(self.data)
class arvore_binaria:#para dizer quem é raiz e para conter metodos
    def __init__(self,data):
        node=Node(data)
        self.root=node
if __name__=="__main__":
    arvore=arvore_binaria(7)
    arvore.root.esquerda=Node(18)
    arvore.root.direita=Node(14)
    print(f'Raíz da Arvore :{arvore.root}')
    print(f'Lado esquerdo da Arvore:{arvore.root.direita}')
    print(f'Lado Direito da Arvore:{arvore.root.esquerda}')

       
