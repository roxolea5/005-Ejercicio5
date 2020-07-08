def square(x):
    return x*x

square(5)

def launch_missiles():
    print('Missiles launched')

launch_missiles()

def even_or_odd(n):
    if n%2==0:
        print('even')
        return
    print('odd')

even_or_odd(4)
even_or_odd(5)

w = even_or_odd(31)

w is None