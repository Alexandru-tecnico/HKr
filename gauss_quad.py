from gaussxw import gaussxw


def gauss_quad(a,b,N,f,par):
     #Exato para polinómios de grau até 2N-1 -taylor ate ordem 199 acc =16
    
    

    #Calculate sample points and weights, then map them
    x,w=gaussxw(N)
    xp=0.5*(b-a)*x+0.5*(b+a)
    wp = 0.5*(b-a)*w

    #Perform integration
    s=0.0
    for k in range(N):
        s+=wp[k]*f(xp[k],par) # Só aqui é que f é avaliada
    return s



def Dgauss_quad(xa,xb,ya,yb,N,f,z):
     #Exato para polinómios de grau até 2N-1 -taylor ate ordem 199 acc =16
    
    

    #Calculate sample points and weights, then map them, for x
    x,xw=gaussxw(N)
    xp=0.5*(xb-xa)*x+0.5*(xb+xa)
    xwp = 0.5*(xb-xa)*xw

    
    #for y
    y,yw = gaussxw(N)
    yp = 0.5*(yb-ya)*x+0.5*(yb+ya)
    ywp = 0.5*(yb-ya)*yw
    

    #Calculate integral
    
    s = 0.0
    for k in range(N):
        for j in range(N):
            s+=ywp[k]*xwp[j]*f(xp[j],yp[k],z) # Só aqui é que f é avaliada

    return s



    



