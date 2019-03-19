print('Este codigo calcula os zeros da funcao')

a = 3

b = -4

c = -10

delta = (b ** 2) - 4 * a * c

x_01 = (-b + ((delta)**(1/2)))/(2*a)

x_02 = (-b - ((delta)**(1/2)))/(2*a)

print('Os zeros da funcao acontecem quando x = ', "%.2f" % x_01 , ' e x = ' , "%.2f" % x_02)
