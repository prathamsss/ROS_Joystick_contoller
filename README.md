# ROS_Joystick_contoller

This package could be used on any industry based robot having ROS.


1. Jetson Nano is been used for this operation as MASTER device. 
2. Arduino is used as SLAVE device for serial communication with Nano.
3. L293d is used as motor driver and Wireless Joystick to control robot.
4. Packages are been return in python and C++

4. ROS parameters: Publisher- Joystick values as Twist Msg
                 : Subsciber- Controller Node based on values to drive robot.
                 
                 
For using this project-
1. Install ROS Melodic.
2. Build your Motor driver and arduino connection.
3. If you are using diffrent motor driver other than L293d, than write your functions for moving Fordward, backward, right, left, etc in arduino.
4. Connect your arduino to your ROS device, change your port name in above RoboController file.
5. Launch ROS file using  "roslaunch joystick_control joystick.py"

Enjoy!!


Thank you!
