X,Y,Z = map(int,input().split())
time = X*Y
t = 1440*Z
if time<= t:
    print("YES")
else:
    print("NO")
