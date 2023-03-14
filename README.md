
Welcome tWilltp,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

---

 # Project 3
 
## Python essentials project

* This site shows a basic example of an interactive game, battleships.
* This project is designed as a training excersize, to consolidate my knowledge of python.  
[Project3 view](URL 'blank')

---

# Table of contents

- [UX](#UX)
   - [Game creator aim](#Game-creator-aim)
   - [Player aim](#Game-aim)
   - [Game structure](#Game-structure)
- [Technology](#Technology)
- [Testing](#Testing)
   - [Is the programme functional](#Is-the-programme-functional)
   - [Main Bugs and Fixes](#Main-Bugs-and-Fixes)
   - [Performance Testing](#Performance-Testing)
   - [Code Validation](#Code-Validation)
   - [Development Issues](#Development-Issues)
- [Deployment](#Deployment)
- [Credits](#Credits)

# UX

## Game Creator Aim

In this project I aimed to create a game that would be easily understandable with a flow that would feel intuitive from the user's perspective. The game had to weave the aspects/information I wanted it to contain, in a well structured layout, not only being enjoyable but demonstrating my grasp of python.

## Player Aim

The user should have all the necessary information laid out to them in a concise yet descriptive manor, if by their first move they are able to shoot accurately and know the parameters for winning and losing and carry the game out to it's final conclusion then I would consider the game a success.

## Game Structure

The game begins with a positive welcome message followed by the rules being explained immediately, if the player decides to play then their board is displayed allowing the player to see their ships (with randomly generated positions) while the enemy ships are hidden from sight (randomly generated also). The player is prompted to input the position of their shot after which, the computer will fire it's shot (randomly generated) a message is displayed letting the player know the outcomes of either shot. That is the play cycle, the new board is displayed with each of the shot's effects being added and the player continues until the and of the game when the player is shown how many shots away they were from winning or how many it took for them to secure victory.

## features

* The board size is 9 * 9 using letters and numbers to denote the coordinates
* A hit is represented by 'S' for sunk
* A miss is represented by '-'
* player sunk ship is represented by 'L' for loss
* player ship is represented by 'X'
* if the player puts in the same shot, they are told by the message 'Area clear, Guess again'
* The player has 20 turns to win

---

# Technology

## Python

* The programming language I used to develop the code for this project.

## Git-hub

* The software hosting platform I used for this project.

## Git-pod

* The development hosting platform I used for this Project.

---

# Testing

## Is the programme funtional

The progamme runs as I expect it to, with the information coming in an order that is easy to follow and gameplay that properly relates to the player, their position and options as they move through to the end.

## Main Bugs and Fixes

* Bug: due to the different ways the game can end, the relevant information was not accurately displayed.
* Fix: differnet endgame functions were created so after the different types of losses/wins the code was directed properly.

* Bug: the number of shots a player has left is always registered as 19.
* Fix: I used a global value since the local value was always reset with each shot meaning 20 would go down to 19 repeatedly.

* Bug: if the player hits a sunken enemy ship it is registered as 'shot missed'.
* Fix: I added a condition to the shots fired function so that if the player hits 'S' 'Area clear' is printed.

* Bug: if the computer hits an unnacceptable target e.g. '-', 'L', 'S' the board is printed and it guesses again instead of guessing again and printing the board with the acceptable target.
* Fix: I changed the structure of the computer shot function so that displayboard() was printed after the computer found an acceptable target.

## Performance Testing

The final tests I ran on my code were as follows:

Test | Desired result yes | Desired result no | Fail
---|---|---|---
can the player input the same coordinates twice | | X |
can the player fire on their own ships | | X |
can the computer fire on an unacceptable coordinate ('-','L','S') | | X |
can the player fire on the enemy ships | X | |
if the computer sinks all of the players ships, is the proper end game function called | X | |
if the player sinks all of the enemy ships, is the proper end game function called | X | |
if the player turns expire, is the proper end game function called | X | |
is the amount of shots taken for the player to win displayed at the end of the game | X | |

## Code Validation

The python code passes through the pep8 linter, with no significant issues.

## Development Issues

The largest and most time consuming issue I encountered while developing the game was to clear the board of all previous ships and shots. I tried many different tactics in order to get through this problem such as: using multiple if statements to change every symbol on the board back to a blank area; employing a while loop to loop through every square on the board changing them individually; placing the variable that generated the board in many different positions so that it would be built anew in a comprehensible way for the flow of the code. Some variant of the last attempt was correct as I had to set the board fresh in a new function using a global variable, then call that function for each of the respective endGame() functions.

---

# Deployment

The project is deployed using Heroku

---

# Credits

* 
* 
* 