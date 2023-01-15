k = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
g = []
l = []
n = []
s=0
for i in range(1, 7):
    l=[]
    g=[]
    l.append(i)
    for s in range(3):
        if len(k) == 2:
            g.append(k[0])
            g.append(k[1])
            break
        elif len(k) == 1:
            g.append(k[0])
            break
        g.append(k[s])
        if s == 2:
            break
        pass
    for s in range(3):
        if len(k)==0:
            break
        k.remove(k[0])
    l.append(tuple(g))
    n.append(tuple(l))
    if len(k) == 0:
        break
    pass

print(tuple(n))


for i, j in n:
    for x in j:
        print(i, x)
        pass

    pass
