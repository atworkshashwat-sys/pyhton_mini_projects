givennumber = int(input("enter a number: "))
divisor = 0
#checking if it is a prime number or not
for i in range(1, givennumber+1):
    if givennumber%i == 0:
        divisor = divisor + 1
if divisor > 2:
    print("not a prime number")
else:
    print("number is a prime number")
    
    for j in range(0, givennumber+1):
     print(j) 
    
    

        