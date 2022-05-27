#This program is done in python 3
#Below is the about of the program considering the criterias given here
#About the program
'''
A Simple program to calculate the sum of last two digit of a list
if the 1st number is greater than the last, else substraction is done
If the result is negative it prints 'Bad Luck', if zero then 'Neutral',
if postive than 'Good Luck'
'''
#Psuedocode

'''
Get the number of elements of the list
Loop (till the given number of elements)
    Get the elements of the list

Get the 1st value of the list
Get the last value of the list
If the 1st value is greater than last value then,
    result = Add 1st value and last value

else
    result = Substract 1st value and last value

if the result is greater than 0 then,
    print Good Luck

else if the result is smaller than 0 then,
    print Bad Luck

else
    print Neutral
'''

#Name of the author

#===============================================================================


#Function for input data

def input_data():

    a = int(input("Enter the number of element : "))
    l = []
    for i in range(1, a+1):
        n = int(input("Enter the elements : "))
        l.append(n)

    return l

#===============================================================================
#Function for output data

def output_data(result):
    print("Required result : ",result)

#===============================================================================

#Function for conditional statements and calculation

def calc(l):

    a = l[0] #First element of the list is stored
    b = l[len(l)-1] #Last element of the list is stored
    cal = 0

    if(a > b):
        cal = a + b

    else:
        cal = a - b

    if(cal > 0):
        return('Good Luck')

    elif(cal < 0):
        return('Bad Luck')

    else:
        return('Neutral')


#===============================================================================
A = input_data()
res = calc(A)
output_data(res)
