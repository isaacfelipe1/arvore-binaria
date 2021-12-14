
class No:
    def __init__(self, data):
        self.data = data
        self.setaFilhos(None, None)
    def setaFilhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita
    def balanco(self):
        profundidade_esquerda = 0
        if self.esquerda:
            profundidade_esquerda = self.esquerda.profundidade()
        profundidade_direita = 0
        if self.direita:
            profundidade_direita = self.direita.profundidade()
        return profundidade_esquerda - profundidade_direita
    def profundidade(self):
        profundidade_esquerda = 0
        if self.esquerda:
            profundidade_esquerda = self.esquerda.profundidade()
        profundidade_direita = 0
        if self.direita:
            profundidade_direita = self.direita.profundidade()
        return 1 + max(profundidade_esquerda, profundidade_direita)
    def rotacaoEsquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        old_esquerda = self.esquerda
        self.setaFilhos(self.direita, self.direita.direita)
        self.esquerda.setaFilhos(old_esquerda, self.esquerda.esquerda)

    def rotacaoDireita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        old_direita = self.direita
        self.setaFilhos(self.esquerda.esquerda, self.esquerda)
        self.direita.setaFilhos(self.direita.direita, old_direita)

    def rotacaoEsquerdaDireita(self):
        self.esquerda.rotacaoEsquerda()
        self.rotacaoDireita()
    def rotacaoDireitaEsquerda(self):
        self.direita.rotacaoDireita()
        self.rotacaoEsquerda()
    def executaBalanco(self):
        balanco = self.balanco()
        if balanco > 1:
            if self.esquerda.balanco() > 0:
                print("Rotação esquerda: ",self.rotacaoDireita())
            else:
                print("Rotação Direita)",self.rotacaoEsquerdaDireita())
        elif balanco < -1:
            if self.direita.balanco() < 0:
                self.rotacaoEsquerda()
            else:
                self.rotacaoDireitaEsquerda()
    def insere(self, data):
        if data <= self.data:
            if not self.esquerda:
                self.esquerda = No(data)
            else:
                self.esquerda.insere(data)
        else:
            if not self.direita:
                self.direita = No(data)
            else:
                self.direita.insere(data)
        self.executaBalanco()
    def imprimeArvore(self, indent = 0):
        print ("" * indent + str(self.data))
        if self.esquerda:
           self.esquerda.imprimeArvore(indent + 2)
           print(">="*30)
        if self.direita:
            self.direita.imprimeArvore(indent + 2)
if __name__=="__main__":
    arvore=No(7)
    arvore.direita=No(19)
    arvore.direita.insere(45)
    arvore.direita.insere(48)
    arvore.esquerda=No(34)
    arvore.esquerda.insere(20)
    arvore.esquerda.insere(26)
    arvore.executaBalanco()
    arvore.imprimeArvore()
    #arvore.rotacaoDireita()
    #arvore.imprimeArvore()
    #arvore.rotacaoEsquerda()
    #arvore.imprimeArvore()
    
    

    
           