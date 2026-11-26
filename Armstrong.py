def Armstrong(n):
    dup = n
    l = len(str(n))
    res = 0
    while n > 0:
        rem = n % 10
        res = res + rem ** l
        n = n // 10
    if dup == res:
        return "Armstrong"
    return 'Not Armstrong'
n = 153
print(Armstrong(n))








def int2bin(n):
    res =''
    while n > 0:
        rem = n%2
        res=res+str(rem)
        n=n//2    
    return '0b'+ res
        
n = 7
print(int2bin(n))
