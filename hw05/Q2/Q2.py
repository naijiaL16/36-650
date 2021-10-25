
# Q2
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

new_string = []
def remove_punctations(string):
    # check the type of input
    if(not isinstance(string, str)):
        return("Invalid Input")
    else:
        # for loop in list to create a new string without punctuations
        for i in range(len(string)):
            if string[i] not in punctuations:
                new_string.append(string[i])
    # conbine the list back to a string    
    return ''.join(new_string)

input_string ='Hello in 36-650,& other MSP courses.'

remove_punctations(input_string)