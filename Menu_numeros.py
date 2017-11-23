def suma(num1,num2):
        suma2=num1+num2
        return suma2
def resta(num1,num2):
        resta2=num1-num2
        return resta2
def multiplicacion(num1,num2):
        multiplica2=num1*num2
        return multiplica2
def division(num1,num2):
        dividi2=num1/num2
        return dividi2
        
def menu_numeros():
    seguir="Si"
    num1=input("Dime un numero: ")
    num2=input("Dime otro numero: ")
    while (seguir=="Si"):
        print "¿Que deseas hacer con los numeros?"
        print "1. Sumarlos"
        print "2. Restarlos"
        print "3. Multiplicarlos"
        print "4. Dividirlos"
        respuesta = input()
        if respuesta==1:
            print "Has elegido la opcion 1. Sumarlos"
            sumatotal=suma(num1,num2)
            print "La suma es: ", sumatotal
        if respuesta==2:
            print "Has elegido la opcion 2. Restarlos"
            restatotal=resta(num1,num2)
            print "La resta es: ", restatotal
        if respuesta==3:
            print "Has elegido la opcion 3. Multiplicarlos"
            multiplicaciontotal=multiplicacion(num1,num2)
            print "La multiplicacion es: ", multiplicaciontotal
        if respuesta==4:
            print "Has elegido la opcion 4. Dividirlos"
            divisiontotal=division(num1,num2)
            print "La division es: ", divisiontotal
        quieres =raw_input("¿Quieres seguir operando?: ")
        if (quieres=="Si"):
            seguir="Si"
            print "Has elegido -Seguir-"
        else:
            seguir="No"
            print "Has elegido -No seguir-"
menu_numeros()
