#!/usr/bin/env python
import rospy

from geometry_msgs.msg import PoseStamped
import numpy as np
import math
from std_msgs.msg import Bool
import time
from Tkinter import *


def callback(data):
    if(data):
	pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(15) # 15hz
	msg = PoseStamped()
	print(msg)
	msg.header.frame_id="map"
	t = - math.pi
	while not rospy.is_shutdown():
		while t <=  math.pi :	    
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(msg.pose.position.x)
			t = t + 0.1
			pub.publish(msg)
			rate.sleep()
			
		while t >=  -math.pi :	    
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(- msg.pose.position.x)
			t = t - 0.1
			pub.publish(msg)
			rate.sleep()
    else:
	time.sleep(2)
def talker():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('button', Bool, callback)

    rospy.spin()



if __name__ == '__main__':

		talker()
	
