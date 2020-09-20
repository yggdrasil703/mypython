number=int(input("input a number\n"))
if number >= 128:
    number=number-128
    #print("number1:",number)
    print("1") 
else:
    print("0")
if number >= 64:
   number=number-64
   #print("number2:",number)
   print("1")
else:
    print("0")
if number >= 32:
    number=number-32
    #print("number3:",number)
    print("1")
else:
    print("0") 
if number >= 16:
    number=number-16
    #print("number4:",number)
    print("1")
else:
    print("0") 
if number >= 8:
    number=number-8
    #print("number2:",number)
    print("1")
else:
    print("0") 
if number >= 4:
    number=number-4
    #print("number2:",number)
    print("1")
else:
    print("0")
if number >= 2:
    number=number-2
    #print("number2:",number)
    print("1")
else:
    print("0") 
if number >= 1:
    number=number-1
    #print("number2:",number)
    print("1")
else:
    print("0") 
print(bin(number))
 

    

