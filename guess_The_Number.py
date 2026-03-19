import random
print("welcome to the guessing game!")
number = random.randint(1,100)
user = int(input("guess the number: "))
if user>number:
 print("too high")
elif user<number:
 print("too low")
else:
 print("correct!")

