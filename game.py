import random


def play(user, comp):
    global rate
    if user == comp:
        print(f'There is a draw ({comp})')
        rate += 50
    else:
        i = options.index(user)
        # sort options - first put all options, which are after user choice, then all options before user choice
        sorted_op = options[i + 1:] + options[:i]
        # first half options of a list beat user choice, second - get defeated by it
        strong_options = sorted_op[:(len(sorted_op) // 2)]
        if comp in strong_options:
            print(f'Sorry, but the computer chose {comp}')
        else:
            print(f'Well done. The computer chose {comp} and failed')
            rate += 100


def get_rate(_name):
    with open('rating.txt', 'r') as f:
        for line in f:
            if _name in line.split():
                return int(line.split()[1])
    return 0


name = input('Enter your name:')
print(f'Hello, {name}')

rate = get_rate(name)

# options = 'rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire'
options = input('Press enter for default options - rock, paper, scissors\n '
                'or input your options(odd number) separated by coma \n')

if not options:
    options = ['rock', 'paper', 'scissors']
else:
    options = options.split(',')

print("Okay, let's start\n"
      "input your option or \n"
      "'!exit' to exit game or \n"
      "'!rating' to see your rating")

while True:
    user_choice = input()
    if user_choice == '!exit':
        print('Bye!')
        break
    elif user_choice == '!rating':
        print(rate)
    elif user_choice in options:
        comp_choice = random.choice(options)
        play(user_choice, comp_choice)
    else:
        print('Invalid input')
