#define a function to calculate the vavlue of x: a*x^2+b*x+c=0

import math

def quad(a,b,c):
  x1 = (-b + math.sqrt(b^2-4*a*c))/(2*a)
  x2 = (-b - math.sqrt(b^2-4*a*c))/(2*a)
  return x1,x2

x1, x2 = quad(3,4,-5)
print(x1, x2)



  
