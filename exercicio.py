def do_twice (f,g): 
    f (g) 
    f (g)

def print_spam (h): 
    print(h)
    print(h) 

#do_twice (print_spam,'spam')

def do_four(x,y):
    do_twice(x,y)
    do_twice(x,y)

do_four(print_spam,'spam')
