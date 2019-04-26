import turtle

t= turtle.Turtle()

lenght = int(input("Digite o tamanho do lado do quadrado: "))

def square(t,lenght):
	jn = turtle.Screen()         # Configurar a janela e seus atributos#
	jn.bgcolor("lightyellow")
	jn.title("Quadrado")
	for i in range (4):
		t.forward(lenght)            
		t.left(90)

square(t,lenght)

