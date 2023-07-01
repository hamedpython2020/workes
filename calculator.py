

def calculate_floor(s):
    h = 0
    l = list(s.strip())
    print(l)
    for i in range(0,len(l)) :
        if l[i] == 'U':
            h += 1
        elif l[i] == 'D':
            h -= 1
        else:
            break
    
    return h 
