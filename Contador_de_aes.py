def Contador_vocales():
    palabra=raw_input ('Dime una palabra')
    suma=[0,0,0,0,0]
    for cont in range(0,len(palabra),1):
        if palabra[cont]=='a':
            suma[0]=suma[0]+1
        if palabra[cont]=='e':
            suma[1]=suma[1]+1
        if palabra[cont]=='i':
            suma[2]=suma[2]+1
        if palabra[cont]=='o':
            suma[3]=suma[3]+1
        if palabra[cont]=='u':
            suma[4]=suma[4]+1
    print "La palabra ",palabra," tiene",suma[0], " aes"
    print "La palabra ",palabra," tiene",suma[1], " ees"
    print "La palabra ",palabra," tiene",suma[2], " ies"
    print "La palabra ",palabra," tiene",suma[3], " oes"
    print "La palabra ",palabra," tiene",suma[4], " ues"
    
Contador_vocales()
