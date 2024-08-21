import math
def complex_sum(a,b):
    return (a[0]+b[0],a[1]+b[1])


def complex_multiplication(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def complex_division(a,b):
    denominator = b[0]**2 * b[1]**2
    if denominator !=0:
        return((a[0]*b[0]+a[1]*b[1])/denominator,
               (b[0]*a[1]-a[0]*b[1])/denominator)
    else:
        return "Es imposible dividir entre 0 "

def complex_rest(a,b):
    return (a[0]-b[0],a[1]-b[1])

def complex_module(a):
    return math.sqrt(a[0]**2 + a[1]**2)

def complex_conjugated(a):
    return (a[0],-a[1])

def Cartesian_to_polar(a):
    p = complex_module(a)
    theta = math.atan(a[1]/a[0])
    return (p,theta)

def polar_to_Cartesian(a,b):
    return (a*math.cos(b),a*math.sin(b))

def fase(a):
    return math.atan(a[1]/a[0])
