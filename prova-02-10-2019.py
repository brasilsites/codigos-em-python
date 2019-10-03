def main():
    '''
    02/10/2019
    Aluno: Edson Ferreira da Silva
    P3 - Sistemas da Informação
    '''
    questao=int(input("Informe a questao:"))

    if questao==1:
        ano=int(input("Informe o ano a pesquisar: "))
        #condicao 1: verificar se o ano pode ser dividido por 4 igualmente
        if ano%4==0:
            if ano%100==0:
                if ano%400==0:
                    print("Ano bissexto!")
                else:
                    print("Nao e um ano bissexto")
            else:
                print("Nao e um ano bissexto")

        else:
            print("Nao e um ano bissexto")

    if questao == 2:
        lista=[]
        for i in range(1,6):
            numero=int(input("Informe o "+str(i)+"° numero inteiro:"))
            lista.append(numero)
        for i in range(len(lista)):
            if lista[i]<=10:
                print("Numero menor ou igual a 10 encontrado: ",lista[i],"na posicao "+str(i))
main()
