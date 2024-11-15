N , m = map(int,input().split())
n = list(map(int,input().split()))
num=0
num2 =0
for i in range(len(n)):
    if n[i]%m != 0:
        num+= n[i]
    else:
        num2+=n[i]
print(num2-num)
    
