def numeros():
    pares=0
    n=input("Dime un numero: ")
    print """1. Suma de sus cifras pares
2. Suma de sus cifras impares
3. Mayor de sus cifras
4. Cifras ordenadas de menor a mayor"""
    o=input("¿Que quieres hacer?: ")
    if o==1:
        while n>0:
            r=n%10
            n=n/10
            if r %2==0:
                pares=pares +r
        print pares
numeros()
   

