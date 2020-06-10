Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 04
How precise do you want to be? How nay points do you want?8
What function do you want? Square,square root,cube,or inverse function? Type 1,2,3 or 41
16.798117670639524
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 04
How precise do you want to be? How nay points do you want?100
What function do you want? Square,square root,cube,or inverse function? Type 1,2,3 or 41
16.818501263043622
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 04
How precise do you want to be? How nay points do you want?1000
What function do you want? Square,square root,cube,or inverse function? Type 1,2,3 or 41
16.81863224374086
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 04
How precise do you want to be? How nay points do you want?1000000
What function do you want? Square,square root,cube,or inverse function? Type 1,2,3 or 41
16.818633567031302
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 04
How precise do you want to be? How nay points do you want?1000000000
What function do you want? Square,square root,cube,or inverse function? Type 1,2,3 or 41

============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval?    starting on 0
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   4
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse functionType 1,2,3 or 4   3
Traceback (most recent call last):
  File "/Users/casahuet/Desktop/Ferréol/longuerfx.py", line 59, in <module>
    print(givelength(a,b,c))
  File "/Users/casahuet/Desktop/Ferréol/longuerfx.py", line 46, in givelength
    w=givehyp3(x,y)+w
  File "/Users/casahuet/Desktop/Ferréol/longuerfx.py", line 21, in givehyp3
    a=y^3
TypeError: unsupported operand type(s) for ^: 'float' and 'int'
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   4
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse functionType 1,2,3 or 4   2
74.30863956171481
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   4
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse functionType 1,2,3 or 4   3
64.6717727636225
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   4
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse functionType 1,2,3 or 4   4
100000000002.30269
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   3
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse functionType 1,2,3 or 4   1
9.930385469180619
>>> givelength(3,100,2)
46.536241344348184
>>> givelength(3,100,3)
28.476649355546208
>>> givelength(3,100,4)
100000000001.32944
>>> givelength(3,5,4)
100000000001.24298
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   6
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse function? Type 1,2,3 or 4   4
1000000000000000.9
>>> givelength(50,200,4)
1000000000000048.1
>>> givelength(1,100,4)
999999999999997.6
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   
================================ RESTART: Shell ================================
>>> givelength(1,100,4)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    givelength(1,100,4)
NameError: name 'givelength' is not defined
>>> givelength(3,100,4)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    givelength(3,100,4)
NameError: name 'givelength' is not defined
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   5
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse function? Type 1,2,3 or 4   4
9999999999999998.0
>>> givelength(5,5,4)
1.0000000000000008e+16
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   4
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse function? Type 1,2,3 or 4   3
The approximate length of the arc youchose is 64.6717727636225
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   4
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse function? Type 1,2,3 or 4   1
The approximate length of the arc you chose is 16.818501263043622
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   5
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse function? Type 1,2,3 or 4   4
Traceback (most recent call last):
  File "/Users/casahuet/Desktop/Ferréol/longuerfx.py", line 61, in <module>
    print("The approximate length of the arc you chose is",givelength(a,b,c))
  File "/Users/casahuet/Desktop/Ferréol/longuerfx.py", line 51, in givelength
    w=giveinverse(x,y)+w
NameError: name 'giveinverse' is not defined
>>> 
============ RESTART: /Users/casahuet/Desktop/Ferréol/longuerfx.py ============
What number do you wish to be the higher bound of the interval starting on 0?   67
How precise do you want to be? Aka how many points do you want?   100
What function do you want? Square, square root, cube, or inverse function? Type 1,2,3 or 4   4
The approximate length of the arc you chose is 81.09763076041158
>>> 