#define a function to calculate the vavlue of x: a*x^2+b*x+c=0

import math

def quad(a,b,c):
  x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
  x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
  return x1,x2

x1, x2 = quad(3,4,-5)
print(x1, x2)


#calculate x1^2+x2^2+x3^2+...

def cal(*numbers):
    r = 0
    for n in numbers:
        r = r + n*n
    return r

print(cal(3))
print(cal(3,4,5))

numbers = [3, 4, 5]
print(cal(*numbers)
  
      
#key-words
   
def student(id, name, **kw):
    print('ID:', id, 'Name:', name, 'Other:', kw)
    
student('123', 'Mike', Major='Engineering')
student('1234', 'John', Major="Business",Age=20)

other = {'Major': 'Finance', 'Age': '23'}
student('12345','Sara', **other)
      
      
def student2(id, name, *grades, major = 'Engineering', age):
    print(id, name, grades, major, age)

grades = ['A','B']
student2('345', 'Laura', grades, age = 22)
