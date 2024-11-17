X,Y = input().split()
if X == "S" and Y == "R" or X == "R" and Y =="P" or X == "P" and Y == "S":
    print("Charan")
elif Y == "S" and X == "R" or Y == "R" and X =="P" or Y == "P" and X == "S":
    print("Vignesh")
else:
    print("NULL")
