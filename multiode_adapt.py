from math import sin
from numpy import array,arange
from pylab import plot,xlabel,show

        



def rkstep(f,h,t,r):#ki's here are also vectors
    k1 = h*f(r,t) #euler
    k2 = h*f(r + 0.5*k1,t+0.5*h)
    k3 = h*f(r + 0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    return (r + ((k1+2*k2+2*k3+k4)/6))


def Mode_ad(f,a,b,r_0,delta,l): #delta decides step
 
    h = 10**(-2) #initial step
    

    #parametros do problema
    
    xpoints = []
    ypoints = []
    tpoints = []

    r = r_0
    
    

    t = a
    tpoints.append(t)
    xpoints.append(r[0])
    ypoints.append(r[1])

    e = 0.1
    n = 0
    while (t< b ):
        # determination of r2 & r1
        r_2 =rkstep(f,2*h,t,r)
    
        r_1 = rkstep(f,h,t,r)
        r_1 = rkstep(f,h,t+h,r_1) 

        # rho if
        p = 30*delta*h/abs(r_1[0]-r_2[0]) 

       
        if (p >= 1 ):#rk better than target, make h bigger,keep results

            #atualizar variáveis
            t+=2*h
            r = r_1 + (1/15)*(r_1-r_2)
            #if(n%10**4 == 0):
             #   print(h,p,r_1[0],r_2[0])
        
            xpoints.append(r[0])
            ypoints.append(r[1])
            tpoints.append(t)
            
            if ((p**(1/4)) > 2 ):
                h = 2*h
                
            else:
                h = h*(p**(1/4))

        if (p < 1):
            
            h = h*(p**(1/4))
        
        n = n+1
        
    

    return [tpoints,xpoints,ypoints]









