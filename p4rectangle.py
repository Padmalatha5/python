n=4
for r in range(1,n+1):
    for c in range(1, n*2+1):
        if r == 1 or c == 1 or r == n or c == n*2:
           print('*', end = ' ')
        else: print(' ', end = ' ')
    print()