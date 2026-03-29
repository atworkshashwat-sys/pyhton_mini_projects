#importing random module to generate random number
import random
print("welcome to the guessing game!")
#generating a random number between 1 and 100
number = random.randint(1,100)
user = int(input("guess the number: "))
#using while loop to check if the user's guess is correct or not
while user != number:
 if user < number:
  print("too low")
 else:
  print("too high")
 user = int(input("guess the number: "))
print("correct!")