#here we are going to check if the given number is prime or not using function
#below is the function defined
def primecheker(n):
    multiple = 0
    for i in range(1, n+1):

     if n % i == 0:
            multiple = multiple + 1

    if multiple == 2:
          result = "prime number" 
    else:
         result = "not a prime number"
    
    return result

givennumber = int(input("enter a number:"))
#edge case for 1 and 0 as they are neither prime nor composite
if givennumber == 1 or givennumber == 0:
        print("neither prime nor composite")
else:
 #calling the function and printing the result
 print(primecheker(givennumber))