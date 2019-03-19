print('Este programa calcula a distancia entre o expectador de uma queima de fogos de atificios do Reveillon')

v_som = 343 #em m/s

print('Supondo que a luz chega aos olhos do observador depois de um tempo muito pequeno , ou seja, o tempo que a luz demora é de aproximadamente zero. Considerando a velocidade do som igual a ',  v_som,'m/s.') 

t_som = input('Insira o tempo que o som demorou achegar: ')

distancia = (float(t_som))*(int(v_som))

print('A distancia entre o local da queima de fogos e o boservador e de ', "%.2f" % distancia, 'metros')

