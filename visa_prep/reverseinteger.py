n = int(input())
if n >=0:
    m = int(str(n)[::-1]) 
else:
    m = -int(str(n)[:0:-1])

   
if m>= ((2**31)-1) or m <= (-2**31):
    print("0")
else:
    print(m)
