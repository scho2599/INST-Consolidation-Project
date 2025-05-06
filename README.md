# INST-Consolidation-Project
# BY: Shua Cho

## Overview:

I created a card game for my second project, called Tricksy Battle. In this game two players each receive a set of cards. They then take turns playing them to win rounds by matching suits and card values aiming to be the first to reach a minimum of 9 points to win the game. This software is created to adhere to the principles of a card game that relies on tricks, where the type of the first card played is significant and higher ranks typically prevail when suits align. 

## How to Run:

1. Make sure you have **Python 3** installed on your computer.
2. Download the file `tricksy_battle.py` from this project.
3. Open a terminal or command prompt and navigate to the folder where the file is saved.
4. Run the game by typing:  python tricksy_battle.py
5. The game will then start to run on the terminal wah lah

Note: There is no need to input anything as the game will play itself

## Features Included:

- Shuffling and dealing a standard 48-card deck minus the kings 
- The players are dealt 8 cards at a time.
- A new "public card" is shown each round but not used for scoring.
- Players alternate who leads the round.
- Cards are compared based on suit and value to determine who wins each round.
- The game will end when a player reaches 9 points or after a default 16 rounds.
- “Shooting the Moon” was added as well if a player reaches the maximum possible points.

## Shortcoming:

Something I noticed about my code is a small error involving the game giving the round win to the wrong player sometimes. Sometime like even when someone shouldve won based on the suits it like unintentionally gives the win to the opponent. I wasnt able to figure out why exactly this was happening as I got caught up in studying for other finals however the game still runs normally besides that, it still keeps score normally and plays the rounds as normal. 

## What I Learned:

This project allowed me to work on utilizing loops, lists, and tuples while also helping me grasping the concept of using conditionals to compare values in my codes. Additionally although I wasnt able to make the game run flawless I still gained confidence in my codings skills. 
