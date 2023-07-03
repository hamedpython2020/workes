
w = 0
#float(input('---\t w\t---'))
a = 0
#float(input('---\t a\t---'))
n = 0.5
#float(input('---\t n\t---'))
f = 0.5
#float(input('--- \t f \t ---'))
k = 0.25
#float(input('---\t k\t---'))
x = 1
#float(input('---\t x\t---'))
b = 1
#float(input('---\t b\t---'))
l = 20
#float(input('---\t l\t---'))
ei = 1
#float(input('---\tei\t---'))
q1 = 10
#float(input('---\tq1\t---'))
q2 = 20
#float(input('---\tq2\t---'))
p = 000
#float(input('---\t p\t---'))
m = 00
#float(input('---\t m\t---'))
# print(w,a,n,f,k,x,b)

# react for P force 
r_p_A = p*(l*(1-n))/l
r_p_B = p*(l*n)/l

def  P_M(x):
    if p == 0:
        return 0
    if x <= n*l:
        P_M = r_p_A * x
    else:
        P_M = (r_p_A * x) - p*(x-(n*l))
    return P_M
###################################

#react for  q1,q2 force tri

t_q1_q2 = 0.5*(q2-q1)*f*l
if q2 > q1:
    t_d_q1_q2 = ((2/3)*(f*l))+k*l
elif q1 > q2:
    t_d_q1_q2 = ((1/3)*(f*l))+k*l
else:
    t_d_q1_q2 = 0
r_tq1q2_A = t_q1_q2*(l-t_d_q1_q2)/l
r_tq1q2_B = t_q1_q2*(t_d_q1_q2)/l

def t_q1q2_M(x) :
    if x <= k*l:
        t_q1q2_M = r_tq1q2_A*x
        pass
    elif k*l <= x <= k*l+f*l:
        if q2 > q1:
            sh = (q2-q1)/(f*l)
            t = (sh*(x-(k*l))**2)*0.5
            d_t = (0.66*(x-(k*l)))+(k*l)
        elif q1 > q2:
            sh = (q2-q1)/(f*l)
            t = (sh*(x-(k*l))**2)*0.5
            d_t = (0.33*(x-(k*l)))+(k*l)
        else:
            t = 0
            d_t = 0
            pass
        t_q1q2_M = r_tq1q2_A*x-(t*(x-d_t))
    else:
        t_q1q2_M = r_tq1q2_A*x-(t_q1_q2*(x-t_d_q1_q2))
    return t_q1q2_M
####################################

#react for  q1,q2 force re

if q2 < q1:
    r_q1_q2 = q2*f*l
else:
    r_q1_q2 = q1*f*l
r_d_q1_q2 = (0.5*(f*l))+k*l
r_rq1q2_A = r_q1_q2*(l-r_d_q1_q2)/l
r_rq1q2_B = r_q1_q2*(r_d_q1_q2)/l

def r_q1q2_M(x) :
    if x <=k*l :
        r_q1q2_M = r_rq1q2_A*x
        pass
    elif k*l <= x <= k*l+f*l:
        if q2 < q1:
            r = q2*(x-(k*l))
            d_r = (0.5*(x-(k*l)))+(k*l)
            r_q1q2_M = r_rq1q2_A*x-(r*(x-d_r))
        else:
            r = q1 * (x - (k * l))
            d_r = (0.5 * (x - (k * l))) + (k * l)
            r_q1q2_M = r_rq1q2_A * x - (r * (x - d_r))
    else:
        r_q1q2_M = r_rq1q2_A*x-(r_q1_q2*(x-r_d_q1_q2))
    return r_q1q2_M
####################################

# M in distrubetion q1_q2
def q1q2_M(x):
    q1q2_M = r_q1q2_M(x) + t_q1q2_M(x)
    return q1q2_M
#react for M force

def M_M(x) :
    if x < w*l:
        M_M = 0
    else:
        M_M = m
    return M_M

# print(M_M(8),'\n',P_M(4),'\n',q1q2_M(5))

def sum(x):
    if x <= a*l:
        sum_M = (M_M(x) + P_M(x) + q1q2_M(x))/(b*ei)
    else:
        sum_M = (M_M(x) + P_M(x) + q1q2_M(x))/(x*ei)
    return sum_M

# print(sum(4))

################# force function complete
def mo ():
    dx = round(l/20,2)
    zigma_y = 0
    zigma_ylist = []
    nn = int(l/dx)
    # print(nn,dx,l)
    for i in range(1, nn):
        zigma_y += sum(i*dx)
        zigma_ylist.append(sum(i*dx))
        pass
    zigma_y += sum(0)/2
    zigma_y += sum(l)/2
    A = zigma_y * dx
    xia = []
    Aibar = []
    for i in range(1,nn):
        if sum(i*dx) > sum((i-1)*dx):
            p1 = ((3*abs(sum(i*dx)))+abs(sum((i-1)*dx)))/6
            p2 = abs(sum(i*dx)) + (abs(sum((i-1)*dx))/2)
            pp = round((dx*p1)/p2, 3)
            xibar = ((i-1)*(round(dx,2)))+pp
            xia.append(round(xibar,2))
            p1 = (abs(sum(i*dx))+abs(sum((i-1)*dx)))/2
            Aibar.append(round((dx*p1), 2))
        else:
            p1 = ((3 * abs(sum(i*dx))) + (2 * abs(sum((i-1)*dx)))) / 6
            p2 = abs(sum(i*dx)) + (abs(sum((i-1)*dx)) / 2)
            if p2 == 0:
                pp = 0
            else:
                pp = round((2 * dx * p1) / p2, 3)
            xibar = ((i-1)*dx)+pp
            xia.append(round(xibar,2))
            p1 = (abs(sum(i * dx)) + abs(sum((i - 1) * dx))) / 2
            Aibar.append(round((dx * p1), 2))
        pass
    up = 0
    Atbar = 0
    for i in range(0,len(xia)):
        up += xia[i] * Aibar[i]
        # print(up)
    for j in range(0,len(Aibar)):
        Atbar += Aibar[j]
        # print(Atbar)
    if Atbar == 0:
        xbar = 0
    else:
        xbar = up/Atbar

    Moa = xbar * A
    Mob = (l-xbar)*A
    return Moa, Mob

MM = list(mo())
# print(MM)
MA = round(MM[0], 6)
MB = round(MM[1], 6)
FEM_AB = (2/l**2)*(MA-2*MB)
FEM_BA = (2/l**2)*(2*MA-MB)
print (sum(10))
print(FEM_AB)
print(FEM_BA)

