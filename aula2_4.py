lambda1 = 632.8 # em nm
lambda_convert = lambda1 *(10**(-9))

D = 1.98 #em m

d = 0.250 # em mm
d_convert = d *(10**(-3))

delta_y = (lambda_convert * D)/ d_convert

print('A distancia entre dois maximos de interferencia consecudivos e dada por', "%.2f" % ( delta_y * 100), 'em cm')
