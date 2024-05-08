def kpk(a,b):
    for i in range(1,a*b+1):
        if (i%a==0) and (i%b==0):
            value = i
            break
    return value
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    value = 1
    for i in range(2,n+1):
        value = kpk(value,i)
    print(value)