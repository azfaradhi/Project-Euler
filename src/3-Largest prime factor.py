def cekprima(n):
    a = int(n**(1/2))
    cek_prima = True
    for i in range(2,a+1):
        if n % i == 0:
            cek_prima = False
            break
    return cek_prima

def primaterbesar(n):
    for num in range(n,1,-1):
        if n % num == 0:
            if cekprima(num):
                return num

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primaterbesar(n))