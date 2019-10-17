def main():
    matriz=[
        ["Bruna","12312345"],
        ["Alberto","11221122"]
    ]
    matriz.append("Eduardo")
    matriz[0].append("10.0")
    print(matriz)
    matriz=[
        [1,2,3,4],
        [5,6,7,8]
    ]
    matriz[0].append(int(input("1a matriz: ")))
    matriz[1].append(int(input("2a matriz: ")))

    print(matriz)

    valor=1.5

    print(type(valor))


    matriz=[]
    for i in range(2):
        linha=[]
        for j in range(4):
            linha.append(int(input("digite o item: ")))
        matriz.append(linha)
        print("-----------------")

    print(matriz)


    matriz=[]
    for i in range(4):
        linha=[]
        for j in range(4):
            linha.append(int(input("Digite o valor")))
        print("---------------------")
        matriz.append(linha)

    soma=0
    for i in range(len(matriz)):
        for j in range (len(matriz[i])):
            if (matriz[i][j]>10):
                print("O valor "+str(matriz[i][j])+" eh maior que 10")
                soma+=1

    print("O total de numeros maior que 10 eh "+str(soma))
    print(matriz)
main()
