a=int(input('Enter a whole number:   '))
b=int(input('Enter another whole number:   '))
def pythagoras(a,b):
    ab= abs(a**2-b**2)
    ac=2*a*b
    bc=a**2+b**2
    if a==b:
        return("Dude!It's a flattened triangle! It can't work")
    elif a==0 or b==0:
        return("Dude! It's a flattened triangle! It can't work!")
    else:
        return(ab,ac,bc)
print('Here is your Pythagoras triplet:',pythagoras(a,b))
    


