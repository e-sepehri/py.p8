#from Question 11 to 14 page 459
#Q11 <<
'''
try:
    lst = [0, 0, 0, 0]
    with open('data.txt', 'r') as f:
        count = 0
    for line in f.readlines():
        lst[count] = int(line)
        count += 1
except FileNotFoundError:
    print("This file dosn't exist")
except :
    print("Unexpected error!")
'''
#Q12 <<
'''
a) *i: 22 \n End                 *ii: error---> *EXCEPTION* except ValueError: \n print('Wrong!')
b) *i: 22 \n End                 *ii: Wrong! \n End
c) *i: 22 \n End  *ii: error---> *EXCEPTION* except ValueError: \n print('Wrong!') || replace Index with Value
d) *i: 22 \n End                 *ii: Wrong! \n End
e) *i: 22 \n Wow \n End          *ii: Wrong! \n End
f) *i: 22 \n Done\n End          *ii: Wrong! \n Done \n End
g) *i: 22 \n Wow \n Done\n End   *ii: Wrong! \n Done \n End
'''
#Q13 <<
'''  Exception covers all errors and is written first thus even if we get ValueError in f() \
     the program will run Exception So to solve the problem we can first write ValueError  \
     or divide Exception into more detailed components :) '''
#Q14 <<
'''  OSError checks if the file path is inaccessible or invalid \
     thus we have to check beforehand whether the file exists or not then the file path. '''