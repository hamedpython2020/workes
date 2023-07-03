import numpy as np
import math , cmath

#matrix 10x1 L
M_1 = [
    [653, 1681],
    [2313, 549],
    [3909, 1517],
    [2369, 2829],
    [2357, 1525]
]
L = np.array([
    [653],[1681], 
    [2313],[549], 
    [3909],[1517], 
    [2369],[2829], 
    [2357],[1525]
])
C_1 = np.array([
    [1081, 2557],
    [1289, 801],
    [3473, 877],
    [3597, 2409],
])
M_2 = np.array([
    [1127, 1706],
    [2219, 632],
    [3663, 1296],
    [2115, 2564],
    [2194, 1476]
])
C_2 = np.array([
    [1309, 2318],
    [1513, 1018],
    [3227, 716],
    [1245, 2228],
])
M_3 = np.array([
    [1147, 1460],
    [2513, 658],
    [3587, 1574],
    [2609, 2528],
    [2565, 1468]
])
C_3 = np.array([
    [1577, 2282],
    [1695, 726],
    [3309, 1056],
    [3419, 2214],
])
M_4 = np.array([
    [929, 1548],
    [2353, 596],
    [3803, 1328],
    [2605, 2482],
    [2475, 1374]
])
C_4 = np.array([
    [1385, 2304],
    [1477, 804],
    [3363, 836],
    [3665, 2070],
])
M_5 = np.array([
    [929, 1657],
    [2685, 537],
    [3905, 1677],
    [2581, 2833],
    [2653, 1597]
])
C_5 = np.array([
    [1411, 2599],
    [1637, 673],
    [3653, 1031],
    [3583, 2459],
])
pic = [
    [M_1, C_1],
    [M_2, C_2],
    [M_3, C_3],
    [M_4, C_4],
    [M_5, C_5]
]


def give_A(x):
    A = []
    s = 0
    for i in range(len(x)):
        A.append([])
        for j in range(len(x[0])):
            A[s].append(
                x[i][j]
            )
        if s == 0 or s % 2 == 0:
            A[s].append(1)
            A[s].append(0)
        else:
            A[s].append(0)
            A[s].append(1)
            A[s][1] *= -1
        s += 1
        A.append([])
        for j in range(0,len(x[0])):
            A[s].append(
                x[i][j-1]
            )
        if s == 0 or s % 2 == 0:
            A[s].append(1)
            A[s].append(0)
        else:
            A[s].append(0)
            A[s].append(1)
            A[s][1] *= -1
        s += 1
    return np.array(A)

# print(give_A(M_2))
def give_X(A):
    A_T = A.transpose()
    p1 = A_T.dot(A)
    p1 = np.linalg.inv(p1)
    p2 = p1.dot(A_T)
    x = p2.dot(L)
    Y = math.sqrt((x[0][0]**2)+(x[1][0]**2))
    K = math.atan((x[1][0])/(x[0][0]))
    X0 = x[2][0]
    Y0 = x[3][0]
    a = Y*(math.cos(K))
    b = Y*(math.sin(K))
    return [a, b, X0, Y0]


def give_C(x, C):
    a, b, c, d = x
    X = []
    Y = []
    for i in range(len(C)):
        X.append((a*C[i][0])+(b*C[i][1])+c)
        Y.append((-1*b*C[i][0])+(a*C[i][1])+d)
    return X, Y


def give_E(m):
    x, y = m
    E = []
    for i in range(len(C_1)):
        dx = C_1[i][0]-x[i]
        dy = C_1[i][1]-y[i]
        e = math.sqrt((dx**2)/(dy**2))
        E.append(e)
        pass
    e = 0
    for i in range(len(E)):
        e += E[i]**2
        pass
    RMSE = math.sqrt(e/4)
    return RMSE, E

# A = give_A(M_2)
# x = give_X(A)
# c = give_C(x, C_2)
# m = give_E(c)

def result(w):
    M = pic[w-1][0]
    C = pic[w-1][1]
    A = give_A(M)
    z = give_X(A)
    c = give_C(z, C)
    RMSE, E = give_E(c)

    return 'RMSE = {} \n the error for each point = {}'.format(RMSE, E)


print(result(3))
