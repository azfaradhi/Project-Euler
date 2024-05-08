def solution(num):
    temp = []
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            temp.append(i)
    return sum(temp)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solution(n))