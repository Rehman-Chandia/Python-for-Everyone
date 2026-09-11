#used for floor,ceil,round in python
import math
 #this import function is used for to  import math in it 
A, B = map(int, input().split())
 
floor = A // B
ceiling = math.ceil(A / B)
#used for aound off any number 
around = int(A / B + 0.5)
 #best output stlyle
print("floor", A, "/", B, "=", floor)
print("ceil", A, "/", B, "=", ceiling)
print("round", A, "/", B, "=", around)
