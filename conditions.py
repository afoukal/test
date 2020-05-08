print('Rock...')
print('Paper...')
print('Scissors...')

player_1 = input('Choose ')
print('*** NO CHEATING ***\n ' * 30)
player_2 = input('Choose ')

player_1 = player_1.upper()
player_2 = player_2.upper()

if player_1 == 'ROCK':
    if player_2 == 'ROCK':
        print('Tie')
    elif player_2 == 'PAPER':
        print('Player-2 wins')
    else:
        print('Player-1 wins')
elif player_1 == 'PAPER':
    if player_2 == 'ROCK':
        print('Player-1 wins')
    elif player_2 == 'PAPER':
        print('Tie')
    else:
        print('Player-2 wins')
elif player_1 == 'SCISSORS':
    if player_2 == 'ROCK':
        print('Player-2 wins')
    elif player_2 == 'PAPER':
        print('Player-1 wins')
    else:
        print('tie')
else:
    print('somthing went wrong')
