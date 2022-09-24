
from math import sqrt,exp

from trap_accuracy import Trap_acc

#from simpson_acc import Simpson_acc
from gauss_quad import gauss_quad
from scipy import special

#print(-m*sqrt(m))


def f(z,l):
        x = z/(1-z) + 2
        return (exp(-x**2))/(1-z)**2
        
       

def G(z):
    x = 3 + z/(1-z) #mud de variaveel
    return (1/(1-z)**2)*exp(-x**2)

def j(z,l):
        x = z/(1-z)
        return (1/(1-z)**2)*special.spherical_jn(l,x)**2


def delta_phase(l,E):
        
        p = 3.57
        e = 5.9
        tmax = 5*p
        m = 6.12/p**2

        c = 10**(-12)
        k = sqrt(m*E)
        def LJ(t): # Full Lennard-Jones potential 
                return e* ( (p/t)**12 -2*(p/t)**6 )
        
        def F(z,l):
            x = tmax + z/(1-z)
    
            return (1/(1-z)**2)*LJ(x)*(special.spherical_jn(l,k*x)**2)*(x**2) #variável ja está mudada

        def G(x,l):
            return LJ(x)*(special.spherical_jn(l,k*x)**2)*(x**2)

        return(Trap_acc(tmax,85,G,10**(-6),l))
        #return gauss_quad(tmax,50,1000,G,l)





