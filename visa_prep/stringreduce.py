st = input().strip()
res = ""
count = 1
for i in range(1,len(st)):
    if st[i] == st[i-1]:
        count +=1
    else:
        res += st[i-1]+ str(count)
        count = 1
res += st[-1]+ str(count)
print(res)


