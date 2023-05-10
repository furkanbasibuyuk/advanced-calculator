import math
import time

print("""**********************
      
       --CALCULATOR--
Addition : 1
Subraction : 2
Multipication : 3
Division : 4
Involve : 5
Square Root : 6
Logarithm : 7
Radian to Degree Convert : 8
Find Sinus : 9
Find Cosinus : 10
Find Tangent : 11
Find Cotangent : 12

If you want to quit, enter the q letter...

**************************
""")

while True:
    
    process = int(input("Please choose the process : "))
    
    if (process == 0):
        print("The program ending..")
        time.sleep(1)
        break
    
    elif (process == 1):
        value_1 = int(input("Please enter the first value : "))
        value_2 = int(input("Please enter the second value : "))
        print("Calculating...")
        time.sleep(1)
        print("{} + {} = {}".format(value_1,value_2,value_1+value_2))
    elif (process == 2):
        value_1 = int(input("Please enter the first value : "))
        value_2 = int(input("Please enter the second value : "))
        print("Calculating...")
        time.sleep(1)
        print("{} - {} = {}".format(value_1,value_2,value_1-value_2))
    elif (process == 3):
        value_1 = int(input("Please enter the first value : "))
        value_2 = int(input("Please enter the second value : "))
        time.sleep(1)
        print("Calculating...")
        print("{} x {} = {}".format(value_1,value_2,value_1*value_2))
    elif (process == 4):
        value_1 = int(input("Please enter the first value : "))
        value_2 = int(input("Please enter the second value : "))
        print("Calculating...")
        time.sleep(1)
        print("{} / {} = {}".format(value_1,value_2,value_1/value_2))
    elif (process == 5):
        value_1 = int(input("Please enter the first value : "))
        value_2 = int(input("Please enter the exponent value : "))
        print("Calculating...")
        time.sleep(1)
        print("{} exponent {} equals to {}".format(value_1,value_2,math.pow(value_1,value_2)))
    elif (process == 6):
        value_1 = int(input("Please enter the first value : "))
        print("Calculating...")
        time.sleep(1)
        print("{} square root of equals to {}".format(value_1,math.sqrt(value_1)))
    elif (process == 7):
        value_1 = int(input("Please enter the first value : "))
        value_2 = int(input("Please enter the logarithm base value : "))
        print("Calculating")
        time.sleep(1)
        print("Logarithm of {} to base {} equals to {}".format(value_1,value_2,math.log(value_1,value_2)))
    elif (process == 8):
        value_1 = int(input("Please enter the first value : "))
        print("Calculating...")
        time.sleep(1)
        print("{} radians equals to {} degree.".format(value_1,math.radians(value_1)))
    elif (process == 9):
        value_1 = int(input("Please enter the degree : "))
        print("Calculating...")
        time.sleep(1)
        print("sin({}) = {}".format(value_1,math.sin(value_1)))
    elif (procces == 10):
        value_1 = int(input("Please enter the degree : "))
        print("Calculating...")
        time.sleep(1)
        print("cos({}) = {}".format(value_1,math.cos(value_1)))
    elif (procces == 11):
        value_1 = int(input("Please enter the degree : "))
        print("Calculating...")
        time.sleep(1)
        print("tan({}) = {}".format(value_1,math.tan(value_1)))
    elif (procces == 12):
        value_1 = int(input("Please enter the degree : "))
        print("Calculating...")
        time.sleep(1)
        print("cot({}) = {}".format(value_1,math.tan(value_1)))
        