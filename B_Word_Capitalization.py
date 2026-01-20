strs = str(input())

if strs[0].islower():
    strs = strs[0].upper() + strs[1:]  
print(strs)