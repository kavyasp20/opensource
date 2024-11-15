yr = int(input())
if yr>= 1500 and yr<=3000:
    
    if (yr % 400 ==0) or (yr % 100!= 0 and yr%4==0):
        
         print("YES")
    else:
        print("NO")
