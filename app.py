#jUST BY REMOVING HASHTAGS FROM ANY CODE EXAMPLE YOU CAN RUN IT
#print ("hello")
#Multi line triple commas string
#print('''hi
 #     thr''')
#f string
#colour = input('what is your favourite colour?')
#p= print(f'favourite colour of {name} is {colour}')
#age = 20
#age = 30
#first_name = "Mosh"
#is_online = False
#print (age)
#name = input("what is your name?")
#print ("hello"+ name)
#name = input ("what is your name")
#print ("hello" + name )
#Birth_year = input ("Enter your birth year:")
#print (2024 - int(Birth_year))
#f=input ("first:")
#s = input ("second:")
#print (float(f) + float (s))
# course = 'python for begginers'
#print(course.find ('r'))
#print(course.replace('for' , '4'))
#print('for' in course) ///print will be 'true' in written
#print(course.upper())
#print(course.lower())
#print((10+1)*2) ans 22
#x=2
#x+=2
#print(x) ans 4
# +=
# -=
# *= and so on, arethmatic operators
#x=10
#print(x>=7) boolean true
# >
#<
#<=
#== equal
#!= not equal    it was Comparison operators
#x=20
##########Round Function####
#a=3/2
#print(round(a)) #it will ignore the decimels
#######Absolute Function#######
#t=1-22
#print(abs(t)) #result will be positive not negative
#now logical operators
#print(x>2 and x<21)
#print(x>21 or x<=21) #or will be boolean true if one of them is right
#print(not x>21) #not will give true if its not right
#temprature = 8
#if temprature > 25:
 #   print("its hot today")
#elif temprature > 19 :
 #   print("its nice day")
#elif temprature > 10 :
 #   print("its cold")
#else:
 #   print("its very cold today") #itended space for using in if or elif and else:
#print(" done ")   ##itended space difference
#exercise
#t = 5
#if t>10 :print('its hot')
#elif t>7 : print('ni')
#else:print('not')
from statistics import correlation

#ishot= False
#iscold = False
#isis = True
#if ishot:
 #   print('hot')
#elif iscold:
 #   print('cold')
#elif isis:
 #   print('elif2')
 #-------
#w = float(input("weight:"))
#u = input("type k for kgs and l for lbs:")
#if u=="k":
 #   convert =w / 0.45
  #  print('your weight in lbs:'+str (convert)  )
#else:
 #   con = w*0.45
  #  print('your weight in kgs:' + str(convert))
##########While loop######
#i =0
#while i<=10:
  #  print(i*"*")  #it has identation
  #  i=i+1
#####Lists
#names = ["bob","steve","mary"] #it has no identation
#print(names[0])  #will print 0 index item/object "bob"
#print(names[0:2]) #will print 0 index item and 1 index object and will exculde 2nd place item in 0,1,2
#names[0]="bib" #will change 0 item "bob" to "bib"
#print(names)   #will simply print all list
####List Methods
#nums= [1,2,3,4,5]
#nums.insert(1,-2)  #add index,object and old object will go next index to it.
#print(nums)
#nums.append(9) #add one item more in last index of list
#print(nums)
#nums.remove(9)
#print(nums)
#print( 9 in nums)   #it will give boolean answer by searching that object in list
#print(len(nums))  #this function counts all objects of list, len for length
#nums.clear() #it will delete all objects of list, empty list will be printed []
#print(nums)
######for loops, are used for simpler approach
#num=[1,2,3,4]
#for items in num: #for is loop, items is entries or objects of lis, in is function refreing to list
 #   print(items)
#i=0          #it declares i as 0
#while i< len(num): #it will check if iteration is less than length,
 #   print(num[i]) # ith index item in list will be printed
 #   i=i+1
##########  range function
#numbers = range(5)   #works 0-4 means like index or place
#print(numbers)
#numbers = range(5,10)
#for number in numbers:    #"""number""" in variable number because range is always number etc
   # print(number)
#numbers = range(5,10,2) #skips 2 numbers , third is for skipping
#for number in numbers:
 #  print(number)
#for number in range(5):     #directly declare range in a for loop
 #   print(number)
 #### Tuples
#numbers = (1,2,3)    #tuple list has () not []
#numbers.remove(2) ### it will not work beacuse tuples dont change
#numbers.insert(0,1) ### it will not work beacuse tuples dont change
#print(len(numbers))  ##works
#print(numbers)
#####while game of guess
#secretnumber=9
#limitsecret=3
#i=0
#while limitsecret>i:
 #      guess=int(input("Guess:"))
  #     i+=1
   #    if guess==secretnumber:            #very indentant sensitive code
    #          print("You won")            #dont forget colons
   #           break                       #maxlimit must be greater > in while
#else:                                     #add break when game is won
 #             print("You los")
####Exercise#> help get list start stop quit if type any thing else we get 'i dont understand that'
#and if already started or stoped, use boolean flag to check.
# #cmd=""
#started= False
#while cmd != "quit":
 #      cmd=input('> ')
  #     if cmd=="start":
   #           if started:
    #                 print('already started')
     #         else:
      #               started = True
       #              print('car started')
       #elif cmd=='stop':
        #      if not started:
         #            print('car is already stopped')
          #    else:
           #          started = False
            #         print('car stoped')
       #elif cmd=='help':
        #      print('''start-to car start
#stop-car stop
#quit- to quit''')
 #      else:
  #            print('i dont understand that shit')
######---------------------------------------------
##Sum of a list
#prices=[1,2,3]
#total=0
#for price in prices:
#    total+= price
#print(total)
#####nested loop  ########
# for n in range(5):
#    for m in range(4):
#        print(f'({n},{m})')
# n=[5,2,5,2,2]
# for xcount in n:
#    output=''
#    for count in range(xcount):
#        output +='x'
#    print(output)
######n= [2,2,2,6,6]#########
#for xcount in n:
#    output=''
#    for count in range(xcount):
#        output+="x"
#    print(output)
#####Coordinates#############
#coordinates = (1,2,3)
#x,y,z = coordinates    #assign x as 1 ,y as 2 and z as 3
#print(x)
########Dictionary-------code###
#customer= {
#        "name": "Bob",
#        "age": 30,
#        "birthdate": '11-12-12',
#        "verified": True
#}
#print(customer.get("verified",'NA')) #get method for dictionary along with printing
#customer["name"]='mic' #updating a dictionary item
#print(customer['name'])
####getting number string input and giving alphabetic string program
#phone=input('phone: ')
#num_map={
#    '1':'one',
#    '2':'two',
#    '3':'three',
#    '4':'four'
#}
#o=''
#for ch in phone: #include input in for loop not dictionary name
#    o+=num.get(ch,'!')+'   '  #should be displayed if input character doesnt match to dictionary character
#print(o)
######Unpacking
#c=[1,2,3]
#x,y,z=c
#print(x)
#print(y)
############Emoji--------Converter###########
#words=input(">")
#msg=words.split(" ")
#emojis={
#    ':)': "😃",
#    ':(':"🙁"
# }
# o=""
# for word in words:
#     o+=emojis.get(word,word)
# print(o)
#-----------Defining----Function
#def greet (name,second_name):   #parametering
#    print(f"hi {name} {second_name} how r u?")
##   print('how r u doing?')
#print('whts up')
#greet("bob",'mosh')  #argumenting   #key word argumenting(name=bob)
#print('end')
#---------------------
#def square(x):
 #   return x*x    #to return result outside function we use return.
#y=square(3)
#print(y)
#----------------------
#def square (number):
#     return number*number
# print (square(9))
#------------------------
#----------REUSABLE FUNCTION syntax!!!!!
# def convert (input123):
#     words=input123.split(" ")
#     e={
#         ':)':"1",
#         ":(":"2"
#     }
#     o=""
#     for word in words:
#         o+= e.get(word,word)+" "
#     return o
# input123 = input(">")
# print (convert(input123))
#____________________-____
##Exceptions Syntax
# try:              #part of except method
#     a=(int(input('age:')))
#     print(a)
# except ValueError:       #now it will not give errors and will print
#     print('n/a')
#------------------------------------
#-----------Class
# class Point():   #class name starts with capital letter.
#     def move(self):  #move function of class Point
#         print('move')
#     def draw(self):  #draw function of class Point
#         print('draw')
# p=Point()
# p.draw()
# p.move()
# p.x = 10              #giving attributes to class variable along x-axis
# p.y = 12   #giving attributes to class variable along y-axis
# print(p.x)
# print(p.y)
#  print(p.x,p.y)
# p2=Point()     #declaring another variable as previous class
# p2.x=1    #giving attributes to class variable
# p2.y=2     #giving attributes to class variable
# print(p2.x)
# print(p2.y)
#-------------------------
#Giving contructors to class
# class P():
#     def __init__(self, x,y):   #defining x and y giving init self constructors
#         self.x=x       #defining x and y giving init self constructors
#         self.y=y        #defining x and y giving init self constructors
#     def move(self):
#         print('self')
#     def draw(self):
#         print('draw')
# p=P(10,20)        #x and y values
# p.x=11          # X updated  again
# print(p.x)
# print(p.y)
#print(p.x,p.y)    #printing both
#-------------Constructors------------
# class Person():
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print('hi im am {self.name}')
#         john=Person('john')
# print(john.name)
# john=Person
# print(john.talk)
# #-------------------
# class Person():
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print(f'hi i am {self.name}')
# john=Person("johnny")
# print(john.name)
# john.talk()
#-------------------------
# class Person ():
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print(f"hi i m {self.name}")
# john=Person('bob')   #declaring john as a person variable with names value
# john.name='mike'  #changing value of name to mike from bob
# john.talk()       #talk  with its print value
#-------------Inheritance---------------
# class Mammal:
#     def walk(self):  #mammal class
#         print('walk')
# class Cat(Mammal):    #inheriting mammal for cat class, cat could be left--
#     def annoy(self):   #--empty it would still have mammal's method in it.
#         print('anoying')
# class Dog(Mammal):
#     def bark(self):
#         print('bark')
# cat=Cat()
# cat.walk()  #after pressing dot (.) i had walk and annoy 2 methods from mammal and cat both
# dog=Dog()
# dog.bark()
#----------------------Importing a module
#from converters import kgsTolbs
#print(kgsTolbs(10))
#--------------------importing max value function
# from converters import max_value
# nums=[2,3,222,333,444,555,1]
# maximum=max_value(nums)
# print(maximum)
#------------Importing a module
# from ecommerce.shipping import calculate_shipping
# calculate_shipping()
#-----Builtin random method keeping in range 4
# import random
# for i in range(4):
#     print(random.random())
#---------givig it limits in randint method
# import random
# for i in range(4):
#     print(random.randint(11,20))
#----------------using random.choice method for random names
# import random
# names=['bob','mary','mosh','naymer','messi']
# print (random.choice(names))
#-------------Dice game with 2 randint methods
# import random
# def roll():
#     first=random.randint(1,6)
#     second=random.randint(1,6)
#     z=(first,second)
#     return z
# print(roll())
#------Creating email directory with Path from pathlib
# from pathlib import Path
# p=Path("emails")
# print(p.mkdir())
#---------Removing email directory with Path from pathlib method
# from pathlib import Path
# p=Path("emails")
# print(p.rmdir())
#--------print file names in current directory
# from pathlib import Path
# p=Path()
# for file in p.glob('*.*'): ##/ we need to iterate glob method for some files reasons
#     print(file)
#----Transactions sheet updating/correction
# def pricing(filenamehere):
#     import openpyxl as xl #loading an excel file by module
#     from openpyxl.chart import Reference,BarChart
#     from openpyxl.chart import bar_chart
#     wb=xl.load_workbook(filenamehere)  #loading file
#     sheet=wb['Sheet1']   #loading sheet
#     cell=sheet['a1']   #selecting cell
#     cell= sheet.cell(1,1)   #cell selection another way
#     # print(cell.value) #printing value of that cell
#     # print(sheet.max_row) #printing max number of rows
#     for row in range(2,sheet.max_row+1):
#         cell=sheet.cell(row,3)
#         correction=cell.value*0.9
#         new_prices=sheet.cell(row,4)
#         new_prices.value=correction
#     cell=sheet.cell(1,4)
#     cell.value='new prices'
#     values=Reference(sheet,min_row=2,max_row=4,min_col=4,max_col=4)
#     chart= BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart,'e2')
# wb.save(filenamehere)
#-------------------------
