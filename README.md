# Head_Soccer

by 6182175 & 5629204

## Prerequisites

- installed python (python 3.7 recommended)
- installed pygame

## Installation

- install the current version of PyCharm from https://www.jetbrains.com/de-de/pycharm/download/#section=windows
- install git (https://git-scm.com/download/win)
- open PyCharm, then click on "Configure" -> "Settings" -> "Git" and add the path of your installed git executable "git.exe"
- press "Ok" and click on "Get from Version Control"
- clone the repository from git and paste it into the URL field
- press "clone"
- login to github
- configure python interpreter
- if pygame is not preinstalled it can also be installed via the package manager in PyCharm

## Frameworks

Pygame was used as the framework for the Head-Soccer project. Here the sprite class plays an important role to easily detect the collision of two objects. It also allows to easily load image files and transform them, as well as position and display them on the screen. The pygame Clock Object furthermore keeps track of the FPS of the game.

## Start the game

Run the project by running the file "head_soccer_main.py". Afterwards click the Button "Start the Game!" and the game will start immediately. The left-hand player can be moved by pressing the keys 'w', 'a' and 'd' and is able to shoot by pressing space. You can move the right-hand player by using the arrow keys. He will shoot after pressing 'p'.

## Particularities

### Constants

To configure the game easily, there is the file "constants.py". This file contains all constants like field size, gravity, the maximum ball speed, the game duration, etc. If you want to change the basic settings for the game, you only have to change the constants to the desired value.

### Ball physic

To make the game look realistic, a good implementation of the ball physics plays an important role. For this purpose, the ball has two variables for the speed in the X and Y direction. These values are changed accordingly when the ball collides with the ground, a player or the goal. How the speeds of the ball change depends on where the ball collides with the goal or the player and the speed at which the player moves. There are also values for gravity and friction, which influence the behaviour of the ball.

## Credits

@ Liam O'Meara (Goal Sprite)
