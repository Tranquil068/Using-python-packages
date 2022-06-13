import random

def RPS():
    while True:
        options=["R","P","S"]
        CPU= random.choice(options)
        print("CPUs choice=", CPU)
        Player= input("Pick an option from R,P,S :")
        print("Players choice=", Player)
        if Player==CPU:
            print("It is a tie!")
    
        elif Player=="R":
            if CPU=="P":
                print("Computer wins!")
            else:
                print("Yay. You win!")
            break  
        elif Player=="P":
             if CPU=="S":
                 print("Computer wins!")
             else:
                 print("Yay. You win!")
             break
        elif Player=="S":
             if CPU=="R":
                 print("Computer wins!")
             else:
                 print("Yay. You win!")
             break
        else:
             print("Error! Enter a valid option.")
        
    
