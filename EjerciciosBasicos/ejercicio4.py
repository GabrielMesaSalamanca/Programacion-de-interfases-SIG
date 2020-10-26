#numero de digitos de un numero
def digitos(a):
    num=a
    digitos=0
    while abs(num)>=1:
        num/=10
        digitos+=1
    return digitos
print(digitos(10000))
