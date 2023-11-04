#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

#Escribe un minijuego de consola de rock, sicssors, paper
import random
import os
import time

os.system("cls")
print("Welcome to the game Rock, Scissors, Paper")
print("You will play against the computer")
print("You will have 3 attempts")
print("Good luck!")
time.sleep(1)
os.system("cls")

attempts = 3
while attempts > 0:
    attempts -= 1
    print("Choose:")
    print("1. Rock")
    print("2. Scissors")
    print("3. Paper")
    user_input = int(input())
    if user_input == 1:
        print("You choose Rock")
    elif user_input == 2:
        print("You choose Scissors")
    elif user_input == 3:
        print("You choose Paper")
    else:
        print("You didn't choose a valid option")
        continue
    
    computer_input = random.randint(1,3)
    if computer_input == 1:
        print("Computer choose Rock")
    elif computer_input == 2:
        print("Computer choose Scissors")
    elif computer_input == 3:
        print("Computer choose Paper")

    if user_input == computer_input:
        print("It's a tie")
    elif user_input == 1 and computer_input == 2:
        print("You win!")
        break
    elif user_input == 2 and computer_input == 3:
        print("You win!")
        break
    elif user_input == 3 and computer_input == 1:
        print("You win!")
        break
    else:
        print("You lose!")
else:
    print("You don't have more attempts")
    print("Game over")