README file for Python LED Assesment

Project description:
The project is found inside the LIGHTSABER folder. Lightsaber v1 is the python
file where the code is found

My project consist of a small Star Wars themed "game". Where you act as a Jedi
choosing a lightsaber colour out of the 6 most common ones (blue,green,purple,
yellow, orange, white). The lightsaber the user choses will be the weapon that
will fight the duel against the red (Sith) lightsaber. The winner will be randomly
chosen. So, the player only choses the colour but the choice does't affect the 
outcome. 

The 6 lightsaber options are first shown in the OPC. The python UI gives a list of 
the 6 options to choose from, each of them assigned to a lightsaber colour. 
Using an animation the other lightsabers disappear leaving your choice after that 
the colour of your choice will roll through the screen and then the empty screen will
display the enemy's red lightsaber igniting (through a created function followed by 
an animation of your chosen lightsaber igniting (also through a function).
An animation of a "VS" sign being written will be displayed. Then according to the 
outcome of the random result the whole OPC screen will be crossed by diagonals in an
animation of your colour (if you win) followed by a message on UI or red diagonals 
with a different message (if you lose).

INSTRUCTIONS:
Open the examples folder where all necessary libraries are found, download opc.py, and
make sure time, colorsys, and random python libraries are installed in your machines, 
then, open the folder "LIGHTSABER" and then open "Lightsaber_v1.py" and run it.

CHANGELOG:

Version 0.1:
-created the .py file
-added some first light experiments

Version 0.2:
-created an experimental Python UI

Version 0.3:
-created a tkinter applied to the case
-added possible useful Animations

Version 0.4:
-created the lightsaber functions for each colour and displayed them
-some comments added

Version 0.5:
-the transition Animation was added
-the lighsaber chosen was displayed alone after choice
-animations file created separately to test different animations and modify existing
ones without changing the code
-animations were tested in animations file

Version 0.6:
-lightsaber with colour of choice is ignited in an Animation
-red lightsaber is also ignited
-these animations where first created in animation file
-some comments added

Version  0.7:
-Python UI from 0.2 is modified to choose input and lightsaber directly in UI. 
(tkinter discarded)
-Error message for invalid input and loop for correct choice
-scroll Animation of colour of choice added in main loop of the code from animation
file

Version 0.8:
-VS animation created in animation file

Version 0.9:
-VS animation added to main lightsaber file (branch)
-animation file, newselect file, lightsaber file combined into one version

Version 1
-winner and loser determined through randomness displaying a message on UI
-animation to show winner and loser added
-final comments and explanations added
