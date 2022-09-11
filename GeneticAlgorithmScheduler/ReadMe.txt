Genetic Algorithm Class Scheduler with GUI

This is a project I made to learn GUI development and machine learning. 

I asked the engineering professors at my college if there were any tasks that they spent time on that a simple machine learning
program could solev. One of them told me that they spend a lot of time trying to come up with a course schedule that allows all 9 of our
professors to teach all of the courses that they want to offer that semester that doesn't have any conflicts and preferentially has classes
end the earliest time possible each day.

I used tkinter to build a GUI and scripted a genetic algorithm in python to optimize the schedules. The program works by initializing 100 random schedules
and then assigning each one of them a numerical fitness score, and then using roulete wheel selection to determine the two parents for each member of the next
population. There is also a random chance for each child to mutate in order to help prevent the algorithm from getting stuck in a local minima.

The algorithm is controled from the GUI that pops up while running Gene_Display.py. The user controls the algorithm by either running more generations through the
Control dropdown in the top left corner and viewing the best or second best member of each population by using the View dropdown options. The user can also run through
a custom amount of generations by entering in a value next to the Generate button and then clicking the button.
