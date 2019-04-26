import math

def multiplicar(list):
	x = (list[0])
	for i in range(1,len(list)):
		x = x * (list[i])
		print("A multiplicacao dos valores da lista e: ", x)
		

list = [1,2,3,4,5,8,9,10]  

multiplicar(list)
