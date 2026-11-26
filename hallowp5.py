n = 4
for r in range(n+1,0,-1):
    for c in range(r,0,-1):
           print('*', end = ' ')
    print()
    
    
    
    
    
    
    
    
    
#hallow pattern
n = 4
s= n
for r in range(1,n+1):
    for c in range(1,s+1):
        if c == s or c == 1 or r == 1:
           print('*', end = ' ')
        else:print(" ", end =' ')
    print()
    s = s-1