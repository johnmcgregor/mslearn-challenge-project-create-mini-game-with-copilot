# write 'hello world' to the console
# print('hello world, are you out there?')
# declare a variable to count player wins
playerWins = 0
computerWins = 0    


###################################
def GetResult(choice):
    import random
    #   create a list of choices
    choices = ['rock', 'paper', 'scissors']
    #   randomly select a choice from the list  
    computer_choice = random.choice(choices)
    res = 0

    # compare the user's choice with the computer's choice
    if choice == computer_choice:
        print('Computer chose ' + computer_choice + ' -> It\'s a tie!')
    elif (choice == 'rock' and computer_choice == 'paper') or (choice == 'paper' and computer_choice == 'scissors') or (choice == 'scissors' and computer_choice == 'rock'):
        print('Computer chose ' + computer_choice + ' -> You Lose!') 
        res = -1 #computer wins
    else :
        print('Computer chose ' + computer_choice + ' -> You Win!')
        res = 1 #player wins
        
    return res


def my_function():
    print("Hello from a function")

def CalculateResults(playerWins, computerWins):
    print('Player wins: ' + str(playerWins))
    print('Computer wins: ' + str(computerWins))
    if playerWins > computerWins:
        print('Player wins!')
    elif playerWins < computerWins:
        print('The Computer Wins!')
    else:
        print('It\'s a tie!')
    print('Game Over')
    exit()

#########################
    


while True:
    print('Enter rock, paper, or scissors, Quit to Quit')
    choice = input().lower()
    while not (choice == 'rock' or choice == 'paper' or choice == 'scissors' or choice == 'quit') :
        print('Invalid choice, please choose again')
        choice = input().lower()
        
    if choice == 'quit':
        CalculateResults(playerWins, computerWins)
        #print('Goodbye, Loser....')
        #exit()


    result = GetResult(choice)
    if result == 1 : #increment player wins 
        playerWins += 1
    elif result == -1 : #increment computer wins
        computerWins += 1



