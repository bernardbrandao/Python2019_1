import turtle

t= turtle.Turtle()

lenght = int(input("Digite o tamanho do lado do seu poligono: "))
n = int(input("Digite o numero de lados do seu poligono: "))

def polygon(t,lenght,n):
	jn = turtle.Screen()         # Configurar a janela e seus atributos
	jn.bgcolor("lightyellow")
	jn.title("Polygon")
	perimetro = n * lenght
	for i in range (n):
		t.forward(lenght)            
		t.left(360/n)

def circle(t,r):
	r = n * 
	t.color(red)
	t.circle(n * lenght)		

#polygon(t,lenght,n)
circle(t,r)
