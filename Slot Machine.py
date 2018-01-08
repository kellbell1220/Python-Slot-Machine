# Slot Machine - Kelli Stasiak

v_credits = 0
a_wheel1 = []
a_wheel2 = []
a_wheel3 = []
v_winnings = 0
playAgain = 'y'


import random

v_credits = input("Welcome! 1 Credit = 1 Spin ~ How Many Credits Would You Like to Add? ")

while v_credits > 0 and (playAgain == ('y')) :
    print ("Lets Play!!!")

    v_credits= (v_credits - 1)

    a_wheel1 = ["Cherry", "Horseshoe", "Diamond", "Lemon", "Bar", "Jackpot", "Lemon"]
    randNum = random.randint(0,6)
    print a_wheel1[randNum]

    a_wheel2 = ["Cherry", "Horseshoe", "Diamond", "Lemon", "Bar", "Jackpot", "Lemon"]
    randNum = random.randint(0,6)
    print a_wheel1[randNum]

    a_wheel3 = ["Cherry", "Horseshoe", "Diamond", "Lemon", "Bar", "Jackpot", "Lemon"]
    randNum = random.randint(0,6)
    print a_wheel1[randNum]

   

#Compare Winner
    if a_wheel1 =="JackPot" and a_wheel2 == "JackPot" and a_wheel3 == "Jackpot":
        v_winnings = (v_winnings + 5000)
        print ("JACKPOT!!!! You Win 5000 Credits")

    elif a_wheel1 =="Cherry" and a_wheel2 == "Cherry" and a_wheel3 == "Cherry":
        v_winnings = (v_winnings + 100)
        print ("You win 100 credits")

    elif a_wheel1 =="Diamond" and a_wheel2 == "Diamond" and a_wheel3 == "Diamond":
        v_winnings = (v_winnings + 50)
        print ("You win 50 credits")

    elif a_wheel1 =="Horseshoe" and a_wheel2 == "Horseshoe" and a_wheel3 == "Horseshoe":
        v_winnings =(v_winnings + 25)
        print ("You win 25 credits")

    elif a_wheel1 =="Bar" and a_wheel2 == "Bar" and a_wheel3 == "Bar":
        v_winnings =(v_winnings + 10)
        print ("You win 10 credits")

    elif a_wheel1 =="Lemon" and a_wheel2 == "Lemon" and a_wheel3 == "Lemon":
        v_winnings = (v_winnings + 5)
        print ("You win 5 credits")

    else:
        print ("Please Try Again")

    v_credits = (v_credits + v_winnings)
        
    
    print v_credits
    v_playAgain = raw_input("Would you like to play again Y or N ").lower

if (v_playAgain == 'n'):
    print ("Have A Nice Day")
        


   




    
    


