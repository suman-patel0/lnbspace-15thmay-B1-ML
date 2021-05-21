s = input()
occurence = {i : s.count(i) for i in s}
min_occ = min(list(occurence.values()))
extra = 0
mystring = True
for i in list(occurence.values()):
    if i - min_occ == 1:
        extra = extra + 1
        if extra > 1:
           mystring = False
           break
    elif i-min_occ == 0:
        continue
    else:
        mystring = False
        break
if mystring == True:
    print('MY STRING')
else:
    print('NOT MY STRING')
    
    
              
        

              
