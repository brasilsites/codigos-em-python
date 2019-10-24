import arquifila

def main():
    filavar=arquifila.Fila()

    for i in range(5):
        filavar.inserirDado(str(input('Insira um dado')))
    print(filavar.getfila())

    valor=input('Qual valor deseja remover? ')
    filavar.removeDado(valor)
    print(filavar.getfila())
main()

'''fila=arquifila.Fila().getfila()

for i in range(len(fila)):
    print(fila[i],"\n")'''
