from trapezoidal import Trapezoidal



def Trap_acc(a,b,f,acc,l):
    

    N = 1 
    i1 = Trapezoidal(a,b,N,f,l)
    N = 2*N 
    i2 = Trapezoidal(a,b,N,f,l)  # I calcultate again this is not efficient

    error = (1/3)*abs(i2-i1)



    while( abs(error) > acc):
        odd=0
        
        N=N*2  #update number of slices

        h = (b-a)/N #update step size
        for k in range(1,N,2):#sum over odd values
            odd+=f(a + k*h,l) #a = 0 que é o início da integração
            
        i1 = i2
        i2  = 0.5*i2 + h*odd

        error = (1/3)*abs(i2-i1)

        #print("N: ",N,"I2:",i2,"error",error)
    
    return i2    
    
