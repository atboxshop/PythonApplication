new_pi = 0
pi = 0
x = 1
y = 4
flag = False
term = 0
while flag == False:
    if new_pi > 3.14159:
        flag = True
    if new_pi < 3.14159:
        pi = (y/x) - (y/(x+2))
        new_pi += pi
        term += 1
        x = x + 4
        print('Pi of term number',term,'is:',new_pi)
print('End Of Script')


