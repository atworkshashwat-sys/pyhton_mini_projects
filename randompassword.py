import secrets
import string

print("hey you want a random password?")
choice = input(" YES (1) / NO (2):")
if choice == "1":
 characters = string.ascii_letters + string.digits
 try:
  lenght = int(input("enter the lenght of the password:"))
 except ValueError:
  print("please enter a valid number")
  exit(1)
 password = "".join(secrets.choice(characters) for _ in range(lenght))
 print("your random password is :" + password)
