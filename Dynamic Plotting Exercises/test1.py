import matplotlib.pyplot as plt
import math
import numpy as np
from math import cos, sin, pi
#Zadanie 1
fig = plt.figure('Zadanie1')
plt.xticks(range(-4,4,2))
plt.yticks(range(0,11,2))
plt.plot()
plt.savefig('zadanie1.png')
plt.show()

#Zadanie 2
fig = plt.figure('Zadanie2')
x = np.arange(-5, 5, 0.1)
y=[i*i for i in x]
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y)
plt.grid(True)
plt.savefig('zadanie2.png')
plt.show()

#Zadanie 3
fig3 = plt.figure('Zadanie3')
theta = np.radians(np.linspace(0,180*5,1000))*2
x_2 = theta*np.cos(theta)
y_2 = theta*np.sin(theta)
ax = fig3.add_subplot(111)
plt.plot(x_2,y_2,label='Spiral')
plt.yticks(range(-30,31,10))
ax.set_aspect('equal')
plt.legend()
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.grid(True)
plt.savefig('zadanie3.png')
plt.show()

#Zadanie 4
x = np.linspace(-10,10)
y = np.linspace(-1000, 1000, 250)
wsp_on_inch=2.54
for i in x:
   y1=x
for i in x:
    y2=x*x
for i in x:
    y3=x*x*x
fig = plt.figure('Zadanie4')
#plt.figure(figsize=(2,1),dpi=92)
plt.plot(x,y1,'r', label="f(x)=x")
#plt.figure(fig,figsize=(10/wsp_on_inch,20/wsp_on_inch))
plt.plot(x, y2,'--y', label="g(x)=x^2")
plt.plot(x, y3,'-.m', label="g(x)=x^3")
plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.savefig('zadanie4.png')
plt.savefig('zadanie4.pdf')
#plt.savefig('zadanie4.pdf',dpi=300)
plt.show()

#Zadanie 5
fig = plt.figure('Zadanie5')
def printAP(a, d, n):
    curr_term
a = 10
d = 0.9
n = 100
curr_term = a
arry=[]
arrx=[]
for i in range(n):
    arrx.append(i)
for i in range(1,n+1):
    curr_term =a+curr_term*d
    arry.append(curr_term)
plt.grid(True)
plt.xlabel("n")
plt.ylabel("a(n)")
plt.plot(arrx,arry,'.')
plt.savefig('zadanie5.png')
plt.show()
