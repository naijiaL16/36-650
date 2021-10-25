
# Q3
def check_trueedits(a,b):
    count,i,j = 0,0,0
    while i < len(a) and j < len(b):
         if a[i] != b[j]:
            if count == 1:
               return 'false'
            if len(a) < len(b):
               j += 1
            elif len(a) > len(b):
               i += 1
            else:
               count,i,j = count+1,i+1,j+1
         else:
            i,j = i+1,j+1
    return 'true'

def check_edits(a,b):
    if(not isinstance(a, str) and not isinstance(b, str)):
        return("Invalid Input")
    # when length difference is larger than 2, edits > 2
    elif(abs(len(a)-len(b))>1):
        return 'false'
    else:
        return check_trueedits(a,b)


check_edits('pale','ple')
check_edits('pales','pale')
check_edits('pale', 'bale')
check_edits('pale', 'bake')
