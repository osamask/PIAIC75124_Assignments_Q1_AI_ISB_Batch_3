import math
from datetime import datetime, date, time


# 1. Calculate area of a circle

def circle_area():
  r = float(input("Input Radius: "))
  area = math.pi * r * r
  print("Area of Circle with radius {} is {}".format(r, area))
  
  
# 2. Check Number either positive, negative or zero

def sign_check():
  num = int(input("Enter Number: "))
  if num == 0:
    print("Zero Entered")
  elif num > 0:
    print("Positive Number Entered")
  else:
    print("Negative Number Entered")
  
  
# 3. Divisibility Check of two numbers

def div():
  nume = int(input("Enter Numerator: "))
  denom = int(input("Enter Denominator: "))
  if nume % denom:
    print("Number {} is not Completely divisible by {}".format(nume, denom))
  else:
    print("Number {} is Completely divisible by {}".format(nume, denom))


# 4. Days Calculator

def days():
  date_1 = input("Enter a date in (dd/mm/yyyy) format: ")  
  date_2 = input("Enter a date in (dd/mm/yyyy) format: ")
  dt1 = datetime.strptime(date_1, "%d/%m/%Y")
  dt2 = datetime.strptime(date_2, "%d/%m/%Y")  
  delta = dt1 - dt2
  print("There are {} days in between {} and {}".format(abs(delta.days), date_1, date_2))


# 5. Calculate Volume of a shpere

def circle_vol():
  r = float(input("Enter Radius of Sphere: "))
  v = 4/3 * math.pi * r * r * r
  print("Volume of the Sphere with Radius %.2f is %.2f"%(r, v))
  
  
# 6. Copy string n times

def cpy_str():
  str = input("Enter String: ")
  cpy = int(input("How many copies of String you need: "))
  print("{} copies of {} are {}".format(cpy, str, str * cpy))  


# 7. Check if number is Even or Odd

def even_odd():
  num = int(input("Enter Number: "))
  if num % 2:
    print("%d is Odd"%num)
  else:
    print("%d is Even"%num)
    

# 8. Vowel Tester

def vow():
  char = input("Enter a character: ")
  charl = char.lower()
  if charl == "a" or charl == "e" or charl == "i" or charl == "o" or charl == "u":
    print("Letter %s is Vowel"%char)
  else:
    print("Letter %s is not Vowel"%char)


# 9. Triangle area

def tri():
  b = int(input("Enter magnitude of triangle base: "))
  h = int(input("Enter magnitude of triangle height: "))
  print("Area of a Triangle with Height {} and Base {} is {}".format(h, b, 1/2*b*h))  


# 10. Calculate Interest

def interest():
  pa = int(input("Please enter principal amount: "))
  ri = float(input("Please enter rate of interest in %: "))
  y = int(input("Enter number of years for investment: "))
  print("After {} years, your principal amount {} over an interest rate of {}% will be {}".format(y, pa, ri, pa+(y*pa*(ri/100))))


# 11. Euclidean Distance

def eucl():
  x1 = int(input("Enter Co-ordinate for x1: "))
  x2 = int(input("Enter Co-ordinate for x2: "))
  y1 = int(input("Enter Co-ordinate for y1: "))
  y2 = int(input("Enter Co-ordinate for y2: "))
  print("Distance between points ({}, {}) and ({}, {}) is {}".format(x1, y1, x2, y2, abs(int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)))))
  

# 12. Feet to Centimeter Converter

def feet_to_cm():
  feet = int(input("Enter Height in Feet:"))
  print("There are {} cm in {} ft".format(feet * 30.48, feet))


# 13. BMI Calculator

def bmi():
  h = int(input("Enter Height in cm: "))
  w = int(input("Enter Weight in kg: "))
  print("Your BMI is %.2f"%(w/(h/100)**2))    


# 14. Sum of n Positive Integers

def nsum():
  n = int(input("Enter value of n: "))
  sum = 0
  for i in range(n + 1):
    sum = i + sum
  print("Sum of n positive integers till {} is {}".format(n, sum))


# 15. Digits Sum of a Number

def dsum():
  n = input("Enter a number: ")
  sum = 0
  str = ''
  for i in n:
    sum = sum + int(i)
    str = str + i + '+'
  str = str[:len(str)-1]
  print("Sum of {} is {}".format(str, sum))    


# 16. Decimal to Binary Converter

def dec_to_bin():
  d = int(input("Enter a decimal number: "))
  bin = ''
  q = d
  while q != 0:
    if q % 2 == 0:
      bin = bin + '0'
    else:
      bin = bin + '1'
    q = int(q/2)  
  print("Binary Representation of {} is {}".format(d, bin[::-1]))
  

# 17. Binary to Decimal Converter

def bin_to_dec():
  bin = input("Enter a Binary number: ")
  rbin = bin[::-1]
  d = 0
  for i in range(len(rbin)):
    d = d + (2**i) * int(rbin[i])
  print("Decimal Representation of {} is {}".format(bin, d))


# 18. Vowel and Consonants Counter

def vow_cons():
  txt = input("Enter text: ")
  str = txt.lower()
  vowels = 'aeiou'
  v = 0
  c = 0
  for i in range(len(str)):
    if str[i] in vowels:
      v += 1
    else:
      c +=1
  print("Vowels: {}\nConsonants: {}".format(v, c))
  

# 19. Palindrome tester

def palin_test():
  txt = input("Enter text: ")
  if txt == txt[::-1]:
    print("Text %s is Palindrome"%txt)
  else:
    print("Text %s is not a Palindrome"%txt)  


# 20. Count Alphabets, Numbers and Special Characters

def count():
  txt = input("Enter text: ")
  str = txt.lower()
  n = 0
  a = 0
  sc = 0
  sp = 0
  for i in range(len(str)):
    if str[i] in '1234567890':
      n += 1
    elif str[i] in 'abcdefghijklmnopqrstuvwxyz':
      a += 1
    elif str[i] in ' ':
      sp += 1
    else:
      sc += 1
  print("Numbers = {}\nAlphabets = {}\nSpecial Characters = {}\nSpaces = {}".format(n, a, sc, sp))      
  

# 21.

def pattern():
  str = ''
  for i in range(9):
    if i < 5:
      str = str + '*'
      print(str)
    else:
      str = str[:-1]
      print(str)      


# 22.

def num_pattern():
  line = ''
  for i in range(9):
    if i < 5:
      line = line + str(i+1)
      print(line)
    else:
      line = line[:-1]
      print(line) 


# 23.

def triangle():
  for i in range(9):
    line = ''
    for j in range(i+1):
      line = line + str(i+1)
    print(line)
      
def main():
  print("1. Calculate area of a circle\n")
  circle_area()
  print("\n2. Check Number either positive, negative or zero\n")
  sign_check()
  print("\n3. Divisibility Check of two numbers\n")
  div()
  print("\n4. Days Calculator\n")
  days()
  print("\n5. Calculate Volume of a shpere\n")
  circle_vol()
  print("\n6. Copy string n times\n")
  cpy_str()
  print("\n7. Check if number is Even or Odd\n")
  even_odd()
  print("\n8. Vowel Tester\n")
  vow()
  print("\n9. Triangle area\n")
  tri()
  print("\n10. Calculate Interest\n")
  interest()
  print("\n11. Euclidean Distance\n")
  eucl()
  print("\n12. Feet to Centimeter Converter\n")
  feet_to_cm()  
  print("\n13. BMI Calculator\n")
  bmi()
  print("\n14. Sum of n Positive Integers\n")
  nsum()
  print("\n15. Digits Sum of a Number\n")
  dsum()
  print("\n16. Decimal to Binary Converter\n")
  dec_to_bin()
  print("\n17. Binary to Decimal Converter\n")
  bin_to_dec()
  print("\n18. Vowel and Consonants Counter\n")
  vow_cons()  
  print("\n19. Palindrome tester\n")
  palin_test()
  print("\n20. Count Alphabets, Numbers and Special Characters\n")
  count()
  print("\n21. Steric Pattern\n")
  pattern()
  print("\n22. Number Pattern\n")
  num_pattern()
  print("\n23. Number Triangle\n")
  triangle()
if __name__ == '__main__':
  main()
