#include<iostream>

int main(){
    
    int a;
    int b;
    int c;
    int salir;
    int solucion;
    a=2;
    b=4;
    c=1;
    solucion=a+b+c;
    std::cout<<"La solucion es: "<< solucion << std::endl;
    std::cout<<"Para seguir, pulsa cualquier tecla";
    std::cin>>salir;
    return 0;
}
