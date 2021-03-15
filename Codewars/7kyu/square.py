import math

def is_square(num):
    n = math.sqrt(num)
    if int(n+0.5)**2 == num:
        print([n,True])
    else:
        print(False)


is_square(25)