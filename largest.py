def x():
    num1=input()
    num2=input()
    num3=input()
    if (num1>=num2) and (num1>=num3):
        largest=num1
    if (num2>=num1) and (num2>=num3):
        largest=num2
    if(num3>=num1) and (num3>=num2):
        largest=num3
    print "The largest number between",num1,",",num2,"and",num3,"is", largest
x()
