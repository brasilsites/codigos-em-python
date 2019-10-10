def main():
    lista = [
        [39, 14, 27],
        [21, 83, 92],
        [31, 12, 43]
    ]
    #Primeiro loop, lista linha a linha
    for i in range(len(lista)):
        # Segundo loop, lista coluna a coluna da linha
        for j in range(len(lista[i])):
            #se o item da coluna j for igual ao tamanho da lista -1, chegou no final da lista
            if j == (len(lista[i])) - 1:
                #remova o ultimo elemento
                lista[i].remove(lista[i][j])
    print(lista)
main()

#matriz[1].remove("Alberto")
#matriz[0].pop(0)
