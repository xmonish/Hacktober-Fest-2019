
import math
a = float(input("coefficient a:"))
b = float(input("coefficient b:"))
c = float(input("coefficient c:"))
posroot = (-b + (math.sqrt((b*b) - (4*a*c))))/2*a
negroot = (-b - (math.sqrt((b*b) - (4*a*c))))/2*a
print ("The roots are : "),print(posroot), ",", print(negroot)
