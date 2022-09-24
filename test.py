from pylab import plot,xlabel,show,ylabel,xlim,ylim
from numpy import array,size,linspace

e = 5.9 #meV
p = 3.57 #Angstroms
m = 6.12/p**2 # m == 2m/h**2


tmin = 0.75*p
tmax = 5*p

l = 3
E = 0.5

def LJ(t): #Lennard-Jones potential ; 
        if(t<tmax):
            return e* ( (p/t)**12 -2*(p/t)**6 )
        else:
            return 0

def F(l,t,E):
        return (LJ(t)+ l*(l+1)/(m*t**2) - E)

x_values = linspace(tmin,tmax,1000)
y=[]
u = []


for n in range (size(x_values)):
    y.append(LJ(x_values[n]))
    u.append(0)

plot(x_values,y)
plot(x_values,u,"k--")
xlim(2,10)
ylim(-10,15)
show()
