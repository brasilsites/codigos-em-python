class Fila (object):
    def __init__(self):
        self.dados=[]
    def getfila(self):
        return self.dados
    def inserirDado(self,valor):
        self.dados.append(valor)
    def removeDado(self,valor):
        pos=self.dados.index(valor)
        self.dados.pop(pos)

