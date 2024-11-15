T = int(input())
for j in range(T):
    X = list(map(int,input().split()))
    for i in range(len(X)):
        if X[i]>=67 and X[i]<=45000:
            print("YES")
        else:
            print("NO")
        
