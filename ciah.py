#!/usr/bin/env python

import random

def main():
 """Start a music genre guessing game."""
 print("Guess the music genre game!")
 
music = [
    "pop music",
    "jazz",
    "hip hop",
    "contemporary R&B",
    "rock",
    "music theatre",
    "art music"
    ]

x = random.choice(music)
guess = None

while x != guess:
    
    guess = str(input("What kind of music genre am I thinking of? "))
    
    if x == guess:
        print("You guessed {}. Congratulations, you got it right!".format(guess))
    else:
        print("You guessed {}. Sorry, you got the wrong answer. Please try again!".format(guess))
    main()
    