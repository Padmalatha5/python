n = 4
stars =1
spaces = n - 1
for r in range(n,0,-1):
    for c in range(1, spaces+1):
      print(' ', end = ' ')
    for c2 in range(stars,0,-1):
        print("*", end = ' ')
    print()
    spaces -= 1
    stars += 1