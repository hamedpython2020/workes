x = input()

data = x.split()

n = int(data[0])

k = float(data[1])

s = float(data[2])

if n*k <= s:
    print('Kafie!')
else:
    print('Na! yeki bayad bere sabzi bekhare')