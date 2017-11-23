/*Este programa sirve para leer 10 numeros enteros y que te devuelva el mayor*/
#include<iostream>
int main(){
    /*Definicion de variable*/
    int cont,n,mayor,salir;
    /*Bucle tipo for cont=cont+1 es lo mismo que cont++
    for (cont=0;cont<=10;cont--;)*/
    std::cout<<"Dime un numero entero: ";
    std::cin>>numero;
    mayor=numero;
    for (cont=0;cont<=10;cont=cont+1){
        std::cout<<"Dime un numero entero: ";
        std::cin>>n;
        if (n>mayor){
           mayor=n;}
        }
    std::cout<<"El mayor es: "<<mayor;
    std::cout<<"Toca cualquier letra para finalizar: ";
    std::cin>>salir;
    return 0;
}

    
