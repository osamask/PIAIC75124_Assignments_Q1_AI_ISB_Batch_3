import re
import operator as op
from math import *

'''
Question 1:
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a
farm. How many rabbits and how many chickens do we have?
'''

def rabbits():
  heads = 35
  legs = 94
  for rabbits in range(heads + 1):
    chickens = heads - rabbits
    if 2 * chickens + 4 * rabbits == legs:
      print("There are {} chickens and {} rabbits".format(chickens, rabbits))
    
'''
Question 2:
Please write a program which accepts a string from console and print
the characters that have even indexes.
'''    

def even_index():
  txt = input("Enter string: ")
  print(txt[::2])  

'''
Question 3:
Please write a program which accepts a string from console and print
it in reverse order.
'''    
  
def reverse():
  txt = input("Enter string: ")
  print(txt[::-1])

'''
Question 4:
Please write a program which count and print the numbers of each
character in a string input by console.
'''

def count():
  txt = input("Enter string: ")
  dict = {}
  for char in txt:
    if dict.get(char):
      dict[char] += 1
    else:
      dict[char] = 1
  for char in dict.keys():
    print("{}, {}".format(char, dict[char]))

'''
Question 5:
Define a class named Shape and its subclass Square. The Square class
has an init function which takes a length as argument. Both classes
have a area function which can print the area of the shape where
Shape's area is 0 by default.
'''

def inheritance():
  class Shape():
    def __init__(self):
      pass
    def area(self):
      return 0  
  class Square(Shape):
    def __init__(self, l):
      self.length = l
    def area(self):
      return self.length**2 
  sqr = Square(2)
  print("Area of square = {}".format(sqr.area()))

'''
Question 6:
Write a function to compute 5/0 and use try/except to catch the
exceptions.
'''

def excep():
  try:
    print(5/0)
  except ZeroDivisionError:
    print("Cannot compute division by zero")      

'''
Question 7:
Assuming that we have some email addresses in the
"username@companyname.com" format, please write program to print the
user name of a given email address. Both user names and company
names are composed of letters only.
'''  

def email():
  txt = input("Enter email address (letters only): ")
  for i in range(len(txt)):
    if txt[i] == '@':
      index = i
      break
  print(txt[:index])      

'''
Question 8:
Write a program which accepts a sequence of words separated by
whitespace as input to print the words composed of digits only.
'''

def digits():
  txt = input("Enter a string (numbers and letters): ")
  nums = re.findall('\d', txt)
  print(nums)  
  
'''  
Question 9:
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n
input by console (n>0).
'''

def sequence():
  num = int(input("Enter a number: "))
  x = 0
  for i in range(num + 1):
    #y = float(i)
    x = x + i/(i+1)
  print("%.2f"%x)    
  
'''
Question 10:
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
'''  

def func():
  def f(n):
    if n == 0:
      return 0
    else:
      result = f(n-1) + 100
      return result
  num = int(input("Enter a number: "))
  print(f(num))  

'''
Question 11:
A website requires the users to input username and password to
register. Write a program to check the validity of password input by
users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords
and will check them according to the above criteria. Passwords that
match the criteria are to be printed, each separated by a comma.
'''  

def pwd():
  pwds = [x for x in input("Enter passwords seperated by comma: ").split(',')]
  valid = []
  for p in pwds:
    if 6 < len(p) <12 and re.search("[a-z]", p) and re.search("[0-9]", p) and re.search("[A-Z]", p) and re.search("[$#@]", p):
      valid.append(p)
  print(",".join(valid))

'''
Question 12:
You are required to write a program to sort the (name, age, height)
tuples by ascending order where name is string, age and height are
numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
'''

def sort_tuple():
  num = int(input("Enter number of persons: "))
  counter = 0
  list = []
  while(counter < num):
    str = input("Enter data (format: name,age,score): ")
    list.append(tuple(str.split(',')))
    counter += 1
  print(sorted(list, key = op.itemgetter(0,1,2)))

'''
Question 13:
Define a class with a generator which can iterate the numbers, which
are divisible by 7, between a given range 0 and n.
'''

def gen():
  class seven:
    def __init__(self):
      self.a = 1
    def __iter__(self):
      while True:
        if self.a%7 == 0:
          yield self.a
        self.a += 1
  obj = iter(seven())
  r = int(input("Enter range: "))
  for i in range(r):
    print(next(obj))

'''
Question 14:
A robot moves in a plane starting from the original point (0,0). The
robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡
The numbers after the direction are steps. Please write a program to
compute the distance from current position after a sequence of
movement and original point. If the distance is a float, then just
print the nearest integer.
'''

def robot():
  moves = int(input("Enter number of moves: "))
  c = 0
  list = []
  point = [0,0]
  while (moves > c):
    list.append(tuple(input("Enter move(format: UP or DOWN or Left or Right <space> distance): ").split(' ')))
    c += 1
  for i in list:
    if i[0] == 'UP':
      point[1] += int(i[1])
    if i[0] == 'DOWN':
      point[1] -= int(i[1])
    if i[0] == 'LEFT':
      point[0] -= int(i[1])
    if i[0] == 'RIGHT':
      point[0] += int(i[1])
  print("Distance = {}".format(round(sqrt(point[0]**2 + point[1]**2))))

'''
Question 15:
Write a program to compute the frequency of the words from the
input. The output should output after sorting the key
alphanumerically.
'''

def word_freq():
  words = input("Enter sentence: ")
  word_list = words.split()
  dict = {}
  for word in word_list:
    count = 0
    for occurrence in word_list:
      if occurrence == word:
        count += 1
    dict[word] = count
  list = []
  for key in dict.keys():
    list.append(key)
  list = sorted(list)
  for word in list:
    for key in dict.keys():
      if key == word:
        print(key + ":" + str(dict[key]))
  
def main():
  print("Question 1:\nWrite a program to solve a classic ancient Chinese puzzle:\n"
  "We count 35 heads and 94 legs among the chickens and rabbits in a farm.\nHow many rabbits and how many chickens do we have?\n")
  rabbits()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 2:\nPlease write a program which accepts a string from console and print "
  "the characters that have even indexes.\n")
  even_index()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 3:\nPlease write a program which accepts a string from console and print it in reverse order.\n")
  reverse()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 4:\nPlease write a program which count and print the numbers of each character in a string input by console.\n")
  count()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 5:\nDefine a class named Shape and its subclass Square. The Square class has an init function\nwhich takes a length as argument. Both classes have a area function\nwhich can print the area of the shape where Shape's area is 0 by default.\n")
  inheritance()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 6:\nWrite a function to compute 5/0 and use try/except to catch the exceptions.\n")
  excep()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 7:\nAssuming that we have some email addresses in the \"username@companyname.com\" format, please write program\nto print the user name of a given email address. Both user names and company names are composed of letters only.\n")
  email()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 8:\nWrite a program which accepts a sequence of words separated by whitespace as input\nto print the words composed of digits only.")
  digits()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 9:\nWrite a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).\n")
  sequence()
  input("\nPress Enter to continue . . . \n")
  print("\nQuestion 10:\nWrite a program to compute:\nf(n)=f(n-1)+100 when n>0 and f(0)=1\n")
  func()
  input("\nPress Enter to continue . . . \n")
  print("Question 11:\nA website requires the users to input username and password to\nregister."
        "Write a program to check the validity of password input by users.\nFollowing are the criteria"
        " for checking the password:\n1. At least 1 letter between [a-z]\n2. At least 1 number between [0-9]"
        "\n1. At least 1 letter between [A-Z]\n3. At least 1 character from [$#@]\n4. Minimum length of"
        " transaction password: 6\n5. Maximum length of transaction password: 12\nYour program should accept"
        " a sequence of comma separated passwords and will check them according to the above criteria.\n"
        "Passwords that match the criteria are to be printed, each separated by a comma.\n")
  pwd()
  input("\nPress Enter to continue . . . \n")
  print("Question 12:\n"
        "You are required to write a program to sort the (name, age, height)\n"
        "tuples by ascending order where name is string, age and height are\n"
        "numbers. The tuples are input by console. The sort criteria is:\n"
        "1: Sort based on name;\n"
        "2: Then sort based on age;\n"
        "3: Then sort by score.\n"
        "The priority is that name > age > score.\n")
  sort_tuple()
  input("\nPress Enter to continue . . . \n")
  print("Question 13:\n"
        "Define a class with a generator which can iterate the numbers, which\n"
        "are divisible by 7, between a given range 0 and n.\n")
  gen()
  input("\nPress Enter to continue . . . \n")
  print("Question 14:\n"
        "A robot moves in a plane starting from the original point (0,0). The\n"
        "robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.\n"
        "The trace of robot movement is shown as the following:\n"
        "UP 5\n"
        "DOWN 3\n"
        "LEFT 3\n"
        "RIGHT 2\n"
        "¡\n"
        "The numbers after the direction are steps. Please write a program to\n"
        "compute the distance from current position after a sequence of\n"
        "movement and original point. If the distance is a float, then just\n"
        "print the nearest integer.\n")
  robot()
  input("\nPress Enter to continue . . . \n")
  print("Question 15:\n"
        "Write a program to compute the frequency of the words from the\n"
        "input. The output should output after sorting the key\n"
        "alphanumerically.\n")
  word_freq()        
  input("\nPress Enter to continue . . . \n")

if __name__ == '__main__':
  main()