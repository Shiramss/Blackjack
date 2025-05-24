card = [1,2,3,4,5,6,7,8,9,10,10,10,0] #values of each card in a deck, 0 is placeholder value for ace as it has two values
no_ace = [1,2,3,4,5,6,7,8,9,10,10,10] # card deck with no aces to prevent people from getting a hand with just zero 
import random

def blackjack(): #pick two random cards for player and dealer
  player_card = random.choice(no_ace) + random.choice(no_ace) #calculate initial values of player 1 and player 2
  dealer_card = random.choice(no_ace) + random.choice(no_ace)
  turn  = 0 #set turns to zero to keep the game going until someone wins or looses
  x = 0 # define player turn variables outside of the loop
  z = 0 
  choicex = 'a' #define choice variables out side of loop
  choicey = 'b'
  while turn == 0: #loop game until someone wins
    while x == 0: #loop player 1 turn until it is over
        wrong = False #boolean variable for if player inputs wrong command
        print(f"Player 1: your current value is: {player_card}")
        choicex = input("Player 1: Hit or Stand: ")
        if choicex.lower() == "stand" :
            print("Player 1: you have chosen to stand ") #ends loop for player 1
            x = 1
            z = 0
        elif choicex.lower() == "hit" :
            y = random.choice(card) # y is card value for the turn
            if y == 0: # y = 0 -> refers to an ace
                ace = int(input("You got an ace! 11 or 1: "))
                if ace == 1: 
                    player_card += 1
                    print(f"Player 1: your current value is: {player_card}")
                elif ace == 11:
                    player_card += 11
                    print(f"Player 1: your current value is: {player_card}")
            else:
                 player_card += y # Add card value 
            print(f"Player 1: your current value is: {player_card}")
        else:
            print("Player 1, please choose hit or stand") #handling if player inputs something other than hit or stand
            wrong = True
        if player_card == 21: #pssoible win outcomes for each player
                print("Player 1: you win")
                turn = 1 #ends the entire game
                x = 1
                z = 1
        elif player_card > 21:
                print("Player 2: Player 1 has gone bust. You win!")
                turn = 1
                x = 1
                z = 1  
        else: #checks if player 2 is standing or not
                if choicex.lower() == "stand" and choicey.lower() == "stand":
                    z = 1
                    x = 1
                elif choicey.lower() == "stand":
                     x = 0 
                     z = 1
                elif wrong == True:
                     z = 1
                     x = 0
                else:
                     z = 0
                     x = 1

    while z == 0: #loop player 2 turn until it is over
        wrong = False #variable for if player inputs wrong command
        print(f"Player 2: your current value is {dealer_card}") #same code as player 1
        choicey = input("Player 2: Hit or Stand: ")
        if choicey.lower() == "stand" :
                print("you have chosen to stand")
                z = 1       
                x = 0    
        elif choicey.lower() == "hit":
            y = random.choice(card)
            if y == 0:
                ace = int(input("11 or 1: "))
                if ace == 1: 
                    dealer_card += 1
                    print(f"Player 2: your current value is: {dealer_card}")
                elif ace == 11:
                    dealer_card += 11
                    print(f"Player 2: your current value is: {dealer_card}")
            else: 
                dealer_card += y
            print(f"Player 2: your current value is: {dealer_card}")
        else:
            print("pick a hit or a stand")
            wrong = True

        if dealer_card == 21:
                    print("Player 2 wins!")
                    z = 1
                    turn = 1
        elif dealer_card > 21:
                    print("Player 2 has gone bust. Player 1 wins!")
                    z = 1
                    turn = 1
        else:
            print('standing or not?')
            if choicex.lower() == "stand" and choicey.lower() == "stand":
                x = 1
                z = 1
            elif choicex.lower() == "stand":
                 x = 1
                 z = 0
            elif wrong == True:
                 x = 1
                 z = 0
            else:   
                x = 0
                z = 1

    if choicex.lower() == "stand" and choicey.lower() == "stand": #win conditions incase both players are standing
         print("both players are standing")
         print(f"Player 1 score: {player_card}")
         print(f"Player 2 score: {dealer_card}")
         turn = 1
         if player_card > dealer_card:
              print("Player 1 has a value closer to 21 and thus wins!")
         elif dealer_card > player_card:
              print("Player 2 has a score closer to 21 and thus wins!")
         else:
              print("You guys have both somehow tied. Congrats?")
    
            


blackjack()
