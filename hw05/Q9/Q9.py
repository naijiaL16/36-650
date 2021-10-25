
# Q9

def palindrome(string):
    if (len(string) < 2):
        return 'true'
    elif(string[0] != string[-1]):
        return 'false'
    else:
        return palindrome(string[1:-1])


palindrome('kayak')
palindrome('hello')