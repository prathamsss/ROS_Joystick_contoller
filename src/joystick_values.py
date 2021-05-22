#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from joystick_utils import JoyStick


#Axix  = [x1,y1,x2,y2,r2,l2], 1= First nobe, 2 = secound Nobe
 
class Joystick_publisher():
     def __init__(self):
         self.joy_publisher = rospy.Publisher('joystick_command', Twist, queue_size=10)
          

     def publish_joystick(self, event=None):
         try:
           j= JoyStick()
           self.axis = j.read_axis()
           self.vel_msg = Twist()
           self.vel_msg.linear.x= self.axis[0]
           self.vel_msg.linear.y =self.axis[1]
           self.vel_msg.angular.z = self.axis[2]
           self.vel_msg.angular.x = self.axis[3]
           print("Vel_msg - ",self.vel_msg)
           self.joy_publisher.publish(self.vel_msg)

         except Exception as e:
            rospy.logwarn('[Warning] ' + str(e))

     def on_shutdown(self):
         rospy.logwarn('Stopping joystick_node!!!')






if __name__ == "__main__":
    try:
        rospy.init_node('joystick_node', anonymous=True)

        joystick_pub = Joystick_publisher()
        rospy.Timer(rospy.Duration(0.2), joystick_pub.publish_joystick)
        rospy.on_shutdown(joystick_pub.on_shutdown)
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.logerr('Could not start joystick_publisher!!!')






