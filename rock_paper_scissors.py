# This is a game of Rock, Paper, Scissor
import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:  # Main Game Loop
    print('%d Wins, %d Losses, %d Ties' % (wins, losses, ties))
    while True:  # Player Input Loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()  # Quit the Program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # Break out of Player Input Loop
        print('Type either r, p, s, or q.')

    # Display what the player chose
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Display what the computer chose
    random_choice = random.randint(1,3)
    if random_choice == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_choice == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_choice == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1