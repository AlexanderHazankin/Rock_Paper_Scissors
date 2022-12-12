import random
from time import sleep  # for extra effect

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Introduction
player_name = str(input("Hello! I am your smart device. What is your name? \n"))
player_name = player_name.title()
print(f"Hallo {player_name},\n"
      "This is a rock, paper, scissors game. You play against me.\n"
      "We will play a \033[1m\033[34mseveral rounds Tournament \033[22m\033[39mand see who is stronger!!!")
sleep(1)
print("If you don't know the rules of the game, you can find the 'official' rules of the game at the link below. \n"
      "https://wrpsa.com/the-official-rules-of-rock-paper-scissors")
sleep(1)

# Tournament scoring
user_winn = 0
pc_winn = 0
draw = 0

# Tournament rounds count
rounds = input("How many rounds are you willing to play?\n")
while not rounds.isdigit():
    print("Invalid choice. Please try again.")
    rounds = input("How many rounds are you willing to play?\n")
# convert the input to an integer
rounds = int(rounds)
sleep(1)
# Play the game for the specified number of rounds
for user in range(rounds):

    # User's input storing
    user = input("What do you choose? Enter 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    # Use a while loop to repeatedly prompt the user until they enter a valid choice
    while not user.isdigit() or int(user) not in [0, 1, 2]:
        print("Invalid choice. Please try again.")
        user = input("Enter 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    # convert the input to an integer
    user = int(user)
    if user == 0:
        print(rock)
    elif user == 1:
        print(paper)
    elif user == 2:
        print(scissors)

# Random selection generator for computer
    pc = random.choice([0, 1, 2])
    if pc == 0:
        print(rock)
    elif pc == 1:
        print(paper)
    elif pc == 2:
        print(scissors)

# Comparing user and computer choices to determine a winner (or a draw)
    if user == 0 and pc == 2 or user == 1 and pc == 0 or user == 2 and pc == 1:
        print(f"{player_name}, you won this round!!!")
        user_winn += 1
    elif pc == 0 and user == 2 or pc == 1 and user == 0 or pc == 2 and user == 1:
        print(f"{player_name}, you lost this round!!!")
        pc_winn += 1
    elif user == pc:
        print("It's a Draw.")
        draw += 1

# Tournament result
if user_winn > pc_winn:
    print('''\033[1m\033[32m
_____.___.               __      __              
\__  |   | ____  __ __  /  \    /  \____   ____  
 /   |   |/  _ \|  |  \ \   \/\/   /  _ \ /    \ 
 \____   (  <_> )  |  /  \        (  <_> )   |  |
 / ______|\____/|____/    \__/\  / \____/|___|  /
 \/                            \/             \/
''')
    sleep(1)
    print("\033[1m\033[32mThis time you showed yourself to be a big winner.")
    sleep(1)
    print(f"You are my Herro {player_name}!!!")
    sleep(1)
elif user_winn < pc_winn:
    print('''\033[1m\033[31m
_____.___.              .____                   __   
\__  |   | ____  __ __  |    |    ____  _______/  |_ 
 /   |   |/  _ \|  |  \ |    |   /  _ \/  ___/\   __|
 \____   (  <_> )  |  / |    |__(  <_> )___ \  |  |  
 / ______|\____/|____/  |_______ \____/____  > |__|  
 \/                             \/         \/
''')
    sleep(1)
    print(f"\033[1m\033[31m{player_name}, you had no chance against me. You need more practice!!!")
    sleep(1)
else:
    print('''\033[1m\033[33m
________                       
_____    \______ \____________ __  _  __
\__  \    |    |  \_  __ \__  \ \/ \/  /
 / __ \_  |    `   \  | \// __ \      / 
(____  / /_______  /__|  (____  /\/\_/  
     \/          \/           \/
''')
    sleep(1)
    print("\033[1m\033[33mIt's a draw. It was a tough game. You are strong like me!\n")
    sleep(1)
    print(f"It was my honor to play with you {player_name}!")
    sleep(1)
