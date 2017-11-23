def texto_us():
    texto=raw_input ('Escribe algo')
    lista1=list(texto)
    for cont in range(0,len(texto),1):
        if texto[cont]=="a"or texto[cont]=="e" or texto[cont]=="i"or texto[cont]=="o":
            lista1[cont]="u" 
    listafinal="".join(lista1)
    print listafinal
texto_us()
    
            
            
