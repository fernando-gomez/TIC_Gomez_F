def cual_par():
    pares=0
    n=input("Dime un numero: ")
    while n>1:
        if (n%10)%2==0:
            pares=pares+1
        n=n/10
    print "El numero tiene ",pares," pares"
cual_par()
