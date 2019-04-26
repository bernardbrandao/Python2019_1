import math

def maior(x,y,z):
    if ((x>y) and (x>z)):
        return print("O valor maior e: ", x)
    if ((y>x) and (y>z)):
        return print("O valor maior e: ", y)
    if ((z>x) and (z>y)):
        return print("O valor maior e: ", z)

x = float(input("Digite um valor: "))
y = float(input("Digite outro valor: "))
z = float(input("Digite outro valor: "))

maior(x,y,z)
