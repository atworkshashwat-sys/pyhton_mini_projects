import random
#random is the element to bring randomness in your program 
#to bring it you have to impport it first
print("This is a fortune cookie simulator ")
print("-------------------------------------------------------------------------------")
fortunes = [
"Great opportunities are coming your way.",
"A small step today will lead to big success tomorrow.",
"Your hard work will soon pay off.",
"Someone appreciates your efforts more than you know.",
"A pleasant surprise is waiting for you.",
"Patience will bring you the reward you seek.",
"You will learn something valuable very soon.",
"A new challenge will make you stronger.",
"Today is a good day to start something new.",
"Your determination will open new doors.",
"Good news will arrive when you least expect it.",
"A wise decision will lead to success.",
"Someone will offer help when you need it.",
"Your creativity will solve a difficult problem.",
"A positive attitude will attract good things.",
"A new friendship may change your life.",
"Your efforts today will shape your future.",
"Trust your instincts; they will guide you well.",
"An exciting opportunity will appear soon.",
"The path you are on will lead to growth."
]
#here you are randomly choosing a fortune from the list using random.choice
print("your fortune is : " + random.choice(fortunes))
print("thank you")

