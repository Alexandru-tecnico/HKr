

def Trapezoidal(a,b,N,f,l):

   
    h = (b-a)/N

    s = 0.5*f(a,l) + 0.5*f(b,l)
    for k in range(1,N):
        s += f(a+k*h,l)

    return (h*s)
