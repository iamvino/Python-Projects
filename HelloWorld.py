# Chapter 1 - Working with numbers, texts and dates
# This is a python comment in my first Python app
print("Hello World!")
# This variable contains an integer
quantity = 10
# This variable contains a float
unit_price = 1.99
# This variable contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price
# Show the results
print(extended_price)
quantity = 14
unit_price = 26.99
extended_price = quantity * unit_price
print(extended_price)
num = 10
if num > 0:
    print("Positive number")
else:
    print("Negative number")
# Calculating Numbers with Functions
first_name = "Alan"
last_name = "Simpson"
print(first_name, last_name)
#codes where two or three lines of code work together
x = 10
if x == 10:
    print("x is zero")
else:
    print("x is ", x)
print("All done")
# Absolute numbers
x = -4
y = abs(x)
print(x)
print(y)
# whole numbers
x = 3.141592653589793238462643
y = round(x,2)
print(x)
print(y)
# Built-in Python Functions for numbers
x=128
pi=3.14159265358979
y=-345.67890987
z=-999.9999
print(abs(z))
print(int(z))
print(int(abs(z)))
print(round(pi,4))
print(bin(x))
print(hex(x))
print(oct(x))
print(max(pi,x,y,z))
print(min(pi,x,y,x))
print(type(pi))
print(type(x))
print(type(str(y)))
# Built-in Python Functions for Math
from cmath import sqrt
import math
print(sqrt(81))
z = 81
print(math.sqrt(81))
pi = math.pi
e = math.e
tau = math.tau
x = 81
y = 7
z = -23234.5454
print(pi)
print(e)
print(tau)
print(math.sqrt(x))
print(math.factorial(y))
print(math.floor(z))
print(math.degrees(y))
print(math.radians(45))
# Formatting with f strings
username = "Vino"
f"Hello {username}"
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price}")
# To show commas in thousand places
print(f"Subtotal: ${quantity * unit_price:,}")
# To get the pennies to show as two digits
print(f"Subtotal: ${quantity * unit_price:,.2f}")
# Formatting percent numbers
sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")
# Formatting percent numbers to 2 decimal places
print(f"Sales Tax Rate {sales_tax_rate:.2%}")
# Formatting percent numbers to 1 decimal places
print(f"Sales Tax Rate {sales_tax_rate:.1%}")
# Use \n to get a line break
user1 = "Alberto"
user2 = "Baba"
user3 = "Basha"
output=f"{user1} \n{user2} \n{user3}"
print(output)
# Use triple quotation mark to get line break
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output=f"""
Subtotal:  ${subtotal:,.2f}
Sales Tax: ${sales_tax:,.2f}
Total:     ${total:,.2f} 
"""
print(output)
# Formatting width and alignment
output=f"""
Subtotal:  ${subtotal:>9,.2f}
Sales Tax: ${sales_tax:>9,.2f}
Total:     ${total:>9,.2f} 
"""
print(output)
# Convert numbers to Binary, Octal & Hexadecimal numbers
x = 254
print(bin(x))
print(oct(x))
print(hex(x))
# Working with dates
import datetime as dt
today = dt.date.today()
last_of_teens = dt.date(2023,10,18)
print(today)
print(last_of_teens)
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)
print(f"{last_of_teens: %A, %B %d, %Y}")
todays_date = f"{today: %m%d%Y}"
midnight = dt.time()
print(midnight)
now = dt.datetime.now()
birthdatetime = dt.datetime(1995, 3, 31, 8 ,26)
age = now - birthdatetime
print(age)
print(type(age))
# Chapter 2 - Controlling the actions
# If else and nested if else
sun = "down"
if sun == "down": 
    print("Good night")
elif sun == "up":
    print("I am here")
else:
    print("It is dawn")
# Ternary operations 
age = 35
if age < 21:
    beverage = "milk"
elif age >=21:
    beverage = "beer"
else:
    beverage = "prune juice"
print("Have a " + beverage)
# Repeating a process with for
for x in range(9):
    print(x)
print("All done")
for x in range(1,10):
    print(x)
print("All done")
for x in "adamant":
    print(x)
print("done")
my_word = "adamant"
for x in my_word:
    print(x)
print("done")
#Looping through a list
for x in {"The", "rain", "in", "Spain"}:
    print(x)
print("done")
# Bailing out of a loop
answers = ["A", "B", "C", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is complete")
# Looping with continue
answers = ["A", "B", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        continue
    print(answer)
print("Loop is complete")
# Nested Loops
for outer in ["first", "second", "third"]:
    print(outer)
    for inner in range(3):
        print(inner + 1)
print("Both loops are done")
# loopig with while
counter = 65
while counter < 91:
    print(str(counter) + "=" + chr(counter))
    counter += 1
print("all done")
# Starting while loops over with continue
import random
print("Odd numbers")
counter = 0 
while counter < 10:
    # get a random number
    number = random.randint(1,999)
    if int(number / 2) == number / 2:
        #if it is an even number, do not print it
        continue
    #if it is odd, print it and increment it by 1
    print(number)
    counter += 1
print("Loop is done")
# Breaking while loops with break
import random
print("Odd numbers")
counter = 0 
while counter < 10:
    # get a random number
    number = random.randint(1,999)
    if int(number / 5) == number / 5:
        #if it is divisible by 5, stop the loop
        break
    #otherwise, print it and increment it by 1
    print(number)
    counter += 1
print("Loop is done")
#Chapter 3 - Lists and Tuples
# Lists
scores = [88, 92, 78, 90, 98, 84]
students = ["Mark", "Amber", "Suvi", "Viswa", "Suga"]
print(students)
print(students[0])
print(scores[3])
# Looping through a list
for score in scores:
    print(score)
print("done")
# Check contents of a list
has_suvi = "Suvi" in students
print(has_suvi)
has_vino = "Vino" in students
print(has_vino)
# Counting the length of a list
print(len(students))
# Add an item to the list - append
student_name = "Amanda"
# add student_name only if not already in the list
if student_name in students:
    print(student_name + " already in the list")
else:
    students.append(student_name)
    print(student_name + " added to the list")
# Inserting an item into a list
student_name = "Vino"
# Add student name to front of the list
students.insert(0,student_name)
print(students)
# Changing/replacing an item in a list
students[3] = "Kamal"
print(students)
# Combining lists
list1 = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
list2 = ["Foxtrot", "Golf", "Hotel", "India", "Juliet"]
# Add list2 to list1
list1.extend(list2)
print(list1)
# Removing items from a list
list1.remove("Juliet")
print(list1)
# Remove the first item
list1.pop(0)
# Remove the last item
list1.pop()
print(list1)
# deleting a item from a list
del list1[2]
print(list1)
# Counting item instances in a list
grades = ["C", "B", "A", "D", "C", "B", "C"]
b_grades = grades.count("B")
look_for = "C"
c_grades = grades.count(look_for)
print("There are " + str(b_grades) + " B grades in the list.")
print("There are " + str(c_grades) + " " + look_for + " grades in the list.")
print("There are " + str(grades.count("F")) + " F grades in the list.")
# Finding an list item's index
b_index = grades.index("B")
look_for = "A"
a_index = grades.index(look_for)
print("The first B is index " + str(b_index))
print("The first " + look_for + " is at " + str(a_index))
# Use if in finding an item in a list
look_for = "F"
if look_for in grades:
    print(str(look_for) + " is at index" + str(grades.index(look_for)))
else:
    print(str(look_for) + " is not in the list")
# Sorting lists
names = ["Vino", "Suga", "Suvi", "Visu"]
numbers = [11, 20, 27, 25] 
names.sort()
numbers.sort()
print(names)
print(numbers)
# Reversing a list
names.reverse()
print(names)
# List with dates
import datetime as dt
datelist = [dt.date(1988,7,11), dt.date(1988,11,20), dt.date(2017,2,27), dt.date(2020,6,25)]
print(datelist)
datelist.sort()
print(datelist)
datelist.sort(reverse=True)
for date in datelist:
    print(f"{date:%d/%m/%Y}")
datelist = []
datelist.append(dt.date(1988,7,11))
datelist.append(dt.date(1988,11,20))
datelist.append(dt.date(2017,2,27))
datelist.append(dt.date(2020,6,25))
datelist.sort()
for date in datelist:
    print(f"{date:%m/%d/%y}")
datelist.sort(reverse=True)
for date in datelist:
    print(f"{date:%d/%m/%Y}")   
# Copying a list
names = ["Vino", "Suga", "Suvi", "Visu"]
backward_names = names.copy()
backward_names.reverse()
print(names)
print(backward_names)
backward_names.clear()
print(backward_names)
# Tuples has same syntax as list but use parantheses instead if []
prices = (9.98, 4.95, 79.98, 2.96, 29.95)
print(len(prices))
print(prices.count(4.95))
print(4.95 in prices)
look_for = 12345
if look_for in prices:
    position = prices.index(look_for)
else:
    position=-1
print(position)
# Loop in tuples
for price in prices:
    print(f"${price:.2f}")
# Cannot replace an item in tuples, can be used to show data but not change
#prices[1] = 234.56
# Working with sets
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
print(sample_set)
sample_set.add(11.23)
print(sample_set)
sample_set.update([88, 12.45, 2.98])
print(sample_set)
print(len(sample_set))
ss2 = sample_set.copy()
for price in sample_set:
    print(f"{price:>6.2f}")
# Chatper 4 - Data dictionaries
people = {
    'velumalai': 'Vinothraj Elumalai',
    'ppatel': 'Priya Patel',
    'svinothraj': 'Suganya Vinothraj',
    'hjackson': 'Hugh Jackson',
    'jpatel': 'Jaymin Patel',
    }
print(people) 
print(people["svinothraj"])
person = 'htanaka'
print(person)
# Getting the length of a dictionary
howmany = len(people)
print(howmany)
# Check if a key exists in dictionary
print('hjackson' in people)
print('vvinothraj' in people)
# Getting dictionary data with get()
person = 'velumalai'
print(people.get(person))
person = 'vvinothraj'
print(people.get(person))
# Changing the value of key
people["hjackson"] = "Hugh Jackson-Smith"
print(people["hjackson"])
# Adding or changing dictionary data
people.update({'wwiggins':'Wanda Wiggins'})
for person in people.keys():
    print(person + " = " + people[person])
# Looping through a dictionary
for person in people:
    print(person)
for person in people:
    print(people[person])
for key, value in people.items():
    print(key, "=", value)
# clear(), copy(), fromkeys()returns a new copy but with only specified keys and values
# get(), items(), keys(), pop(), popitem(), setdefault(), update(), values()
# Copying a dictionary
peeps2 = people.copy()
print(people)
print(peeps2)
del people["wwiggins"]
print(people)
people.clear()
print(people)
# Using pop() with Data Dictionaries
people = {
    'velumalai': 'Vinothraj Elumalai',
    'ppatel': 'Priya Patel',
    'svinothraj': 'Suganya Vinothraj',
    'hjackson': 'Hugh Jackson',
    'jpatel': 'Jaymin Patel',
    }
adios = people.pop("jpatel")
print(adios)
print(people)
# Fun with Multi-Key Dictionaries
product = {
    'name' : 'Ray-Ban Wayfarer Sunglasses',
    'unit_price' : 112.99,
    'taxable' : True,
    'in_stock' : 10,
    'models' : ['Black', 'Tortoise']
}
print(product["name"])
print(product["unit_price"])
print(product["taxable"])
print(product["in_stock"])
print(product["models"])
# fancy print
print('Name:     ', product["name"])
print('Price:    ',f"${product['unit_price']:.2f}")
print('Taxable:  ',product["taxable"])
print('Models:   ')
for model in product["models"]:
    print(" " * 11 + model)
# Using fromkeys and setdefault methods
product = {
    'name': '',
    'unit_price': 0,
    'taxable': True,
    'in_stock': 0,
    'models': []
}
DWC001 = dict.fromkeys(product.keys())
DWC001.setdefault('taxable',True)
DWC001.setdefault('models',[])
DWC001.setdefault('reorder_point',100)
print("Dictionary after fromkeys() and setdefault()")
print(DWC001)
print("\nDictionary after fromkeys() and setdefault()")
DWC001['taxable']=True
print(DWC001)
# Nesting Dictionaries
products = {
    'RB00111':{'name':'Rayban Sunglasses', 'price':112.98, 'models':['black', 'tortoise']},
    'DWC0317':{'name':'Drone with Camera','price':72.95,'models':['white', 'black']},
    'MTS0540':{'name':'T-Shirt', 'price':2.95, 'models':['small','medium','large']},
    'ECD2989':{'name':'Echo Dot','price':29.99,'models':[]},
}
for oneproduct in products.keys():
    id = oneproduct
    name = products[oneproduct]['name']
    unit_price = '$' + f"{products[oneproduct]['price']:,.2f}"
    models = ''
    for m in products[oneproduct]['models']:
        models += m + ','
    if len(models) > 2:
        models = models[:-2]
    else:
        models="<none>"
    print(f"{id:<6} {name:<17} {unit_price:<8} {models}")
    # Wrangling bigger chunks of code
    # Creating a function
    def hello():
        print('Hello')
    hello()
    # Passing information to a function
    def hello(user_name):
        print('Hello ' + user_name)

    hello('Allan')
# Defining optional parameters with defaults
# def hell(parameter name = defaultvalue):
def hello(user_name = 'nobody'):
    print('Hello ' + user_name)

hello('Allan')
hello()
# Passing multiple values to a function
def hello(fname, lname, datestring):
    msg = "Hello " + fname + " " + lname
    msg += " you mentioned " + datestring
    print(msg)

hello('Alan', 'Simpson', '12/31/2019')
# defaults and if statements in function
def hello(fname, lname, datestring=''):
    msg = "Hello " + fname + " " + lname
    if len(datestring) > 0:
        msg += " you mentioned " + datestring
    print(msg)

hello('Alan', 'Simpson', '12/31/2019')
hello('Aaru', 'Saami')
# Using keyword arguments(kwargs)
apt_date = '09/10/2023'
last_name = 'Alan'
first_name = 'Mark'
hello(datestring=apt_date, lname=last_name, fname=first_name)
# Passing multiple values in a list
def alphabetize(original_list=[]):
    """Pass any list in square brackets, displays a string with items sorted"""
    # Inside the function make a copy of the list passed in
    sorted_list = original_list.copy()
    # Sort the working copy
    sorted_list.sort()
    # Make a new empty string output
    final_list = ''
    # Loop through sorted list and append name and comma and space
    for name in sorted_list:
        final_list += name + ', '
    # Knock off last comma space if final list is long enough
    final_list = final_list[:-2]
    # Print the alphabetized list
    print(final_list)

alphabetize(['Suvi', 'Visu', 'Vino', 'Suga'])
names = ['Suvi', 'Visu', 'Vino', 'Suga']
alphabetize(names)
# Passing in an arbitrart number of arguments
def sorter(*args):
    """Pass in any number of arguments seperated by commas
    Inside the function, they are treated as a tuple named args"""
    # The passed-in
    # Create a list from the passed-in tuple
    newlist = list(args)
    # Sort and show the list
    newlist.sort()
    print(newlist)

sorter(1, 0.001, 100, 999, 9)

# Returning values from functions
def alphabetize(original_list=[]):
    """Pass any list in square brackets, displays a string with items sorted"""
    # Inside the function make a copy of the list passed in
    sorted_list = original_list.copy()
    # Sort the working copy
    sorted_list.sort()
    # Make a new empty string output
    final_list = ''
    # Loop through sorted list and append name and comma and space
    for name in sorted_list:
        final_list += name + ', '
    # Knock off last comma space if final list is long enough
    final_list = final_list[:-2]
    # Print the alphabetized list
    return final_list

names = ['Suvi', 'Visu', 'Vino', 'Suga']
alpha_list = alphabetize(names)
print(alpha_list)

# Unmasking anonymous(lambda) functions

# Chapter 6 - Doing Python with Class
# Important to remember - Class, Instance, Attribute & Method
# Define a new class name member
import datetime as dt

class Member:
    """" Create a new member"""
    def __init__(self, uname, fname):
        # Define attributes and give them values
        self.username = uname
        self.fullname = fname
        self.date_joined = dt.date.today()
        self.is_active = True
    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date:%m/%d/%y}"
    
# The class ends at the first un-indented line

# Create an instance of the Member class named new_guy
new_guy = Member('Rambo', 'Rocco Moe')

# See what is in the instance as well as it individual properties
print(new_guy)
print(new_guy.username)
print(new_guy.fullname)
print(type(new_guy))

# Changing the value of an attribute
new_guy.username = "Suviksha"

print(new_guy.username)
print(new_guy.fullname)

# Default date_joined to today's date
new_guy.date_joined = dt.date.today()
# Set is_active to True initially
new_guy.is_active = True

print(new_guy.date_joined)
print(new_guy.is_active)

# print(new_guy.date_joined())

# Passing parameters to methods

# Calling a class method by class name
wilbur = Member('wblomgren', 'Wilbur Blomgren')
print(wilbur.date_joined())
print(Member.date_joined(wilbur))

# Using class variables
import datetime as dt
# Define a class named Member for making member objects
class Member:
    """" Create a member object """
    free_days = 90
    
    def __init__(self, username, fullname):
        self.date_joined = dt.date.today()
        # Set an expiration date
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)

# The class ends at the first instance un-indented line

# Create an instance of the Member class named new_guy
wilbur = Member('wblomgren', 'Wilbur Blomgren')

print(wilbur.date_joined)
print(wilbur.free_expires)

# Using class methods
import datetime as dt
# Define a new class name Member
class Member:
    # Default number of free days
    free_days = 365
    """ Create a new member """
    def __intit__(self, username, fullname):
        self.date_joined = dt.date.today()
        # Set an expiration date
        self.free_expires = dt.date.today() + dt.timedelta(days = Member.free_days)
    # Class methods follow @classmethod decorator and refer to cls rather than to self
    @classmethod
    def setfreedays(cls,days):
        cls.free_days = days
    # Using static methods
    @staticmethod
    def currenttime():
        now = dt.datetime.now()
        return f"{now:%I:%M:%p}"
# class definition ends at last indented line
# Try out the new static method (no object required)
print(Member.currenttime())

# Create the base (main) class
import datetime as dt
# Class is used for all kinds of people
import datetime as dt

# Base class is used for all kinds of Members
class Member:
    """ The Member class attributes and methods are for everyone """
    # By default, a new account expires in one year (365 days)
    expiry_days = 365

    # Initialize a member object
    def __init__(self, firstname, lastname):
        # Attributes (instance variables) for everybody
        self.firstname = firstname
        self.lastname = lastname
        # Calculate expiry data from today's date
        self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)
# Outside the class now
Joe = Member('Joe', 'Anybody')
print(Joe.firstname)
print(Joe.lastname)
print(Joe.expiry_date)

# Defining a subclass
class Admin(Member):
    pass

# Subclass for Users
class User(Member):
    pass

Ann = Admin('Annie', 'Angst')
print(Ann.firstname)
print(Ann.lastname)
print(Ann.expiry_date)
print()
Uli = User('Uli', 'Ungula')
print(Uli.firstname)
print(Uli.lastname)
print(Uli.expiry_date)
print()

# Overriding a default value from a subclass
# subclass for Admins
class Admin(Member):
    # Admin accounts dont expire for 100 years
    expiry_days = 365.2422 * 100
    # Subclass parameters
    def __init__(self, firstname, lastname, secret_code):
        # Pass Member parameters on up to Member class
        super().__init__(firstname, lastname)
        # Assign the remaining parameter to this object
        self.secret_code = secret_code

# Subclass for Users
class User(Member):
    pass

Ann = Admin('Annie', 'Angst', 'PRESTO')
print(Ann.firstname, Ann.lastname, Ann.expiry_date, Ann.secret_code)
print()
Uli = User('Uli', 'Ungula')
print(Uli.firstname, Uli.lastname, Uli.expiry_date)

import datetime as dt

# Base class is used for all kinds of Members
class Member:
    """ The Member class propertues and methods are for everyone """
    # By default, a new account expires in one year (365 days)
    expiry_days = 365

    # Initialize a member object
    def __init__(self, firstname, lastname):
        # Attribues (instance variables) for everybody
        self.firstname = firstname
        self.lastname = lastname
        # Calculate expiry date from today's date
        self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)
        # Default secret code is nothing
        self.secret_code = ''
    
    # Method in the base class
    def showexpiry(self):
        return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"
    
# Subclass for Admins
class Admin(Member):
    # Admin accounts don't expire for 100 years
    expiry_days = 365.2422 * 100

    # Subclass parameters
    def __init__(self, firstname, lastname, secret_code):
        # Pass Member parameters on uo to Member class
        super().__init__(firstname, lastname)
        # Assign the remaining parameter to this object
        self.secret_code = secret_code

# Subclass for Users
class User(Member):
    pass

Ann = Admin('Annie', 'Angst', 'PRESTO')
print(Ann.firstname, Ann.lastname, Ann.expiry_date, Ann.secret_code)
print() # Add a blank line to output

Uli = User('Uli', 'Ungula')
print(Uli.firstname, Uli.lastname, Uli.expiry_date, Uli.secret_code)

# Calling a base class method
import datetime as dt
class Member:
    """ True Member class attributes and methods are for everyone """
    # By default, a new account expires in one year (365 days)
    expiry_days = 365

    # Initialize a member object
    def __init__(self, firstname, lastname):
        # Attributes (instance variables) for everybody
        self.firstname = firstname
        self.lastname = lastname
        # Calculate expiry date from today's date
        self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)
        # Default secret code is nothing
        self.secret_code = ''

    # Method in the base class
    def showexpiry(self):
        return f"{self.firstname} {self.lastname} expires on {self.expiry_date}"
    
Ann = Admin('Annie', 'Angst', 'PRESTO')
print(Ann.showexpiry())
Uli = User('Uli', 'Ungula')
print(Uli.showexpiry())

# Usiing the same name twice
class Member:
    """ The Member class attributes and methods """
    # Intialize a member object
    def __init__(self, firstname, lastname):
        # Attributes (instance variables) for everybody
        self.firstname = firstname
        self.lastname = lastname

    # Method in the base class
    def get_status(self):
        return f"{self.firstname} is a Member"

# Subclass for Administrations
class Admin(Member):
    def get_status(self):
        return f"{self.firstname} is an Admin"

# Subclass for regular Users
class User(Member):
    def get_status(self):
        return f'{self.firstname} is a regular User'
    
# Create an admin
Ann = Admin('Annie', 'Angst')
print(Ann.get_status())

# Create a user
Uli = User('Uli', 'Ungula')
print(Uli.get_status())

# Create a member
Manny = Member('Mindy', 'Membo')
print(Manny.get_status())

# Sidestepping Errors
# Understandimg Exceptions - refers to error that isn't due to a programming error
# open file that is in the same folder
thefile = open("E:/Test/test.csv")
# Show the file name
print(thefile.name)

# Handling errors gracefully
try:
    # Open file and shows its name
    thefile = open("E:/Test/test.csv")
    print(thefile.name)
except Exception:
    print("Sorry, I don't see a file named 'people.csv' here")

# Being Specific about Exceptions
try:
    # Open file and show its name
    thefile = open("E:/Test/test.csv")
    print(thefile.name)
    print(thefile.wookems())
except Exception:
    print("Sorry, I don't see a file named people.csv here")

try:
    # Open file and show its name
    thefile = open("E:/Test/test.csv")
    print(thefile.name)
    print(thefile.wookems())
except FileNotFoundError:
    print("Sorry, I don't see a file named test.csv here")

# Keeping Your App from Crashing
try:
    # Open file and show its name
    thefile = open("E:/Test/test.csv")
    # Print a couple blank lines then the first line from the file
    print('\n\n', thefile.readline())
    #Close the file
    thefile.closed()

except FileNotFoundError:
    print("Sorry, I don't see a file name test.csv here")
except Exception:
    print("Sorry, something else went wrong")

try:
    # Open file and show its name
    thefile = open("E:/Test/test.csv")
    # Print a couple blank lines then the first line from the file
    print('\n\n', thefile.readline())
    #Close the file
    thefile.wigwam()

except FileNotFoundError:
    print("Sorry, I don't see a file name test.csv here")
except Exception as e:
    print(e)

# Adding an else to the mix
try:
    # Open file and show its name
    thefile = open("E:/Test/test.csv")
# Watch for common error and stop program if it happens
except FileNotFoundError:
    print("Sorry, I don't see a file name test.csv here")
except Exception as err:
    print(err)
# Otherwise, if nothing bad has happened by now, just keep going
else:
    # File must be open by now if we got here
    print('\n') # print a blank line
    # Print each line from the file
    for one_line in thefile:
        print(one_line)
    thefile.close()
    print("Success!")

# Using try..except..else...finally
print('Do this first')
try:
    # Open file and show its name
    open("E:/Test/test.csv")
# Watch for common error and stop program if it happens
except FileNotFoundError:
    print("Sorry, I don't see a file name test.csv here")
except Exception as err:
    print(err)
# Otherwise, if nothing bad has happened by now, just keep going
else:
    # File must be open by now if we got here
    print("Show this if no exception")
# Print this line no matter what happened above
finally:
    print("This is in the finally block")
print("This is outside the try...except...else..finally")

# Raising your own errors
try:
    # Open file and show its name
    thefile = open("E:/Test/test.csv")
    # Count the number of lines in file
    line_count = len(thefile.readlines())
    # If there is fewer than 2 lines, raise exception
    if line_count < 2:
        raise Exception
# Handles missing file error
except FileNotFoundError:
    print('\nThere is no test.csv file here')
# Handles all other exceptions
except Exception as e:
    # Show the error
    print('\n\nFailed: the error was' + str(e))
    # Close the file
    thefile.close()

# Excepttions hanlded in class
# Base class for defining your own user-defined exception
class Error(Exception):
    """ Base class for other exception """
    pass

# Now define your exception as a subclass of Error
class EmptyFileError(Error):
    pass

try:
    # Open the file (no error check for this example)
    thefile = open("E:/Test/test.csv")
    # Count the number of lines in file
    line_count = len(thefile.readlines())
    # If there is fewer than 2 lines, raise exception
    if line_count < 2:
        raise EmptyFileError

# Handles missing file error
except FileNotFoundError:
        print('\nThere is not test.csv file here')

# Handles my custom error for too few rows
except EmptyFileError:
        print("\nYour test.csv file doesn't have enough stuff")

# Handles all other exceptions
except Exception as e:
        # Show the error
        print('\nFailed error was ' + str(e))
        # Close the file
        thefile.close()
else:
    # This code runs only if no exception above
    print()

    # File must be open by now if we got here, show content
    for one_line in thefile:
        print(one_line)
    thefile.close()
    print("Success!")
