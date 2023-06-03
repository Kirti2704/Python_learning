#while loop, print no. form 1 to 10 using while loop
i=1
while i<=10:
    print(i)
    i+=1

#print 100 times welcome to vit university using while loop
i=1
while i<100: 
 print("Welcome to VIT university")
 i+=1

#break keyword
i=0
while i<=10:
   print(i)
   if i==6:
       break
   i+=1

#continue keyword    
i=0
while i<10:
    i+=1
    if i==3:
        continue
    print(i)

#else statement       
i=1
while i<=10:
    print(i)
    i+=1
else:
        print("Finished")


#for loop
#22/03/2022

for x in "vellore":
     print(x)

sports = ["badminton", "cricket", "basketball", "football"]
for a in sports:
    print(a)

#write down a for loop to exist where a=baskteball
sports = ["badminton", "cricket", "basketball", "football"]
for b in sports:
    if b == "basketball":
     break
    print(b)

#continue keyword in for loop
sports = ["badminton", "cricket", "basketball", "football"]
for c in sports:
    if c == "cricket":
     continue
    print(c)

#range
for x in range(10):
  print(x)

for x in range(2,9):
    print(x)

for x in range(1,9):
     print(x)

for x in range(1,25,3):
    print(x)

#print the no ranging from 0 to 10 and also print a message when loop has ended
for a in range(0,10):
    print(a)
else:
    print("Loop has ended")


###24/03/2022
#stirngs, strings slicing
str = "peter, paul and marry"
print(str[0:5])
print(str[2:3])
print(str[7:11])
print(str[17:21])
print(str[:3])
print(str[3:])
print(str[:])

str="banana"
str1="banana"
print(str==str1)

#take and emppty string and replace it with your name
str = ""
str1 = "kirti"
str=str1
print(str1)

#find function
s = "I am Indian."
x = s.find("I")
print(x)

#type function
print(type(10))
print(type("a"))
print(type("10"))

str="Peter, Paul, and Mary"
print(str[0:5])


##25/03/2022
id(3)
134882108
betty = 3
print(id(betty))
134882108

#type conversion
int("32")
print(int("hello"))
#can not convert from int to stirng

int(3.9999)
print(int(-2,3))
-2 #int() can't convert non-string with explicit base

float(32)
print(float("3.14159"))

str(32)
'32'
print(str(3.14149))
'3.14149'

a="kirti"
print(id(a))


print(int("Dkay"))

# float to integer
print(float(3))
print(float(-23))
print(float("Vellore"))
print(str(34))
a=str(34.67)
print(a)

#write a program to take a int and a float value as an input from the user,
#convert that to string first and then multiply the int converted value 
#with nuo. 3 and float converted value with no. 10.

a = input("enter an integer value : ")
b = input("enter a float value : ")
i = str(a*3)
f = str(b*10)
print(i)
print(f,)

#calling a math function
import math

dacibel = math.log10(17.0)
angle = 1.5
height = math.sin(angle)

x = math.exp(math.log(10.0))

print(height)
print(x)

""" 
what is the difference between a parameter and arguments. be ready to 
present in class

A parameter is a named variable passed into a function. Parameter variables
are used to import arguments into functions.
For example:

from doctest import Example


function Example(parameter) 
console.log(parameter)


const argument = 'hello'

example(argument)

Note the difference between parameters and arguments:

Function parameters are the names listed in the function's definition.
Function arguments are the real values passed to the function.
Parameters are initialized to the values of the arguments supplied.
Two kinds of parameters:

input parameters: the most common kind; they pass values into functions. 
Depending on programming language, input parameters can be passed several 
ways (e.g., call-by-value, call-by-address, call-by-reference).

output/return parameters: primarily return multiple values from a function,
but not recommended since they cause confusion


Sum = 0
for i in list : 
    Sum = sum + I
print(sum)
Mul = 0
for i in list : 
    Mul = multiply*i
print(mul)
"""
def sum(a,b):   # Here a,b are the parameters
  print(a+b)
  
sum(1,2)  # Here the values 1,2 are arguments  


#python program to find factorial of a number using recusrion
def recursive_factorial(n):
  if n == 1:
     return n
  else:
     return n*recursive_factorial(n-1)     #function calling itself

#taking input from the user
number = int(input("Enter a positive number : "))
print("The factorial of", number, "is", recursive_factorial(number))

list(range(1,10,2)) #1 is starting point, 10 is ending point which is 
#excluded in output and 2 is skipping range
#output is [1,3,5,7,9]

#list me exam me jab tak range function use karne na bole tab tak nhi krna

#can a string have multiple data types 
# ...........print a lsit of characters from a to z with range function.

#make 2 list compare them and print the output as true if the elements of 
#the list are same else print false
def test_includes_any(nums, lsts):
    for x in lsts:
        if x in nums:
            return True
    return False 
l1 = ['my', 'name', 'is']
l2 = ['my', 'name', 'is']

#write a program a list of numbers. print the sum of all numbers and also 
#print the multipication of all the numbers by 5.
total = 0
list1 = [11, 5, 17, 18, 23]

for element in range(0, len(list1)):
    total = total + list1[element]
 
print("Sum of all elements in given list: ", total)

for element in list1:
    list1.append(element * 5)

print(list1)

#take some strings as values in list and write a program to reverse a list.

list = ["my", "name", "is", "kirti"]
print ("The original list is : " + str(list))
res = [i[::-1] for i in list]
  
print ("The reversed string list is : " + str(res))

#tuples
t1 = (1,2,3,4,5)
print(t1)

#when we define a single value in tuple then we have to put a comma after 
#single value
t2 = (45,)
print(type(t1))

#create a tuple for a single value integer and string
t1=input('enter a string',)
t2=input('enter a integer',)

#take a tuple = a,b,c and print the index of value b
t3 = ('a','b','c')
print(t3.index('b'))
#index of 3

#change the value with 42 and print the output

#2 tuples, t1 and t2 and replace the value of t1 to t2.
t1 = (1,2,3,4)
t2 = (4,5,6,7)
s = t1 = t2
print(s)

#slicing in tuple
tuple1 = (2,36,45,78,95,41,25,25)
print(tuple[3:6])
#counting in tuple
#find the minimum and maximum from tuple1
print(min(tuple1))
print(max(tuple1))

def swap(x,y):
 x,y = y,x
a=(1,)
b=(2,)
swap(a,b)
print(a,b)

def mydemo(v):
    print(id(v))
    return v[2:]
w = mydemo([1,2,3,4,5])
type(w)
print(id(w))

#dictionaries in python

fruitdic = {"fruit1" : "mango", "fruit2" : "apple", "fruit3" : "strawberry",
"fruit4" : "orange"}
print(fruitdic)
print(fruitdic["fruit3"])

i = fruitdic.items()
k = fruitdic.keys()
v = fruitdic.values()
fruitdic.update({"fruit5" : "banana"})
g = fruitdic.get("fruit1")
p = fruitdic.pop("fruit2")
print(i,k,v,g,p)
print(len(fruitdic))

#fruitdic.update({"fruit3" : "banana"}) : same name ke sath aa sakte h but
#key name change hoga
#to concatenate 2 dictionaries into 1 as 3rd dictionary
dic1 = {"name1" : "kirti", "name2" : "amisha", "name3" : "sanskriti"}
dic2 = {"dob1" : "22", "dob2" : "2002", "dob3" : "8" }
print(dic1, dic2)
dict1 = dic2
del(dic2)
print(dict1)

#data types in python with example explanation

#sets 
#create a set a2 = 1,2,3,4,1,3 and print a2 and perform all the operations
#the set, pop, clear, type, id, ........
#write a program to differentiate between ordered and unordered data 
#sructures in python

#class(keyword) Employee(class name)
# class is collection of object
# obejcts are real time things
# class is a data type, no memory location occupied for class
# instaciation of class
from turtle import color


class sum1:
 def sum(self):
  return self.a, self.b
# instance for a class
s1=sum1()
s1.a = 10
s1.b = 20

# program for creating a class named as calculator having methods 1 : for calculating 
# bmi, 2 : conversion of kms in meters, 3 : conversion of farenhite to celsius
class calculator:
    def bmi(self):
        height = float(input("Enter the height in cm: "))  
        weight = float(input("Enter the weight in kg: "))    
        bmi = weight / (height/100)**2   
        return bmi
    def kminm(self):
        kms = int(input("Enter kms"))
        result = kms*1000
        return result
    def fahtocel(self):
        fah=int(input("Enter ferhenhiet value"))
        result=(5/9)*(fah-32)
        return result
c=calculator()
print(c.bmi())
print(c.kminm())
print(c.fahtocel()) 


#consturctors in python
class laptop:
    def compname_one(self):
        print("welcomes you:")
    def price_laptop(self):
        print("price of laptop is:")
#creating instance for class
s1 = laptop()
s1.compname_one()
s1.price_laptop()

class Laptop1:
    def set_color(self, color):
        self.color=color
    def set_price(self, price):
        self.price=price
    def show_color(self):
        #return self.color
        print(self.color)
    def show_price(self):
        return self.price

#creating instance for class
s2 = Laptop1()
s2.set_color("black")
s2.set_price(1000)
#print(s2.show_color)
s2.show_color()
s2.show_price()

print("laptop details are" , s2)

class laptop3:
    def __init__(self, color, price)
    self.color = color
    self.price = price

    def show_laptopdetails(self):
        print("color of the laptop is", self.color)
        print("color of the laptop is", self.color)

lap1 = laptop3('blue', 1919)
lap1.show_laptopdetails


#program to demonstrate the use of class abstraction and encapsulation with example
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")   
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")   
          
# Driver code   
t= Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  

# Python program to define   
# abstract class  

from abc import ABC  
  
class Polygon(ABC):   
  
   # abstract method   
   def sides(self):   
      pass  
  
class Triangle(Polygon):   
  
     
   def sides(self):   
      print("Triangle has 3 sides")   
  
class Pentagon(Polygon):   
  
     
   def sides(self):   
      print("Pentagon has 5 sides")   
  
class Hexagon(Polygon):   
  
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):   
  
   def sides(self):   
      print("Square have 4 sides")   
  
# Driver code   
t = Triangle()   
t.sides()   
  
s = square()   
s.sides()   
  
p = Pentagon()   
p.sides()   
  
k = Hexagon()   
k.sides()   


# using public members
class pub_mod:
    # constructor
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
 
    def Age(self): 
        # accessing public data member 
        print("Age: ", self.age)
# creating object 
obj = pub_mod("Jason", 35);
# accessing public data member 
print("Name: ", obj.name)  
# calling public member function of the class 
obj.Age()

# using private member
class Rectangle:
  length = 0 #private variable
  breadth = 0#private variable
  def __init__(self): 
    #constructor
    self.length = 5
    self.breadth = 3
    #printing values of the private variable within the class
    print(self.length)
    print(self.breadth)
 
rect = Rectangle() #object created 
#printing values of the private variable outside the class 
print(rect.length)
print(rect.breadth)

# illustrating protected members & protected access modifier 
class details:
    name="Jason"
    age=35
    job="Developer"
class pro_mod(details):
    def __init__(self):
        print(self.name)
        print(self.age)
        print(self.job)
 
# creating object of the class 
obj = pro_mod()
# direct access of protected member
print("Name:",obj.name)
print("Age:",obj.age)



#create a file using notepad on desktop that has the massage my name, welcome to
#the university
#be very careful while using os. delete kar dega sab
# program to create a file on desktop appends some information into it. display 
#file contents nd again append our subject name in the file and save it(close it).
f = open("D:\Programming\Python \ files.txt", 'a+')
f.read()
f.write("\nWe are learning python!")
f.writelines("\nWe are learning python!", 'w' )
print(f.read())
f.close()

#what do you understand by tickling & deticking (civilisation & decivilisation )
#exceptions : occurance of runtime error
print(55/0)

b = {}
print(b['what'])

a = []
print(a[5])

f = open("idontexist", "r")

#try statement. try: -except: -else: -finally:
#what do you mean by assert nd raise.
#what happens when a=5, b=0, a/b. it is not completely executing the code
x,y=5,0
try:
    x/y
except:
    print("Divison by zero")
print("program is still executing")


try:
    f=open("nomore.txt")
except FileNotFoundError as msg:
 print("File not found")
 print(msg)


try:
    f=open("nomore.txt")
except FileNotFoundError as msg:
    print("File not found")
else:
    print("Data from file")
    print(f.read())
finally: 
    print("i am going to close file")
    f.close()

#raise
class myError(Exception):
    pass
try:
    raise myError("this exception is created by kirti")
except myError as msg:
    print(msg)

#assert
x,y=5,6 
try:
    assert (x==y), "this statement is false"
except AssertionError as msg:
    print(msg)

###25/04/22
#tkinter for ui in pyhton
#create a gui window using tkinter module
import tkinter
mybox=tkinter.Tk()
mybox.geometry("400x200")
mybox.configure(bg='red')
mybox.title("This is window")
tkinter.mainloop()

#program for creating a button and adding it into a window
import tkinter
mybox=tkinter.Tk()
mybox.geometry("400x200")
mybox.title("This is window")
myb1=tkinter.Button(mybox,text="Button 1", bg='blue', fg='yellow').pack(side="left")
myb2=tkinter.Button(mybox,text="Button 2").pack(side="top")
myb3=tkinter.Button(mybox,text="Button 3").pack(side="right")
myb4=tkinter.Button(mybox,text="Button 4").pack(side="bottom")
tkinter.mainloop()

#where we can place attributes in this. fg is text color on the button.

#define a function 
import tkinter
mybox=tkinter.Tk()
mybox.geometry("400x200")
mybox.title("This is window")
def bfun():
    tkinter.Label(mybox,text="You have clicked the Button, thanks").pack()
myb=tkinter.Button(mybox,text="Click Me",bg='blue',fg='yellow',command=bfun).pack(side="left")
tkinter.mainloop()

#entry and label
#import tkinter
from tkinter import *
#myw=Tk()
#import tkinter
myw=tkinter.Tk()
myw.geometry('300x200')
Label(myw,text="User Id").grid(row=0)
Label(myw,text="Password").grid(row=1)
t1=Entry(myw)
t2=Entry(myw)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
myb=tkinter.Button(myw,text="Continue", bg='blue', fg='yellow').pack(side="bottom")
tkinter.mainloop()

import tkinter
from tkinter import messagebox 

#hide main window
root = tkinter.Tk()
root.withdraw()

#message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning", "Warning message")
messagebox.showinfo("Information", "Informative MessageBox")


####26/04
from tkinter import * 
myw=Tk()
myw.geometry('300x300')
myc=Canvas(myw,width=200,height=200,bg='yellow')
myarc=myc.create_arc(10,10,150,110,start=0,extent=300,fill='red',outline='green',width=10)
myc.place(relx=.1,rely=.1)
mainloop()

#frame widget
from tkinter import * 
myw=Tk()
myw.geometry('500x200')
myw.configure(bg='yellow')
myw.title("Example for frame widget")
leftframe=Frame(myw,height=100,width=200,bg='red')
leftframe.place(x=10,y=10)
rightframe=Frame(myw,height=100,width=200,bg='green')
rightframe.place(x=220,y=10)
l1=Label(leftframe,text="Label 1")
l1.place(x=10,y=10)
l2=Label(rightframe,text="Label 2")
l2.place(x=10,y=10)
l3=Label(rightframe,text="Label 3")
l3.place(x=10,y=50)
mainloop()

#list box
from tkinter import * 
myw=Tk()
myw.geometry('300x200')
myw.configure(bg='yellow')
myw.title("Listbox widget using tkinter")
mylst=Listbox(myw)
mylst.grid(row=0)
mylst.insert(0, 'Delhi')
mylst.insert(1, 'Bombay')
mylst.insert(2, 'Bangalore')
mylst.insert(3, 'Jaipur')
mylst.insert(END, 'Goa')
Label(myw,text="Enter index to delete").grid(row=0,column=1)
e1=Entry(myw,width=5)
e1.grid(row=0,column=2)
def mydel():
    mylst.delete(int(e1.get()))
Button(myw,text="Delete",command=mydel).grid(row=1,column=1)
mainloop()

####
from tkinter import *
mybox=tkinter.Tk()
mybox.geometry("500x300")
mybox.configure(bg='blue')
mybox.title("Login page")

myw=tkinter.Tk()
myw.geometry('200x100')
myw.configure(bg='yellow')
Label(myw,text="User Id").grid(row=0)
Label(myw,text="Password").grid(row=1)

e1=Entry(myw,width=5)
e1.grid(row=0,column=2)
def mydel():
    myw.insert(int(e1.get()))
Button(myw,text="Submit",command=mydel).pack(side="bottom")

tkinter.mainloop()

##amisha's try
from tkinter import *
myw=Tk()
myw.geometry('300x200')
myw.configure(bg='blue')
myw.title('Login Page')
leftframe=Frame(myw,height=100,width=200,bg='yellow')
leftframe.place(x=10,y=10)


Label(myw,text="User Id").grid(row=0)
Label(myw,text="Password").grid(row=1)
t1=Entry(myw)
t2=Entry(myw)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
mainloop()


####Radiobutton using tkinter
from tkinter import * 
myw=Tk()
myw.geometry('300x200')
myw.configure(bg='yellow')
myw.title("Radiobutton widget using tkinter")
myvar=IntVar()
myl=Label(myw,width=18)
myl.grid(row=0)
def myf():
    myl.configure(text="You have selected"+str(myvar.get()))
rb1=Radiobutton(myw,text="Male",variable=myvar,value=0,width=15,\
                anchor='w',coomand=myf)
rb1.grid(row=1)
rb2=Radiobutton(myw,text="FeMale",variable=myvar,value=1,width=15,\
                anchor='w',coomand=myf)
rb1.grid(row=2)
rb2.select()
mainloop()

##
from tkinter import * 
myw=Tk()
myw.geometry('300x200')
myw.configure(bg='yellow')
myw.title("Radiobutton widget using tkinter")
myvar=IntVar()
myl=Label(myw,width=18)
myl.grid(row=0)
def myf():
    myl.configure(text="You have selected"+str(myvar.get()))
rb1=Radiobutton(myw,text="Option A",variable=myvar,value=0,width=15,\
                anchor='w',coomand=myf)
rb1.grid(row=1)
rb2=Radiobutton(myw,text="Option B",variable=myvar,value=1,width=15,\
                anchor='w',coomand=myf)
rb2.grid(row=2)
rb3=Radiobutton(myw,text="Option C",variable=myvar,value=2,width=15,\
                anchor='w',command=myf)
rb3.grid(row=3)
rb4=Radiobutton(myw,text="Option D",variable=myvar,value=3,width=15,\
                anchor='w',command=myf)
rb4.grid(row=4)
rb2.select()
mainloop()

###checkbutton using tkinter
from tkinter import * 
myw=Tk()
myw.geometry('300x200')
myw.configure(bg='yellow')
myw.title("Checkbutton widget using tkinter")
myvar1=IntVar()
myvar2=IntVar()
myl=Label(myw,width=18)
myl.grid(row=0)
def myf():
    myl.configure(text="Music"+str(myvar1.get())+"Reading"+\
              str(myvar2.get()))
cb1=Checkbutton(myw,text="Music",variable=myvar1,onvalue=1,offvalue=0,\
                width=15,anchor='w',command=myf)
cb1.grid(row=1)
cb2=Checkbutton(myw,text="Reading",variable=myvar2,onvalue=1,offvalue=0,\
                width=15,anchor='w',command=myf)
cb2.grid(row=2)
mainloop()

###menubutton
from tkinter import *
from tkinter.filedialog import askopenfilename
myw=Tk()
myw.geometry('300x200')
myw.configure(bg='yellow')
myw.title("Menu widget using tkinter")
mymenu=Menu(myw)
myw.configure(menu=mymenu)
filemenu=Menu(mymenu)
mymenu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='Save')
filemenu.add_command(label='SaveAs')
editmenu=Menu(mymenu)
mymenu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
mainloop()


## registraion form using tkinter
from tkinter import *
myw=Tk()
myw.geometry('300x200')
myw.title("Sign up")
Label(myw,text="Name").grid(row=0)
Label(myw,text="Email Id").grid(row=1)
Label(myw,text="Password").grid(row=2)
Label(myw,text="Confirm Password").grid(row=3)
t1=Entry(myw)
t2=Entry(myw)
t3=Entry(myw)
t4=Entry(myw)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
t3.grid(row=2,column=1)
t4.grid(row=3,column=1)
myb1=Button(myw,text="Cancel", bg='blue', fg='yellow').pack(side="bottom")
myb2=Button(myw,text="Sign up", bg='blue', fg='yellow').pack(side="bottom")

from tkinter import *
myw=Tk()
myw.geometry('300x200')
myw.title("Registration form")
Label(myw,text="Name").grid(row=0, column=1)
Label(myw,text="Surname").grid(row=0, coulmn=2)
Label(myw,text="Father name").grid(row=1, column=1)
Label(myw,text="Mother name").grid(row=1,column=2)
t1=Entry(myw)
t2=Entry(myw)
t3=Entry(myw)
t4=Entry(myw)
t1.grid(row=0,column=1)
t2.grid(row=0,column=2)
t3.grid(row=1,column=1)
t4.grid(row=1,column=2)

myvar1=IntVar()
myl=Label(myw,width=18)
myl.grid(row=0)
def myf():
    myl.configure(text="Nationality"+str(myvar1.get()))
rb1=Radiobutton(myw,text="Indian",variable=myvar1,value=0,width=15,\
                anchor='w',coomand=myf)
rb1.grid(row=1)
rb2=Radiobutton(myw,text="Non-Indian",variable=myvar1,value=1,width=15,\
                anchor='w',coomand=myf)
rb1.grid(row=2)
rb2.select()
mainloop()

myvar2=IntVar()
myvar3=IntVar()
myl=Label(myw,width=18)
myl.grid(row=0)
def myf():
    myl.configure(text="Music"+str(myvar2.get())+"Reading"+\
              str(myvar2.get()))
cb1=Checkbutton(myw,text="Music",variable=myvar1,onvalue=1,offvalue=0,\
                width=15,anchor='w',command=myf)
cb1.grid(row=1)
cb2=Checkbutton(myw,text="Reading",variable=myvar3,onvalue=1,offvalue=0,\
                width=15,anchor='w',command=myf)
cb2.grid(row=2)

myb=Button(myw,text="Submit", bg='blue', fg='yellow').pack(side="bottom")
mainloop()