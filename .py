n = 5
spaces = n - 1
for r in range(n,0,-1):
    for c1 in range(1,spaces+1):
        print(' ', end = ' ')
    for c3 in range(r,n+1):
        print(c3, end = ' ')
    print()
    spaces -=1