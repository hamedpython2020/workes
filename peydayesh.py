def find(num1, num2, num3):
    l = [2,1,3,4]
    m = [num1,num2,num3]
    for i in range(len(m)):
        l.remove((m[i]))

    return l[0]

