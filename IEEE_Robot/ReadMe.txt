2019 Southeast IEEE Robot Competetion

This is the code for Murray State's 2019 IEEE Southeast robotics competition robot.

The theme of the competition was pi and the robots either had to stack lego blocks that were color coded to digits in the order of pi,
or press buttons in an area of the playing field in the order of pi. The robots were given 3 minutes to score as many points as they could.

We chose to have our robot press buttons because it was simpler to implement than building a robot that was able to collect and stack loose
lego blocks. Each button had a debounce timer that the button had to be held down for the gameboard to register it as pressed or released.
However, you were able to press down a different button before the debounce timer finishes as long as you hold each press for the required
debounce time.

Our solution to optimize the amount of ordered button presses in 3 minutes was to build a robot that had 10 solenoids and folding arms that
would be able to reach all 10 buttons without the robot moving. Once the robot had driven to the buttons and latched onto the wall nearby,
the robot would fire the solenoids in order to score as many points as possible.

The code works by storing timestamps of when each button was pressed or released back and iterating through an array of the digits of pi,
pressing each one in order and waiting until the debounce timers have finished where required. We added another debounce timer to ensure that
each distinct button press happened in the order required with a small amount of spacing to ensure the game board would register each press 
correctly. 

 
