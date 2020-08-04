import random, time


numDice = int(input('How many dice are being simulated? '))


if numDice > 1:     # Plural Grammar
    while True:
        numSide = int(input('How many sides should each have? '))
        if numSide < 2:
            print('A larger number, please.')
        elif numSide == 2:     #If they're coins
            print('Those are coins, but whatever.\n')
            time.sleep(0.8)
            print('\nTossing now!')
            time.sleep(0.5)
            break
        elif numSide > 2:      #If they're dice
            print('\nRolling now!')
            time.sleep(0.8)
            break
else:               # Singular grammar
    while True:
        numSide = int(input('How many sides should it have? '))
        if numSide < 2:
            print('A larger number, please.')
        elif numSide == 2:    #If it's a coin
            print("That's a coin, but whatever.")
            time.sleep(0.8)
            print('\nTossing now!')
            time.sleep(0.5)
            break
        elif numSide > 2:     # If it's a die
            print('\nRolling now!')
            time.sleep(0.8)
            break


for i in range(numDice):
    if numSide == 2:
        coinFace = ['Heads', 'Tails']
        print('Coin ' + str(i+1) + ': ' + coinFace[random.randint(0, 1)])
    else:
        print('Die ' + str(i+1) + ': ' + str(random.randint(1, numSide)))
    time.sleep(0.4)
