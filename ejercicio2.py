'''
#determinar la sumatoria de numeros primos, no retorna valor y no pide valor
def sumaPrimos():
    print("Escriba un numero entero mayor a 1:")
    a=int(input())
    sum=0
    if a>1:
        for x in range(2,a+1):
            primo=1
            for y in range(2,x):
                if(x%y)==0:
                    primo=0
                    break
            if(primo==1):
                sum+=x          
        print("la sumatoria de los primos entre 1 y",a,"es",sum)
    else:
        print("El numero no es valido")
        
sumaPrimos()
'''
#determinar la sumatoria de numeros primos, con un valor y retornando la suma
def sumaPrimos(a):
    sum = 0
    if a > 1:
        for x in range(2, a + 1):
            primo = 1
            for y in range(2, x):
                if (x % y) == 0:
                    primo = 0
                    break
            if (primo == 1):
                sum += x
        return sum
    else:
        print("El numero no es valido")
x=sumaPrimos(-1)
print(x)