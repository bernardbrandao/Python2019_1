import math

def ang_zenital(altura, sombra):
    tan = float(sombra) / float(altura)
    ang_rad = (math.atan(tan))
    ang_graus = (math.degrees(ang_rad)) 
    print("O angulo e aproximadamente ", "%.2f" % (ang_rad) , " radianos e corresponde a ", "%.2f" %(ang_graus), " graus.")

sombra = input("Digite o tamanho da sombra: ")

altura = input("Digite a altura do objeto: ")

ang_zenital(altura, sombra)
