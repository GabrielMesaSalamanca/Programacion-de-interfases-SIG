#Numero de años, meses, semanas y dias a partir de numero de dias
def num(a):
    if(a>=0):
        dias = a
        años = a/365
        meses=a/31
        semanas=a/7
        return dias,semanas,meses,años
    else:
        print("El numero no es valido")
x,y,z,w=num(4564)
print("Dias =",x,"\nSemanas =",y,"\nMeses =",z,"\nAños =",w)
