def sumador_numeros():
    suma=0
    numero=input("Dime un numero")
    lista=list(numero)
    for cont in range(0,len(numero),1):
        suma+lista[cont]=suma
    print cont
sumador_numeros()
            
        
