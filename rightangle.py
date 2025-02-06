# n=int(input("enter a num or range:"))
# for i in range(0,n+1):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()



# #for rectangles
# n=int(input("enter a num or range:"))
# for i in range(0,n+1):
#     for j in range(0,n+1):
#         print("*",end="")
#     print()

#reverse right angle
n=int(input("enter a num or range:"))
for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()

