count1 = 1
space1 = 13
count2 = 10
space2 = 3
count3 = 10
space3 = 13
count4 = 1
space_f1 = 1

for row in range(10):
    if row < 1: 
        print('(A)',end='')
        for space_f2 in range(11):
            print('',end=' ')
        print('(B)',end='')
        for space_f3 in range(11):
            print('',end=' ')
        print('(C)',end='')
        for space_f4 in range(11):
            print('',end=' ')
        print('(D)',end='')
        print('\n')
    for star1 in range(count1):
        print('*',end='')
    for space_s1 in range(space1):
        print('',end=' ')
    for star2 in range(count2):
        print('*',end='')
    for space_s2 in range(space2):
        print('',end=' ')
    if row < 1:
        for space_f in range(space_f1):
            print('',end=' ')
        for star3 in range(count3):
            print('*',end='')
        for space_s3 in range(space3):
            print('',end=' ')
        for star4 in range(count4):
            print('*',end='')
    if row >= 1:
        for space_f in range(space_f1):
            print('',end=' ')
        for star3 in range(count3):
            print('*',end='')
        for space_s3 in range(space3):
            print('',end=' ')
        for star4 in range(count4):
            print('*',end='')
    count1 += 1
    space1 -= 1
    count2 -= 1
    space2 += 1
    count3 -= 1
    space3 -= 1
    count4 += 1
    space_f1 += 1
    print('\n')
