

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

print(M_M(8) + P_M(4) + q1q2_M(5))