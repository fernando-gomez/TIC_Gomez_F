def nif2():
    letras="TRWAGMYFPDXBNJZSQVHLCKE"
    n=input("Dime tu numero de DNI: ")
    resto=n%23
    print "Tu DNI entero es: ", n, "-",letras[resto]
nif2()
