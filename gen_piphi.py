# nice way to compute pi and phi using infinite sums and fibonacci
from math import factorial


def phi(n):
    x = 0
    a = 1
    for i in range(1, n):
        x = x + a
        a = x + a
    return a/x


def pi(n):
    s = 0
    for i in range(1, n):
        r = ((2**(i-1))*((factorial(i-1))**2))/(factorial(1+((i-1)*2)))
        s = s + r
    p = 2 * s
    return p

#add "if  __name__=="__main__"" here if main file.
inp = int(input("Quelle précision?  "))
inp2 = str(input("What number do you want, phi or pi?   "))

if inp2 == "phi":
    print("Phi vaut ", phi(inp), "!")
else:
    print("Pi vaut ", pi(inp), "!")
