def cifras():
    numero=input("Dime un numero: ")
    cifras=0
    while numero>0:
        numero=numero/10
        cifras=cifras+1
    print cifras
cifras()

def orden_numeros():
    numero=input("Dime un numero: ")
    str_numero=str(numero)
    lista=list(str_numero)
    orden=list.sort([lista])
    print orden
orden_numeros()
