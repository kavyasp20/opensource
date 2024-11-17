n = int(input())
A = list(map(int,input().split()))
c = []

for i in A:
    
    if i not in c:
        c.append(i)
print(*c)
