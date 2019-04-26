import turtle

size_bin = float(input('Digite o tamanho do bin desejado: '))
cor_1 = (input('Digite a cor das linhas do histograma: '))
cor_2 = (input('Digite a cor para preencher o histograma: '))
nbins = int(input('Digite quantos bins voce quer para seu histograma: '))

x = 1
lista = []
print('Digite ', nbins, ' números.')
while x <= nbins:
    n = float(input('Digite um número: [ %s ]: '%x))
    lista.append(n)
    x += 1

print(lista)

print(type(lista))

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
#	if type(lista) == list
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(size_bin)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line
    #t.forward(10)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color(cor_1, cor_2)
tess.pensize(3)

for a in lista:
    draw_bar(tess, a)

#wn.mainloop()
