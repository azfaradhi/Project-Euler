def palindrom(n):
    return str(n) == str(n)[::-1]
    
list = []
for i in range(100,1000):
    for j in range(i,1000):
        if palindrom(i*j):
            list.append(i*j)
list.sort()
length = len(list)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(length-1,-1,-1):
        value = list[i]
        if list[i] < n:
            break
    print(value)