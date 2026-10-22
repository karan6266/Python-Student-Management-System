import random
'''
1 for sanke
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}

you = youdict[youstr]

# by now we have 2 numbers (variables),You and computer

print(f"You chose: {reversedict[you]}\n computer chose: {reversedict[computer]}")

if (computer == you):
    print("It's a draw!")

else:
    '''
    if (computer == -1 and you == 1): (computer - you) = -2
        print("You win!")
        
    elif (computer == -1 and you == 0): ( computer - you) = -1
        print("You lose!")    
        
    elif (computer == 1 and you == -1): (computer - you) = 2
        print("You lose!")    
        
    elif (computer == 1 and you == 0): (computer - you) = 1
        print("You win!")    
        
    elif (computer == 0 and you == -1): (computer - you) = 1
    
        print("You win!")    
        
    elif (computer == 0 and you == 1): (computer - you) = -1
        print("You lose!") 
        
        The blow logic is written on the basis of the values of computer - you.
           
        '''
        
    if ((computer - you) == -1 or (computer - you) == 2):
            print("You lose!")
        
    else:
        print("You win!")
            
