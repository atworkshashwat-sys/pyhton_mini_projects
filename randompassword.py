import random
print("hey you want a random password?")
choice = input(" YES (1) / NO (2):")
if choice == "1":
 characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0)","1)","2)","3)","4)","5)","6)","7)","8)","9)"]
lenght = int(input("enter the lenght of the password:"))
password = ""
for i in range(lenght):
 index = random.randint(0,len(characters)-1)
 password = password + characters[index]
print("your random password is :" + password)
