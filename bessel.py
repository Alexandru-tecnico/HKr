from math import sin,cos,pi


def Be_2(l,x): 

    def n_0(x):
        return (-(cos(x)/x))
    def n_1(x):
        return (-(cos(x)/x**2) - sin(x)/x)

    s_0=n_0(x)
    s_1 = n_1(x)

    #recurrence loop
    
    for n in range(1,l,1):
        s_2 = -s_0 + ((2*n+1)/x)*s_1
        s_0 = s_1
        s_1=s_2

    return s_1






def Be(l,x): 

    values = [(3/2)*int(x)+20,l+20]
    l_max = int(max(values))
    
    
    delta = 10**(-6)


    s_1 = delta
    s_2 = 0.0
    b = 0
    #Downward Recursion - Need recursion cuz of (x)
    for n in range(l_max,0,-1):
        
        s_0 =  -s_2 + ((2*n+1)/x)*s_1
        if n!= 1:
            s_2 = s_1
            s_1 = s_0
        if n == l+1:
            b = s_0

    #Normalization
    scale = 1 /(((s_0-x*s_1)*cos(x))+x*(s_0)*sin(x))
    return scale*(b)  




















