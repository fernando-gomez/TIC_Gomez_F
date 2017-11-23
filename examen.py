def suma_impares():
    suma=0
    for cont in range (0,1001,1):
        if cont%2!=0:
            suma=suma+cont
    print suma
suma_impares()
