import turtle

t = input("Insira a cor que voce deseja para a cor de fundo: ")

jn = turtle.Screen()
jn.bgcolor(t)

cor_tartaruga = input("Insira a cor que voce deseja para a tartaruga: ")
largura_tartaruga = int(input("Insira largura voce deseja para a tartaruga: "))

teca = turtle.Turtle()       # Criar e configurar alguns atributos de Teca
teca.color(cor_tartaruga)
teca.pensize(largura_tartaruga)

turtle.speed(9)

for i in [0,1,2,3,4]:
	teca.forward(130)
	teca.left(144)
