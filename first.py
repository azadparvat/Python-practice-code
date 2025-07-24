# import pyttsx3
# engine = pyttsx3.init()
# engine.say(" hey ajju welcome to the coding world .  I wish you have a great  coding jouney .")
# engine.runAndWait()




# import os

# # Set the path of the directory you want to list
# directory_path = "D:\codes" # '.' means current directory

# # Check if the path exists and is a directory
# if os.path.exists(directory_path) and os.path.isdir(directory_path):
#     print(f"Contents of '{directory_path}':")
#     for item in os.listdir(directory_path):
#         print(item)
# else:
#     print("The specified path is not a valid directory.")

# use  of int(input function
# a = int int(input("Enter the number "))
# b =  int int(input("Enter the number 2 "))
# print (a+b)

# import pyttsx3;

# engine = pyttsx3.init()
# engine.say int(input("enter the line "))# use of iput funtion in  module

'''

                                    Python program to  find sqare of a number 

 a = int(input("enter the number "))
 print("The sqare of this number is ", a**a) # ** mean power like if you want to find 2of power 3 then you write 2**3

 a = int(input("Enter the name")
 b = int(input("Enter the date ")
 print(" Dear ", a)
 print("You are selected!")
 print("on date ", b)
 '''


'''  
                             program to count and replace  double space 
 Text  = int(input("Enter the text")
 print(Text.count("  "))
 print(Text.replace("  "," "))

'''

'''
 text = " dear harry you are really nice\n  you are  gem person\t  you are my \' hero\' "
 print(text)
 '''

'''
list = int(input("Enter the fruits  name")
print(list)
'''

'''

                     # write a program to  accept the marks of 6 students and  also arramge them in increasing order
Marks = []
m1 = int(input("Enter the marks1: "))
Marks.append(m1)
m2 = int(input("Enter the marks2: "))
Marks.append(m2)
m3 = int(input("Enter the marks3: "))
Marks.append(m3)
m4 = int(input("Enter the marks4: "))
Marks.append(m4)
m5 = int(input("Enter the marks5: "))
Marks.append(m5)
m6 = int(input("Enter the marks6: "))
Marks.append(m6)
Marks.sort()
print(Marks)


'''

'''

                               #Write a program to  show that a tuple is not change 
a = (23, "harry", 45.3, "ajju")
a[1] = "azad"
print(a)

'''



'''
                              #write a program to sum 4 number in a list
list = [24,56,67,53]
print(sum(list))
'''

'''
                             #Write a program to find the occourence of 0 in a list
list = [0,34,0,0,0,45,0,75,0]
print(list.count(0))



'''

#Practice question 1:  write a set of hindi world as keysa and their  english  version as  the  values
words = { 
      "Bili": "Cat",
      "Kutta": "dog",
      "kursi":"Chair"
 }
word = input("Enter the word that you want to search: ")
print(words[word])


#Task 1 : Input  eight no. from the user and display them uniqley
sets= set()
sets.add(int(input("Enter  the no.: ")))
sets.add(input("Enter  the no.: "))
sets.add(input("Enter  the no."))
sets.add(input("Enter  the no."))
sets.add(input("Enter  the no."))
sets.add(input("Enter  the no."))
sets.add(input("Enter  the no."))
sets.add(input("Enter  the no."))
print(sets)
               


#Task 2 :  create a empty dictinary and take input from the user and update the dictionary  with name and language 
dic = {}

name = input("Enter the name: ")
Language  = input("Enter the laguage: ")
dic.update({name: Language})
name = input("Enter the name: ")
Language  = input("Enter the laguage: ")
dic.update({name: Language})
name = input("Enter the name: ")
Language  = input("Enter the laguage: ")
dic.update({name: Language})
name = input("Enter the name: ")
Language  = input("Enter the laguage: ")
dic.update({name: Language})
print(dic)


# task 2: check the student is pass or  fail based on the percentage of marks obtained in three subjects      
hindi_mark_obtained = int(input("Enter the marks obtained in hindi: "))
hindi_total_marks  = int(input("Enter the total marks hindi: "))
math_mark_obtained = int(input("Enter the marks obtained in maths: "))
math_total_marks  = int(input("Enter the total marks obtained in maths: "))
english_mark_obtained = int(input("Enter the marks obtained in english: "))
english_total_marks  = int(input("Enter the total marks  english:"))

# Calculate total marks obtained and total possible marks
marks_obtained = hindi_mark_obtained + math_mark_obtained + english_mark_obtained
total_marks = hindi_total_marks + math_total_marks + english_total_marks

# Calculate percentage
p = (marks_obtained / total_marks) * 100

if p >= 33:
    print("Congratulations! You passed all the exams with percentage:", round(p, 2))
else:
    print("Sorry, you failed in the exam with percentage:", round(p, 2))


    
#task4: take  a input from  the user and check if  the username is of 10 charchter or not 
username = input("Enter the username: ")
l = len(username)
if l<10 :
    print("Please enter complete   valid username of 10 charchters")
else:
    print("Valid username")



#task5:  write a program to check the marks of prity and display the grade based on the marks obtained
marks = int(input("Enter the marks of the Prity: "))
if (marks >= 90 and marks <= 100):
    print("COngratulation ! you have score excellent marks")
elif (marks >=80 and marks < 90):
    print("Congratulation ! you have score A grade marks")   
elif (marks >=70 and marks < 80):
    print("Congratulation ! you have scored B grade marks")    
elif ( marks >=60 and marks < 70):
    print("Good work ! you have scored C grade marks:")
elif (marks >= 50 and marks < 60):
    print("You have scored D grade marks , you need  to work hards")
else:
    print("Sorry! you don't pass the exam , you need to try again next time")    


    # task 6:  write a program to accept to note and search for a name in it
note = input("Enter the note: ")
name =  input("Enter  the name you want to search: ")
if (name in note):
    print("This  notes is about you")
else:
    print(" Sorry! This notes is not about you")    
  

                                          #loops 
#task : Print number from 100 to 1 by using for loop
for i in range(100,0,-1):
    print(i)

 # task 1:  write down the number from 0to 50 using while loop
i = 0 
while i <= 50 :
    print(i)
    i+=1                                         


#task 2: print the  content of the list using while loop
list  = [ 1, "ajju","false", 2,3,4,5,"vikas"]
i = 0
while i < len(list):
    print(list[i])
    i +=1

                                      # LOOOPs
    # task 1 : write a program to print the multiplication table of a number entered by the user
n =  int(input("Enter the number : "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
    i += 1

    #Task : Write a program to  great all the name in a list by using for loop
list = [ "Azad", "Vikas", "Prity","Ridhi"]
for i in (list):
    print(f" Hello {i} , Welcome to the python world")
    i += i

 #Task: Write a program ti greet all the name in list "l" and which name start with "S"
l = []
l.append(input("Enter the name: "))
l.append(input("Enter the name: "))
l.append(input("Enter the name: "))
l.append(input("Enter the name: "))
for name in l:
      if name.startswith("S"):
         print(f" HEllo , {name}")

#task: write the multiplication table of any number using while loop
n = int(input("Enter the number: "))
i = 0
while (i < 11):
    print(f" {n}X{i} = {n*i}")
    i+= 1

#Write a program to check a number is prime number or not
n = int(input("Enter the number : "))
for i in range(2, n):
    if n % i == 0:
        print("This is not a prime number")
    break;
else:
    print("This is a prime number")

       
#Task: Write a program to  finnd the sum of first n natural numbers
n = int(input("Enter the quanity of natural number: "))
i = 0
sum = 0
while (i<= n):
    sum += i
    i += 1
print(sum)
   

 #Task : Write a program to find the factorial of a number
 # n = int(input("Enter the number: "))
product = 1
for i in range (1 ,n+1):
    product *= i
print(f"The factorial of {n} is {product}")  