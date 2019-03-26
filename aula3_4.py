import math

def km_to_mile(km):
    mile = km / 1.61
    print("O valor de ", "%.2f" % (km), " quilometros corresponde a ", "%.2f" %(mile), " milhas")

def mile_to_km(mile):
    km = mile * 1.61
    print("O valor de ", "%.2f" % (mile), " milhas corresponde a ", "%.2f" %(km), " quilometros")

def tempo_to_h(seg, minutos, h):
    h1 = seg / 3600
    h2 = minutos / 60
    h_tot = h1 + h2 + h    
    print("O valor de ", "%.2f" % (seg), "segundos e ", "%.2f" %(minutos), " minutos equivale a ", "%.2f" % (h_tot) , " horas")

def tempo_to_s(seg):
    s1 = minutos * 60
    s2 = h * 3600
    seg = s1 + s2
    print("O valor de ", "%.2f" % (h) , " horas e ", "%.2f" %(minutos)," minutos equivale a ", "%.2f" % (seg) , " segundos")

def velocidade_media(km,h_tot):
    vm_km = km / h_tot
    print("A velocidade media e ", vm_km, "km/s")

def tempo_km(vm_km):
    t_km = 1/vm_km
    print("O tempo gasto por km e ", t_km, "horas")

h = input("Digite a quantidade de horas: ")
minutos = input("Digite a quantidade de minutos: ")
seg = input("Digite a quantidade de segundos: ")
mile = input("Digite o espaco em milhas: ")

velocidade_media(km,h_tot)


