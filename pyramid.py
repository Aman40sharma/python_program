n=int(input("enter num of rows"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()

#reverse pyramid
n=int(input("enter num of rows"))
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()



#full pyramid
n=int(input("enter num of rows"))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()