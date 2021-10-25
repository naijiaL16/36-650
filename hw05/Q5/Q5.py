
# Q5
def print_startriangles(n):
    if (isinstance(n,float)):
        return("Invalid Input")
    elif (n <= 0):
        return("Invalid Input")
    else:
        for j in range(1,n+1):
            for i in range(n+1-j):
                print(" ", end='')
            for i in range(j):
                print("*", end=' ')
            print()


print_startriangles(3.4)
print_startriangles(-2)
print_startriangles(5)
