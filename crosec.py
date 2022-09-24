from phase import phase_par
from bessel import Be,Be_2
from math import atan,pi,sin,sqrt
from numpy import linspace,array,size
from pylab import plot,show,xlabel,ylabel,xlim,ylim
from schrodinger import scatter
from phase import closest
from phase_error import delta_phase
import matplotlib.pyplot as plt


p = 3.57
rmax = 5*p
m = 6.12/p**2





def phase(l,E,rmax):
    par = phase_par(l,E,rmax) 
    r1 = par[0]
    r2 = par[1]
    u1 = par[2]
    u2 = par[3]
    
    J = r1*u2/(r2*u1) 
    k = sqrt(m*E)

    phase =atan( (J*Be(l,k*r1)-Be(l,k*r2)) / (J*Be_2(l,k*r1) - Be_2(l,k*r2) )) #em rad obv
    
    return phase

#total cross section calculation
def total_cross(E,rmax):
    s = 0
    k = sqrt(m*E)
    
    
    n = 0
    
    for l in range(0,7,1): 
        
        s+= (2*l+1)*(sin(phase(l,E,rmax)))**2
        
        n = n+1
        

    
    return  (4*pi/(k**2))*s/(p**2) 


def integ_sq(n1,n2,sol):
    s = 0
    for n in range(n1,n2,1):
        delta = abs(sol[0][n] - sol[0][n+1])
        s += (sol[0][n]**2)*delta*(sol[1][n])**2 # tem r^2 por causa das coord. esfericas
        
    return s


def closest2(r0,sol,h): 
    r1 = 0.0
    n = 0
    s1 = 0
    s2 = 0
    while(r1 == 0.0):  #danger
          s1 = sol[n]
          s2 = sol[n+1]
          if( (abs(r0-s1) > abs(r0-s2)) and  (abs(r0-s2) < abs(r0-sol[n+2]) )):
              r1 = sol[n+1]
              if( abs(r0-r1) < 1 and n>h):
                  n = n+1
                  continue
              else:
                  r1 = 0.0
             
                 
         
          if (  abs(r0-s1) == abs(r0-s2) ): 
              r1 = sol[n]
              continue
          n = n+1  
                  
                  
    return array([n,sol[n]],float)

def maxz(v):
    n = 0
    for n in range(0,size(v),1):
        if(v[n]< max(v)):
            continue
        else:
            return n
    
    

def FWHM(E_values,cs):
    half_max = max(cs)/2
    maximizante = maxz(cs)
    
    e1 = closest2(half_max,cs,0)[0]
    e2 = closest2(half_max,cs,maximizante)[0]
    fw = (E_values[int(e1)]-E_values[int(e2)])*(10**(-3))*2*10**(-19)
    return [(6.626*10**(-34))/ (2*fw), (E_values[int(e1)]-E_values[int(e2)]) ]
    


def cross_graph(a,b,N):
    #--------Fazer o gráfico.-------------#
    cs =[]
    E = linspace(a,b,N)
    n = 0
    for e in E:
        cs.append(total_cross(e,rmax))
        n = n+1
        print(n)

    return array([E,cs],float)

def wf():
    e = [0.25,0.35,0.425,0.4764,0.60,1.0]
    u=[]
    x_values = []
    E =0.454


    sol = scatter(4,E,rmax)

    x_values = sol[0]
    for j in range(0,size(sol[1]),1):
        u.append(sol[1][j])
    

    n1= int(closest(3.292,sol)[0]) 
    n2 = int(closest(12.7667,sol)[0])

    norm = sqrt(integ_sq(n1,n2,sol))

    for j in range(0,size(sol[1]),1):
        u[j] =  u[j]/norm 
       
    #------ y = 0------"
    y = []
    x = linspace(0,50,1000)
    for n in x:
        y.append(0)


    plot(x_values,u)
    xlabel("r")
    ylabel("u/r")
    plot(x,y,"k--")
    xlim(0,50)
    ylim(-0.15,0.15)
    plt.text(25, .05, r'E=1.0 meV')
    show()





#cs = cross_graph(2.4,2.7,150)
#E = cs[0]
#s = cs[1]

# y = b #
#------ y = 0------"
#y = []
#u =[]
#x = linspace(0.3,0.7,1000)
#for n in x:
 #   y.append(24.5)
  #  u.append(27)

#print(E[maxz(cs[1])])


#E = 0.4552
#E = 1.37
#E = 1.425
#E = 2.855
E = 1.425
k = sqrt(m*E)
#k = sqrt(m*0.6)

for l in range(0,15,1): 
    print(l,"&",phase(l,E,rmax)/(pi/2),"&",sin(phase(l,E ,rmax))**2,"&",delta_phase(l,E)*m*k)
#for e in linspace(0.3,0.6,100):
#    u = scatter(4,e,rmax)[1]
 #   n = integ_sq(3,13,scatter(4,e,rmax))
  #  u = u/sqrt(n)
   # print(e,max(u))
#wf()



  










