class Sequencia(object):
    def __init__(self):
        self.dados=[]

    def listaCidade(self):
        self.dados=["rio grande do norte","maranhao","piaui","ceara","pernambuco","paraiba"]
    def inserirDados(self,dado):
        for i in range(len(dado)):
            self.dados.append(dado[i])

    def imprimeDados(self):
        return self.dados

    def removeDados(self):
        self.dados.pop()

    def insereNomeSobre(self,nome,sobrenome):
        self.dados.append(nome)
        self.dados.append(sobrenome)

    def topo(self):
        return self.dados[len(self.dados)-1]

class Pilha():
    def __init__(self):
        self.dados=["Amarelo","Vermelho","Verde","Azul"]

    def getPilha(self):
        return self.dados

    def buscaPosicao(self,valor):
        self.valor=valor
        posicao=self.dados.index(self.valor)
        return "a posicao do valor "+self.valor+" eh "+str(posicao)

    def inserirPosicao(self,novo):
        self.dados.append(novo)
