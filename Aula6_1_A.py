import turtle

t= turtle.Turtle()

def square(t):
	jn = turtle.Screen()         # Configurar a janela e seus atributos
	jn.bgcolor("lightyellow")
	jn.title("Quadrado")
	for i in range (4):
		t.forward(50)            
		t.left(90)

square(t)

