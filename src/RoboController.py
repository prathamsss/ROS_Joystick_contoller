#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Header
from geometry_msgs.msg import Twist
import serial
import time
import pygame as pyg
from joystick_utils import SlaveContact


class RoboController():
     def __init__(self,port,baud_rate):
       self.slave = SlaveContact(port,baud_rate)
       rospy.Subscriber('joystick_command', Twist, self.CommandCallback)
                                              
     def CommandCallback(self, commandMessage):
        self.command = commandMessage
        print(self.command.linear.x,self.command.linear.y)

        if self.command.linear.x==self.command.linear.y == 0.0:
            self.slave.sendData('v')
           
        
        elif (self.command.linear.y) <= -0.3:
            self.slave.sendData('w')
           

        elif (self.command.linear.x) <= -0.3:
            self.slave.sendData('d')
           

        elif (self.command.linear.x) > 0.3:
            self.slave.sendData('a')
            
                  
        elif (self.command.linear.y) >0.3:
            self.slave.sendData('s')
            
   
     def on_shutdown(self):
        rospy.logwarn('Stopping car_controller_node!!!')
     
 
rospy.init_node('joystick_controller_node', anonymous=False)
car_controller = RoboController('/dev/ttyACM0',9600)
rospy.on_shutdown(car_controller.on_shutdown)
rospy.spin()



