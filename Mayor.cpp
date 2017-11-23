#include<iostream>

int main(){
    /*Este prgrama sirve para leer tres numeros enteros y devolver el mayor*/
    int n1,n2,n3,mayor,fin;
    std::cout<<"Escribe un numero: ";
    std::cin>>n1;
    std::cout<<"Escribe otro numero: ";
    std::cin>>n2;
    std::cout<<"Escribe otro numero: ";
    std::cin>>n3;
    if ( n1>n2 ){
         if ( n1>n3 ){
              mayor=n1;}}
    if ( n2>n1 ){
       if ( n2>n3 ){
              mayor=n2;}}
    if ( n3>n1 ){
         if ( n3>n2 ){
              mayor=n3;}}
    std::cout<<"El mayor es:";
    std::cout<<mayor;
    std::cin>>fin;
    return 0;
}
    
