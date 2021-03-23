import random
game_list = ['Rock', 'Paper', 'Scissors']
computer = c = 0 #c for computer
command = p = 0 #p for player
print('Score: Computer: ' + str(c) + ' Player: ' + str(p))

#loop
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input('Rock, Paper, Scissors or Quit: ')
    if command == computer_choice:
        print('Tie')

    elif command == 'Rock':
        if computer_choice == 'Scissors':
            print('Player won!')
            p += 1
        else:
            print('Computer won!')
            c += 1

    elif command == 'Paper':  
        if command == 'Rock':
            print('Player won!')
            p += 1
        else:
            print('Computer won!')
            c += 1

    elif command == 'Scissors':
        if computer_choice == 'Paper':
            print('Player won!')
            p += 1
        else:
            print('Computer won!')
            c += 1   

    elif command == 'Quit':
        break
    else:
        print('Wrong command! ')

    print('Player: ' + command)
    print('Computer: ' + computer_choice)
    print(' ')
    print('Score: Computer: ' + str(c) + ' Player: ' + str(p))
    print(' ')