The Final Project: Python Snake Readme!
======

##### This is now associated with Project 3! The game itself hasn't been edited, however the format and the way it has been presented has.  

## How it works (not edited since last time)

How Snake works is that when it runs, the user can play the game and see their score as they play. If they lose, they have the option to quit or play again.

### Changes that accomodated Project 2 requirements:
 
- I have expanded on this project to include logging. Now, after every game of snake, a file will be created and updated to record the time that the game finished and the score that the player had. For example, if you lost with a score of 2, the log will say that `The Player got a score of 2.` As well as the time that the game ended. After every game, the log file will update.
- I changed the six of the window to actually work properly (originally I had the window/game be determined by width/width instead of width by height, messing up the gameplay a little). 
- I added a variable of score that can be tracked in order to be recorded in the log file. This will also be displayed on the when the user loses and wants to play again or not. Originally, this wasn't the case and the score only displayed during the actual gameplay. 

### Changes from last time to accomodate Project 3:

- The intention of this game is to be played locally, but the information of this game is to be referenced on the server. 
- A server was created, and on said server, links will take you to the code of the snake game, to this current README, and to the score logs that the game makes.

## Path

The path to the all of what the user needs is on my github: https://github.com/uc-bintzhm/it3038c-scripts/tree/main/FinalProject

##### The user should save all of the contents in this folder to be safe EXCEPT the pythonsnake.txt file, as that is the file that will be made by the snake game itself. 
##### The user should also make sure when they save these that they are all in the same folder, I would recommend saving to a folder on the C drive to be simple, like `C:\folder\` or something along those lines.

## Things to note/change for the user!

- Make sure that you have pygame installed and it works, or else the game will not run. 
- Make sure you change the file name for your log to the desired one that you want. In the script currently, the name of the file that will be created the first time that you use it will be called `pythonsnake.txt` and will save to whatever folder you have this game saved too. For example, my game is currently saved to my `C:\Users\madis\OneDrive\Documents\it3038c-scripts\python>` location, meaning that the log file will be created in this python folder. I would recommend saving this to its own folder so that way you have your game and log file separate from the rest of your files.

## Project 3 Instructions to make the server work!!
1. Make sure node is installed and all modules -- this includes "body-parser","fs", and "http"
2. Once you can run node, in your terminal run `node server` . If there are any errors, check to see if you have all of the required modules for node installed and that the code has everything responding to the proper path. 
3. You have some options! you can either play the game Snake from your file server first (which I would recommend because it is fun), or you can check out each different "click here"'s. If you haven't played the game however, the pythonsnake.txt will not have any data in it, and there will be an error if you haven't played snake yet to create that file. 
##### Fun Feature! The user can real time update the log for the scores as long as the server is running. To see an updated list as you are playing the game, click your browser's refresh button. 

Overall, the goal is for the user to start the server and see the snake information. 


#### Script inspiration
I mentioned this in project 1, but I got a lot of inspiration from Edureka, changing bits of it to make it my own and adding commentary throughout to show that I at least understood what I took inspiration from. For Project 2, I referenced a little bit of realpython.com, to understand the format of python logging, but for the most part, I figured out the placement of this code by myself in order to have the code log where I wanted it to. I also didn't really reference any other materials for the other changes except for maybe past labs in order to get proper syntax. For project 3, I primarily referenced the labs 6 through 10 and some stacked overflow and w3 to make sure I had proper syntax in a lot of places. I mainly referenced them when my code was breaking for some reason.
