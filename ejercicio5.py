#ingresado un numero entero positivo encontrar su factorial
def factorial(a):
    if a>=0:
        fact=1
        while(a>0):
            fact *= a
            a-=1
        return fact
    else:
        print("El numero no es valido")
print(0,"Factorial es",factorial(0))

