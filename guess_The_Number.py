import random
print("welcome to the guessing game!")
number = random.randint(1,100)
user = int(input("guess the number: "))
while user != number:
 if user < number:
  print("too low")
 else:
  print("too high")
 user = int(input("guess the number: "))
print("correct!")