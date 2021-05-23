s = input()

occurence = {i : s.count(i) for i in s}       ##this dictionary has count of all the distinct characters in input string

min_occ = min(list(occurence.values()))       ##the minimum count

extra = 0                                     ##variable to check if any character has more than one extra count
mystring = True                               ##variable to check if the given input is my string or not

for i in list(occurence.values()):
    
    if i - min_occ == 1:                      ##if a character has one extra count than the min count then increase the extra variable
        extra = extra + 1
        
        if extra > 1:                         ##if more than one character have extra counts then  it is not my string and come out of the loop
           mystring = False
           break
            
    elif i-min_occ == 0:                      ##if a character has same count as that of the min count then no issue
        continue
        
    else:                                     ##if a character has more than one count then it is not my string and come out of the loop
        mystring = False
        break
        
if mystring == True:
    print('MY STRING')
else:
    print('NOT MY STRING')
