#------------------------Setup---------------------------
from __future__ import print_function
from platform import *
from sympy import *
import math
x = symbols('x')    #Define variable "x"
legal = [0, 0, 0]   #Check the input is legal or not
ip = x              #Input function
bound = [0.0, 0.0]  #Boundary of integral
n = 0               #Number n
count = 0.0         #Every f(count) will use
output = 0.0        #The answer using function
i = 1               #Count of for and while loop
#--------------------------------------------------------
def clean_screen():
    if (system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

clean_screen()

while (legal[0] == 0):
    print ("Please insert the case you want.")
    case = input("Testing case 1 ~ 6: ")
    clean_screen()
    if (case > 0 and case < 7):
        legal[0] = 1
    else:
        print ("Invaild input.")

clean_screen()

while (legal[1] == 0):
    print ("Please choose what method you want to use.")
    method = input("(1 is composite trapezoidal rule, 2 is composite Simpson's rule) ")
    clean_screen()
    if (method > 0 and method < 3):
        legal[1] = 1
    else:
        print ("Invaild input.")

while (legal[2] == 0):
    n = input("What's the value of n? ")
    if (n > 2 and ((n % 2 == 0 and method == 2) or method == 1)):
        legal[2] = 1
    else:
        clean_screen()
        print ("Invaild input.")
        if (method == 2 and n % 2 != 0):
            print ("Composite Simpson's rule's n must be an even number.")

if (case == 1):
    ip = x**2
    bound = [1.0, 3.0]
elif (case == 2):
    ip = 1/x**3
    bound = [1.0, 3.0]
elif (case == 3):
    ip = sqrt(x+1)
    bound = [0.0, 1.0]
elif (case == 4):
    ip = sin(x)
    bound = [0.0, math.pi]
elif (case == 5):
    ip = E**x
    bound = [0.0, 1.0]
elif (case == 6):
    ip = atan(x)
    bound = [0.0, 1.0]

h = ((bound[1] - bound[0]) / float(n))
count = float(bound[0]) + float(h)

print ("Testing case is:")
pprint (ip)
print ("Boundary is from " + str(bound[0]) + " to " + str(bound[1]) + ", n = " + str(n) + ", h = " + str(h) + ".\nIntegral of the f(x) using ", end = '')

if (method == 1):
    print ("composite trapezoidal rule:")
    print ("  " + str(h) + "/2 * (f(" + str(bound[0]) + ") + f(" + str(bound[1]) + ")", end = "")
    for i in range(0, 2):
        output += float(ip.subs(x, bound[i]))
    while (count < bound[1]):
        print (" + 2 * f(" + str(count) + ")", end = "")
        output += 2 * (float(ip.subs(x, count)))
        count += h
    output *= (h / 2)
    print (")\n= " + str(output))

elif (method == 2):
    print ("composite Simpson's rule:")
    print ("  " + str(h) + "/3 * (f(" + str(bound[0]) + ") + f(" + str(bound[1]) + ")", end = "")
    for i in range(0, 2):
        output += float(ip.subs(x, bound[i]))
    while (count < bound[1]):
        if (i % 2 == 1):
            print (" + 4 * f(" + str(count) + ")", end = "")
            output += 4 * (float(ip.subs(x, count)))
        else:
            print (" + 2 * f(" + str(count) + ")", end = "")
            output += 2 * (float(ip.subs(x, count)))
        count += h
        i += 1
    output *= (h / 3)
    print (")\n= " + str(output))

print ("Real value of the answer should be " + str(integrate(ip, (x, bound[0], bound[1]))))