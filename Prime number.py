# at first : we want to find the prime number
def get_prime_number(end):
    i = 2
    while i < end:
        g = 0
        h = 0
        for x in range(2, i):
            g += 1
            if i % x == 0:
                break
                pass
            else:
                h += 1
                pass
            pass
        if h == g:
            print(i)
            pass

        i += 1
        pass
    pass

def recognise_prime_number(number):
    l = []
    for i in range(2, number):
        if number % i == 0:
            l = [2]
            break
        pass
    if number == 1:
        print('the number is not eny one')
    else:
        if len(l) == 1:
            print('not prime')
        else:
            print('prime number')
            pass
        pass