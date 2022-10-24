import random

name = input("What's your name?:\n ")
question = input("\nAsk a yes or no question:\n")
answer = ''

random_number = random.randint(1, 9)

if random_number == 1:
    answer = f'Yes {name}, definitely.'
elif random_number == 2:
    answer = F'It is decidedly so {name}.'
elif random_number == 3:
    answer = f'Without a doubt., {name}'
elif random_number == 4:
    answer = f'Reply hazy {name}, try again.'
elif random_number == 5:
    answer = f'Ask again later {name}'
elif random_number == 6:
    answer = f'Better not tell you now {name}.'
elif random_number == 7:
    answer = f'My sources say no {name}.'
elif random_number == 8:
    answer = f'Sorry {name}. Outlook not so good.'
elif random_number == 9:
    answer = f'Very doubtful {name}.'
else:
    answer = 'Error'

print(answer)
