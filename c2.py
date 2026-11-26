p=int(input("Enter a Num: "))
q=int(input("Enter a Num: "))
r=int(input("Enter a Num: "))
if (p>q & p>r):
    print("P is Large")
elif (q>r & q>p):
    print("Q is large")
else:
    print("R is large")