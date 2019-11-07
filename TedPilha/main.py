import TedPilha as t

carrega=t.Pilha()
resposta="s"
while (resposta=="s"):
    inserepilha1=(carrega.carregaPilha1(input("Insira um valor para a pilha 1: ")))
    resposta=input("Deseja continuar (s/n)? ")

resposta="s"
while (resposta=="s"):
    inserepilha2=(carrega.carregaPilha2(input("Insira um valor para a pilha 2: ")))
    resposta=input("Deseja continuar (s/n)? ")

print(carrega.testaMaisElementos())
