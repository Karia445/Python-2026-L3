from ast import Break
#ex 1
radius = float(input('enter circle radius ?:' ))
area = 3.14 * radius ** 2
print('Circle area=', area)

#ex 2
Celcius = float(input('enter the temperature in Celcius ?:'))
Fahrenheit = Celcius * 9/5 + 32
print(Celcius, "(C)=", Fahrenheit,'(F)')

#ex 3
Numbers = [2,3,4,5,6,7,8,9,10]
for Number in Numbers:
  prime = True
  if Number < 2:
    prime = False
  else:
   for i in range(2,Number):
    if Number % i==0:
       prime = False
       Break
  if prime :
   print(Number, 'is a prime number')
  else :
   print(Number, 'is NOT a prime number')


#ex 4
number = int(input('enter a number? '))
sum = 0
for i in range(1,number):
  if number % i ==0:
    sum = sum + i
if sum == number:
  print(number,'is a perfect number')
else:
  print(number,'is NOT a perfect number')

#ex 5
colors = ['blue','red','white','green','purple','black']
color = input('what is your favourite color? ')
if color in colors:
  index=colors.index(color)
  print("your color is at index",index,"in my list")
else:
  print("Sorry i could not find your color")

#ex 6
print('range 1:')
for i in range(0,7):
 print(i,end=" ")

print('\nrange 2:')
for i in range(1,11,3):
  print(i,end=" ")

print('\nrange 3:')
for i in range(5,0,-1):
  print(i,end=" ")

print('\nrange 4:')
for i in range(6,-3,-2):
  print(i,end=" ")
print()

#ex 7
def remove_dollar_sign(s):
     return s.replace('$','')

print(remove_dollar_sign('$50'))

#ex 8
def extract_even(l):
  even=[]
  for number in l:
    if number % 2 == 0:
      even.append(number)
  return even
print(extract_even([1,4,5,-1,10]))

#ex 9
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result

print(factorial(5))

#ex 10
def divisors(number):
    result = []

    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)

    return result

print(divisors(12))

#ex 11
import math

def distance(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result

print(distance(0, 0, 3, 4))

#ex 12
def rectangle(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

rectangle(4, 5)