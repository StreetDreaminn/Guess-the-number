# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:46:23 2020

@author: frank
"""

import random

answer = random.randint(1,10) 

guess = int(input("Guess a number between 1 and 10: "))

# print(answer)

guess_turns = 2

while guess_turns > 0:
        if guess < answer:
            print("Incorrect! Guess higher!")
            guess_turns -= 1
            guess = int(input())
        elif guess > answer:
            print("Incorrect! Guess lower!")
            guess_turns -= 1
            guess = int(input())
        else:
            print("Correct!")
            break

if guess_turns == 0:
    print("Guess turns finished! The answer was {}!".format(answer))