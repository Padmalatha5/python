n = 4
stars =1
spaces = n - 1
for r in range(1,n+1):
    for c in range(1,spaces+1):
      print(' ', end = ' ')
    for c2 in range(1,stars + 1):
        if c2 == 1 or r == n or c2 == r:
            print('*', end = ' ')
        else:
            print(' ',end = ' ')
    print()
    spaces -= 1
    stars += 1