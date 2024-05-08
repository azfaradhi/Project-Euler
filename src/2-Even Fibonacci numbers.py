def sum_even(n):
    a = 0
    b = 1
    list_fibonacci = []
    while b < n:
        b = b + a
        a = b - a
        if b > n:
            break
        else:
            list_fibonacci.append(b)
    sum = 0
    for num in list_fibonacci:
        if num % 2 == 0:
            sum += num
    return sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_even(n))