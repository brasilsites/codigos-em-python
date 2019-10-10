def main():
    lista = [
            [39, 14, 27],
            [21, 83, 92],
            [31, 12, 43]
    ]
    '''
    for i in range(len(lista)):
        print ("---- Lista "+str(i+1)+" ----")
        for j in range (len(lista[i])):
            print (str(lista[i][j])+" x7 = "+str(lista[i][j]*7))
    '''
    for i in range(len(lista)):
        for j in range (len(lista[i])):
            if j==(len(lista[i]))-1:
               lista[i].remove(lista[i][j])
                
    print(lista)
main()

#matriz[1].remove("Alberto")
#matriz[0].pop(0)
