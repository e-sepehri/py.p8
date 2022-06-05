#Q1 << tuples are immutable,can't modify tuples like add del elements modifiction &...
#Q2 << some operations can work on lists, but not on tuples so i think for make difference.
#Q3 << tuples are immutable.
#Q4 << elements in tuples are ordered.
#Q5 <<
''' a = (1,2,3,4,5,6,7,8)
    first, second , *others ,seventh , last = a
    print(others)  '''
#Q6 <<
''' a = (1,2,3,4,5,6,7,8)
    print(a[3:7])  '''
#Q7 <<
''' tpl = 7, 10, -3, 18, 6, 10
    x , *others , y = tpl  '''
#Q8 <<
'''
def product(lst):
    mult = 1
    for i in lst:
        mult *= i
    return mult

def creat_list():
    test_list = []
    counter = 0
    while counter >= 0:
        counter= float(input("Enter intigers(-1 quit)"))
        if counter != 0 and counter > -1:
            test_list += [counter]
    return test_list

ls = creat_list()
print('original list:',ls)
print('multiplication:',product(ls))
'''
#Q9 <<
'''
def zero_sum(lst):
    sumation = 0
    falg = True
    for i in lst:
        sumation += i
        if sumation == 0:
            falg = True
        else:
            falg = False
    return falg

def creat_list():
    test_list = []
    counter = 0
    while counter <= 99:
        counter= int(input("Enter intigers(100 quit)"))
        if counter <= 99:
            test_list += [counter]
    return test_list

ls = creat_list()
print(ls)
print(zero_sum(ls))
'''
#Q10 << cause dictionary associates a key with an item just like array's indices.
#Q11 << d = {}
#Q12 << print(d['Fred'])
#Q13 << python key error is what would happen.
#Q14 << same as question 13.
#Q15 << values are mutable.
#Q16<<
'''
a){3: 0, 5: 1, 10: 1, 8: 2, 15: 4}
b)the program prints keys: 3 5 10 8 15
c)same as b
d)the program prints values: 0 1 1 2 4
'''
#Q17 << dictionaries are unordered.
#Q18 << modify
'''
from tkinter import Tk, Canvas
from tkinter.ttk import Button, Frame
def do_button_press():
    global color
    if color == 'black':
        color = 'yellow'
        canvas.itemconfigure(yellow_lamp, fill='yellow')  # Turn on
    else:
        canvas.itemconfigure(yellow_lamp, fill='black')  # Turn off

color = 'black'
root = Tk()
root.title("Traffic Light")
frame = Frame(root)
frame.pack()
canvas = Canvas(frame, width=150, height=300)
canvas.create_rectangle(50, 20, 150, 280, fill='gray')
yellow_lamp = canvas.create_oval(70, 120, 130, 180, fill='black')
button = Button(frame, text='Change', command=do_button_press)
button.grid(row=0, column=0)
canvas.grid(row=0, column=1)

root.mainloop()
'''
#Q19 <<
#Q20 << by using carly brace{} we will get an empty dictionary NOT set.
#Q21 << A = set()
#Q22 << mutable ,Set in python is similar to mathematical sets we can add ,remove etc.
#Q23 <<
'''
a){2, 7, 10, 19, 20}        b)true                              c)false
d){10, 7}                   e){2, 4, 5, 6, 7, 9, 10, 19, 20}    f)true
g)true                      h)false                             i)true
j)false                     k)5                                 l){2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
m){0, 5, 8, 17, 18}         n){0, 5}
'''