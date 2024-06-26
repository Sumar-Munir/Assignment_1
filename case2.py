#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

def roll_two_dice():
    return random.randint(1, 6), random.randint(1, 6)

def play_game():
    while True:
        input("Press Enter to roll the dice...")
        dice1, dice2 = roll_two_dice()
        total = dice1 + dice2
        print(f"You rolled {dice1} + {dice2} = {total}")
        
        if total in (7, 11):
            print("You win!")
            break
        elif total in (2, 3, 12):
            print("Craps! You lose!")
            break
        else:
            target = total
            print(f"Your target is {target}. Keep rolling to match your target, but avoid rolling a 7.")
            
            while True:
                input("Press Enter to roll the dice...")
                dice1, dice2 = roll_two_dice()
                total = dice1 + dice2
                print(f"You rolled {dice1} + {dice2} = {total}")
                
                if total == target:
                    print("You matched your target! You win!")
                    return
                elif total == 7:
                    print("You rolled a 7! You lose!")
                    return

if __name__ == "__main__":
    play_game()

