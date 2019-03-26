import math

def IMC(massa,altura):
    imc = float(massa) / ((float(altura))**2)
    print('o indice de massa corporal e ', "%.2f" % imc)

altura = input("Digite a altura da pessoa: ")
massa = input("Digite a massa da pessoa: ")
IMC(massa,altura)

def calc_vol(r):## em metros cubicos
    Volume = (4/3)*(math.pi)* float(r)**3
    print('O volume e ',"%.2f" % Volume, "metros cubicos")

r = input('Insira o Raio da Esfera em metros: ')
calc_vol(r)

def d_max(D,lambda1,d)
    lambda_convert = lambda1 *(10**(-9))
    d_convert = d *(10**(-3))
    delta_y = (lambda_convert * D)/ d_convert
    print("A distancia entre dois maximosde interferencia consecutivos e ", delta_y, "metros")

D = input("Digite a distancia do anteparo a fenda em metros")
d = input("Digite o espaçamento entre as fendas em mm")
lambda1 = input("Digite o comprimento de onda em metros")
