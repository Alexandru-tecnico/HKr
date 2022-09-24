from schrodinger import scatter
from math import atan,pi,sqrt
from numpy import array


def closest(r0,sol):
    r1 = 0.0
    n = 0
    s1 = 0
    s2 = 0
    while(r1 == 0.0):  #danger
          s1 = sol[0][n]
          s2 = sol[0][n+1]
          if( (abs(r0-s1) > abs(r0-s2)) and  (abs(r0-s2) < abs(r0-sol[0][n+2]) )  ):
              
              r1 = sol[0][n+1]
              n = n+1
              continue
         
          if (  abs(r0-s1) == abs(r0-s2) ): 
              r1 = sol[0][n]
              continue
          n = n+1  
                  
                  
    return array([n,sol[0][n]],float)  
        
    




def phase_par(l,E,rmax):
    
    p = 3.57
    m = 6.12/p**2
   
    k = sqrt(m*E)

    r1 = 0
    r2 = 0
    u1 = 0
    u2 = 0
    wl = 2*pi/k
    
    
    
    sol = scatter(l,E,rmax)
    
    
    

    r1 = closest(rmax,sol)[1]
    u1 = sol[1][int(closest(rmax,sol)[0])]

    r2 = closest(rmax + 3*0.5*wl,sol)[1]
    u2 = sol[1][int(closest(rmax + 3*0.5*wl,sol)[0])]
    
    
    if(abs(r1)<10**(-10) or abs(r2)<10**(-10) or abs(u1)<10**(-10) or abs(u2)<10**(-10)):
        
        print("r1ui=0")
        
    else:
        
        return [r1,r2,u1,u2]





