import turtle , numpy as np

w = 0.8 
#float(input('---\t w\t---'))
a =  0.5
#float(input('---\t a\t---'))
n = 0.3
#float(input('---\t n\t---'))
f = 0.5
#float(input('--- \t f \t ---'))
k = 0.4
#float(input('---\t k\t---'))
x = 1
#float(input('---\t x\t---'))
b = 1
#float(input('---\t b\t---'))
l = 10
#float(input('---\t l\t---'))
ei = 1
#float(input('---\tei\t---'))
q1 = 4
#float(input('---\tq1\t---'))
q2 = 8
#float(input('---\tq2\t---'))
p = 10
#float(input('---\t p\t---'))
m = 10
#float(input('---\t m\t---'))
print(w,a,n,f,k,x,b)

# react for P force 
r_p_A = p*(l*(1-n))/l
r_p_B = p*(l*n)/l

def  P_M(x):
    if x <= n*l :
        P_M = r_p_A * x
    else:
        P_M = (r_p_A * x) - p*(x-(n*l))
    return P_M
###################################

#react for  q1,q2 force tri

t_q1_q2 = 0.5*(q2-q1)*f*l
t_d_q1_q2 = ((2/3)*(f*l))+k*l
r_tq1q2_A = t_q1_q2*(l-t_d_q1_q2)/l
r_tq1q2_B = t_q1_q2*(t_d_q1_q2)/l

def t_q1q2_M(x) :
    if x <=k*l :
        t_q1q2_M = r_tq1q2_A*x
        pass
    elif  k*l<=x<=k*l+f*l :
        sh = (q2-q1)/(f*l)
        t = (sh*(x-(k*l))**2)*0.5
        d_t = 0.66*(x-(k*l))
        t_q1q2_M = r_tq1q2_A*x-(t*(x-d_t))
    else :
        t_q1q2_M = r_tq1q2_A*x- (t_q1_q2*(x-t_d_q1_q2))
    return t_q1q2_M
####################################

#react for  q1,q2 force re

r_q1_q2 = q1*f*l
r_d_q1_q2 = (0.5*(f*l))+k*l
r_rq1q2_A = r_q1_q2*(l-r_d_q1_q2)/l
r_rq1q2_B = r_q1_q2*(r_d_q1_q2)/l

def r_q1q2_M(x) :
    if x <=k*l :
        r_q1q2_M = r_rq1q2_A*x
        pass
    elif  k*l<=x<=k*l+f*l :
        r = q1*(x-(k*l))
        d_r = 0.5*(x-(k*l))
        r_q1q2_M = r_rq1q2_A*x-(r*(d_r))
    else :
        r_q1q2_M = r_rq1q2_A*x- (r_q1_q2*(x-r_d_q1_q2))
    return r_q1q2_M
####################################

# M in distrubetion q1_q2
def q1q2_M(x):
    q1q2_M = r_q1q2_M(x) + t_q1q2_M(x)
    return q1q2_M
#react for M force  

def M_M(x) :
    if x <= w*l:
        M_M = -(x)
    else:
        M_M = -x + m
    return M_M

print(M_M(8),'\n',P_M(4),'\n',q1q2_M(5))

def sum(x):
    sum_M = M_M(x) + P_M(x) + q1q2_M(x)
    return sum_M

print(sum(4))

################# force function complete
def mo ():
    dx = l/(3*l)
    mylist = []
    zigma_y = 0
    nn = int(l/dx)
    print(nn,dx,l)
    for i in range(1,nn):
        mylist.append(sum(i*dx))
        zigma_y += sum(i*dx)
        pass
    zigma_y += sum(0)/2
    zigma_y += sum(l)/2
    A = zigma_y * dx
    print(zigma_y)
    xia = []
    Aibar = []
    for i in range(1,nn):
        if sum(i) > sum(i-1):
            pp = (dx*(3*abs(sum(i))+abs(sum(i-1)))/(6))/(abs(sum(i))+abs(sum(i-1))/2)
            xibar = (abs(sum(i-1))*dx)+pp
            xia.append(round(xibar,2))
            Aibar.append(round(dx*(abs(sum(i))+abs(sum(i-1))/2),2))
        else:
            pp = (2*dx*(3*abs(sum(i))+abs(sum(i-1))*2)/(6))/(abs(sum(i))+abs(sum(i-1))/2)
            xibar = (abs(sum(i-1))*dx)+pp
            xia.append(round(xibar,2))
            Aibar.append(round(dx*(abs(sum(i))+abs(sum(i-1))/2),2))
        pass
    print(xia)
    xtbar = 0
    Atbar = 0
    for i in range(0,len(xia)):
        xtbar += xia[i]
        print(xtbar)
    for j in range(0,len(Aibar)):
        Atbar += Aibar[j]
    xbar = xtbar/Atbar

    Moa = xbar * A
    Mob = (l-xbar)*A
    return Moa, Mob
# print(Mob,Moa)
print(mo())




MM = list(mo())
print(MM)
MA = round(MM[0], 6)
MB = round(MM[1], 6)
FEM_AB = (2/l**2)*(MA-2*MB)
FEM_BA = (2/l**2)*(2*MA-MB)
print(FEM_AB)
print(FEM_BA)
