Python Snake Readme!
======

## How it works

How Snake works is that when it runs, the user can play the game and see their score as they play. If they lose, they have the option to quit or play again.

### Changes from last time to accomodate Project 2 requirements:
 
- I have expanded on this project to include logging. Now, after every game of snake, a file will be created and updated to record the time that the game finished and the score that the player had. For example, if you lost with a score of 2, the log will say that `The Player got a score of 2.` As well as the time that the game ended. After every game, the log file will update.
- I  changed the six of the window to actually work properly (originally I had the window/game be determined by width/width instead of width by height, messing up the gameplay a little). 
- I added a variable of score that can be tracked in order to be recorded in the log file. This will also be displayed on the when the user loses and wants to play again or not. Originally, this wasn't the case and the score only displayed during the actual gameplay. 

## Path

The path to the game on my github is https://github.com/uc-bintzhm/it3038c-scripts/blob/main/python/Snake.py

## Things to note/change for the user!

- Make sure that you have pygame installed and it works, or else the game will not run. 
- Make sure you change the file name for your log to the desired one that you want. In the script currently, the name of the file that will be created the first time that you use it will be called `pythonsnake.txt` and will save to whatever folder you have this game saved too. For example, my game is currently saved to my `C:\Users\madis\OneDrive\Documents\it3038c-scripts\python>` location, meaning that the log file will be created in this python folder. I would recommend saving this to its own folder so that way you have your game and log file separate from the rest of your files.

#### Script inspiration
I mentioned this in project 1, but I got a lot of inspiration from Edureka, changing bits of it to make it my own and adding commentary throughout to show that I at least understood what I took inspiration from. For Project 2, I referenced a little bit of realpython.com, to understand the format of python logging, but for the most part, I figured out the placement of this code by myself in order to have the code log where I wanted it to. I also didn't really reference any other materials for the other changes except for maybe past labs in order to get proper syntax. 
