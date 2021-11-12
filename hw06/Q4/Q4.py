# Q4
def delete_keys(keylist,dic):
    keylist = list(set(keylist))
    for each in keylist:
        if each in list(dic.keys()):
            del dic[each]
    return dic


dic = {'x': 12,'y':145,'z':124}
keylist = ['x', 'q', 'p']
print(delete_keys(keylist,dic))


