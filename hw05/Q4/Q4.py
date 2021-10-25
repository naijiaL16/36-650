
# Q4
def print_triangles(n):
    if (isinstance(n,float)):
        return("Invalid Input")
    elif (n <= 0):
        return("Invalid Input")
    else:
        i,j = 1,2
        for c in range(n):
            for d in range(1, j):
                print(i, end=' ')
                i += 1
            print('')
            j += 1

print_triangles(3.2)
print_triangles(-1)
print_triangles(3)
print_triangles(6)