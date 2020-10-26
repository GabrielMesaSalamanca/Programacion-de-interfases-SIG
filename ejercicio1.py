'''
#determinar si un numero es primo o no, no pide ningun valor y no retorna
def esPrimo():
    print("Escriba un numero entero:")
    a=int(raw_input())
    if a>1:
        for x in range(2,a):
            if (a%x)==0:
                print("El numero no es primo")
                break
        else:
            print("El numero es primo")
    else:
        print("El numero no es primo")
        
esPrimo()
        
'''


# determinar si un numero es primo o no, retorna falso o verdadero
def esPrimo(a):
    if a > 1:
        for x in range(2, a):
            if (a % x) == 0:
                return False
                break
        else:
            return True
    else:
        return False
print(esPrimo(55))