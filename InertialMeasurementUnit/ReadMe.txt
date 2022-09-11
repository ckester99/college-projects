Inertial Measurement Unit for Aviation Vehicles

This is a project I made to practice programming embedded systems and hone my C++ skills. 

I bought an Arduino microcontroller and an MP5060 Accelerometer/Gyroscope sensor. I connected the two with a battery
on a breadboard and connected the serial communication pins.

I integrated the gyroscope output and accounted for the drift overtime by having the output slowly trend toward the accelerometer data.
I also used Euler angles to convert the changes in roll, pitch, and yaw relative to the IMU to the roll, pitch, and yaw in real space.
Finally, I applied a first order low pass filter to the output to smooth the data so that there wouldn't be instabilities due to rapid
data swings that may not reflect the true position of the device.

 
