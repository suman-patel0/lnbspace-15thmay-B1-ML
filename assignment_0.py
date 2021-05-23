################################################################
#----------------------QUESTION 1------------------------------#
################################################################

print('Question 1')

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]

#iterating over the numbrs list
for item in numbers:
    
    if item == 237:      #if item is 237 then come out of the loop
        break

    if not item%2:       #if item even the print it
        print(item, end = ' ')

        
print()
print()


################################################################
#----------------------QUESTION 2------------------------------#
################################################################

print('Question 2')

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1 - color_list_2)     #print the items from color_list_1 which are not present in color_list_2

print()


################################################################
#----------------------QUESTION 3------------------------------#
################################################################

print('Question 3')

#take the input and convert it in uppercase
#so that uppercase alphabets and lowercase alphabets do not get differentiated
input_string = input().upper()

alpha_string = ''     #empty string to store the alphabets of input_string

#iterating over the input_string
for i in input_string:

    if i.isalpha():   #if the letter in input_string is an alphabet then store it in alpha_string
        alpha_string += i

#convert the alpha_string  to a set so that every character is different
#if length of the set is 26 then all the alphabets are present in alpha_string
if len(set(alpha_string)) == 26:
    print('Pangram')
else:
    print('Not pangram')

print()

################################################################
#----------------------QUESTION 4------------------------------#
################################################################

print('Question 4')

n = input()          #take the input but don't convert into integer

nn = int(n*2)
nnn = int(n*3)

n = int(n)           #once nn and nnn are computed then convert n into an intger

print(n+nn+nnn)      #prints the output

print()


################################################################
#----------------------QUESTION 5-------------------------------#
################################################################

print('Question 5')

input_string = input().split('#')   #split the input into two # separarted portions

#split the two portions to make them lists
list1=[i for i in list(input_string[0].split())]
list2=[i for i in list(input_string[1].split())]

#print the lists
print(list1)
print(list2)

print()


################################################################
#----------------------QUESTION 6-------------------------------#
################################################################

print('Question 6')

sequence = input().split(',')       #split the comma separated input and insert them into a list

result = ','.join(sorted(sequence)) #sort the list and join the elements with comma

print(result)                       #print the output

print()


################################################################
#----------------------QUESTION 7-------------------------------#
################################################################

print('Question 7')

d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}

#variable that will keep count of index of highest marks element
index = 0;

#iterating over the Marks key
for i in d['Marks']:

    if i == max(d['Marks']):     #if the highest marks is found then come out of the loop
        break

    else:                        #if highest marks is not found then increase the index
        index += 1

print(d['Student'][index])       #print the student who has highest marks
            
print()


################################################################
#----------------------QUESTION 8-------------------------------#
################################################################

print('Question 8')

sentence = input()               #take the input

#variables to keep a count of digits and letters in sentence
digits = 0
letters = 0

#iterating over sentence
for i in sentence:
    
    if i.isalpha():              #if the element is an alphabet then increase letters count by 1
        letters += 1

    elif i.isnumeric():          #if the element is a number then increase degits count by 1
        digits += 1

#print the output
print('LETTERS ' + str(letters))
print('DIGITS ' + str(digits))

print()


################################################################
#----------------------QUESTION 9-------------------------------#
################################################################

print('Question 9')

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

subject = input()               #take the input

newData = {'Name': [], 'Subject': [], 'Ratings':[] }                    #create an empty dictionary with keys

#make a list of indices of the given input from the previously given dictionary
subject_index_list = [index for index in range(len(d['Subject'])) if subject == d['Subject'][index]]

#iterate over the indices list and add items
#to the newly created dictionary corresponding to the indices
for i in subject_index_list:
    
    newData['Name'].append(d['Name'][i])
    newData['Subject'].append(d['Subject'][i])
    newData['Ratings'].append(d['Ratings'][i] )

print(newData)                  #print the dictionary

print()


################################################################
#----------------------QUESTION 10-----------------------------#
################################################################

print('Question 10')

n = int(input())                 #take input and convert it into integer

class Generator:                 #generator class 

    def generator(self, n):      #generator function

        for i in range(n):       #iterating over the numbers in range n

            if not i%7:          #if the number is divisible by 7 then return it
                yield i

gen = Generator()                #create an object of Generator class


for i in gen.generator(n):       #iterating to print the returned values from generator function of generator class
    print(i, end = ' ')


print()
print()


################################################################
#----------------------QUESTION 11-----------------------------#
################################################################

print('Question 11')

import math

lst = []      #create an empty list to append the input tuples into it

for i in range(4):
    
    tuple_input = input().split()            #take input and split it 
    tuple_input[1] = int(tuple_input[1])     #convert the second entered input into integer
    make_tuple = tuple(tuple_input)          #convert the input into tuple
    lst.append(make_tuple)                   #append the input tuple into the list

vertical = abs(lst[0][1] - lst[1][1])        #vertical distance travelled
horizontal = abs(lst[2][1] - lst[3][1])      #horizontal distance travelled

distance = math.sqrt(vertical**2 + horizontal**2)  #total distance from current position
print(round(distance))


