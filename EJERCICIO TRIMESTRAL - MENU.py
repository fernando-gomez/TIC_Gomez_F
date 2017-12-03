def suma_pares(n):
    pares=0
    while n>0:
        r=n%10
        n=n/10
        if r%2==0:
            pares=pares+r
    return pares
def suma_impares(n):
    impares=0
    while n>0:
        r=n%10
        n=n/10
        if r%2!=0:
            impares=impares+r
    return impares
def mayor (n):
    contador=0
    num=str(n)
    lista=list(num)
    for cont in range(0,len(lista),1):
        for i in range(0,len(lista),1):
            if lista[cont]>=lista[i]:
                contador=contador+1
                if contador==len(lista):
                    mayor=lista[cont]
        contador=0
        
    return mayor
def orden (n):
    num=str(n)
    lista=list(num)
    orden=list.sort(lista)
    return orden
def numeros():
    seguir="Si"
    while seguir=="Si":
        n=input("Dime un numero: ")
        print """1. Suma de sus cifras pares
    2. Suma de sus cifras impares
    3. Mayor de sus cifras
    4. Cifras ordenadas de menor a mayor"""
        o=input("¿Que quieres hacer?: ")
        if o==1:
            print "Has elegido la opcion 1. Suma de sus cifras pares"
            sumapares=suma_pares(n)
            print "La suma de sus cifras pares es: ", sumapares
        if o==2:
            print "Has elegido la opcion 2. Suma de sus cifras impares"
            sumaimpares=suma_impares(n)
            print "La suma de sus cifras impares es: ", sumaimpares
        if o==3:
            print "Has elegido la opcion 3. Mayor de sus cifras"
            ciframayor=mayor(n)
            print "La cifra mayor es: ", ciframayor
        if o==4:
            print "Has elegido la opcion 4. Cifras ordenadas de menor a mayor"
            num=str(n)
            lista=list(num)
            print "Sus cifras ordenadas de menor a mayor son:"
            print sorted(lista)
        quieres =raw_input("¿Quieres seguir operando?: ")
        if (quieres=="Si"):
            seguir="Si"
            print "Has elegido -Seguir-"
        else:
            seguir="No"
            print "Has elegido -No seguir-" 
numeros()
   

