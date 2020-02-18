for i in range (9):
    print('\n')
    if (i-8 >=0):
        i=i-8
        print(8)
    if (i-4 >=0):
        i=i-4
        print(4)
    if (i-2 >=0):
        i=i-2
        print(2)
    if (i-1 >=0):
        i=i-1
        print(1)
--------------------------
for k in range (9):
    print('\n')
    for j in range(4):
        if(k-2**j>=0):
            k=k-2**j
            print(2**j)
