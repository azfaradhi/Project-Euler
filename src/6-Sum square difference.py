def jumlahkuadrat(n):
    sum = 0
    for i in range(1,n+1):
        sum += (i*i)
    return sum

def kuadratjumlah(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum**2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(abs(jumlahkuadrat(n) - kuadratjumlah(n)))