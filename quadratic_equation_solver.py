#find out the roots of the quadratic equation
import math 
def eqroots(x,y,z): 
    d= y*y-4*x*z 
    sqrt= math.sqrt(abs(d)) 
# checking condition for discriminant
    if d>0: 
        print(" real and different roots ") 
        print((-y+sqrt)/(2 * x)) 
        print((-y-sqrt)/(2 * x)) 
    elif d==0: 
        print(" real and same roots") 
        print(-y / (2 * x)) 
# when discriminant is less than 0
    else:
        print("Complex Roots") 
        print(- y / (2 * x), " + i",sqrt)
        print(- y / (2 * x), " - i",sqrt)  
a=1
while a!=0:
    x=int(input("enter x:"))
    y=int(input("enter y:"))
    z=int(input("enter z:"))
    if x == 0: 
        print("Input correct quadratic equation") 
    else:
        eqroots(x, y, z)
