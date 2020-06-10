'''This project allows you to obtain the arc length over a chosen interval for a chosen function'''
from math import sqrt,sin

def givehyp1(x,y):
    a=x*x
    b=y*y
    w=sqrt((b-a)**2+(y-x)**2)
    return(w)

def givehyp2(x,y):
    if x<0 or y<0:
        return("error")
    else:
        a=sqrt(x)
        b=sqrt(y)
        w=sqrt((b-a)**2+(x-a)**2)
        return(w)
    return(x)
def givehyp3(x,y):
    b=x**3
    a=y**3
    w=sqrt((a-b)**2+(y-x)**2)
    return(w)
    
def givesin(x,y):
    if x==0 or y==0:
        return("error")
    else:
        a=sin(x)
        b=sin(y)
        w=sqrt((b-a)**2+(y-x)**2)
        return(w)

def givelength(a,b,c):
    dx=a/b
    tx=0
    if c!=4:
        x=0
    else:
        x=0.0000000000000001
    y=x+dx
    w=0
    while tx<a:
        if c==1:
            w=givehyp1(x,y)+w
        elif c==2:
            w=givehyp2(x,y)+w
        elif c==3:
            w=givehyp3(x,y)+w
        else :
            w=givesin(x,y)+w
        tx=tx+dx
        x=x+dx
        y=y+dx
    return(w)

if __name__=="__main__":
    a=int(input("What number do you wish to be the higher bound of the interval starting on 0?   "))
    b=int(input("How precise do you want to be? Aka how many points do you want?   "))
    c=int(input("What function do you want? Square, square root, cube, or inverse function? Type 1,2,3 or 4   "))
    print("The approximate length of the arc you chose is",givelength(a,b,c))
      
            
            
            
    
            
            
        
        
