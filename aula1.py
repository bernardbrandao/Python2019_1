print('Este programa converte quilometros para milhas, calcula o tempo medio gasto por milha e a velocidade media em milhas por horas')

d = input('insira a distancia em quilometro ')

milha = float(d)/1.61

print('A distancia ', d, ' quilometros representa ', milha, 'milha')
print('Agora separe o tempo em 3 partes: horas, minutos e segundos')

h= input('insira a quantidade de horas ')

min = input('insira a quantidade de minutos ')
min = float(min) / 60

s = input('insira a quantidade de segundos ')
s = float(s)/3600

h_tot =  float(h) + min + s

print('A quantidade de horas ', h_tot)

vm = milha/h_tot

print('A velocidade media e ', vm, 'milhas/horas')

tempo = 1 / vm

print('O tempo gasto para percorrer uma milha:', tempo, 'horas')
