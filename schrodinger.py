from multiode_adapt import Mode_ad

from pylab import plot,xlabel,show,ylabel
from math import sqrt,exp,pi
from numpy import array,size,linspace





def scatter(l,E,tmax):

    
    e = 5.9 #meV
    p = 3.57 #Angstroms
    m = 6.12/p**2 # m == 2m/h**2



    C = sqrt(e*m/25) #2m/h_bar

    def step(t):
        if ( t<p):
            return -2
        else:
            return 0
    def step2(t):
        if ( t<p):
            return -15
        else:
            return 0
        

    def start(t):
        return exp(-C*t**(-5))
        

    def startp(t):
        return 5*C*exp(-C*t**(-5))*t**(-6)
        


    def LJ(t): #Lennard-Jones potential ; 
        if(t<tmax):
            return e* ( (p/t)**12 -2*(p/t)**6 )
        else:
            return 0

   
    def F(l,t,E):
        return (LJ(t)+ l*(l+1)/(m*t**2) - E)
        
    def F2(l,t,E):
        return (step2(t) - E)
        


    #função derivada
    def f(r,t):
        u = r[0]
        v = r[1]
        fu = v
        
       
        fv =m*F(l,t,E)*u
        
       

        return (array ([fu,fv],float))
    def f2(r,t):
        u = r[0]
        v = r[1]
        fu = v
        
       
        fv =m*F2(l,t,E)*u
        
       

        return (array ([fu,fv],float))

    #initial r:
    tmin = 0.75*p  
    #tmin = -5

    #range of solutions
    
    #tmax = 5
    trange=tmax + 4*pi/sqrt(m*E) # maximo valor de 2* comp de onda


    #cond init
    r0 = array([start(tmin),startp(tmin)],float)
    #r0 = array([0,10],float)
    #r0 = array ([start(tmin),startp(tmin)],float)
    #print(tmin,start(tmin),startp(tmin))

    #erro fixo
    delta = 5*10**(-4)

    #vetor sol
    sol = Mode_ad(f,tmin,trange,r0,delta,l) 
    
  

    
    #Integration stuff
    radial = []
    for n in range(0,size(sol[0]),1):
        radial.append(sol[1][n]/sol[0][n]) #u/r
        
    #return [sol[0],radial] #Já manda a radial, good,depois mudar maybe
    #return [sol1,sol2]
    #return array([sol[0],radial],float)
    return sol

#print(scatter(0,0.3,5*3.57)[0][2])
#sol1 = scatter(0,2,5*3.57)[0]
#sol2 = scatter(0,2,5*3.57)[1]

y = []
y_dom = linspace(0,35,1000)
for n in y_dom:
    y.append(0)
   

#plot(sol1[0],sol1[1],"r-")
#plot(sol2[0],sol2[1])
#plot(y_dom,y,"k--")
#xlabel("r")
#ylabel("u(r)")
#show()
















